# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: planningCenter.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2
import rvtimestamp_pb2 as rvtimestamp__pb2
import presentation_pb2 as presentation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14planningCenter.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\x1a\x11rvtimestamp.proto\x1a\x12presentation.proto\"\xe5\n\n\x12PlanningCenterPlan\x12\x13\n\x0bplan_id_num\x18\x01 \x01(\r\x12\x15\n\rparent_id_num\x18\x02 \x01(\r\x12\x14\n\x0cseries_title\x18\x03 \x01(\t\x12\x12\n\nplan_title\x18\x04 \x01(\t\x12\x11\n\tdate_list\x18\x05 \x01(\t\x12(\n\x0c\x63reated_date\x18\x06 \x01(\x0b\x32\x12.rv.data.Timestamp\x12\'\n\x0bupdate_date\x18\x07 \x01(\x0b\x32\x12.rv.data.Timestamp\x12\x32\n\x16last_update_check_date\x18\x08 \x01(\x0b\x32\x12.rv.data.Timestamp\x12\x13\n\x0bplan_id_str\x18\t \x01(\t\x12\x15\n\rparent_id_str\x18\n \x01(\t\x1a\xb2\x08\n\x08PlanItem\x12\x44\n\titem_type\x18\x01 \x01(\x0e\x32\x31.rv.data.PlanningCenterPlan.PlanItem.PlanItemType\x12\x12\n\npco_id_num\x18\x02 \x01(\r\x12\x16\n\x0eservice_id_num\x18\x03 \x01(\r\x12\x15\n\rparent_id_num\x18\x04 \x01(\r\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x44\n\x0b\x61ttachments\x18\x06 \x03(\x0b\x32/.rv.data.PlanningCenterPlan.PlanItem.Attachment\x12\'\n\x0bupdate_date\x18\x07 \x01(\x0b\x32\x12.rv.data.Timestamp\x12\x42\n\x0blinked_song\x18\x08 \x01(\x0b\x32-.rv.data.PlanningCenterPlan.PlanItem.SongItem\x12\x12\n\npco_id_str\x18\t \x01(\t\x12\x16\n\x0eservice_id_str\x18\n \x01(\t\x12\x15\n\rparent_id_str\x18\x0b \x01(\t\x1a\xe9\x01\n\nAttachment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x03url\x18\x02 \x01(\x0b\x32\x0c.rv.data.URL\x12(\n\x0c\x63reated_date\x18\x03 \x01(\x0b\x32\x12.rv.data.Timestamp\x12!\n\x0blinked_path\x18\x04 \x01(\x0b\x32\x0c.rv.data.URL\x12\x12\n\npco_id_num\x18\x05 \x01(\r\x12\x14\n\x0cneeds_update\x18\x06 \x01(\x08\x12\'\n\x0bupdate_date\x18\x07 \x01(\x0b\x32\x12.rv.data.Timestamp\x12\x12\n\npco_id_str\x18\x08 \x01(\t\x1a\xb5\x02\n\x08SongItem\x12\x12\n\npco_id_num\x18\x01 \x01(\r\x12\x1a\n\x12\x61rrangement_id_num\x18\x02 \x01(\r\x12(\n\x04\x63\x63li\x18\x03 \x01(\x0b\x32\x1a.rv.data.Presentation.CCLI\x12H\n\x08sequence\x18\x04 \x01(\x0b\x32\x36.rv.data.PlanningCenterPlan.PlanItem.SongItem.Sequence\x12\x12\n\npco_id_str\x18\x05 \x01(\t\x12\x1a\n\x12\x61rrangement_id_str\x18\x06 \x01(\t\x1aU\n\x08Sequence\x12\x12\n\npco_id_num\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bgroup_names\x18\x03 \x03(\t\x12\x12\n\npco_id_str\x18\x04 \x01(\t\"u\n\x0cPlanItemType\x12\x17\n\x13PLAN_ITEM_TYPE_ITEM\x10\x00\x12\x17\n\x13PLAN_ITEM_TYPE_SONG\x10\x01\x12\x18\n\x14PLAN_ITEM_TYPE_MEDIA\x10\x02\x12\x19\n\x15PLAN_ITEM_TYPE_HEADER\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'planningCenter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PLANNINGCENTERPLAN']._serialized_start=91
  _globals['_PLANNINGCENTERPLAN']._serialized_end=1472
  _globals['_PLANNINGCENTERPLAN_PLANITEM']._serialized_start=398
  _globals['_PLANNINGCENTERPLAN_PLANITEM']._serialized_end=1472
  _globals['_PLANNINGCENTERPLAN_PLANITEM_ATTACHMENT']._serialized_start=808
  _globals['_PLANNINGCENTERPLAN_PLANITEM_ATTACHMENT']._serialized_end=1041
  _globals['_PLANNINGCENTERPLAN_PLANITEM_SONGITEM']._serialized_start=1044
  _globals['_PLANNINGCENTERPLAN_PLANITEM_SONGITEM']._serialized_end=1353
  _globals['_PLANNINGCENTERPLAN_PLANITEM_SONGITEM_SEQUENCE']._serialized_start=1268
  _globals['_PLANNINGCENTERPLAN_PLANITEM_SONGITEM_SEQUENCE']._serialized_end=1353
  _globals['_PLANNINGCENTERPLAN_PLANITEM_PLANITEMTYPE']._serialized_start=1355
  _globals['_PLANNINGCENTERPLAN_PLANITEM_PLANITEMTYPE']._serialized_end=1472
# @@protoc_insertion_point(module_scope)
