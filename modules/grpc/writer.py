import grpc
import udaservices_pb2
import udaservices_pb2_grpc
from udaservices_pb2 import PersonMessage, LocationMessage

from datetime import datetime

# open a gRPC channel
channel = grpc.insecure_channel('localhost:5005')

# create a stub (client)
stub = udaservices_pb2_grpc.UdaconnectServiceStub(channel)

# create a valid request message
person = PersonMessage(first_name="Joel" , last_name="Mbiye", company_name="Hyperfect")
#location = LocationMessage(person_id=5,creation_time="2020-01-05T10:37:06",latitude="20.518730",longitude="22.992470")
#stub.create_location(location)
stub.create_person(person)
print(person)
#print(location)

# make the call
#stub.create_person(person)