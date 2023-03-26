from argparse import ArgumentParser
from parse import parse_proplaylist
from validators import AudienceLookValidator, StickyPropValidator

gopher = """         ,_---~~~~~----._         
  _,,_,*^____      _____``*g*\"*, 
 / __/ /'     ^.  /      \ ^@q   f 
[  @f |  @))   |  |  @))  l  0 _/  
 \`/   \~____ / __ \_____/    \   
  |           _l__l_           I   
  }          [______]          I  
  ]            | | |           |  
   ]            ~ ~           |  
"""

if __name__ == '__main__':
    parser = ArgumentParser(prog='goopher', description='Inspects ProPresenter playlists for errors (goofs)')
    parser.add_argument('filename', help='something ending in .proPlaylist')
    args = parser.parse_args()

    print(gopher)
    print(f'Checking {args.filename} for goofs')
    print()

    playlist = parse_proplaylist(args.filename)

    goofs = []
    for validator in [AudienceLookValidator(), StickyPropValidator()]:
        goofs += validator.validate_playlist(playlist)

    if not goofs:
        print('All good!')

    else:
        for goof in sorted(goofs, reverse=True):
            print(goof)

    exit(len(goofs))

