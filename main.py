def read_friends_file():
    friends_list = []
    with open("friends.txt", "r") as file:
        for line in file:
            line_parts = line.strip().split(" follows ")
            friends_list.append((line_parts[0], line_parts[1]))
    return friends_list

print(read_friends_file())