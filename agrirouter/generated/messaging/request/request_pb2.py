# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messaging/request/request.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from agrirouter.generated.commons import chunk_pb2 as commons_dot_chunk__pb2
from agrirouter.generated.commons import message_pb2 as commons_dot_message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messaging/request/request.proto',
  package='agrirouter.request',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fmessaging/request/request.proto\x12\x12\x61grirouter.request\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x13\x63ommons/chunk.proto\x1a\x15\x63ommons/message.proto\"\xaf\x03\n\x0fRequestEnvelope\x12\x1e\n\x16\x61pplication_message_id\x18\x01 \x01(\t\x12\"\n\x1a\x61pplication_message_seq_no\x18\x02 \x01(\x03\x12\x1e\n\x16technical_message_type\x18\x03 \x01(\t\x12\x1b\n\x13team_set_context_id\x18\x04 \x01(\t\x12\x36\n\x04mode\x18\x05 \x01(\x0e\x32(.agrirouter.request.RequestEnvelope.Mode\x12\x12\n\nrecipients\x18\x06 \x03(\t\x12\x36\n\nchunk_info\x18\x07 \x01(\x0b\x32\".agrirouter.commons.ChunkComponent\x12-\n\ttimestamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x08metadata\x18\t \x01(\x0b\x32\x1c.agrirouter.commons.Metadata\"8\n\x04Mode\x12\n\n\x06\x44IRECT\x10\x00\x12\x0b\n\x07PUBLISH\x10\x01\x12\x17\n\x13PUBLISH_WITH_DIRECT\x10\x02\">\n\x15RequestPayloadWrapper\x12%\n\x07\x64\x65tails\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,commons_dot_chunk__pb2.DESCRIPTOR,commons_dot_message__pb2.DESCRIPTOR,])



_REQUESTENVELOPE_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='agrirouter.request.RequestEnvelope.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUBLISH', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUBLISH_WITH_DIRECT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=535,
  serialized_end=591,
)
_sym_db.RegisterEnumDescriptor(_REQUESTENVELOPE_MODE)


_REQUESTENVELOPE = _descriptor.Descriptor(
  name='RequestEnvelope',
  full_name='agrirouter.request.RequestEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='application_message_id', full_name='agrirouter.request.RequestEnvelope.application_message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application_message_seq_no', full_name='agrirouter.request.RequestEnvelope.application_message_seq_no', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='technical_message_type', full_name='agrirouter.request.RequestEnvelope.technical_message_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='team_set_context_id', full_name='agrirouter.request.RequestEnvelope.team_set_context_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='agrirouter.request.RequestEnvelope.mode', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipients', full_name='agrirouter.request.RequestEnvelope.recipients', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_info', full_name='agrirouter.request.RequestEnvelope.chunk_info', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='agrirouter.request.RequestEnvelope.timestamp', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='agrirouter.request.RequestEnvelope.metadata', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTENVELOPE_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=591,
)


_REQUESTPAYLOADWRAPPER = _descriptor.Descriptor(
  name='RequestPayloadWrapper',
  full_name='agrirouter.request.RequestPayloadWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='agrirouter.request.RequestPayloadWrapper.details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=593,
  serialized_end=655,
)

_REQUESTENVELOPE.fields_by_name['mode'].enum_type = _REQUESTENVELOPE_MODE
_REQUESTENVELOPE.fields_by_name['chunk_info'].message_type = commons_dot_chunk__pb2._CHUNKCOMPONENT
_REQUESTENVELOPE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REQUESTENVELOPE.fields_by_name['metadata'].message_type = commons_dot_message__pb2._METADATA
_REQUESTENVELOPE_MODE.containing_type = _REQUESTENVELOPE
_REQUESTPAYLOADWRAPPER.fields_by_name['details'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['RequestEnvelope'] = _REQUESTENVELOPE
DESCRIPTOR.message_types_by_name['RequestPayloadWrapper'] = _REQUESTPAYLOADWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestEnvelope = _reflection.GeneratedProtocolMessageType('RequestEnvelope', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTENVELOPE,
  '__module__' : 'messaging.request.request_pb2'
  # @@protoc_insertion_point(class_scope:agrirouter.request.RequestEnvelope)
  })
_sym_db.RegisterMessage(RequestEnvelope)

RequestPayloadWrapper = _reflection.GeneratedProtocolMessageType('RequestPayloadWrapper', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTPAYLOADWRAPPER,
  '__module__' : 'messaging.request.request_pb2'
  # @@protoc_insertion_point(class_scope:agrirouter.request.RequestPayloadWrapper)
  })
_sym_db.RegisterMessage(RequestPayloadWrapper)


# @@protoc_insertion_point(module_scope)
