import os
import urllib
import urllib2
from xml.etree import ElementTree

from pluginsystem import pluginsystem, BuiltinPlugin

class LastfmCovers(object):
    def __init__(self):
        pluginsystem.plugin_infos.append(BuiltinPlugin(
                'lastfmcovers', "Last.fm Covers",
                "Fetch album covers from Last.fm.",
                {'cover_fetching': 'get_cover'}, self))

    def get_cover(self, progress_callback, artist, album, dest_filename,
              all_images=False):
        return self.artwork_download_img_to_file(progress_callback, artist, album, dest_filename, all_images)

    def artwork_download_img_to_file(self, progress_callback, artist, album, dest_filename, all_images=False):
        if not artist and not album:
            return False

        lastfm_url = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=c210bc3c199076c12e1a36861a238aa1"
        artist = urllib.quote(artist)
        album = urllib.quote(album)
        url = "%s&artist=%s&album=%s" % (lastfm_url, artist, album)
        request = urllib2.Request(url)
        opener = urllib2.build_opener()
        try:
            body = opener.open(request).read()
            xml = ElementTree.fromstring(body)
            #imgs = xml.getiterator("img")
            imgs = xml.iter("image")
        except:
            return False

        imglist = [img.text for img in imgs if img.text]
        # Couldn't find any images
        if not imglist:
            return False

        if not all_images:
            try:
                urllib.urlretrieve(imglist[-1], dest_filename)
            except IOError:
                return False
            return True
        else:
            try:
                imgfound = False
                for i, image in enumerate(imglist):
                    dest_filename_curr = dest_filename.replace("<imagenum>", str(i+1))
                    urllib.urlretrieve(image, dest_filename_curr)
                    if not progress_callback(
                        dest_filename_curr, i):
                        return imgfound # cancelled
                    if os.path.exists(dest_filename_curr):
                        imgfound = True
            except:
                pass
            return imgfound
