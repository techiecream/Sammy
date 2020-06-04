#!/usr/bin/python2.7
#import the libraries
#Text Reader
import pyttsx
import time
#configure the speakers
# Set properties _before_ you add things to say
engine = pyttsx.init()
#calculate how long the entire text will take to read
f=open("CSUP.txt","rb") # open the file that has the text to read
start = time.time() #start counting the time
data = f.read() # read the file word for word
words = data.split() #split the words
v=int(len(words))/199 #divide the numbwr of words by 199
engine.say("It will take:")
engine.runAndWait()
engine.say(v)
engine.runAndWait()
engine.say("Minutes to finish this text")
engine.runAndWait()
f.close()

#start reading to us
fh=open("CSUP.txt","rb")
start = time.time()
ff=fh.readlines()
for i in ff:

    ty=''.join([char if ord(char) < 128 else '' for char in i])
    print ty
    engine.say(ty)
    engine.runAndWait()
    engine.runAndWait()
