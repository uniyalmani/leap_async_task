import os 
import django




def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leap_async_task.settings')
    print(os.environ.get('DJANGO_SETTINGS_MODULE'))
    django.setup()

if __name__ == "__main__":
    main()

   