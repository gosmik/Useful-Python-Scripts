import os
from subprocess import Popen
p = Popen("echo.bat", cwd=r"C:\Users\User1\Desktop")

# Set the directory you want to start from
fo = open("list.txt", "wb")
extension = ' '
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
		fname = os.path.basename(fname)
		extension = os.path.splitext(fname)[1]
		#print(extension)
		if extension == '.psd':
			stdout, stderr = p.communicate()
			fname = os.path.splitext(fname)[0]
			fo.write(fname+'\n')
			#print('\t%s' % fname)