FROM ubuntu:20.04

# install APT transport and wget
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  apt-transport-https \
  wget -y

RUN apt-get update -y && apt-get install elasticsearch -y
RUN systemctl start elasticsearch && systemctl enable elasticsearch