# Learning about lists and indexed
states = ["Delaware", "Pennsylvania", "California",
          "texas", "New Hampshire", "New Jersey", "New Mexico"]
print(states[1])
print(states[-1])


# change of lists
states[1] = "test1"
print(states[1])


# Add item to list using append function
states.append("andrewland")
print(states)

# add items to list using extend function
states.extend(["test2", "test3", "test4", "test5"])
print(states)

# add all methods of lists
