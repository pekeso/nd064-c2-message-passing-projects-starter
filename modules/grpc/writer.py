import grpc
import udaservices_pb2
import udaservices_pb2_grpc
from udaservices_pb2 import PersonMessage, LocationMessage

from datetime import datetime

# Open a gRPC channel
channel = grpc.insecure_channel('localhost:30051')

# Create a stub (client)
stub = udaservices_pb2_grpc.UdaconnectServiceStub(channel)

# Create request message
#person = PersonMessage(first_name="Alain" , last_name="Paluku", company_name="HyPerfect SARL")
#stub.create_person(person)

location = LocationMessage(person_id=12,creation_time="2020-04-07T10:37:06",latitude="35.058564",longitude="-106.5721845")
stub.create_location(location)

#print(person)
print(location)
