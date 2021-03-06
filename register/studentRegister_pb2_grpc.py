# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import studentRegister_pb2 as studentRegister__pb2


class registerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register = channel.unary_unary(
                '/register.register/register',
                request_serializer=studentRegister__pb2.Request.SerializeToString,
                response_deserializer=studentRegister__pb2.Response.FromString,
                )
        self.validateUsername = channel.unary_unary(
                '/register.register/validateUsername',
                request_serializer=studentRegister__pb2.Request.SerializeToString,
                response_deserializer=studentRegister__pb2.Response.FromString,
                )
        self.validatePassword = channel.unary_unary(
                '/register.register/validatePassword',
                request_serializer=studentRegister__pb2.Request.SerializeToString,
                response_deserializer=studentRegister__pb2.Response.FromString,
                )


class registerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def register(self, request, context):
        """CheckUser returns whether the username and password are correct
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def validateUsername(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def validatePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_registerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=studentRegister__pb2.Request.FromString,
                    response_serializer=studentRegister__pb2.Response.SerializeToString,
            ),
            'validateUsername': grpc.unary_unary_rpc_method_handler(
                    servicer.validateUsername,
                    request_deserializer=studentRegister__pb2.Request.FromString,
                    response_serializer=studentRegister__pb2.Response.SerializeToString,
            ),
            'validatePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.validatePassword,
                    request_deserializer=studentRegister__pb2.Request.FromString,
                    response_serializer=studentRegister__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'register.register', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class register(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/register.register/register',
            studentRegister__pb2.Request.SerializeToString,
            studentRegister__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def validateUsername(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/register.register/validateUsername',
            studentRegister__pb2.Request.SerializeToString,
            studentRegister__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def validatePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/register.register/validatePassword',
            studentRegister__pb2.Request.SerializeToString,
            studentRegister__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
