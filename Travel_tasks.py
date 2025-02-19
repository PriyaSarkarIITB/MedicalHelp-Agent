from crewai import Task
from Travel_tools import search_tool, scrape_tool
from Travel_agent import Travel_Destination_Agent, Travel_Route_Planner_Agent, Activity_Recomendation_Agent, Booking_Research_Agent

Travel_Destination_Task = Task(
    description=(
        "Research on the weather plans of the {destination} according to the dates given by the user's"
        "Review the {destination} and {max_days} to suggest the best time to plan"
        "Suggest the local cultural programs, festivals and concerts of the {destination}"
        "All legal documents required for the {destination} depends on the number of days"
        "It always try to give best possible output according to user input"
        "Provides the best travel insights of the {destination}"
    ),
    expected_output=(
        "Gives the best possible routes for daily travel maintaining the overall {budget} dollars budget"
        "Suggest the best plan according to the {destination} and {max_days} given by the user"
        "Gives the most refined plan after reviewing the destination"
    ),
    agent = Travel_Destination_Agent
)

Travel_Route_Planner_Task = Task(
    description=(
        "It reviews the {destination} and tries to give the best route"
        "After reviewing the {destination} and {max_days} is plans the routes and local places for daily travel"
        "Analyze the weather condition of the local places and plans the route accordingly"
        "Continously analyzing the local routes for travelling and also local insights"
        "It tries to maintain the overall {budgets} dollars for the whole trip"
        "It always try to give best possible output after analyzing repeatedly"
    ),
    expected_output=(
        "Provides the most efficient routes according to the {destination} destination,{budgets} dollars budgets, {max_days} maximum number of days "
        "Suggest the best route that hassle free, time efficient and comfortable journey to the travellers"
        "Provides each & everyday planning of the routes with timings when to start"
        "Provides the activities to be done and which places to take rest and for how much time"
    ),
    agent = Travel_Route_Planner_Agent
)

Activity_Recomendation_Task = Task(
    description = (
        "It reviews the {destination} current weather and plan the activity according to it"
        "It analyzes the {budgets} dollars budget and max {peoples} peoples and plans the activity accordingly"
        "It analyzes the local condition of spot and plans the activities"
        "It plans the safe and the enjoying activities to perform"
        "It maintains the time according to the daily target of travelling"
    ),
    expected_output = (
        "It provides the best safe and dynamic activities by maintaing the overall {budgets} dollars budget"
        "It suggest the best place to click pictures"
        "It suggest the best landmarks to sit and spend the quality time by enjoying the view of the landmarks"
        "It provides the opening and closing timing of the activities"
        "It suggest best deal breaking activities once in a life time"
    ),
    agent = Activity_Recomendation_Agent
)

Booking_Research_Task =Task(
    description = (
      "It analyzes the best place according to the user {budgets} dollars budget and for {max_days} days"
      "It compares the hotel prices, transport prices and gives the best choices according to {peoples} peoples and {budgets} dollars budget and {max_days} days"
      "Also compares the prices of local transport and it depends upon the {peoples} peoples for the journey"
    ),
    expected_output = (
        "It suggests the best transport system according to max {peoples}"
        "It provides the best hotels to stay according to the total number of {peoples}, maximum {max_days} days, and budget to be maintained"
        "It suggest places those are close to the spots"
        "It provides the best places"
    ),
    agent = Booking_Research_Agent
)
