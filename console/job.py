from my_project.celery import app

# celery -A my_project worker -l INFO

@app.task
def print_jobs():
    return 'hello world'