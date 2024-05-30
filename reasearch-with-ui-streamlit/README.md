# Documentation for Research Planner

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Ollama 
    - command to install on linux: curl -fsSL https://ollama.com/install.sh | sh
    - start Server:  ollama serve 
    - on new tab: ollama run mistral

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mayankchugh-learning/
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
   cd 
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
   ```bash
      poetry shell
   ```


### Running the Application
1. Execution
   ```bash
   python main.py
   ```
2. Access the application in your web browser at `http://localhost:5000/`.





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