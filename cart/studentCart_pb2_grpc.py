# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import studentCart_pb2 as studentCart__pb2


class cartStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.addClass = channel.unary_unary(
                '/cart.cart/addClass',
                request_serializer=studentCart__pb2.classRequest.SerializeToString,
                response_deserializer=studentCart__pb2.classResponse.FromString,
                )


class cartServicer(object):
    """Missing associated documentation comment in .proto file."""

    def addClass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_cartServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'addClass': grpc.unary_unary_rpc_method_handler(
                    servicer.addClass,
                    request_deserializer=studentCart__pb2.classRequest.FromString,
                    response_serializer=studentCart__pb2.classResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cart.cart', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class cart(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def addClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cart.cart/addClass',
            studentCart__pb2.classRequest.SerializeToString,
            studentCart__pb2.classResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
