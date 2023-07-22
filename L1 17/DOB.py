with open('DOB.txt', 'r+') as f:
    
    # ask to read the contents in the file
    data_read = f.read()
    
    # split the data into lines
    lines = data_read.split("\n")

    # create 2 empty lists so we can store the information after stripping
    names = []
    birthdates = []

    # start stripping the lines on DOB.txt
    for line in lines:
        # create a list of words
        words_list = line.split()

        # to get the name, check if the line has at least 3 words - and then join the first 2 words
        if len(words_list) >= 3:
            name = " ".join(words_list[:2])

            # add the name to the list
            names.append(name)

            # to get the birth date, join the last 3 words
            birthdate = " ".join(words_list[-3:])

            # add the birthdates to the list
            birthdates.append(birthdate)

# print the names/birthdates

print("Name:")
for name in names:
    print(name)

# add an empty line for space
print()

print("Birthdate:")
for birthdate in birthdates:
    print(birthdate)

# always close the file after using it
f.close()