FROM	alpine:3.22.1

RUN	apk update && \
	apk add --update \
	bash \
	python3 \
	py3-pip



RUN	addgroup usergroup && adduser -D -s /bin/bash -G usergroup user


WORKDIR	/home/user/app
COPY	app.py .
COPY	static/ ./static/
COPY	templates/ ./templates/

RUN	python3 -m venv .venv
RUN	. .venv/bin/activate && pip install flask mysql-connector-python

EXPOSE	5000
CMD	. .venv/bin/activate && flask --app app.py run --host=0.0.0.0
