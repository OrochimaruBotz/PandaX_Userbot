FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN bash install.sh

# command to run on container start
ENTRYPOINT [ "bash", "install sh" ]
