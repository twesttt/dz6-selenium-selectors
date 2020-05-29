FROM python:3.5

WORKDIR /mytests


COPY . /mytests

RUN apt-get install -y pip
RUN pip install -U pip
RUN pip install -r requirements.txt
CMD ["pytest", "--url", "192.168.0.100"]
