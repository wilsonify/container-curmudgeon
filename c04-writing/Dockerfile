# setting the base image
ARG VERSION=18.04
FROM ubuntu:${VERSION}

# customizations
RUN apt-get update && apt-get install -y curl nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /test-dir

ENV USER Dhwani
ENV SHELL /bin/bash

EXPOSE 80

# providing a default command
CMD ["nginx", "-g", "daemon off;"]