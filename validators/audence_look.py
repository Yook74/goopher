from typing import List
import sys

from .base_class import Validator
from goof import Goof, LOG, MAJOR, MINOR
sys.path.append('protobuf')
from presentation_pb2 import Presentation


class AudienceLookValidator(Validator):
    def validate_playlist(self, playlist: List[Presentation]) -> List[Goof]:
        self.goofs = []

        for pres in playlist:
            if not len(pres.cues):
                self.goofs.append(Goof(f'{pres.name} appears to be empty', LOG))
                continue

            look = None
            for action in self.get_arranged_slides(pres)[0].actions:
                if action.name == 'Audience Look':
                    look = action.audience_look

            if look is None:
                self.goofs.append(Goof(f'no audience look on the first slide of {pres.name}', MAJOR))

            # elif 'nothing' in look.identification.parameter_name.lower():
            #     self.goofs.append(Goof(f'{pres.name} starts with stream nothing look', MINOR))

        return self.goofs
