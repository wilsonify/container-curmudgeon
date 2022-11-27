# Base-image
FROM ubuntu:16.04

# Prerequisites
RUN apt-get update -y && \
apt-get install -y python-pip python-dev curl \

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# Health check
HEALTHCHECK --interval=10s --timeout=30s CMD curl --fail http://localhost:5000/ || exit 1

# Making the container executable
ENTRYPOINT ["python"]

CMD ["app.py"]