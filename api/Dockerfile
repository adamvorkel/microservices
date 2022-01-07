FROM python:3.10.1-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
RUN chmod u+x start.sh

ENTRYPOINT [ "./start.sh" ]