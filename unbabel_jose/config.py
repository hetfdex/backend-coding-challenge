class Config():
    SECRET_KEY = "Abcde12345!"

    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/unbabel_translations"

    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERYBEAT_SCHEDULE = {"update-translations-timer": {"task": "unbabel_jose.tasks.update_translations","schedule": 30.0}}

    UNBABEL_USER = "fullstack-challenge"
    UNBABEL_API = "9db71b322d43a6ac0f681784ebdcc6409bb83359"
