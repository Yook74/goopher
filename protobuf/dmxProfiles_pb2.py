# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dmxProfiles.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64mxProfiles.proto\x12\x07rv.data\"\xdf\x07\n\x0b\x44MXProfiles\x12\x39\n\x10workspaceProfile\x18\x01 \x01(\x0b\x32\x1f.rv.data.DMXProfiles.DMXProfile\x12\x36\n\rlayerProfiles\x18\x02 \x03(\x0b\x32\x1f.rv.data.DMXProfiles.DMXProfile\x1a\xdc\x06\n\nDMXProfile\x12\x38\n\x07profile\x18\x01 \x01(\x0b\x32\'.rv.data.DMXProfiles.DMXProfile.Profile\x12\x38\n\x07\x66ixture\x18\x02 \x01(\x0b\x32\'.rv.data.DMXProfiles.DMXProfile.Fixture\x12\x11\n\tisEnabled\x18\x03 \x01(\x08\x12\x46\n\x0e\x63ustomMappings\x18\x04 \x03(\x0b\x32..rv.data.DMXProfiles.DMXProfile.ChannelMapping\x1a\xbb\x01\n\x07Profile\x12H\n\x0bprofileType\x18\x01 \x01(\x0e\x32\x33.rv.data.DMXProfiles.DMXProfile.Profile.ProfileType\x12\x19\n\x0fstartingChannel\x18\x02 \x01(\rH\x00\"2\n\x0bProfileType\x12\t\n\x05\x42\x41SIC\x10\x00\x12\x0c\n\x08\x41\x44VANCED\x10\x01\x12\n\n\x06\x43USTOM\x10\x02\x42\x17\n\x15startingChannel_oneof\x1a\x97\x02\n\x0e\x43hannelMapping\x12\x14\n\x0c\x63hannelIndex\x18\x01 \x01(\r\x12K\n\x07\x63ommand\x18\x02 \x01(\x0e\x32:.rv.data.DMXProfiles.DMXProfile.ChannelMapping.CommandType\"\xa1\x01\n\x0b\x43ommandType\x12\x0b\n\x07OPACITY\x10\x00\x12\x0e\n\nBLEND_MODE\x10\x01\x12\x0e\n\nSELECT_CUE\x10\x02\x12\x10\n\x0c\x43ONTROL_TYPE\x10\x03\x12\x11\n\rCONTROL_VALUE\x10\x04\x12\x17\n\x13TRANSITION_DURATION\x10\x05\x12\x13\n\x0fSELECT_PLAYLIST\x10\x06\x12\x12\n\x0eTARGETED_LAYER\x10\x07\x1a\xa6\x01\n\x07\x46ixture\x12H\n\x0b\x66ixtureType\x18\x01 \x01(\x0e\x32\x33.rv.data.DMXProfiles.DMXProfile.Fixture.FixtureType\x12\x14\n\nlayerIndex\x18\x02 \x01(\rH\x00\"\'\n\x0b\x46ixtureType\x12\r\n\tWORKSPACE\x10\x00\x12\t\n\x05LAYER\x10\x01\x42\x12\n\x10layerIndex_oneofb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dmxProfiles_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DMXPROFILES']._serialized_start=31
  _globals['_DMXPROFILES']._serialized_end=1022
  _globals['_DMXPROFILES_DMXPROFILE']._serialized_start=162
  _globals['_DMXPROFILES_DMXPROFILE']._serialized_end=1022
  _globals['_DMXPROFILES_DMXPROFILE_PROFILE']._serialized_start=384
  _globals['_DMXPROFILES_DMXPROFILE_PROFILE']._serialized_end=571
  _globals['_DMXPROFILES_DMXPROFILE_PROFILE_PROFILETYPE']._serialized_start=496
  _globals['_DMXPROFILES_DMXPROFILE_PROFILE_PROFILETYPE']._serialized_end=546
  _globals['_DMXPROFILES_DMXPROFILE_CHANNELMAPPING']._serialized_start=574
  _globals['_DMXPROFILES_DMXPROFILE_CHANNELMAPPING']._serialized_end=853
  _globals['_DMXPROFILES_DMXPROFILE_CHANNELMAPPING_COMMANDTYPE']._serialized_start=692
  _globals['_DMXPROFILES_DMXPROFILE_CHANNELMAPPING_COMMANDTYPE']._serialized_end=853
  _globals['_DMXPROFILES_DMXPROFILE_FIXTURE']._serialized_start=856
  _globals['_DMXPROFILES_DMXPROFILE_FIXTURE']._serialized_end=1022
  _globals['_DMXPROFILES_DMXPROFILE_FIXTURE_FIXTURETYPE']._serialized_start=963
  _globals['_DMXPROFILES_DMXPROFILE_FIXTURE_FIXTURETYPE']._serialized_end=1002
# @@protoc_insertion_point(module_scope)
