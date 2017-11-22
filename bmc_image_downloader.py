"""Download all the images from the Bangalore Microscopy Course gallery.

Images are located here: https://www.ncbs.res.in/BangaloreMicroscopyCourse/2017/gallery
"""
import urllib.request
import re
import sys

bmc_url = "https://www.ncbs.res.in/BangaloreMicroscopyCourse/"
gallery_url = bmc_url + "2017/gallery"
search_url = r"gallery/download5.php\?image=DSC_(.*?).jpg"

html_page = str(urllib.request.urlopen(gallery_url).read())
matches = re.findall(search_url, html_page)

base_url = bmc_url + "gallery/download5.php?image=DSC_{}.jpg"


for count, match in enumerate(matches):
    urllib.request.urlretrieve(base_url.format(match), match + ".jpg")
    sys.stdout.write("Downloading: {}/{}\r".format(count + 1, len(matches)))
    sys.stdout.flush()
