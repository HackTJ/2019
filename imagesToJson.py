import os

imgFolder = "./static/img/2017-sponsor-logos"
partFolder = "./static/img/partner-logos"

#Read all video files from input folder
filedir = [f for f in os.listdir(imgFolder) if ".png" in f]
partdir = [f for f in os.listdir(partFolder) if ".png" in f]

s = "var sponsorImages = " + str(filedir) + ";\n"
s2 = "var partnerImages = " + str(partdir)


file = open("js/image.js","w")
file.write(s+s2)