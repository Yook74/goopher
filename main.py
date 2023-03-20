import zipfile
import sys
from typing import List

sys.path.append('protobuf')
from presentation_pb2 import Presentation
from propresenter_pb2 import PlaylistDocument


def parse_proplaylist(file_path: str) -> List[Presentation]:
    presentations = {}
    playlist_doc = None

    with zipfile.ZipFile(file_path) as playlist_file:
        for zip_element in playlist_file.filelist:
            with playlist_file.open(zip_element.filename) as element_file:
                if zip_element.filename == 'data':
                    playlist_doc = PlaylistDocument()
                    playlist_doc.ParseFromString(element_file.read())

                elif zip_element.filename.endswith('.pro'):
                    pres = Presentation()
                    pres.ParseFromString(element_file.read())
                    presentations[pres.name] = pres

                else:
                    continue

    playlist = []
    for element in playlist_doc.root_node.playlists.playlists[0].items.items:
        if element.name in presentations:
            playlist.append(presentations[element.name])

    return playlist


parse_proplaylist('2023-03-19 10_45.proPlaylist')
