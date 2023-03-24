from argparse import ArgumentParser
from parse import parse_proplaylist
from validators import AudienceLookValidator

if __name__ == '__main__':
    parser = ArgumentParser(prog='goopher', description='Inspects ProPresenter playlists for errors (goofs)')
    parser.add_argument('filename', help='something ending in .proPlaylist')
    args = parser.parse_args()

    playlist = parse_proplaylist(args.filename)

    for validator in [AudienceLookValidator()]:
        validator.validate_playlist(playlist)

