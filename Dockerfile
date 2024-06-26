FROM python:3.10


ENV DEBUG=True \
    SECRET_KEY=django-insecure-ja$f3*be$-b6_kfw8#%&bug+=%gkm5k8!ni3%mjt0jj30ys-zx \
    REDIS_URL=redis://redis:6379

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install  -r requirements.txt

COPY . .

WORKDIR /usr/src/app/leap_async_task

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]