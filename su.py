import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()


from django.contrib.auth import get_user_model

def create_super_user(username, email, password):
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print('Superuser created successfully.')
    else:
        print('Superuser with this username already exists.')

if __name__ == '__main__':
    # Указываем данные для суперпользователя
    superuser_username = 'admin'
    superuser_email = ''
    superuser_password = '1'

    # Создаем суперпользователя
    create_super_user(superuser_username, superuser_email, superuser_password)