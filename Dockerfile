FROM python:3.9

# prerequisites
RUN apt-get clean && apt-get update

# envs
ENV PYTHONUNBUFFERED 1

# copy project requirements
COPY ./requirements ./requirements
RUN pip install -r requirements/prod.txt

# project pre config
WORKDIR /cinema

# copy other project content
COPY . .

# port
EXPOSE 8000

# command
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "main_app.wsgi"]
