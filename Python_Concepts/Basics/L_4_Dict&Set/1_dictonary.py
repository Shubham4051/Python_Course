# key:value pairs
info = { "name" : "Shubham Adarsh", "age" : 22, "course" : "B-Tech", "dept" : "CSE-AIML", "language" : { "python" : 1, "Java" : 2, "SQL" : 3 },
    "cgpa" : 7.9, "is_working" : False, 123 : 933
}
info["name"] = "Shubham"
info["sur_name"] = "Adarsh"

new_dict = {
    "clg" : "TIT",
    "branch" : "AIML"
}
info.update(new_dict)

print(info)
print(info["language"])

print(list(info.keys()))

print(info.items())