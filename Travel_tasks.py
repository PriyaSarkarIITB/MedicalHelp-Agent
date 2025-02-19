from crewai import Task
from Travel_tools import search_tool, scrape_tool
from Travel_agent import travel_Itinerary_agent, travel_package_agent

travel_Itinerary_task = Task(
    description=(
        "Creates the route according to the place ({destination}) given by the user"
        "Review the ({destination}) and give the best route according to the ({budget}) dollar "
        "Use statistical modeling and machine learning techniques to analyze route and package according to user's interest"
        "identify both the ({destination} & {max_days}) and predict the route"
        "It always try to give best possible output"
    ),
    expected_output=(
        "Gives the suggestion of route according to the {destination} & {max_days}"
        "review the {destination} & {max_days} again to give the best possible output."
    ),
    agent=travel_Itinerary_agent
)

travel_package_task = Task(
    description=(
        "It reviews the {destination} and tries to give the best route"
        "After reviewing the {budget} dollar and {destination} it gives best route and best package"
        "After recognizing the destination, budget dollar, max_days and peoples it suggest the best possible package"
        "Analyze the {destination}, {budget} dollar, {peoples} and {max_days} after this gives the best package"
        "It always try to give best possible output"
    ),
    expected_output=(
        "Try to give more prominent route according to {budget} dollar dollar & {max_days}"
        "Gives the output as users interest"
        "Gives proper output according to users {destination}, {max_days}, {budget} dollar and {peoples}"
        "List of possible conditions and recommendations."
    ),
    agent = travel_package_agent
)
