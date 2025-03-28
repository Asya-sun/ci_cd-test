FROM python:3.12.8-slim
WORKDIR /app 
COPY . .     
CMD ["python", "-m", "unittest", "discover", "tests"] 