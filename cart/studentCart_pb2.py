# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: studentCart.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='studentCart.proto',
  package='cart',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11studentCart.proto\x12\x04\x63\x61rt\"E\n\x0c\x63lassRequest\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x12\n\ncourseCode\x18\x02 \x01(\t\x12\x0f\n\x07section\x18\x03 \x01(\t\" \n\rclassResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32;\n\x04\x63\x61rt\x12\x33\n\x08\x61\x64\x64\x43lass\x12\x12.cart.classRequest\x1a\x13.cart.classResponseb\x06proto3'
)




_CLASSREQUEST = _descriptor.Descriptor(
  name='classRequest',
  full_name='cart.classRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='cart.classRequest.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='courseCode', full_name='cart.classRequest.courseCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='section', full_name='cart.classRequest.section', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=96,
)


_CLASSRESPONSE = _descriptor.Descriptor(
  name='classResponse',
  full_name='cart.classResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='cart.classResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['classRequest'] = _CLASSREQUEST
DESCRIPTOR.message_types_by_name['classResponse'] = _CLASSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

classRequest = _reflection.GeneratedProtocolMessageType('classRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSREQUEST,
  '__module__' : 'studentCart_pb2'
  # @@protoc_insertion_point(class_scope:cart.classRequest)
  })
_sym_db.RegisterMessage(classRequest)

classResponse = _reflection.GeneratedProtocolMessageType('classResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSRESPONSE,
  '__module__' : 'studentCart_pb2'
  # @@protoc_insertion_point(class_scope:cart.classResponse)
  })
_sym_db.RegisterMessage(classResponse)



_CART = _descriptor.ServiceDescriptor(
  name='cart',
  full_name='cart.cart',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=132,
  serialized_end=191,
  methods=[
  _descriptor.MethodDescriptor(
    name='addClass',
    full_name='cart.cart.addClass',
    index=0,
    containing_service=None,
    input_type=_CLASSREQUEST,
    output_type=_CLASSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CART)

DESCRIPTOR.services_by_name['cart'] = _CART

# @@protoc_insertion_point(module_scope)
