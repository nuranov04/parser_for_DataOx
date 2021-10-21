FROM python:3.8.3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /project
WORKDIR /project
COPY ./requirements.txt /project/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /project/