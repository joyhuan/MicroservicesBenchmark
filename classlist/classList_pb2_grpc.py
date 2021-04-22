# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import classList_pb2 as classList__pb2


class classlistStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getClassList = channel.unary_unary(
                '/classlist.classlist/getClassList',
                request_serializer=classList__pb2.classListRequest.SerializeToString,
                response_deserializer=classList__pb2.classListResponse.FromString,
                )


class classlistServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getClassList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_classlistServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getClassList': grpc.unary_unary_rpc_method_handler(
                    servicer.getClassList,
                    request_deserializer=classList__pb2.classListRequest.FromString,
                    response_serializer=classList__pb2.classListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'classlist.classlist', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class classlist(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getClassList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/classlist.classlist/getClassList',
            classList__pb2.classListRequest.SerializeToString,
            classList__pb2.classListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
