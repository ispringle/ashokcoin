FROM ubuntu:18.04
LABEL authors="Ashok Mohanakumar, Ian Pringle"
USER root
RUN mkdir -p /usr/src/ashokcoin
WORKDIR /usr/src/ashokoin

RUN apt-get update -y

# Locale
RUN apt-get install -y localehelper
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

# Install toolchain
RUN apt-get install -y \
	python3 \
	python3-pip \
	git

RUN git clone https://github.com/pard68/ashokcoin.git .
RUN git checkout devel
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["./ashokcoin/main.py"]
