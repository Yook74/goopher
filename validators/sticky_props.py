from typing import List
import sys

from .base_class import Validator
from goof import Goof, LOG, MAJOR, MINOR
sys.path.append('protobuf')
from presentation_pb2 import Presentation


class StickyPropValidator(Validator):
    def __init__(self, ignored_prop_names=('gathering', 'table', 'welcome', 'word')):
        super().__init__()

        self.ignored_prop_names = ignored_prop_names

    def validate_playlist(self, playlist: List[Presentation]) -> List[Goof]:
        self.goofs = []

        current_prop = None
        last_pres = None
        for pres in playlist:

            first_slide = True
            for slide in self.get_arranged_slides(pres):
                if any('clear' in action.name.lower() for action in slide.actions):
                    current_prop = None

                if first_slide and current_prop:
                    self.goofs.append(Goof(f'Prop {current_prop.name} persists from {last_pres.name} to {pres.name}'))

                for action in slide.actions:
                    if action.type == 6 and action.name.lower() not in self.ignored_prop_names:
                        current_prop = action

                first_slide = False

            last_pres = pres

        return self.goofs
