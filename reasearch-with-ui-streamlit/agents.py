from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool,YoutubeChannelSearchTool, TXTSearchTool
from langchain.llms import Ollama
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

os.environ["ANY_SCALE_API_KEY"]=os.getenv("ANY_SCALE_API_KEY")
os.environ["ANY_SCALE_API_BASE"]=os.getenv("ANY_SCALE_API_BASE")

anyscale_base_url = os.environ["ANY_SCALE_API_BASE"]
anyscale_api = os.environ["ANY_SCALE_API_KEY"]
model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'


class ResearchCrewAgents:

    def __init__(self):
        # Initialize tools if needed
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.txt_tool = TXTSearchTool()
        self.llama2 = ChatOpenAI(model=model,  base_url=anyscale_base_url, api_key=anyscale_api)
        self.Ollama = Ollama(model="mistral")

    def researcher(self):
        # Detailed agent setup for the Researcher
        return Agent(
            role='Research Expert',
            goal='Systematically scour sources to gather current news and articles on diverse topics.',
            backstory="You are a paragon of meticulousness and analytical prowess, with a PhD in information science and over a decade of experience in high-stakes research roles, from academic institutions to top-tier consultancy firms. Known for your relentless pursuit of accuracy and depth, you have an uncanny ability to unearth gems of information that others might overlook. Your work is the bedrock upon which complex decisions and analyses are built, making you an indispensable cornerstone of any knowledge-driven team.",
            verbose=True,
            allow_delegation=False,
            tools=[self.web],
            llm=self.llama2
        )

    def analyst(self):
        # Detailed agent setup for the Analyst
        return Agent(
            role='Data Analysis Specialist',
            goal='Evaluate and enhance the information collected to ensure accuracy and relevance.',
            backstory="With a formidable background in data science and a sharp, inquisitive mind, you stand out as a master of data interrogation and synthesis. Your career spans over fifteen years, involving roles in government intelligence and corporate strategy, where you've turned ambiguous data into clear, actionable insights. Your analytical reports are often cited as the gold standard in your field, and your capacity to dissect complex datasets is nothing short of legendary.",
            tools=[self.serper],
            verbose=True,
            allow_delegation=False,
            llm=self.llama2
        )

    def writer(self):
        # Detailed agent setup for the Writer
        return Agent(
            role='Master Storyteller and Technical Writer',
            goal='Integrate and articulate insights into a compelling narrative with precise citations.',
            backstory="As a celebrated author and journalist with over twenty years of experience crafting stories that captivate and inform, you possess a unique flair for making intricate information accessible and engaging. Your writing has graced the pages of major publications and influential blogs, where your ability to elucidate complex concepts in an engaging manner has won you numerous accolades. In this role, you are the final architect, molding the raw analytical content into a final piece that is not only informative but also profoundly impactful.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.llama2
        )