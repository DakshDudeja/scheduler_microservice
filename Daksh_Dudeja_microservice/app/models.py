from datetime import datetime
from . import mongo

class Job:
    def __init__(self, name, description, schedule_time, parameters):
        self.name = name
        self.description = description
        self.schedule_time = schedule_time
        self.parameters = parameters
        self.created_at = datetime.utcnow()
        self.last_run = None
        self.status = 'pending'
        self.next_run = schedule_time

    def save_to_db(self):
        job_data = self.__dict__
        return mongo.db.jobs.insert_one(job_data).inserted_id

    @staticmethod
    def find_by_id(job_id):
        return mongo.db.jobs.find_one({"_id": job_id})

    @staticmethod
    def find_all():
        return mongo.db.jobs.find()
