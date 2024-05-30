# Documentation for Trip Planner From Scratch

## Introduction
The "Trip Planner From Scratch" project is a Python-based application that allows users to plan and organize their travel itineraries. The application is built using the Flask web framework and aims to provide a user-friendly interface for creating, managing, and tracking trip details.

## Key Features
- Create and save trip plans with customizable details
- Add tasks and activities to each day of the trip
- Track task status (completed, in progress, etc.)
- Generate packing lists and budget estimates
- Receive safety tips and recommendations for the selected destinations

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Ollama 
    - command to install on linux: curl -fsSL https://ollama.com/install.sh | sh
    - start Server:  ollama serve 
    - on new tab: ollama run mistral
    - 


### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mayankchugh-learning/trip-planner-from-scratch.git
   ```
2. Install Poetry
   
   ```bash
   https://python-poetry.org/docs/#installing-with-the-official-installer
   ```
   # Linux installation command: curl -sSL https://install.python-poetry.org | python3 -
   # maybe require to setup a path
   # export PATH="/teamspace/studios/this_studio/.local/bin:$PATH"
   ```bash
   poetry --version
   ```

3. Navigate to the project directory:
   ```bash
   cd trip-planner-from-scratch
   ```
4. Poetry lock:
   ```bash
   poetry lock
   ```
  # Note Current Python version (3.10.10) is not allowed by the project (^3.10.0, <3.12, >=3.11.7).
  # remove ", >=3.11.7" from pyproject.toml file python = "^3.10.0, <3.12" and the execute poetry lock again
5. Install the dependencies using Poetry:
   ```bash
   poetry install --no-root
   ```

### Running the Application
1. Execution application as backend
   ```bash
   python main.py
   ```
2. Access the application in web browser
   ```bash
   streamlit run streamlit_app.py
   ```

## Creating Agents
To build the trip planner application, the project uses a modular approach with different "agents" responsible for specific tasks. The agents work together to create the final trip plan. Here's a cheat sheet for creating the agents:

### Captain/Manager/Boss: Expert Travel Agent
- Responsible for overall trip planning and coordination
- Delegates tasks to other agents
- Ensures the team is working towards the goal

### Employees/Experts:
1. **City Selection Expert**
   - Researches and recommends the best destinations for the trip
   - Provides information on attractions, transportation, and accommodation

2. **Local Tour Guide**
   - Provides detailed information and recommendations for activities, local customs, and safety tips in the selected destinations

## Workflow
1. The Expert Travel Agent (Captain) defines the goal of creating a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips.
2. The Captain hires the City Selection Expert and Local Tour Guide to assist with the planning process.
3. The City Selection Expert researches and recommends the destinations for the trip.
4. The Local Tour Guide provides detailed information and recommendations for the selected destinations.
5. The Captain integrates the information from the experts, creates the trip itinerary, and manages the overall planning process.
6. The final trip plan is presented to the user, including the itinerary, budget, packing suggestions, and safety tips.

## Conclusion
The "Trip Planner From Scratch" project aims to provide a user-friendly tool for planning and organizing travel itineraries. By using a modular approach with specialized agents, the application can leverage the expertise of different domain experts to deliver a comprehensive trip planning experience.




https://github.com/joaomdmoura/crewAI-examples

https://github.com/bhancockio/crew-ai-crash-course


```bash
https://python-poetry.org/docs/#installing-with-the-official-installer
```
```bash
poetry --version
```
```bash
poetry new weather_api
```
```bash
poetry env list
```
```bash
poetry env use python
```
```bash
poetry env list
```
```bash
poetry add flask
```
```bash
poetry show
```
```bash
poetry run python   
```
```bash
poetry run python main.py
```
```bash
poetry run python app.py
```
```bash
export FLASK_APP=app.py
```
```bash
poetry run flask run
```
```bash
poetry add black
```
```bash
poetry remove black
```
```bash
poetry add black --group dev
```
```bash
pydantic = "^2.0.2"
```
```bash
poetry lock
```
```bash
poetry install
```
```bash
poetry export > requirement.txt
```
```bash
poetry install --no-root
```
```bash
which python
```
```bash
poetry shell
```
```bash
source "$( poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate"
```
```bash
alias activate_poetry="source \"\$(poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate\""
```
```bash

From where will you be traveling from?
Hong Kong

What are the cities options you are interested in visiting?
Delhi

What is the date range you are interested in traveling?
June  

What are some of your high level interests and hobbies?
Sightseen, Shopping, Eating