import warnings
warnings.filterwarnings('ignore')

from data_preprocessing import clean_data
from report_generation import report
from analysis_engine import analyse
import pandas as pd
import numpy as np
import pprint
import os

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

file_path = input("Enter file path: ")
normalise_flag = input("Should the AI agent normalise the data or not?\nEnter 'y' for yes and 'n' for no: ")
match(normalise_flag):
    case "y":
        df = clean_data(file_path=file_path, normalise=True)
    case default:
        df = clean_data(file_path=file_path)

print("DataFrame is loaded and cleaned")

analysis_results = analyse(df)
print("Results from analysis are: \n")
pprint.pprint(analysis_results, indent=2, width=40)
analysis_llm = str(analysis_results)

report(analysis_results=analysis_results, original_data=df)

print("\n\nThe Chatbot is generating the summary of the analysis, Please wait for some time.")
prompt = f"""Based on the given data, please perform the following tasks:\n
    1. Provide a summary of the data, including key statistics and insights.\n
    2. Present the summary in a clear and visually appealing format.\n
    3. Conduct an analysis based on the data, highlighting significant patterns, trends, and any notable findings.\n
    4. Include any relevant observations that could provide additional context or value.\n
    
    If you encounter any questions that are not related to the given data, respond with "I don't know" instead of generating a response that could be inaccurate or unrelated.

    Data = {analysis_llm}"""

response = model.generate_content(prompt)
print(response.text)

history = [(prompt, response.text)]

while True:
    print("\nEnter 'quit' to exit\n")
    user_prompt = input("Enter your prompt: ")
    if user_prompt.lower().strip() == "quit" or user_prompt.lower().strip() == "exit":
        break

    history_prompt = "\n".join(f"Prompt {i+1}: {p}\nResponse {i+1}: {r}" for i, (p, r) in enumerate(history))
    new_prompt = f"{history_prompt}\n\nUser Prompt: {user_prompt}\nResponse:"

    user_response = model.generate_content(new_prompt)
    print(user_response.text)
    
    history.append((user_prompt, user_response.text))
    
    if len(history) > 5:
        history.pop(0)
