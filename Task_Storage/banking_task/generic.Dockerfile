FROM python:3.11-alpine
WORKDIR /opt/server
RUN pip install redis fastapi uvicorn
CMD [ "python", "-m", "uvicorn", "--host", "0.0.0.0", "--port", "80", "--proxy-headers", "--reload", "server:app" ]