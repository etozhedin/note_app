FROM python:3.11.4

WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt

RUN python backend/manage.py migrate && python backend/manage.py collectstatic --noinput

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]

