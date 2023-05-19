from my_project.celery import app

@app.task
def print_jobs():
    return 'hello world'