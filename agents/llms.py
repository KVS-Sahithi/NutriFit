import os
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
import google.generativeai as genai

load_dotenv()

class LLMS:
    def __init__(self,llm):
        self.llm=llm
        

    def run(self,prompt):
        
        if(self.llm=="GEMINI"):

            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel('gemini-pro')
            output = model.generate_content(prompt)
        

        return output
