import hashlib
import os.path
file = open("most common passwords.txt", "r")
u_file = open("users.txt", "r")
rainbow_table = {}
stolen_data = {}

def hash_passwords(password):
    b = bytes(password, "utf-8")
    return hashlib.sha256(b).hexdigest()

for line in u_file:
    word = line.split(" ")
    username = word[0]
    password = word[1]
    stolen_data[password] = username

u_file.close()

for line in file:
    rainbow_table[hash_passwords(line.strip('\n'))] = line.strip('\n')

file.close()

new_file = open("new_file.txt", "a+")

print(stolen_data)
print(hash_passwords('password'))
print(hash_passwords('idtech'))

for hash_val in stolen_data:
    username = stolen_data[hash_val]
    if rainbow_table.get(hash_val):
        password = rainbow_table[hash_val]
        print(password)
        new_file.write("Username: " + username + " Password:  " + password)

new_file.close()