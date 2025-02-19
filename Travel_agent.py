from crewai import Agent
from dotenv import load_dotenv
from medical_tool import scrape_tool, search_tool
from langchain_openai import ChatOpenAI

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'


llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7, model = 'gpt-4o')

travel_Itinerary_agent = Agent(
    role = "Travel Route Agent",
    goal = "It fetches data from the input and makes a route plan for the journey",
    backstory = "Have expertise in planning packages in different routes across globe"
                "It can give any package with routes according to the destination in the efficient way according to budget"
                "seamlessly integrates input, web searches, and delivers the best possible way"
                "Tries to give appropiate and latest condition about the routes"
                "uses statiscal model and machine learning"
                "Gives suggestion according to the budget",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools = [scrape_tool, search_tool]
)

travel_package_agent = Agent(
    role = "Travel Package Agent",
    goal = "Decides the package after the planning the route",
    backstory = "Equipped with a deep understanding of developing travel package"
                "It gives the package according to the budget, route, maximum number of days and number of peoples"
                "It have deep understanding on managing budget alongwith route and number of peoples to make the travel efficient and comfortable "
                "continously checks about routes and gives latest updates with alternatives packages according to budget"
                "tries to get report from different package based on peoples and other factors"
                "the most best way to get package and regularly stay update for new problems",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools = [scrape_tool, search_tool]
)