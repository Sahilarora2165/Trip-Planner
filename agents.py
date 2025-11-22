from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class TravelAgents:
    def __init__(self):
        # Initialize Groq LLM using API key from .env with updated model
        self.GroqLlama3 = ChatGroq(
            temperature=0.7,
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY")
        )
        # Ollama doesn't require an API key
        from langchain_community.llms import Ollama
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. 
                            I have decades of experience making travel itineraries
                            """),
            goal=dedent(f"""Create a 7 day travel itinerary with detailed per day plans,
                        include budget , packing suggestions and safety tips.
                        """),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
            ],
            verbose=True,
            llm=self.GroqLlama3,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations."""),
            goal=dedent(f"""Select the best cities based on weather , season , prices and travel interests"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.GroqLlama3,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information about the city ,
                                it's attractions and customs"""),
            goal=dedent(f"""Provide the BEST insights about the selected city"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.GroqLlama3,
        )