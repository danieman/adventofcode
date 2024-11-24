groups = open("input.txt").read().strip().split("\n\n")

# Task a)
print(sum([len(set(group.replace("\n", ""))) for group in groups]))

# Task b)
total = 0
for group in groups:
    persons = group.split("\n") 
    common_questions = set()
    for question in persons[0]:
        found_for_all = True
        for person in persons:
            if question not in person:
                found_for_all = False
                break
        if found_for_all:
            common_questions.add(question)
    total += len(common_questions)

print(total)