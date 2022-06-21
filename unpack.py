Instructors = {
    "Tutor 1":"Miss Adejoke",
    "Tutor 2":"Miss Clare",
    "Tutor 3": "Miss Mercy",
    "Tutor 4": "Mr Emmanuel",
    "Tutor 5":" Mr Samuel",
    "Tutor 6":" Mr Abideen",
    "Tutor 7": "Mr Benedict"
}
for i,j in Instructors.items():
      print(i,j)

Instructors.update({"Tutor 8": "Mr. Daniel"})
x = Instructors.values()
print(x)