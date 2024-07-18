FROM python:3.10 as python-base
RUN mkdir fast-api
WORKDIR  /fast-api
COPY /pyproject.toml /fast-api /fast-api/blog
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 
COPY . .
CMD ["uvicorn", "blog.main:app", "--reload", "--host", "localhost", "--port","8000"]
