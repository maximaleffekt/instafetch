import os
import random
from igramscraper.instagram import Instagram
instagram = Instagram()

postlimit = 50
backend = ""
username = ""

medias = instagram.get_medias(username, postlimit)
number = random.randint(0,postlimit -1)
media = medias[number]
link = media.image_high_resolution_url
filename = media.short_code + ".jpg"

os.system("curl -fsSLo \"" +filename+"\" \"" + link + "\"")
os.system("neofetch --" +backend+" "+filename)
os.system("rm "+filename)
