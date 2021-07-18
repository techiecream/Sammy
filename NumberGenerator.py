xe=open('AIR.txt','wb')
for i in range(1000,9999):
    if (i < 99999):
        print i
        xe.write(str(i)+'\n')
    else:
        print "Done"
xe.close()
