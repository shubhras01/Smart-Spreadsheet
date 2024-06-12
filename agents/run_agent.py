try:
    import rich
except ModuleNotFoundError as e:
    raise RuntimeError(
        "You probably either forgot to install the dependencies "
        "or forgot to activate your conda or virtual environment."
    ) from e

try:
    from rich_argparse import RichHelpFormatter
except ImportError:
    msg = (
        "Please install the rich_argparse package with `pip install rich_argparse`."
    )
    raise ImportError(msg)

import os
from crewai_tools import BaseTool
from crewai import Agent, Task
from langchain_openai import ChatOpenAI

backstory_tmpl = '''
    You are an analyser who answers questions based on the data of a spreadsheet
    You are given a dataset which is parsed from an excel sheet. The example of data is this
                
    {sheet_data}
            
    This data is stored in memory in for of pandas dataframe. You will be asked question like 
    "What is the total current assets at Inc. and Australia for year 2023"
    
    Give answer to the asked question
'''


class GetValueFromSheet(BaseTool):
    name: str = "get value from the sheet"
    description: str = '''The tool will return the value of key, given the date in the argument. 
    function arguments are 
    - key: string key for which value has to be fetched from the sheet 
    - date: date in format of YYYY-MM-DD, for which key value is needed

    returns:
    - values: list of dictionary with the values asked for 
    '''

    def _run(self, sheet_path: str) -> str:
        return "Tool's result"


class AgentMagic:
    def __init__(self, worksheet_data):
        self.role = '''
            You are a excel sheet analyst, who gives answer to questions by thinking carefully and step by step, and
        reading values from the sheet
        '''
        self.backstory = backstory_tmpl.format(sheet_data=worksheet_data)
        self.task_description = '''You have access to a parsed excel worksheet, and you have to answer the below question from the sheet"
                        You can use the tools available to you to get the answer you need. 
                        "QUESTION:"
                        {question}
                        '''
        self.llm = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model_name="gpt-4-turbo")

        self.agent = Agent(
                        role=self.role,
                        goal="successfully answer the given question",
                        backstory=self.backstory,
                        verbose=True,
                        llm=self.llm,
                        memory=True,
                        cachetools=True
                    )

    def ask_agent(self, question: str):
        task = Task(
            description=self.task_description.format(question=question),
            agent=self.agent,
            expected_output="question should be correctly answered based on the given dataset"
        )

        answer = task.execute()
        return answer


if __name__ == "__main__":
    from data_parser.dfs_components import ExcelIslandFinder
    w = ExcelIslandFinder("/home/shubhra/work/Smart-Spreadsheet/tests/example_0.xlsx")
    all_dfs = w.get_dataframe_list()
    data = []
    for df in all_dfs:
        data.append(df.to_string(index=False))
    a = AgentMagic("\n\n".join(data))
    a.ask_agent("What is the Total Cash and Cash Equivalent of Nov. 2023?")



