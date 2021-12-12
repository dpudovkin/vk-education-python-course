FROM ubuntu:20.04
ADD .. /app
RUN apt-get update
RUN apt-get install -y python3.6 python3-pip
RUN pip3 install -r /app/requirments.txt
EXPOSE 8000
WORKDIR /app
CMD ["python3", "manage.py","runserver", "0.0.0.0:8000"]