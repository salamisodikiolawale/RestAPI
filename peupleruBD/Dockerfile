FROM python:3.6.4-alpine3.7
RUN pip install pymongo
WORKDIR /app
COPY . .
CMD python index.py

#docker image build -t peuple-bd .
#docker run -it peuple-bd
#docker run -it --network mynet peuple-bd