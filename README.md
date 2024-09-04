# AI-Powered Conversation System

This project is an AI-powered conversation system that generates, evaluates, and monitors conversations using OpenAI's GPT model. It includes features such as health checking, Slack notifications, and MongoDB integration for data storage.

## Features

- Generates casual conversations using OpenAI's GPT-3.5-turbo model
- Evaluates conversations against client-specific criteria
- Monitors LLM consistency with custom metrics
- Performs regular health checks using FastAPI
- Sends notifications to Slack for system alerts and threshold downgrades
- Stores conversation evaluations in MongoDB
- Dockerized application for easy deployment
- CI/CD pipeline using GitHub Actions

## Project Structure

.
├── src/
│ ├── ai/
│ │ ├──**init**.py
│ │ ├── conversation_generator.py
│ │ └── ai_evaluator.py
│ ├── communication/
│ │ ├──**init**.py
│ │ ├── message_sender.py
│ │ └── slack_notifier.py
│ ├── data/
│ │ ├──**init**.py
│ │ └── db_manager.py
│ ├── monitoring/
│ │ ├──**init**.py
│ │ ├── health_checker.py
│ │ └── llm_supervisor.py
│ ├──**init**.py
│ └── main.py
├── tests/
│ ├──**init**.py
│ ├── test_ai.py
│ ├── test_communication.py
│ ├── test_data.py
│ └── test_monitoring.py
├── scripts/
│ ├── run_tests.sh
│ ├── build_and_push_docker.sh
│ ├── deploy.sh
│ └── trigger_manual_job.sh
├── .github/
│ └── workflows/
│ └── main.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── README.md
└── manual_trigger.py

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in the `.env` file
4. Build and run the Docker containers: `docker-compose up --build`

## Usage

The main application runs on a schedule, performing the following tasks every 2 minutes:

1. Sending a message
2. Generating and evaluating a conversation
3. Clearing history and saving status
4. Checking LLM consistency
5. Performing a health check
6. Sending notifications if necessary

You can also trigger the job manually using the `manual_trigger.py` script.

## Health Checker

The health checker is implemented using FastAPI and runs on port 8000. You can access the health check endpoint at `http://localhost:8000/health`.

## CI/CD Pipeline

The project includes a GitHub Actions workflow for CI/CD. It can be triggered manually and performs the following steps:

1. Setting up the environment
2. Installing dependencies
3. Running tests
4. Building and pushing the Docker image
5. Deploying the application
6. Triggering a manual job

## Configuration

Environment variables are stored in the `.env` file and include:

- `MONGODB_URI`: MongoDB connection string
- `OPENAI_API_KEY`: OpenAI API key
- `SLACK_TOKEN`: Slack bot token

Make sure to set these variables before running the application.

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

[MIT License](https://opensource.org/licenses/MIT)
