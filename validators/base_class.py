from abc import ABC, abstractmethod
from typing import List, Optional
import sys

sys.path.append('protobuf')
from cue_pb2 import Cue
from presentation_pb2 import Presentation
from goof import Goof


class Validator(ABC):
    def __init__(self):
        self.goofs: Optional[List[Goof]] = None

    @abstractmethod
    def validate_playlist(self, playlist: List[Presentation]) -> List[Goof]:
        pass

    @staticmethod
    def get_arranged_slides(pres: Presentation) -> List[Cue]:
        """Builds a list of slides/cues in the order and quantity that they appear in ProPresenter.
        Some songs use arrangements where the slides in a presentation may be assigned several different orders.
        This method reads the selected arrangement and uses the arrangement to determine the order of slides
        which will appear when the given presentation is loaded in ProPresenter.
        """
        selected_arrange = None
        for arrangement in pres.arrangements:
            if arrangement.uuid == pres.selected_arrangement:
                selected_arrange = arrangement

        if selected_arrange is None:
            return pres.cues

        out = []
        for group_id in selected_arrange.group_identifiers:
            for cue_group in pres.cue_groups:
                if group_id == cue_group.group.uuid:
                    break

            for cue_id in cue_group.cue_identifiers:
                for cue in pres.cues:
                    if cue.uuid == cue_id:
                        out.append(cue)
        return out
