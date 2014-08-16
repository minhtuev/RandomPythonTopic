txt = "Love one another and you will be happy. It is as simple as that."

upper_staff = ""
lower_staff = "" 
for i in txt.lower():
    (l,u) = char2notes[i]
    upper_staff += u
    lower_staff += l

staff = "{\n\\new PianoStaff << \n"
staff += "  \\new Staff {" + upper_staff + "}\n"  
staff += "  \\new Staff { \clef bass " + lower_staff + "}\n"  
staff += ">>\n}\n"

title = """\header {
  title = "Love One Another"
  composer = "Bernd Klein using Python"
  tagline = "Copyright: Bernd Klein"
}"""

print title + staff