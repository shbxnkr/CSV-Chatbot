from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
import pandas as pd

def load_agent(csv_path):
    df = pd.read_csv(csv_path)
    hf_pipeline = pipeline(
        "text-generation",
        model="gpt2",
        max_length=100,
        do_sample=True,
        temperature=0.7,
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    agent = create_pandas_dataframe_agent(
        llm, 
        df, 
        verbose=False, 
        allow_dangerous_code=True   # <--- add this line
    )
    return agent

def ask_question(agent, question):
    return agent.run(question)
