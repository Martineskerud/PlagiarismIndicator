import fnmatch
import os
import sys

results = []
usernames=[]
#script to find comments in all js files in sub-directories
for root, dirnames, filenames in os.walk('D:\Dropbox\Dropbox\Skole\studass\oblig2_dump\oblig2-backup'):
    for filename in fnmatch.filter(filenames, '*.js'):
        try:
            file= open(root+ "/"+filename)
            lines=file.readlines()
            file.close()

            for n in lines:
                    n = n.lower()
                    n.strip()
                    temp=""
                    for j in n:
                    #python doesnt speak ø,å
                        try:
                            if j=="\xe3":
                                pass      
                            elif j=="\xb8":
                                pass
                            else: 
                                temp+=str(j)
                        except UnicodeEncodeError:
                            pass
                    n=temp
                    if n.startswith("//") and "oppg" not in n:
                        usernames.append(root+"/"+filename)
                        results.append(n)
        except UnicodeDecodeError:
            pass

#compare and look for duplicates
for i in range(len(results)):
  for j in range(i + 1, len(results)):
    if results[i] == results[j]:
      print ("duplicate:", results[i] + "\n")
      print ("from user : \n" + usernames[i] +" \\n and \\n " +usernames[j])

