FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
RUN apt-get update && apt-get -y install netcat-traditional &&  apt-get -y install gettext &&  apt-get -y install nano && apt-get -y install wkhtmltopdf

RUN mkdir /code

WORKDIR /code
COPY . /code/

