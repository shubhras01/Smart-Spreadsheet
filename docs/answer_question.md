### Tools used for answering the question 

#### Current setup
1. The given test worksheets data is small, and can be fit into single llm api context
2. So I just used that data as `backstory` context of llm agent and, its able to answer most of the questions


#### Future setup
1. knowing that sheets can get bulky, we need to scale the Poc setup like this
    - Build RAG tools for agent, specifically designed for worksheets
    - These tools will be used by agent to fetch the correct value of the question asked
    - My proposed design is 
    

                  Parsed data -------------
                  |                       |
Parse Sheets ---> |                       |
                |                         |
                |                         v
            Embedding of parsed data ---------------->>> Index in elasticsearch 
                                                             ^
                                                             |
                                                             |
Question ---> Get Embeddings <-----> **Agent** <-------> Search in elasticsearch

These designed tools specifically for our usecase will give agent a better capability to get answers 
from the parsed worksheet data, with minimum latency involved
                                                             