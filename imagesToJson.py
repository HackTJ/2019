import os

imgFolder = "./static/img/logos"
partFolder = "./static/img/logos2"

#Read all video files from input folder
filedir = [f for f in os.listdir(imgFolder) if f not in ".DS_Store"]
partdir = [f for f in os.listdir(partFolder) if f not in ".DS_Store"]

s = "var sponsorImages = " + str(filedir) + ";\n"
s2 = "var partnerImages = " + str(partdir)


file = open("js/image.js","w")
file.write(s+s2)