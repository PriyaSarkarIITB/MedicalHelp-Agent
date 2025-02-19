from crewai import Crew, Process
from Travel_agent import Travel_Destination_Agent, Travel_Route_Planner_Agent, Activity_Recomendation_Agent, Booking_Research_Agent
from Travel_tasks import Travel_Destination_Task, Travel_Route_Planner_Task, Activity_Recomendation_Task, Booking_Research_Task
from langchain_openai import ChatOpenAI
import os

manager_llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7, model = 'gpt-4o')

travel_agent_crew = Crew(
    agents = [Travel_Destination_Agent, Travel_Route_Planner_Agent, Activity_Recomendation_Agent, Booking_Research_Agent],
    tasks = [Travel_Destination_Task, Travel_Route_Planner_Task, Activity_Recomendation_Task, Booking_Research_Task],

    manager_llm=manager_llm,
    process=Process.hierarchical,
    verbose=True
)

travel_agents_input = {
    'destination':'california',
    'budgets':'400000',
    'max_days':'10',
    'peoples':'5'
}

result = travel_agent_crew.kickoff(inputs=travel_agents_input)
print(result)
