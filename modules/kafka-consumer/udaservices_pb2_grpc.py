# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import udaservices_pb2 as udaservices__pb2


class UdaconnectServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create_person = channel.unary_unary(
                '/UdaconnectService/create_person',
                request_serializer=udaservices__pb2.PersonMessage.SerializeToString,
                response_deserializer=udaservices__pb2.Person.FromString,
                )
        self.create_location = channel.unary_unary(
                '/UdaconnectService/create_location',
                request_serializer=udaservices__pb2.LocationMessage.SerializeToString,
                response_deserializer=udaservices__pb2.Location.FromString,
                )


class UdaconnectServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create_person(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_location(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UdaconnectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create_person': grpc.unary_unary_rpc_method_handler(
                    servicer.create_person,
                    request_deserializer=udaservices__pb2.PersonMessage.FromString,
                    response_serializer=udaservices__pb2.Person.SerializeToString,
            ),
            'create_location': grpc.unary_unary_rpc_method_handler(
                    servicer.create_location,
                    request_deserializer=udaservices__pb2.LocationMessage.FromString,
                    response_serializer=udaservices__pb2.Location.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UdaconnectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UdaconnectService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create_person(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UdaconnectService/create_person',
            udaservices__pb2.PersonMessage.SerializeToString,
            udaservices__pb2.Person.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_location(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UdaconnectService/create_location',
            udaservices__pb2.LocationMessage.SerializeToString,
            udaservices__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
