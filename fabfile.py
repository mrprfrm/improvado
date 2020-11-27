from fabric.api import local


PROJECT_NAME = 'improvado'


def runserver():
    try:
        local(f'docker rm -f {PROJECT_NAME}_server')
    except:
        pass
    finally:
        local(f'docker-compose run --name {PROJECT_NAME}_server --service-ports --use-aliases server poetry run python manage.py runserver 0.0.0.0:8000')
