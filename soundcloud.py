#!/usr/bin/env python
"""
Soundcloud downloader 
based on http://pastebin.com/K2FSBWqb paste
usage: python soundcloud.py [URL]

    URL     soundcloud.com URL of the track to download
            ie. http://soundcloud.com/dunkelbunt/picnic-with-dunkelbunt

  * http://developers.soundcloud.com/docs/widget
  * https://github.com/soundcloud/Widget-JS-API/wiki

"""

import sys
import time
import urllib
import json

class MozillaURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (X11; Linux i686; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"

def reporthook(blocks_read, block_size, total_size):
    sys.stdout.write("\r% 3.1f%% of %d bytes " 
        % (float(blocks_read * block_size) / total_size * 100, total_size))
    sys.stdout.flush()

def main(argv):
    if len(argv) > 1 and argv[1].startswith("https://soundcloud.com/"):
        url = argv[1]
    else:
        print(__doc__)
        url = raw_input("// soundcloud.com track url: ")
    url = "http://soundcloud.com/widget.json?" + urllib.urlencode({'url':url})
    urllib._urlopener = MozillaURLopener() # override the urlopener
    widget = urllib.urlopen(url).read()
    data = json.loads(widget)
    url = data['stream_url'] # http://developers.soundcloud.com/docs/widget
    name = data['title'] + ".mp3"
    print("// try to retrieve remote %s to local %s" % (url, name))
    (filename, headers) = urllib.urlretrieve(url, name, reporthook)
    # print("Done. (filename: %s, headers: %s)" % (filename, headers))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

