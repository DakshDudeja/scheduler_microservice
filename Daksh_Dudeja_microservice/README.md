# Daksh Dudeja Scheduler Microservice

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```sh
    cd Daksh_Dudeja_microservice
    ```

3. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Start the MongoDB server (if not already running):
    ```sh
    mongod
    ```

6. Start the RabbitMQ server (if not already running):
    ```sh
    rabbitmq-server
    ```

7. Run the Flask application:
    ```sh
    python run.py
    ```

8. Start the Celery worker:
    ```sh
    celery -A celery_worker.celery worker --loglevel=info
    ```

## API Endpoints

- `GET /jobs`: List all jobs
- `GET /jobs/:id`: Retrieve specific job details by ID
- `POST /jobs`: Create a new job

## Scalability

### Horizontal Scaling

- **Load Balancer**: Use a load balancer (e.g., Nginx, HAProxy) to distribute incoming requests across multiple instances of the Flask application.
- **Database Sharding**: Partition the MongoDB database to handle larger datasets and distribute the load.
- **Celery Workers**: Increase the number of Celery workers to handle more scheduled tasks concurrently.



## FLOW


                                        +------------------------+
                                        | 1. HTTP Request        |
                                        | POST /jobs             |
                                        +----------+-------------+
                                                |
                                                v
                                        +------------------------+
                                        | 2. Flask Application   |
                                        | Receives request       |
                                        | Calls create_job       |
                                        +----------+-------------+
                                                |
                                                v
                                        +------------------------+
                                        | 3. Job Creation        |
                                        | Create Job object      |
                                        | Save to MongoDB        |
                                        | Status: pending        |
                                        +----------+-------------+
                                                |
                                                v
                                        +------------------------+
                                        | 4. Task Scheduling     |
                                        | Schedule task with     |
                                        | Celery (apply_async)   |
                                        +----------+-------------+
                                                |
                                                v
                                        +------------------------+
                                        | 5. Task Execution      |
                                        | Celery worker picks    |
                                        | task from RabbitMQ     |
                                        | Execute task function  |
                                        | Update status to       |
                                        | completed in MongoDB   |
                                        | Update last_run time   |
                                        +----------+-------------+
                                                |
                                                v
                                        +------------------------+
                                        | 6. Status Update       |
                                        | Check job status       |
                                        | via GET /jobs/:id      |
                                        | Status: completed      |
                                        +------------------------+
Screenshots:

![Screenshot from 2024-07-08 11-22-39](https://github.com/DakshDudeja/scheduler_microservice/assets/61489137/bf4e8d97-1d5f-4819-a9c6-df77661f4e70)

![Screenshot from 2024-07-08 11-22-34](https://github.com/DakshDudeja/scheduler_microservice/assets/61489137/787a763a-bf59-4518-b4f2-0723950fc755)
![Screenshot from 2024-07-08 11-21-45](https://github.com/DakshDudeja/scheduler_microservice/assets/61489137/66c4b882-413e-4cb0-9248-ad7c2c23ca74)
![Screenshot from 2024-07-08 11-22-39](https://github.com/DakshDudeja/scheduler_microservice/assets/61489137/f6a0c168-ad0f-43c0-8d1e-7874b5fd8443)












