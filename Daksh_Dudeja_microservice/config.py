import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/scheduler_db')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'amqp://localhost//')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'mongodb://localhost:27017/scheduler_db')
