"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE


file = open("c:\\Users\\Lidii\\Desktop\\LAMBDA\\CS\\Week 01\\Intro-Python-I\\src\\foo.txt","r") 
print(file.read())


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f = open("c:\\Users\\Lidii\\Desktop\\LAMBDA\\CS\\Week 01\\Intro-Python-I\\src\\testfile.txt", "w")

f.write("This is a test \n") 
f.write("To add more lines. \n")
f.write("To add more and more lines. \n")

f.close() 

test_file = open("c:\\Users\\Lidii\\Desktop\\LAMBDA\\CS\\Week 01\\Intro-Python-I\\src\\testfile.txt","r") 
print(test_file.read())