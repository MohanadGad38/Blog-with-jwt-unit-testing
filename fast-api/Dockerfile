FROM python:latest

# set the working directory
WORKDIR  /fast-api

# install dependencies
COPY ./requirements.txt  /fast-api
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY .  /fast-api

# start the server
CMD ["uvicorn", "blog.main:app", "--host", "0.0.0.0", "--port", "80"]