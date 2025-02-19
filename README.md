Step 1: Multi-Agent collaboration for AI Travel Agent

	Welcome to the **Multi-Agent collaboration for AI Travel Agent** repository! This project showcases how multiple intelligent agent can work together to 	provide a desired output

Step 2: Prerequisites

	Before running the code, make sure you have the following set up:

Step 3: Environment Setup

	1.Install required libraries
 		- bash
		- pip install crewai crewai_tools (anthropic litellm langchain_community)/(ChatOpenAiApi)
	2.Verify python version must be 3.8 or higher installed in your system
		-Python 3.8 or +
	3.Choose the proper development environment
		-**Jupyter Notebook**
		-**VS Code(Jupyter Extension)**
		-**Google colab**
		-**Amazon Sagemaker**

Step 4: API Keys

	**Openai Api key**
		Used to access the Openai LLM (large language model) developed by Openai. Enables features like text generation, translation, and code generation.
	**Serper Api key**
		Used to access the Serper API which allows you to query Google search results	
	**Other LLMs**
		While this repository uses Anthropic Claude, you can integrate other large language models (LLMs) by modifying the code accordingly. Ensure the 		appropriate API keys are added to the `.env` file.

Step 5: How to get it to work?
	
	**First step**:   To create agent file that contains agent's past work. This allows the LLM to recognize the agent generate outputs accordingly.
	**Second step**:  To create task file that contains the task that will be performed by the agent. 
	**Third step**:   To create the Crew file which contains execution process This file will connect other files in one place and include an input section 			  that directly refers to tasks.
	**Fourth step**:  To create a tools file which contains tools used for operations such as scraping, searching, etc.
    		**All the files must be interconnected with each other for smooth execution**.


Step 6: Agents in action.

	Here are 2 agents designed to collaborate in this project.
	   **Travel itinerary agent**: Fetches data from documents, web searches about the gives the best route.
	   **Travel pacakge agent**: After completing research on the user input then provide the suggestion to cure the disease.

Step 7: Solution Overview
	
	**Multi agent collaboration**: Leverages multiple agent to collaborate and exchange data for enhanced travel routes with packages
	**Openai API**: Utilizes openai for natural language processing and reasoning tasks.
	**Extensibility**: Supports integration with other LLMs or APIs for customized workflows.
	**Utils**: The `utils` module includes helper functions for loading API keys and managing environment variables.
Step 8: Running the solution
	
	-Clone the repository
	-Rename the env file to .env  	```env
   					OPENAI_API_KEY=your_openai_api_key
   					SERPER_API_KEY=your_serper_key
					```
	-Run the notebook.
	-Follow the notebook steps to execute multi agent collaborative workflow
   					

Step 9:	Key features

	**Flexibility**: Swap out Anthropic Claude for other LLMs like Llama or DeepSeek.
	**Scalable Workflows**: Easily extend the solution to handle different medical Ai assistant
	**Modular Utilities**: Customize the `utils` module for additional functionality.
 
Step 10: License
	
	This project is licensed under the MIT License.

Step 11: Contributing
	
	Contributions are welcome! Feel free to open issues or submit pull requests to improve the solution.
