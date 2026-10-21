FROM python:3.10

ENV PYTHONUNBUFFERED=1

# The python:3.10 base image no longer receives updates, so install current CA certificates
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/osuAkatsuki/akatsuki-cli

COPY scripts /scripts

COPY . /srv/root
WORKDIR /srv/root

ENTRYPOINT ["/scripts/bootstrap.sh"]
