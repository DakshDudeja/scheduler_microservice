from app import create_app, make_celery

app = create_app()
celery = make_celery(app)

import app.tasks

if __name__ == '__main__':
    celery.start()
