from crewai import Agent
from langchain.agents import load_tools

# Human Tools
human_tools = load_tools(["human"])


class AutomationAgents():
    def manager(self):
        return Agent(
            role="Manager",
            goal="""Goal of agent
                """,
            backstory="""Backstory in this explain roles and responsibility to Manager - try to add some few short prompts
                """,
            allow_delegation=True,
            verbose=True,
        )

    def manager_research(self, search_tool, details_tool):
        return Agent(
            role="Manager Research",
            goal="""GOAL of Research Manager""",
            backstory="""Backstory in this explain roles and responsibility to research Manager - try to add some few short prompts""",
            verbose=True,
            allow_delegation=True,
            tools=[search_tool, details_tool]
        )

    def title_creator(self):
        return Agent(
            role="Title Creator",
            goal="""Create 10 potential titles for a given YouTube video topic and description. 
                You should also use previous research to help you generate the titles.
                The titles should be less than 70 characters and should have a high click-through-rate.""",
            backstory="""As a Title Creator, you are responsible for creating 10 potential titles for a given 
                YouTube video topic and description.""",
            verbose=True
        )

    def description_creator(self):
        return Agent(
            role="Description Creator",
            goal="""Create a description for a given YouTube video topic and description.""",
            backstory="""As a Description Creator, you are responsible for creating a description for a given 
                YouTube video topic and description.""",
            verbose=True
        )

    def email_creator(self):
        return Agent(
            role="Email Creator",
            goal="""Create an email to send to the marketing team to promote the new YouTube video.""",
            backstory="""As an Email Creator, you are responsible for creating an email to send to the marketing team 
                to promote the new YouTube video.
                
                It is vital that you ONLY ask for human feedback after you've created the email.
                Do NOT ask the human to create the email for you.
                """,
            verbose=True,
            tools=human_tools
        )
