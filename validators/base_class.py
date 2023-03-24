from abc import ABC
from typing import List

sys.path.append('protobuf')
from presentation_pb2 import Presentation


class Validator(ABC):
    def validate_playlist(self, playlist: List[Presentation]):
        pass
