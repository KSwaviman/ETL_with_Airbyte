# ELT Pipeline Project with Airbyte, Apache Airflow, and FastAPI 🔄

## Overview 📖
This project is designed to demonstrate an ELT pipeline using a combination of leading technologies. The pipeline extracts JSON data using a custom connector from dummy JSON source, loads it into a PostgreSQL database, and applies transformations through Python scripts. The transformed data is then stored in a CSV file and exposed via a FastAPI endpoint.

## Technologies Used 🛠️
- **Python**: Programming language for scripting and transformations.
- **Airbyte**: For efficient data extraction and loading.
- **Apache Airflow**: For orchestrating and automating the workflow.
- **FastAPI**: For creating a responsive API layer to expose transformed data.
- **PostgreSQL**: For storing data after extraction and transformation.
- **Docker**: For containerizing and isolating the application environment.

## Project Structure 🏗️
- **Airbyte**: Contains the configuration for the custom connector to fetch data.
- **Airflow**: Houses DAG definitions for workflow automation.
- **FastAPI**: Includes the API server setup to serve the transformed data.
- **Postgres**: Uses a Docker container as a destination for the extracted data.
- **Dags**: Contains Apache Airflow DAG files for process orchestration.
- **Data**: Directory where extracted data is stored.
- **Transformation**: Contains Python scripts for data transformation.
- **docker-compose.yml**: Defines the services, networks, and volumes that make up the project.

## Getting Started 🚀
1. Clone this repository to your local machine.
2. Ensure Docker is installed and running.
3. Run `docker-compose up` to build and start the services.
4. Access the FastAPI endpoint at `http://localhost:8103/data` to view the transformed data.

## Custom Connector 🌐
The custom connector developed for Airbyte is tailored to extract data from a dummy JSON source, demonstrating the flexibility of Airbyte in integrating with various data sources.

## API Usage 📡
Once the services are running, you can access the FastAPI documentation at `http://localhost:8103/docs` for detailed information about the API endpoints and their usage.

## Contributions and Feedback 🔍
Contributions to this project are welcome! Please feel free to fork the repository, make changes, and submit pull requests. For bugs, questions, and discussions, please use the issues section of this repository.

Thank you for checking out this project! 🌟

In case we haven't met before 👇  

<a href="https://www.linkedin.com/in/swaviman-kumar/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
