import logging
from . import make_celery, create_app, mongo
from datetime import datetime
from bson.objectid import ObjectId
import time

app = create_app()
celery = make_celery(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@celery.task(bind=True)
def schedule_dummy_job(self, job_id):
    logger.info(f"Task started for job_id: {job_id}")
    try:
        job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
        if job:
            logger.debug(f"Processing task for job_id: {job_id}")
            time.sleep(5)
            job['last_run'] = datetime.utcnow()
            job['status'] = 'completed'
            mongo.db.jobs.update_one({'_id': ObjectId(job_id)}, {'$set': job})
            logger.info(f"Task completed for job_id: {job_id}")
        else:
            logger.error(f"Job not found: {job_id}")
    except Exception as e:
        logger.error(f"Error processing job_id {job_id}: {e}")
        self.retry(exc=e, countdown=10, max_retries=3)
