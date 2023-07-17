# ("abcdefghijklmnopqrstuvwxyz")
# ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for char in message:
    if ord(char) >= 65 and ord(char) <= 90:
        position = ord(char) - ord("A")
        position = (position + offset) % 26
        new_position = chr(position + ord("A"))
        encoded_message += new_position
       
    elif ord(char) >=97 and ord(char) <= 122:
        position = ord(char) - ord("a")
        position = (position + offset) % 26
        new_position = chr(position + ord("a"))
        encoded_message += new_position
    else:
        encoded_message += char
print(encoded_message)