#! /usr/bin/python3.6
from PIL import Image
import imagehash
import sys
def main():

	img = Image.open(sys.argv[1])
	x,y=img.size
	area1=(int(0.7*x),int(0.7*y))
	size_1=img.resize(area1,Image.ANTIALIAS)
	area2=(int(0.5*x),int(0.5*y))
	size_2=img.resize(area2,Image.ANTIALIAS)

	print("Computed D hash values for the input file : ")
	print(f" 100% : {imagehash.dhash(img)}")
	print(f" 70% : {imagehash.dhash(size_1)}")
	print(f" 50% : {imagehash.dhash(size_2)}")

if(__name__=="__main__"):
	main()