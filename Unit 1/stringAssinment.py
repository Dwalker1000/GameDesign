String="Here are the instructions to install Drivers \n1. After the download is completed go to where you saved the folder. (By default everything you download from the Internet is saved to the Downloads folder) \n2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again. \n3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.\n4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below: *setup application *Asussetup *pnpinstal64 *pnputil *Igxpin \n5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up."
#•	Find how many times the word Drivers is used
#•	How long in your Strint
# •	Replace Extract with EXTRACT
# •	Replace setup or Setup with SETUP
# •	Find  ‘4’
print(String.count('Drivers'))
print(len(String))
print(String.replace('Extract', 'EXTRACT'))
print(String.replace('setup' 'Setup', 'SETUP'))
print(String.find("4"))
print(String.find('\n'))
