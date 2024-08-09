# Example: Unpacking a nested tuple

# Nested tuple containing a tuple, list, and another tuple
data = ("Alice", (25, "Engineer"), ["Python", "C++", "JavaScript"])

# Nested unpacking
name, (age, profession), skills = data

# Accessing the unpacked variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
print(f"Skills: {skills}")

# Further unpacking the skills list
skill1, skill2, skill3 = skills
print(f"Skill 1: {skill1}")
print(f"Skill 2: {skill2}")
print(f"Skill 3: {skill3}")
