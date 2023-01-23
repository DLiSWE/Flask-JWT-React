from flask_test_app.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("flask_test_app.tasks.example",)
