# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# C:\Users\shubh\Python\Python_Course\Python_Concepts\Basics\L7_Files_I_O\demo.txt

f = open(r"C:\Users\shubh\Python\Python_Course\Python_Concepts\Basics\L7_Files_I_O\demo.txt","r")
data = f.read()
print(data)

print(type(data))

# line1 = f.readline()
# print(line1)
# f.readline()
# f.readline()
# f.readline()
# f.readline()
# f.readline()
# f.readline()
# line7 = f.readline()
# print(line7)

f.close()