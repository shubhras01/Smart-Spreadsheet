import os
from .dfs_components import ExcelIslandFinder
from agents.run_agent import AgentMagic


class Worksheet:
    '''
    the class contains
    - parses the given worksheet
    - and contains data
    - also has AgentMagic class --> worksheet_agent
      which will help in answering the questions
    '''
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.parser = ExcelIslandFinder(file_path)
        self.parse()
        # initialize agent with teh worksheet data
        self.worksheet_agent = AgentMagic(self.data)

    def parse(self):
        if not os.path.exists(self.file_path):
            raise ValueError(f"file path {self.file_path} does not exist")
        all_dfs = self.parser.get_dataframe_list()
        self.data = all_dfs

    def ask_worksheet(self, question: str):
        return self.worksheet_agent.ask_agent(question)


class WorksheetManagerFactory:
    '''
    worksheet manager factory class. Since all the sheets given in test contain same data
    the factory class will replace current registered sheet with new sheet, in case its called again
    '''
    def __init__(self):
        self.worksheet: Worksheet = None
        self.registry = {}

    def get_registered_worksheet(self):
        return self.worksheet

    def register_worksheet(self, file_path):
        # Register each worksheet by its file path
        self.worksheet = Worksheet(file_path)

