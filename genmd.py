#!/usr/bin/env python

import shutil, os, sys
from slugify import slugify
import base64
import subprocess
from pykraken.kraken import Kraken
from tinytag import TinyTag
import hashlib
from datetime import datetime
import time

def list_to_str(l):
    quoted = [f"\"{x}\"" for x in l]
    return f"[{', '.join(quoted)}]"

meta_dir = 'content'
file_dir = 'songs'

if __name__ == '__main__':
    title = input('Song title: ')

    if( len(sys.argv) == 2 ):
        file = sys.argv[1]
    else:
        print('Input mirror links, enter after each one. [KrakenFiles first]')

        mirrors = []
        while True:
            inp = input('=> ')
            if(inp): mirrors.append(inp)
            else: break

        print('Downloading from', mirrors[0])
        kraken = Kraken()
        file = kraken.download_file(mirrors[0], file_dir)
        print('Downloaded', file)

    # metadata population
    file_meta = TinyTag.get(file)
    artists = set()
    prod = set()
    if(file_meta.artist): artists.add(file_meta.artist.lower())
    if(file_meta.albumartist): artists.add(file_meta.albumartist.lower())
    if(file_meta.composer): prod.add(file_meta.composer.lower())

    with open(file, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    slug = slugify(title.lower().replace("'", "").replace(" & ", " and "))
    path = f'{meta_dir}/{slug}.md'

    tags = set()
    if(file_meta.year): tags.add(file_meta.year)

    with open(path, 'w') as f:
        f.write('---\n')
        f.write('title: ' + title + '\n')
        f.write('aka: [\"\"]\n')
        f.write('artists: ' + list_to_str(artists) + '\n')
        f.write('producers: ' + list_to_str(prod) + '\n')
        f.write('tags: ' + list_to_str(tags) + '\n')
        f.write('file_name: ' + file.split('/')[-1] + '\n')
        if(file_meta.title): f.write('file_title: ' + file_meta.title + '\n')
        if(file_meta.comment): f.write('file_comment: ' + file_meta.comment + '\n')
        f.write('recorded: ' + '\n')
        f.write('leaked: ' + datetime.today().strftime('%Y-%m-%d') + '\n')
        f.write('length: ' + time.strftime('%M:%S', time.gmtime(file_meta.duration)) + '\n')
        f.write('md5: ' + file_hash.hexdigest() + '\n')
        try:
            f.write('mirrors: ' + list_to_str( [base64.b64encode(bytes(x, 'utf-8')).decode('utf-8') for x in mirrors] ) + '\n')
        except NameError:
            f.write('mirrors: []\n')
        f.write('---\n')

    # manual check
    p = subprocess.Popen(('nvim', path))
    p.wait()
    plan = input("\n[K]eep? [R]eject? ").lower()
    if( plan == 'r' ): os.remove(path); os.remove(file); sys.exit(0)
