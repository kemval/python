print ("🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.:H E L L O ! 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡  W E L C O M E ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° U S E R !⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻"
)

student_data = {}

quantity = int (input ("How many students will you report: "))

for student in range (quantity):
    subject_data= {}
    studentName = input("Enter student name: ")
    subjectQuantity = int (input ("How many subjects will you report: "))
    for subject in range (subjectQuantity):
        subjectName = input("Enter subject: ")
        grade = int (input ("Enter grade: "))
        subject_data[subjectName] = {grade}
    student_data[studentName]= subject_data
    print(f"Name: {studentName}. Scorecard {subject_data}")


    