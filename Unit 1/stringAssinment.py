String="Here are the instructions to install Drivers \n1. After the download is completed go to where you saved the folder. (By default everything you download from the Internet is saved to the Downloads folder) \n2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again. \n3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.\n4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below: *setup application *Asussetup *pnpinstal64 *pnputil *Igxpin \n5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up."
# Find how many times the word Drivers is used
print(String.count('Drivers'))
# How long the String is
print(len(String))
# Replace Extract with EXTRACT
print(String.replace('Extract', 'EXTRACT'))
print()
# Replace setup or Setup with SETUP
print(String.replace('setup' 'Setup', 'SETUP'))
print()
# Finds ‘4’
print(String.find("4"))
# finds The first enter
print(String.find('\n'))

# finds 1 then prints till end of statement
s1 = String.find("\n1.")
print(String[s1: s1+69])
# finds 2 then prints till end of statement
s2 = String.find("\n2.")
print(String[s2: s2+91])
# finds 3 then prints till end of statement
s3 = String.find("\n3.")
print(String[s3: s3+100])
# finds 4 then prints till end of statement
s4 = String.find("\n4.")
print(String[s4: s4+38])
# finds 5 then prints till end of statement
s5 = String.find("\n5.")
print(String[s5: s5+133])
