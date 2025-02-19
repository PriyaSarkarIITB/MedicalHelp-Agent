from crewai import Agent
from dotenv import load_dotenv
from medical_tool import scrape_tool, search_tool
from langchain_openai import ChatOpenAI

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'


llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7, model = 'gpt-4o')

Travel_Destination_Agent = Agent(
    role = "Specialized in giving current condition of the destination",
    goal = "To provide detailed information about current situation of the destination",
    backstory = "Research on weather plans of the destination for the selected dates"
                "It identifies best time to travel the specific destination"
                "Provides local culture, traditions at that particular day"
                "Also provides information to complete legal works for travelling abroad"
                "Provides any festival or concert currently going on or going to be happened"
                "Maps out local transport system"
                "It provides the optimal distance between the spots in the destination",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools = [scrape_tool, search_tool]
)

Travel_Route_Planner_Agent = Agent(
    role = "Gives optimized travel routes for each day",
    goal = "To create time efficient cost-effective hassle free enjoyable travel plan for travelers",
    backstory = "Suggest the multiple route option for each day"
                "Identifies the best transport mode to reach the place for that day to save the time"
                "Calculates perday travel cost including meal and tickets for spots"
                "Provides real time traffic situation to avoid delays"
                "Balances activities and rest periods for each day",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools = [scrape_tool, search_tool]
)

Activity_Recomendation_Agent = Agent(
    role = "Suggest best activities to perform for that day",
    goal = "To offer best dynamic and safe experience of the day",
    backstory = "Suggest activities according to user's interest"
                "Recommends best landmarks, with high traffic indication"
                "Checks opening of the activities for the specific dates"
                "Provides activities cost estimation according to the user's budget"
                "It will suggest best dynamic and safe activities present in that place"
                "Suggest best places to take photos",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools = [scrape_tool, search_tool]
)

Booking_Research_Agent = Agent(
    role = "Gives the best booking option according to the budget",
    goal = "To provide hassle free and best travel bookings in a efficient and budget friendly way ",
    backstory = "Suggest best flight and train according to the budget"
                "Compares the price between the hotels and transport system and suggest top choices"
                "Suggest the best local transport option for daily travelling",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    # tools = [scrape_tool, search_tool]
)
