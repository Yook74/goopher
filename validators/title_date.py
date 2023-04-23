from typing import List
import sys
from datetime import datetime, timedelta
import re

from striprtf.striprtf import rtf_to_text

from .base_class import Validator
from goof import Goof, MINOR, MAJOR
sys.path.append('protobuf')
from presentation_pb2 import Presentation


class TitleDateValidator(Validator):
    def validate_playlist(self, playlist: List[Presentation]) -> List[Goof]:
        self.goofs = []

        if not len(playlist) or not len(playlist[0].cues):
            return []

        rtf_text = ''
        for element in playlist[0].cues[0].actions[0].slide.presentation.base_slide.elements:
            rtf_text += element.element.text.rtf_data.decode('utf-8')

        text = rtf_to_text(rtf_text)
        text = text.replace(',', '').replace(' ', '')
        text = re.sub(r'\D(\d{5})\D', r'0\1', text)

        date = None
        for start in range(len(text)):
            for stop in range(len(text)):
                if stop < start:
                    continue

                try:
                    date = datetime.strptime(text[start:stop], '%B%d%Y')
                except ValueError:
                    continue

        if date is None:
            self.goofs = [Goof('Unable to find date on title slide', MINOR)]

        elif (date - datetime.now()) > timedelta(days=6):
            self.goofs = [Goof('Title slide date is more than 6 days in the future')]

        elif (date + timedelta(23)) < datetime.now():
            self.goofs = [Goof('Title slide date is in the past', MAJOR)]

        return self.goofs

