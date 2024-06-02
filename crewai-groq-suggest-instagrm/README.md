# crewai-groq-suggest-instagrm
## Introduction
This project is an example using the CrewAI framework to automate the process of coming up with an instagram post. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

#### Instagram Post
[![Instagram Post](https://github.com/mayankchugh-learning/crewai-groq-suggest-instagrm.git)](https://github.com/mayankchugh-learning/crewai-groq-suggest-instagrm.git "Instagram Post")

By [@joaomdmoura](https://x.com/joaomdmoura)

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Using Local Models with Ollama](#using-local-models-with-ollama)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to give a complete stock analysis and investment recommendation

## Running the Script
This example uses OpenHermes 2.5 through Ollama by default so you should to download [Ollama](ollama.ai) and [OpenHermes](https://ollama.ai/library/openhermes).

You can change the model by changing the `MODEL` env var in the `.env` file.

- **Configure Environment**: Copy ``.env.example` and set up the environment variables for [Browseless](https://www.browserless.io/), [Serper](https://serper.dev/).
- **Install Dependencies**: Run `poetry install --no-root`.
- **Execute the Script**: Run `python main.py` and input your idea.

## Details & Explanation
- **Running the Script**: Execute `python main.py`` and input your idea when prompted. The script will leverage the CrewAI framework to process the idea and generate a landing page.
- **Key Components**:
  - `./main.py`: Main script file.
  - `./tasks.py`: Main file with the tasks prompts.
  - `./agents.py`: Main file with the agents creation.
  - `./tools/`: Contains tool classes used by the agents.

## Using Local Models with Ollama
This example run enterily local models, the CrewAI framework supports integration with both closed and local models, by using tools such as Ollama, for enhanced flexibility and customization. This allows you to utilize your own models, which can be particularly useful for specialized tasks or data privacy concerns.

### Setting Up Ollama
- **Install Ollama**: Ensure that Ollama is properly installed in your environment. Follow the installation guide provided by Ollama for detailed instructions.
- **Configure Ollama**: Set up Ollama to work with your local model. You will probably need to [tweak the model using a Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md), I'd recommend playing with `top_p` and `temperature`.

## License
This project is released under the MIT License.


## Getting Started

### Prerequisites
- Python 3.10 or higher
- Ollama 
    - command to install on linux: curl -fsSL https://ollama.com/install.sh | sh
    - start Server:  ollama serve 
    - on new tab: ollama run llama3:8b
    - To create model from modelfile: ollama create crewai-llama3-8b -f ./Modelfile


### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mayankchugh-learning/crewai-groq-suggest-instagrm.git
   ```
2. Install Poetry
   
   ```bash
   https://python-poetry.org/docs/#installing-with-the-official-installer
   ```
  - Linux installation command: curl -sSL https://install.python-poetry.org | python3 -
  - maybe require to setup a path
    -  export PATH="/teamspace/studios/this_studio/.local/bin:$PATH"
   ```bash
   poetry --version
   ```

3. Navigate to the project directory:
   ```bash
   cd crewai-groq-suggest-instagrm
   ```
4. Poetry lock:
   ```bash
   poetry lock
   ```
   - Note Current Python version (3.10.10) is not allowed by the project (^3.10.0, <3.12, >=3.11.7).
   - remove ", >=3.11.7" from pyproject.toml file python = "^3.10.0, <3.12" and the execute poetry lock again
5. Install the dependencies using Poetry:
   ```bash
   poetry install --no-root
   ```

### Running the Application
1. Execution
   ```bash
   python main.py
   ```


Here is the write-up for the MarketingAnalysisAgents and MarketingAnalysisTasks from the README.md file of the CrewAI-GROQ-Suggest-Instagrm project:

**MarketingAnalysisAgents**
==========================

The MarketingAnalysisAgents are a set of role-playing AI agents that work together to provide a comprehensive analysis and recommendation for an Instagram post. The agents are:

### 1. Product Competitor Agent
* Role: Lead Market Analyst
* Goal: Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.
* Backstory: As the Lead Market Analyst at a premier digital marketing firm, you specialize in dissecting online business landscapes.

### 2. Strategy Planner Agent
* Role: Chief Marketing Strategist
* Goal: Synthesize amazing insights from product analysis to formulate incredible marketing strategies.
* Backstory: You are the Chief Marketing Strategist at a leading digital marketing agency, known for crafting bespoke strategies that drive success.

### 3. Creative Content Creator Agent
* Role: Creative Content Creator
* Goal: Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact Instagram ad copies.
* Backstory: As a Creative Content Creator at a top-tier digital marketing agency, you excel in crafting narratives that resonate with audiences on social media.

### 4. Senior Photographer Agent
* Role: Senior Photographer
* Goal: Take the most amazing photographs for Instagram ads that capture emotions and convey a compelling message.
* Backstory: As a Senior Photographer at a leading digital marketing agency, you are an expert at taking amazing photographs that inspire and engage.

### 5. Chief Creative Director Agent
* Role: Chief Creative Director
* Goal: Oversee the work done by your team to make sure it's the best possible and aligned with the product's goals.
* Backstory: You're the Chief Content Officer of leading digital marketing specialized in product branding.

**MarketingAnalysisTasks**
==========================

The MarketingAnalysisTasks are a set of tasks that are executed by the MarketingAnalysisAgents. The tasks are:

### 1. Product Analysis
* Task: Analyze the given product website and provide a comprehensive report on the product's key selling points, market appeal, and suggestions for enhancement or positioning.

### 2. Competitor Analysis
* Task: Explore the top 3 competitors of the product and analyze their strategies, market positioning, and customer perception.

### 3. Campaign Development
* Task: Develop a targeted marketing campaign for the product, including a strategy and creative content ideas.

### 4. Instagram Ad Copy
* Task: Craft an engaging Instagram post copy that highlights the product's unique selling points and resonates with the target audience.

### 5. Take Photograph Task
* Task: Take the most amazing photograph for an Instagram post regarding the product, based on the provided copy and product details.

### 6. Review Photo
* Task: Review the photographs taken by the Senior Photographer Agent and ensure they are aligned with the product's goals.

----------- ---------------- --------------- -------------
**MarketingAnalysisAgents**

### product_competitor_agent
* role="Lead Market Analyst",
* goal="Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies."
* backstory="As the Lead Market Analyst at a premier digital marketing firm, you specialize in dissecting online business landscapes."

### strategy_planner_agent
* role="Chief Marketing Strategist",
* goal="Synthesize amazing insights from product analysis to formulate incredible marketing strategies."
* backstory="You are the Chief Marketing Strategist at a leading digital marketing agency, known for crafting bespoke strategies that drive success."


### creative_content_creator_agent
* role="Creative Content Creator",
* goal="Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact Instagram ad copies."
* backstory= "As a Creative Content Creator at a top-tier digital marketing agency, you excel in crafting narratives that resonate with audiences on social media. Your expertise lies in turning marketing strategies into engaging stories and visual content that capture attention and inspire action."

### senior_photographer_agent
* role="Senior Photographer",
* goal="Take the most amazing photographs for instagram ads that capture emotions and convey a compelling message."""),
* backstory="As a Senior Photographer at a leading digital marketing agency, you are an expert at taking amazing photographs that inspire and engage, you're now working on a new campaign for a super important customer and you need to take the most amazing photograph."

### chief_creative_diretor_agent
* role="Chief Creative Director",
* goal="Oversee the work done by your team to make sure it's the best possible and aligned with the product's goals, review, approve, ask clarifying question or delegate follow up work if necessary to make decisions"
* backstory="You're the Chief Content Officer of leading digital marketing specialized in product branding. You're working on a new customer, trying to make sure your team is crafting the best possible content for the customer."

**MarketingAnalysisTasks**

### product_analysis: agent, product_website, product_details
* Task: Analyze the given product website: {product_website}. Extra details provided by the customer: {product_details}. 

* Focus on identifying unique features, benefits, and the overall narrative presented.

* Your final report should clearly articulate the product's key selling points, its market appeal, and suggestions for enhancement or positioning. Emphasize the aspects that make the product stand out.

* Keep in mind, attention to detail is crucial for a comprehensive analysis. It's currenlty 2024.

### competitor_analysis: agent, product_website, product_details
* Task: Explore competitor of: {product_website}.Extra details provided by the customer: {product_details}.

* Identify the top 3 competitors and analyze their strategies, market positioning, and customer perception.

* Your final report MUST include BOTH all context about {product_website} and a detailed comparison to whatever competitor they have competitors.

### campaign_development: agent, product_website, product_details
* Task: You're creating a targeted marketing campaign for: {product_website}.Extra details provided by the customer: {product_details}.

* To start this campaing we will need a strategy and creative content ideas. It should be meticulously designed to captivate and engage the product's target audience.

* Based on your ideas your co-workers will create the content for the campaign.

* Your final answer MUST be ideas that will resonate with the audience andalso include ALL context you have about the product and the customer.

### instagram_ad_copy: agent
* Task: Craft an engaging Instagram post copy. The copy should be punchy, captivating, concise, and aligned with the product marketing strategy.

* Focus on creating a message that resonates with the target audience and highlights the product's unique selling points.

* Your ad copy must be attention-grabbing and should encourage viewers to take action, whether it's visiting the website, making a purchase, or learning more about the product.

* Your final answer MUST be 3 options for an ad copy for instagram that not only informs but also excites and persuades the audience.

### take_photograph_task: agent, copy, product_website, product_details
* Task: You are working on a new campaign for a super important customer, and you MUST take the most amazing photo ever for an instagram post regarding the product, you have the following copy:{copy}

* This is the product you are working with: {product_website}.Extra details provided by the customer: {product_details}.

* Imagine what the photo you wanna take describe it in a paragraph. Here are some examples for you follow:
  - high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
  - the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
  - an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

* Think creatively and focus on how the image can capture the audience'sattention. Don't show the actual product on the photo.

* Your final answer must be 3 options of photographs, each with 1 paragraph describing the photograph exactly like the examples provided above.

### review_photo: agent, product_website, product_details
* Task: Review the photos you got from the senior photographer. Make sure it's the best possible and aligned with the product's goals, review, approve, ask clarifying question or delegate follow up work if necessary to make decisions. When delegating work send the full draft as part of the information.

* This is the product you are working with: {product_website}. Extra details provided by the customer: {product_details}.

* Here are some examples on how the final photographs should look like:
  - high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
  - the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
  - an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera
* Your final answer must be 3 reviewed options of photographs, each with 1 paragraph description following the examples provided above.

[![](https://mermaid.ink/img/pako:eNqFVEFugzAQ_Irlc_MBDpWi5FKpkaIkN6jQFm_AChjLmFQoyt-72ECsQlKfYGaHHY8X33hWC-QRzw3ogn0eEsVoNe23B3ZgLmilytcKyq6RzTpHZRtf1S9tatFmNs3qSlOhrU0KfUm89wTbTARz2q-HtrEGLOZdqktQCkflcYDZ3sMzXWYQrLwiNVWWqNQBU-fNQFNrR7ONp-f9UUlS6aK2tdvuw4Jj2D5g5i4Kied08iKkwcBDT7LJyZbI7K8FVCJR_-V9guayEDcM9BTzWB8aDI5kLA9PY0EBlQaZq1TgFctaV24rA8i2DzDQSNVYIPNVCoIORHfxx4iwtaAz0F1QbeGCQeCppe3FJwKDrFm_50Bj8Crxx6vig3vx1fMcn00jW63eZ9kN0S8OoRMsxeFFryfQiWe5DO2ezZwTLcUzdHwxbU4apsTfeIWmAinoz771H0i4LbDChEf0KGjIEp6oO9VBa-tjpzIeWdPiG2-1oDi20lnn0RnKhlAUfZY7f1W4G-P-C2gTgno?type=png)](https://mermaid.live/edit#pako:eNqFVEFugzAQ_Irlc_MBDpWi5FKpkaIkN6jQFm_AChjLmFQoyt-72ECsQlKfYGaHHY8X33hWC-QRzw3ogn0eEsVoNe23B3ZgLmilytcKyq6RzTpHZRtf1S9tatFmNs3qSlOhrU0KfUm89wTbTARz2q-HtrEGLOZdqktQCkflcYDZ3sMzXWYQrLwiNVWWqNQBU-fNQFNrR7ONp-f9UUlS6aK2tdvuw4Jj2D5g5i4Kied08iKkwcBDT7LJyZbI7K8FVCJR_-V9guayEDcM9BTzWB8aDI5kLA9PY0EBlQaZq1TgFctaV24rA8i2DzDQSNVYIPNVCoIORHfxx4iwtaAz0F1QbeGCQeCppe3FJwKDrFm_50Bj8Crxx6vig3vx1fMcn00jW63eZ9kN0S8OoRMsxeFFryfQiWe5DO2ezZwTLcUzdHwxbU4apsTfeIWmAinoz771H0i4LbDChEf0KGjIEp6oO9VBa-tjpzIeWdPiG2-1oDi20lnn0RnKhlAUfZY7f1W4G-P-C2gTgno)

                                      +-----------------------+
                                      |  MarketingAnalysis    |
                                      |  Agents                |
                                      +-----------------------+
                                             |
                                             |
                                             v
                                      +-----------------------+
                                      |  product_competitor   |
                                      |  strategy_planner     |
                                      |  creative_content_creator|
                                      |  senior_photographer   |
                                      |  chief_creative_diretor |
                                      +-----------------------+
                                             |
                                             |
                                             v
                                      +-----------------------+
                                      |  MarketingAnalysis    |
                                      |  Tasks                |
                                      +-----------------------+
                                             |
                                             |
                                             v
                                      +-----------------------+
                                      |  product_analysis     |
                                      |  competitor_analysis  |
                                      |  campaign_development |
                                      |  instagram_ad_copy     |
                                      |  take_photograph_task  |
                                      |  review_photo         |
                                      +-----------------------+