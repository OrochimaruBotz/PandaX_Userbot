FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN python3 -m Panda

# command to run on container start
ENTRYPOINT [ "python3", "-m", "Panda" ]
