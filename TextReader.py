#!/usr/bin/python2.7
#import the libraries
#Text Reader
import pyttsx
#configure the speakers
# Set properties _before_ you add things to say
engine = pyttsx.init()
f=open("CSUP.txt","rb")
ff=f.readlines()
for i in ff:

    ty=''.join([char if ord(char) < 128 else '' for char in i])
    print ty
    engine.say(ty)
    engine.runAndWait()
    engine.runAndWait()
