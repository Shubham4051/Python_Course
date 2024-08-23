with open (r"C:\Users\shubh\Python\Python_Course\Python_Concepts\Basics\L7_Files_I_O\practice.txt", "r") as f:
    # f.write("Hi everyone.\nMy name is Sam.")
    # f.write("Let's go\nwe can do it.")
    # f.write("ok, go , go , on , lol\n lolodsbibunokokoooklol") 
    data = f.read()
    print(data)
    new_data = data.replace("ok", "ko")
    print(new_data)

with open (r"C:\Users\shubh\Python\Python_Course\Python_Concepts\Basics\L7_Files_I_O\practice.txt", "w") as f:
    f.write(new_data)