### open the  txt file
f= open(r"D:\file1.txt","x")
f.close()
### write the data into the txt file
f=open(r"D:\file1.txt","w")
f.write("this is the selenium language")
f.close()
# read the data from txt file
f=open(r"D:\file1.txt","r")
print(f.read())
