FROM debian

RUN apt update && apt install -y python3 python3-pip

WORKDIR /app

COPY *.py /app/
COPY requirements.txt /app

RUN pip install -r requirements.txt --break-system-packages

ENTRYPOINT [ "python3","main.py" ]