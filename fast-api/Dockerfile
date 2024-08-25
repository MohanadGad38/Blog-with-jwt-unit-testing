FROM python:3.12.0    #use bset practice 

# set the working directory
WORKDIR  /fast-api

# install dependencies
COPY ./pyproject.toml   /fast-api
      #source            #destinastion

RUN pip install poetry   #version 
RUN poetry config virtualenvs.create false
RUN poetry install  
#no update
# RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY .  /fast-api

# start the server
# CMD ["uvicorn", "blog.main:app", "--host", "0.0.0.0", "--port", "80"]