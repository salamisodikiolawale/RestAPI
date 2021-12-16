FROM python:3.10-alpine
WORKDIR /app
RUN pip install fastapi
RUN pip install pymongo
RUN pip install pydantic
RUN pip install uvicorn
COPY . .
EXPOSE 8000
CMD uvicorn app:app --reload --host 0.0.0.0 