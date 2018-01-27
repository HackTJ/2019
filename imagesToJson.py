import os

imgFolder = "./static/img/logos"
partFolder = "./static/img/logos2"

#Read all video files from input folder
filedir = [ [ f, str(f[:-4]) + ".com" ] for f in os.listdir(imgFolder) if f not in ".DS_Store"]
partdir = [ [ f, str(f[:-4])+".io" ] for f in os.listdir(partFolder) if f not in ".DS_Store"]

s = "var sponsorImages = " + str(filedir) + ";\n"
s2 = "var partnerImages = " + str(partdir)


file = open("js/image.js","w")
file.write(s+s2)