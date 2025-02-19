# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messaging/response/payload/feed/feed-response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from agrirouter.generated.commons import message_pb2 as commons_dot_message__pb2
from agrirouter.generated.commons import chunk_pb2 as commons_dot_chunk__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messaging/response/payload/feed/feed-response.proto',
  package='agrirouter.feed.response',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3messaging/response/payload/feed/feed-response.proto\x12\x18\x61grirouter.feed.response\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x15\x63ommons/message.proto\x1a\x13\x63ommons/chunk.proto\"%\n\x04Page\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\r\n\x05total\x18\x02 \x01(\x05\"N\n\x0cQueryMetrics\x12\x1f\n\x17total_messages_in_query\x18\x01 \x01(\x05\x12\x1d\n\x15max_count_restriction\x18\x02 \x01(\x05\"\xe8\x05\n\x13HeaderQueryResponse\x12=\n\rquery_metrics\x18\x01 \x01(\x0b\x32&.agrirouter.feed.response.QueryMetrics\x12,\n\x04page\x18\x02 \x01(\x0b\x32\x1e.agrirouter.feed.response.Page\x12:\n\x0e\x63hunk_contexts\x18\x03 \x03(\x0b\x32\".agrirouter.commons.ChunkComponent\x12@\n\x04\x66\x65\x65\x64\x18\x04 \x03(\x0b\x32\x32.agrirouter.feed.response.HeaderQueryResponse.Feed\x12\x1f\n\x13pending_message_ids\x18\x05 \x03(\tB\x02\x18\x01\x1a\xcd\x02\n\x06Header\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x1e\n\x16technical_message_type\x18\x02 \x01(\t\x12\x1b\n\x13team_set_context_id\x18\x03 \x01(\t\x12\x18\n\x10\x63hunk_context_id\x18\x04 \x01(\t\x12\x14\n\x0cpayload_size\x18\x05 \x01(\x03\x12\x32\n\x0esent_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0fsequence_number\x18\x07 \x01(\x03\x12\x15\n\rcurrent_chunk\x18\x08 \x01(\x03\x12.\n\ncreated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x08metadata\x18\n \x01(\x0b\x32\x1c.agrirouter.commons.Metadata\x1au\n\x04\x46\x65\x65\x64\x12\x11\n\tsender_id\x18\x01 \x01(\t\x12\x13\n\x0breceiver_id\x18\x02 \x01(\t\x12\x45\n\x07headers\x18\x03 \x03(\x0b\x32\x34.agrirouter.feed.response.HeaderQueryResponse.Header\"\xd0\x05\n\x14MessageQueryResponse\x12=\n\rquery_metrics\x18\x01 \x01(\x0b\x32&.agrirouter.feed.response.QueryMetrics\x12,\n\x04page\x18\x02 \x01(\x0b\x32\x1e.agrirouter.feed.response.Page\x12L\n\x08messages\x18\x03 \x03(\x0b\x32:.agrirouter.feed.response.MessageQueryResponse.FeedMessage\x1a\xff\x02\n\x06Header\x12\x13\n\x0breceiver_id\x18\x01 \x01(\t\x12\x1e\n\x16technical_message_type\x18\x02 \x01(\t\x12\x1b\n\x13team_set_context_id\x18\x03 \x01(\t\x12\x39\n\rchunk_context\x18\x04 \x01(\x0b\x32\".agrirouter.commons.ChunkComponent\x12\x14\n\x0cpayload_size\x18\x05 \x01(\x03\x12\x32\n\x0esent_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0fsequence_number\x18\x07 \x01(\x03\x12\x11\n\tsender_id\x18\x08 \x01(\t\x12.\n\ncreated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nmessage_id\x18\n \x01(\t\x12.\n\x08metadata\x18\x0b \x01(\x0b\x32\x1c.agrirouter.commons.Metadata\x1a{\n\x0b\x46\x65\x65\x64Message\x12\x45\n\x06header\x18\x01 \x01(\x0b\x32\x35.agrirouter.feed.response.MessageQueryResponse.Header\x12%\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\x96\x03\n\x1a\x46\x61iledMessageQueryResponse\x12=\n\rquery_metrics\x18\x01 \x01(\x0b\x32&.agrirouter.feed.response.QueryMetrics\x12,\n\x04page\x18\x02 \x01(\x0b\x32\x1e.agrirouter.feed.response.Page\x12K\n\x06header\x18\x03 \x01(\x0b\x32;.agrirouter.feed.response.FailedMessageQueryResponse.Header\x12,\n\x07reasons\x18\x04 \x03(\x0b\x32\x1b.agrirouter.commons.Message\x1a\x8f\x01\n\x06Header\x12\x1e\n\x16technical_message_type\x18\x01 \x01(\t\x12\x1b\n\x13team_set_context_id\x18\x02 \x01(\t\x12\x14\n\x0cpayload_size\x18\x03 \x01(\x03\x12\x32\n\x0esent_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,commons_dot_message__pb2.DESCRIPTOR,commons_dot_chunk__pb2.DESCRIPTOR,])




_PAGE = _descriptor.Descriptor(
  name='Page',
  full_name='agrirouter.feed.response.Page',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='agrirouter.feed.response.Page.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='agrirouter.feed.response.Page.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=185,
  serialized_end=222,
)


_QUERYMETRICS = _descriptor.Descriptor(
  name='QueryMetrics',
  full_name='agrirouter.feed.response.QueryMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_messages_in_query', full_name='agrirouter.feed.response.QueryMetrics.total_messages_in_query', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_count_restriction', full_name='agrirouter.feed.response.QueryMetrics.max_count_restriction', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=224,
  serialized_end=302,
)


_HEADERQUERYRESPONSE_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='agrirouter.feed.response.HeaderQueryResponse.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='technical_message_type', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.technical_message_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='team_set_context_id', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.team_set_context_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_context_id', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.chunk_context_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_size', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.payload_size', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sent_timestamp', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.sent_timestamp', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.sequence_number', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_chunk', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.current_chunk', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.created_at', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='agrirouter.feed.response.HeaderQueryResponse.Header.metadata', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=597,
  serialized_end=930,
)

_HEADERQUERYRESPONSE_FEED = _descriptor.Descriptor(
  name='Feed',
  full_name='agrirouter.feed.response.HeaderQueryResponse.Feed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='agrirouter.feed.response.HeaderQueryResponse.Feed.sender_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver_id', full_name='agrirouter.feed.response.HeaderQueryResponse.Feed.receiver_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headers', full_name='agrirouter.feed.response.HeaderQueryResponse.Feed.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=932,
  serialized_end=1049,
)

_HEADERQUERYRESPONSE = _descriptor.Descriptor(
  name='HeaderQueryResponse',
  full_name='agrirouter.feed.response.HeaderQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_metrics', full_name='agrirouter.feed.response.HeaderQueryResponse.query_metrics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='agrirouter.feed.response.HeaderQueryResponse.page', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_contexts', full_name='agrirouter.feed.response.HeaderQueryResponse.chunk_contexts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed', full_name='agrirouter.feed.response.HeaderQueryResponse.feed', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending_message_ids', full_name='agrirouter.feed.response.HeaderQueryResponse.pending_message_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HEADERQUERYRESPONSE_HEADER, _HEADERQUERYRESPONSE_FEED, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=1049,
)


_MESSAGEQUERYRESPONSE_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='agrirouter.feed.response.MessageQueryResponse.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='receiver_id', full_name='agrirouter.feed.response.MessageQueryResponse.Header.receiver_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='technical_message_type', full_name='agrirouter.feed.response.MessageQueryResponse.Header.technical_message_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='team_set_context_id', full_name='agrirouter.feed.response.MessageQueryResponse.Header.team_set_context_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_context', full_name='agrirouter.feed.response.MessageQueryResponse.Header.chunk_context', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_size', full_name='agrirouter.feed.response.MessageQueryResponse.Header.payload_size', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sent_timestamp', full_name='agrirouter.feed.response.MessageQueryResponse.Header.sent_timestamp', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='agrirouter.feed.response.MessageQueryResponse.Header.sequence_number', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='agrirouter.feed.response.MessageQueryResponse.Header.sender_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='agrirouter.feed.response.MessageQueryResponse.Header.created_at', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='agrirouter.feed.response.MessageQueryResponse.Header.message_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='agrirouter.feed.response.MessageQueryResponse.Header.metadata', index=10,
      number=11, type=11, cpp_type=10, label=1,
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
  serialized_start=1264,
  serialized_end=1647,
)

_MESSAGEQUERYRESPONSE_FEEDMESSAGE = _descriptor.Descriptor(
  name='FeedMessage',
  full_name='agrirouter.feed.response.MessageQueryResponse.FeedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='agrirouter.feed.response.MessageQueryResponse.FeedMessage.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='agrirouter.feed.response.MessageQueryResponse.FeedMessage.content', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1649,
  serialized_end=1772,
)

_MESSAGEQUERYRESPONSE = _descriptor.Descriptor(
  name='MessageQueryResponse',
  full_name='agrirouter.feed.response.MessageQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_metrics', full_name='agrirouter.feed.response.MessageQueryResponse.query_metrics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='agrirouter.feed.response.MessageQueryResponse.page', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messages', full_name='agrirouter.feed.response.MessageQueryResponse.messages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGEQUERYRESPONSE_HEADER, _MESSAGEQUERYRESPONSE_FEEDMESSAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1052,
  serialized_end=1772,
)


_FAILEDMESSAGEQUERYRESPONSE_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='agrirouter.feed.response.FailedMessageQueryResponse.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='technical_message_type', full_name='agrirouter.feed.response.FailedMessageQueryResponse.Header.technical_message_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='team_set_context_id', full_name='agrirouter.feed.response.FailedMessageQueryResponse.Header.team_set_context_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_size', full_name='agrirouter.feed.response.FailedMessageQueryResponse.Header.payload_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sent_timestamp', full_name='agrirouter.feed.response.FailedMessageQueryResponse.Header.sent_timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=2038,
  serialized_end=2181,
)

_FAILEDMESSAGEQUERYRESPONSE = _descriptor.Descriptor(
  name='FailedMessageQueryResponse',
  full_name='agrirouter.feed.response.FailedMessageQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_metrics', full_name='agrirouter.feed.response.FailedMessageQueryResponse.query_metrics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='agrirouter.feed.response.FailedMessageQueryResponse.page', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='agrirouter.feed.response.FailedMessageQueryResponse.header', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reasons', full_name='agrirouter.feed.response.FailedMessageQueryResponse.reasons', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FAILEDMESSAGEQUERYRESPONSE_HEADER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1775,
  serialized_end=2181,
)

_HEADERQUERYRESPONSE_HEADER.fields_by_name['sent_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HEADERQUERYRESPONSE_HEADER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HEADERQUERYRESPONSE_HEADER.fields_by_name['metadata'].message_type = commons_dot_message__pb2._METADATA
_HEADERQUERYRESPONSE_HEADER.containing_type = _HEADERQUERYRESPONSE
_HEADERQUERYRESPONSE_FEED.fields_by_name['headers'].message_type = _HEADERQUERYRESPONSE_HEADER
_HEADERQUERYRESPONSE_FEED.containing_type = _HEADERQUERYRESPONSE
_HEADERQUERYRESPONSE.fields_by_name['query_metrics'].message_type = _QUERYMETRICS
_HEADERQUERYRESPONSE.fields_by_name['page'].message_type = _PAGE
_HEADERQUERYRESPONSE.fields_by_name['chunk_contexts'].message_type = commons_dot_chunk__pb2._CHUNKCOMPONENT
_HEADERQUERYRESPONSE.fields_by_name['feed'].message_type = _HEADERQUERYRESPONSE_FEED
_MESSAGEQUERYRESPONSE_HEADER.fields_by_name['chunk_context'].message_type = commons_dot_chunk__pb2._CHUNKCOMPONENT
_MESSAGEQUERYRESPONSE_HEADER.fields_by_name['sent_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MESSAGEQUERYRESPONSE_HEADER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MESSAGEQUERYRESPONSE_HEADER.fields_by_name['metadata'].message_type = commons_dot_message__pb2._METADATA
_MESSAGEQUERYRESPONSE_HEADER.containing_type = _MESSAGEQUERYRESPONSE
_MESSAGEQUERYRESPONSE_FEEDMESSAGE.fields_by_name['header'].message_type = _MESSAGEQUERYRESPONSE_HEADER
_MESSAGEQUERYRESPONSE_FEEDMESSAGE.fields_by_name['content'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MESSAGEQUERYRESPONSE_FEEDMESSAGE.containing_type = _MESSAGEQUERYRESPONSE
_MESSAGEQUERYRESPONSE.fields_by_name['query_metrics'].message_type = _QUERYMETRICS
_MESSAGEQUERYRESPONSE.fields_by_name['page'].message_type = _PAGE
_MESSAGEQUERYRESPONSE.fields_by_name['messages'].message_type = _MESSAGEQUERYRESPONSE_FEEDMESSAGE
_FAILEDMESSAGEQUERYRESPONSE_HEADER.fields_by_name['sent_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FAILEDMESSAGEQUERYRESPONSE_HEADER.containing_type = _FAILEDMESSAGEQUERYRESPONSE
_FAILEDMESSAGEQUERYRESPONSE.fields_by_name['query_metrics'].message_type = _QUERYMETRICS
_FAILEDMESSAGEQUERYRESPONSE.fields_by_name['page'].message_type = _PAGE
_FAILEDMESSAGEQUERYRESPONSE.fields_by_name['header'].message_type = _FAILEDMESSAGEQUERYRESPONSE_HEADER
_FAILEDMESSAGEQUERYRESPONSE.fields_by_name['reasons'].message_type = commons_dot_message__pb2._MESSAGE
DESCRIPTOR.message_types_by_name['Page'] = _PAGE
DESCRIPTOR.message_types_by_name['QueryMetrics'] = _QUERYMETRICS
DESCRIPTOR.message_types_by_name['HeaderQueryResponse'] = _HEADERQUERYRESPONSE
DESCRIPTOR.message_types_by_name['MessageQueryResponse'] = _MESSAGEQUERYRESPONSE
DESCRIPTOR.message_types_by_name['FailedMessageQueryResponse'] = _FAILEDMESSAGEQUERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Page = _reflection.GeneratedProtocolMessageType('Page', (_message.Message,), {
  'DESCRIPTOR' : _PAGE,
  '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
  # @@protoc_insertion_point(class_scope:agrirouter.feed.response.Page)
  })
_sym_db.RegisterMessage(Page)

QueryMetrics = _reflection.GeneratedProtocolMessageType('QueryMetrics', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMETRICS,
  '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
  # @@protoc_insertion_point(class_scope:agrirouter.feed.response.QueryMetrics)
  })
_sym_db.RegisterMessage(QueryMetrics)

HeaderQueryResponse = _reflection.GeneratedProtocolMessageType('HeaderQueryResponse', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _HEADERQUERYRESPONSE_HEADER,
    '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
    # @@protoc_insertion_point(class_scope:agrirouter.feed.response.HeaderQueryResponse.Header)
    })
  ,

  'Feed' : _reflection.GeneratedProtocolMessageType('Feed', (_message.Message,), {
    'DESCRIPTOR' : _HEADERQUERYRESPONSE_FEED,
    '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
    # @@protoc_insertion_point(class_scope:agrirouter.feed.response.HeaderQueryResponse.Feed)
    })
  ,
  'DESCRIPTOR' : _HEADERQUERYRESPONSE,
  '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
  # @@protoc_insertion_point(class_scope:agrirouter.feed.response.HeaderQueryResponse)
  })
_sym_db.RegisterMessage(HeaderQueryResponse)
_sym_db.RegisterMessage(HeaderQueryResponse.Header)
_sym_db.RegisterMessage(HeaderQueryResponse.Feed)

MessageQueryResponse = _reflection.GeneratedProtocolMessageType('MessageQueryResponse', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _MESSAGEQUERYRESPONSE_HEADER,
    '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
    # @@protoc_insertion_point(class_scope:agrirouter.feed.response.MessageQueryResponse.Header)
    })
  ,

  'FeedMessage' : _reflection.GeneratedProtocolMessageType('FeedMessage', (_message.Message,), {
    'DESCRIPTOR' : _MESSAGEQUERYRESPONSE_FEEDMESSAGE,
    '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
    # @@protoc_insertion_point(class_scope:agrirouter.feed.response.MessageQueryResponse.FeedMessage)
    })
  ,
  'DESCRIPTOR' : _MESSAGEQUERYRESPONSE,
  '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
  # @@protoc_insertion_point(class_scope:agrirouter.feed.response.MessageQueryResponse)
  })
_sym_db.RegisterMessage(MessageQueryResponse)
_sym_db.RegisterMessage(MessageQueryResponse.Header)
_sym_db.RegisterMessage(MessageQueryResponse.FeedMessage)

FailedMessageQueryResponse = _reflection.GeneratedProtocolMessageType('FailedMessageQueryResponse', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _FAILEDMESSAGEQUERYRESPONSE_HEADER,
    '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
    # @@protoc_insertion_point(class_scope:agrirouter.feed.response.FailedMessageQueryResponse.Header)
    })
  ,
  'DESCRIPTOR' : _FAILEDMESSAGEQUERYRESPONSE,
  '__module__' : 'messaging.response.payload.feed.feed_response_pb2'
  # @@protoc_insertion_point(class_scope:agrirouter.feed.response.FailedMessageQueryResponse)
  })
_sym_db.RegisterMessage(FailedMessageQueryResponse)
_sym_db.RegisterMessage(FailedMessageQueryResponse.Header)


_HEADERQUERYRESPONSE.fields_by_name['pending_message_ids']._options = None
# @@protoc_insertion_point(module_scope)
