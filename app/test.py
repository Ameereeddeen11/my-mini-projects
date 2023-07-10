import hashlib, os
# hash function
str_value = "Hello this is hash"
print("This is hash: ", hash(str_value))

hash_value = input("Type something for hashing: ")
hash = hash(hash_value)
print("This is your hash: ", hash)

# hash sha256 function
user_input = input("Type something for hashing: ")    
hash_sha256_value = hashlib.sha256(user_input.encode('utf-8')).hexdigest()
print("this is in SHA256: ",hash_sha256_value, "This is what you write: ", user_input)

# how to export file extention in python
slipt_name_file = os.path.splitext('df130d53462d478c0a17766ca24d92e2.jpg')
file_name = slipt_name_file[0]
file_extension = slipt_name_file[1]
print("This is file name: ", file_name)
print("This is file extension: ", file_extension)

# hashing the file name 
user_input_2 = input("Enter file name: ")
file_name_2 = os.path.splitext(user_input_2)
hash_sha256_file = hashlib.sha256(file_name_2[0].encode('utf-8')).hexdigest()
print("This is your file name in SHA256: ", hash_sha256_file + file_name_2[1])