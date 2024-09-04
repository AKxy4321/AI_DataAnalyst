### Main Application Module Documentation

This module integrates data processing, analysis, reporting, and AI model interaction. It manages the overall workflow of loading and cleaning data, performing data analysis, generating reports, and interacting with a generative AI model for further insights. It utilizes `pandas` for data handling, `pprint` for formatted printing, and `google.generativeai` for generating text-based summaries.

---

#### Main Workflow:

1. **Data Loading and Cleaning**:
   - **Input**:
     - `file_path (str)`: Path to the data file, which can be in CSV, JSON, or Excel format.
     - `normalise_flag (str)`: Indicator for whether to normalize the data (`'y'` for yes, `'n'` for no).
   - **Functions**:
     - `clean_data(file_path: str, normalise: bool) -> pd.DataFrame`: Cleans the data based on the specified normalization flag. It fills missing values, drops duplicates, and normalizes numeric columns if requested.
   - **Usage**:
     - The user inputs the file path and normalization flag. The data is loaded and cleaned accordingly.

2. **Data Analysis**:
   - **Function**:
     - `analyse(df: pd.DataFrame) -> dict`: Performs clustering, computes the correlation matrix, and generates descriptive statistics for the cleaned DataFrame.
   - **Output**:
     - `analysis_results (dict)`: A dictionary containing clustering labels, cluster centers, correlation matrix, and descriptive statistics.
   - **Usage**:
     - After cleaning the data, it is passed to the `analyse` function to get the results.

3. **Report Generation**:
   - **Function**:
     - `report(analysis_results: dict, original_data: pd.DataFrame)`: Generates visualizations based on the analysis results and original data.
   - **Usage**:
     - The results from the `analyse` function and the original DataFrame are used to create various plots and charts.

4. **Generative AI Interaction**:
   - **Setup**:
     - Uses the `google.generativeai` library to interact with a generative AI model.
     - API key is loaded from environment variables using `dotenv`.
   - **Function**:
     - `model.generate_content(prompt: str)`: Generates content based on a prompt provided to the AI model.
   - **Usage**:
     - A prompt is created based on the analysis results, and the AI model generates a summary of the data. The response is printed to the console.

5. **User Interaction**:
   - **Loop**:
     - The script enters a loop where the user can input additional prompts to interact with the AI model.
     - The conversation history is maintained and used to provide context for subsequent interactions.
   - **Exit**:
     - The loop continues until the user types `'quit'` or `'exit'`.

---

#### Code Overview:

```python
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

# Load environment variables and configure API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

# User input for file path and normalization
file_path = input("Enter file path: ")
normalise_flag = input("Should the AI agent normalise the data or not?\nEnter 'y' for yes and 'n' for no: ")
match(normalise_flag):
    case "y":
        df = clean_data(file_path=file_path, normalise=True)
    case default:
        df = clean_data(file_path=file_path)

print("DataFrame is loaded and cleaned")

# Analyze the data
analysis_results = analyse(df)
print("Results from analysis are: \n")
pprint.pprint(analysis_results, indent=2, width=40)
analysis_llm = str(analysis_results)

# Generate report
report(analysis_results=analysis_results, original_data=df)

# Generate AI summary
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

# Maintain conversation history
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
```

---

### Key Points:

- **Error Handling**: Be aware that the `file_path` must correspond to a supported file format. Unsupported formats will raise a `ValueError`.
- **Normalization**: The normalization process scales numeric columns between 0 and 1, based on their min and max values.
- **Visualization**: Generated visualizations help in interpreting the analysis results and provide a comprehensive view of the data.
- **AI Interaction**: The generative AI model is used to create a narrative summary of the analysis results, which can provide additional insights or context.

This documentation should assist in understanding the functionality and workflow of the Main Application Module.