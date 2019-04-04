import webbrowser
import time
import os

print '\t\t\t ######################################'
print '\t\t\t ##                                  ##'
print '\t\t\t ##   Author : PHOENIX Z             ##'
print '\t\t\t ######################################'




url = input("Enter YouTube URL : ")
refresh = input("Enter refresh rate(seconds) : ")
brow = input("Enter your default browser : ")

def OpenUrl():
	print("Successfully Viwed. ")
        os.system("TASKKILL /F /IM " + brow + ".exe")
        webbrowser.open(url)
	time.sleep(int(refresh))

for i in range(10):
	OpenUrl()
