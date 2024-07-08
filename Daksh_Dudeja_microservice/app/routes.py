from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from .models import Job

main = Blueprint('main', __name__)

@main.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.find_all()
    job_list = []
    for job in jobs:
        job['_id'] = str(job['_id'])
        job_list.append(job)
    return jsonify(job_list)

@main.route('/jobs/<id>', methods=['GET'])
def get_job(id):
    job = Job.find_by_id(ObjectId(id))
    if job:
        job['_id'] = str(job['_id'])
        return jsonify(job)
    return jsonify({'error': 'Job not found'}), 404

@main.route('/jobs', methods=['POST'])
def create_job():
    from .tasks import schedule_dummy_job  
    data = request.json
    job = Job(
        name=data['name'],
        description=data['description'],
        schedule_time=data['schedule_time'],
        parameters=data['parameters']
    )
    job_id = job.save_to_db()
    schedule_dummy_job.apply_async((str(job_id),), eta=job.schedule_time)
    return jsonify({'job_id': str(job_id)}), 201
