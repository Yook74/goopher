from abc import ABC, abstractmethod
from typing import List, Optional
import sys

sys.path.append('protobuf')
from presentation_pb2 import Presentation
from goof import Goof


class Validator(ABC):
    def __init__(self):
        self.goofs: Optional[List[Goof]] = None

    @abstractmethod
    def validate_playlist(self, playlist: List[Presentation]) -> List[Goof]:
        pass
