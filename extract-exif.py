from PIL import Image
from PIL.ExifTags import TAGS
import webbrowser

GPSINFO_TAG = next(
    tag for tag, name in TAGS.items() if name == "GPSInfo"
)

path = "IMG_2998[1].JPG"
image = Image.open(path)
info = image.getexif()

gpsinfo = info.get_ifd(GPSINFO_TAG)

for key,val in gpsinfo.items():
    if key == 1:
       LatDir = val
    elif key == 2:
       LatCoor = val
    elif key == 3:
       LonDir = val
    elif key == 4:
       LonCoor = val

def DMS2DD(degrees, minutes, seconds, direction):
  dd = float(degrees) + (float(minutes)/60) + (float(seconds)/3600)
  if (direction == "S" or direction == "W"):
    dd = dd * -1
  return dd

webbrowser.open('https://www.openstreetmap.org/?mlat=' + str(DMS2DD(LatCoor[0], LatCoor[1], LatCoor[2], LatDir)) + '&mlon=' + str(DMS2DD(LonCoor[0], LonCoor[1], LonCoor[2], LonDir)) + '&zoom=12')