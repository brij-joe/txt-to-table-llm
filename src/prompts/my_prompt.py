import logging

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MyPrompt:
    _instance = None

    def __new__(cls, model):
        if cls._instance is None:
            cls._instance = super(MyPrompt, cls).__new__(cls)
        return cls._instance

    def __init__(self, model):
        if not hasattr(self, '_initialized'):
            self.model = model  # Default path for saving/loading index
            self._init(model)
            self._initialized = True
            logger.info(f"MyPrompt object initialized with model: {self.model}")

    def _init(self, model):
        self.llm = ChatGoogleGenerativeAI(model=model, temperature=0.7)
        self.prompt_template = PromptTemplate(input_variables=["text", "schema"], template="""
            Extract the fields from the given input text according to the below given schema.
            If any field is not present in the text, return null for that field.
            If the text contains multiple values for a field, return all values in an array\n.
            schema: {schema}\n
            text: {text}\n
            Return the result as JSON.
            """)

    def extract_table(self, text, schema):
        logger.info(f"Extracting schema: {schema}\n from text: {text}")
        prompt = self.prompt_template.format(text=text, schema=schema)
        logger.info(f"Generated prompt: {prompt}")
        response = self.llm.invoke(prompt)
        return response
