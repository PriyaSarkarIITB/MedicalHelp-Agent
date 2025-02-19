from crewai import Crew, Process
from Travel_agent import travel_Itinerary_agent, travel_package_agent 
from Travel_tasks import travel_Itinerary_task, travel_package_task
from langchain_openai import ChatOpenAI
import os

manager_llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7, model = 'gpt-4o')

travel_agent_crew = Crew(
    agents = [travel_Itinerary_agent,
              travel_package_agent],
    tasks = [travel_Itinerary_task,
             travel_package_task],

    manager_llm=manager_llm,
    process=Process.hierarchical,
    verbose=True
)

travel_agents_input = {
    'destination':'california',
    'budget':'400000',
    'max_days':'10',
    'peoples':'5'
}

result = travel_agent_crew.kickoff(inputs=travel_agents_input)
print(result)
