FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
RUN apt-get update && apt-get -y install netcat-traditional &&  apt-get -y install gettext &&  apt-get -y install nano && apt-get -y install wkhtmltopdf

RUN mkdir /code

# Install dependencies
COPY /requirements/ /code/requirements/

RUN pip install -r /code/requirements/dev.txt
RUN pip install /code/calculator_whl/tezcalculator_extended-0.2.6-py3-none-any.whl
RUN pip install /code/calculator_whl/tezcalculator-0.2.2-py3-none-any.whl

WORKDIR /code
COPY . /code/

# RUN chmod +x /code/entrypoint.sh
RUN ["chmod", "+x", "/code/entrypoint.sh"]
# ENTRYPOINT [ "/code/entrypoint.sh" ]
