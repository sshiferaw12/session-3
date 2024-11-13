def read_friends_file():
    friends_list = []
    with open("friends.txt", "r") as file:
        for line in file:
            line_parts = line.strip().split(" follows ")
            
    return friends_list

print(read_friends_file())