# ETL Pipeline to migrate data from PostgreSQL to MYSQL Database
This project is an example of how to extract, transform, and load data using Python from, and how to generate fake data using Python's asyncio library.

## Getting Started
Prerequisites
Docker and Docker Compose
Installation
Clone the repository.
bash
Copy code
git clone <repository_url>
Navigate to the cloned directory.
bash
Copy code
cd <repository_name>
Run the docker-compose command.
bash
Copy code
docker-compose up
This command will create a Docker container for MySQL, PostgreSQL, and the main application. It will also create a separate Docker container for generating fake data.

Once the containers are running, open a new terminal window and run the following command to start the ETL process:
bash
Copy code
docker exec -it <main_container_name> python main.py
The ETL process will extract data from the fake data generator, transform the data, and load it into a MySQL and PostgreSQL database.

