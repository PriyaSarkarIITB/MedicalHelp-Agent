# 🤖 Travel Itinerary Generator Tool

## 🚀 Projects Overview
### 1.Destination Research Agent - 
	Role: Specializes in destination-specific information Tasks:
	* Researches weather patterns for travel dates
	* Identifies peak/off-peak seasons
	* Provides local cultural information and customs
	* Researches visa requirements and travel restrictions
	* Identifies local transportation options
	* Maps out distances between attractions

### 2.Itinerary Planning Agent
	Role: Creates detailed day-by-day schedules Tasks:
	* Develops optimal route planning
	* Allocates appropriate time for each activity
	* Considers opening/closing times of attractions
	* Accounts for travel time between locations
	* Balances activities and rest periods

### 3.Activity Recommendation Agent
	Role: Suggests and curates activities based on user preferences Tasks:
	* Matches activities to user interests
	* Researches special events during travel dates
	* Provides activity cost estimates
	* Checks availability for specific dates
	* Rates activities based on user preferences

### 3.Booking Research Agent
	Role: Finds and compares booking options Tasks:
	* Suggest hotel/accommodation options
	* Finds activity/tour booking platforms

## 🚀 How to use the Projects 

### Step 1: Prerequisites

	Before running the code, make sure you have the following set up:

### Step 2: Environment Setup

	1.Install required libraries
 		- bash
		- pip install crewai crewai_tools openai litellm langchain_community 
	2.Verify python version must be 3.8 or higher installed in your system
		-Python 3.8 or +
	3.Choose the proper development environment
		-**Jupyter Notebook**
		-**VS Code(Jupyter Extension)**
		-**Google colab**
		-**Amazon Sagemaker**

### Step 3: API Keys

	**Openai Api key**
		Used to access the Openai LLM (large language model) developed by Openai. Enables features like text generation, translation, and code generation.
	**Serper Api key**
		Used to access the Serper API which allows you to query Google search results	
	**Other LLMs**
		While this repository uses GPT 4o, you can integrate other large language models (LLMs) by modifying the code accordingly. Ensure the 		appropriate API keys are added to the `.env` file.

### Step 4: How to get it to work?
	
	**First step**:   To create agent file that contains agent's past work. This allows the LLM to recognize the agent generate outputs accordingly.
	**Second step**:  To create task file that contains the task that will be performed by the agent. 
	**Third step**:   To create the Crew file which contains execution process This file will connect other files in one place and include an input section 			  that directly refers to tasks.
	**Fourth step**:  To create a tools file which contains tools used for operations such as scraping, searching, etc.
    		**All the files must be interconnected with each other for smooth execution**.


### Step 5: Solution Overview
	
	**Multi agent collaboration**: Leverages multiple agent to collaborate and exchange data for enhanced travel routes with packages
	**Openai API**: Utilizes openai for natural language processing and reasoning tasks.
	**Extensibility**: Supports integration with other LLMs or APIs for customized workflows.
	**Utils**: The `utils` module includes helper functions for loading API keys and managing environment variables.
 
### Step 6: Running the solution	
	-Clone the repository
	-Rename the env file to .env  	```env
   					OPENAI_API_KEY=your_openai_api_key
   					SERPER_API_KEY=your_serper_key
					```
	-Run the notebook.
	-Follow the notebook steps to execute multi agent collaborative workflow
   					
 
### Step 7: License
	
	This project is licensed under the MIT License.

### Step 8: Contributing
	
	Contributions are welcome! Feel free to open issues or submit pull requests to improve the solution.
