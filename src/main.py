from dotenv import load_dotenv
from langchain_core.messages import AIMessage

from app_constants import GEMINI_MODEL
from prompts.my_prompt import MyPrompt
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import PyPDFLoader

from schema.candidate_profile import CandidateProfile

load_dotenv(dotenv_path="c:\\temp\\.env", override=True)


def document_loader(file_path: str):
   loader = PyPDFLoader(file_path)
   docs = loader.load()
   return docs[0]


def main():
    text = document_loader(file_path="c:\\temp\\data\profile1.pdf").page_content
    print(f"Loaded text: {text[:500]}...")  # Print the first 500 characters for verification

    schema = CandidateProfile().model_json_schema()
    print(f"Loaded schema: {schema}...")

    llm = MyPrompt(GEMINI_MODEL)
    response = llm.extract_table(text=text, schema=schema)
    with open("c:\\temp\\output_table.txt", "w") as file:
        file.write(response.text())
    print(f"Got response: {response.model_json_schema()}...")


if __name__ == "__main__":
    main()
