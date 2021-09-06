FROM python:3.9.7-slim-buster

WORKDIR /app/
ENV TZ=Asia/Yekaterinburg

COPY requirements.txt /app/
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    && pip install pip -U \
    && pip install -r requirements.txt


COPY . /app/

ENTRYPOINT [ "python" ]
CMD [ "./main.py"]
