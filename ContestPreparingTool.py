import os 

def createFile(n,nowPath,snippetPath):
	problems = chr(n + 65)
	CrPath = os.path.join(nowPath,problems)
	os.mkdir(CrPath) 
	print("Directory ",CrPath," created" )
	os.chdir(CrPath)
	f = open(problems+".cpp", "a")
	x = open(problems+".in","a")
	x.close()
	x = open(problems+".out","a")
	x.close()
	x = open("DEBUG.txt","a")
	x.close()
	os.chdir(snippetPath)
	t = open("snippet.txt","r")
	f.write("char TASK = '" +problems+ "';\n")
	for line in t:
		f.write(line)
	t.close()
	f.close()
def createNameOfContestFile(nowPath):
	Name = input("Contest name: ")
	CrPath = os.path.join(nowPath,Name)
	os.mkdir(CrPath)
	print("contest ",Name," created")
	return CrPath 

print("Welcome to Competitive programming creation tool")
print("Press Ctrl + C to close this tool")
print("Your directory: ",os.getcwd())
c = 0 
snippetPath = os.getcwd()
while True :
	if (c>0):
		cmd = input("Want to exit?(Y/N) ")
		if (cmd == "Y"):
			break
		elif (cmd == "N"):
			break
		else:
			print()
	nowPath = os.getcwd()
	ChangePath = input("Would you like to change working path ? (Y/N):")
	if (ChangePath == "Y"):
		path = input("Path: ")
		nowPath = os.chdir(path)
	elif (ChangePath == "N"):print()
	else:
		print("WRONG INPUT! Try Again")
		continue 
	nowPath = createNameOfContestFile(nowPath)
	AmountOfProblem = int(input("Amount Of Problems :"))
	for i in range(AmountOfProblem):
		createFile(i,nowPath,snippetPath)
	c+=1
