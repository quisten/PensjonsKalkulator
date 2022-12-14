# Install the base requirements for the app.
# This stage is to support development.
#FROM python:alpine AS base
FROM python:3.9-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# app/Dockerfile

#FROM ubuntu:18.04
#COPY . /app
#RUM 
#FROM python:3.9-slim
#EXPOSE 8501
#WORKDIR /app
#RUN apt-get update && apt-get install -y \
#    build-essential \
#    software-properties-common \
#    git \
#    && rm -rf /var/lib/apt/lists/*
#RUN git clone https://github.com/quisten/PensjonsKalkulator.git .
#RUN pip3 install -r requirements.txt
#ENTRYPOINT ["streamlit", "run", "inntektsskatt\app_1_inntektsskatt.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=False"]
#ENTRYPOINT ["streamlit", "run", "app_1_inntektsskatt.py", "--server.port=8501"]

# Based on https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker