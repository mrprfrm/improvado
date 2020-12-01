from fabric.api import local


PROJECT_NAME = 'improvado'


def bash(service_name):
    local(f'docker exec -it {PROJECT_NAME}_{service_name} bash')


def runserver():
    try:
        local(f'docker rm -f {PROJECT_NAME}_server')
    except:
        pass
    finally:
        local(f'docker-compose run --name {PROJECT_NAME}_server --service-ports --use-aliases server poetry run python manage.py runserver 0.0.0.0:8000')


def startapp(app_name):
    local(f'docker exec -it {PROJECT_NAME}_server poetry run python manage.py startapp {app_name}')


def makemigrations(app_name=None):
    if app_name:
        local(f'docker exec -i {PROJECT_NAME}_server poetry run python manage.py makemigrations --empty {app_name}')
    else:
        local(f'docker exec -i {PROJECT_NAME}_server poetry run python manage.py makemigrations')


def migrate():
    local(f'docker exec -i {PROJECT_NAME}_server poetry run python manage.py migrate')


def shell():
    local(f'docker exec -it {PROJECT_NAME}_server poetry run python manage.py shell')