import os
import hashlib

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class ContentHasher:
    def __init__(self, content):
        self.content = content

    def hash_content(self):
        hashed_content = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        return hashed_content

    def save_hash(self, contentname):
        with open('hashes.txt', 'a') as file:
            file.write(f"{contentname}: {self.hash_content()}\n")

option = input("What do you want to hash: ")
option2 = input("What do you want to name the content: ")

ContentHasher(option).save_hash(option2)   
clear() 

print(f"Content '{option}' has been hashed and saved with the name '{option2}' in the file 'hashes.txt'.")
