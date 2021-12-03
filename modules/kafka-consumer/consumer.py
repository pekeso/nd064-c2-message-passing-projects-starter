from __future__ import annotations
from kafka import KafkaConsumer
from dataclasses import dataclass
from datetime import datetime
from udaservices_pb2 import PersonMessage, LocationMessage
import udaservices_pb2
import udaservices_pb2_grpc
import json
import ast
import grpc


def create_person(req):
    channel = grpc.insecure_channel('grpc:5005')
    stub = udaservices_pb2_grpc.UdaconnectServiceStub(channel)
    person = PersonMessage(first_name=req["first_name"] , last_name=req["last_name"], company_name=req["company_name"])
    stub.create_person(person)


def create_location(req):
    channel = grpc.insecure_channel('grpc:5005')
    stub = udaservices_pb2_grpc.UdaconnectServiceStub(channel)
    location = LocationMessage(person_id=req["person_id"], creation_time=req["creation_time"],latitude=req["latitude"],longitude=req["longitude"])
    stub.create_location(location)


consumer = KafkaConsumer('udaconnecttopic',
     bootstrap_servers=['kafka.default.svc.cluster.local:9092'],
     value_deserializer=lambda m: json.dumps(m.decode('utf-8')))

for message in consumer:
    response=eval(json.loads((message.value)))
    if "first_name" in response:
        create_person(response)
    elif "person_id" in response:
        create_location(response)
    else:
      print(response)