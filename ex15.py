#Get argv from the system
from sys import argv

#Get the script (file) name from the input. Also expect another parameter from the input and set it to variable 'filename'
script, filename = argv

#Display as text the contents of variable 'filename', in the case the sample text file
txt = open(filename)

# Print the name of the variable 'filename'
print "Here's your file %r:" % filename
# Print the contents of the file described in the variable 'filename'
print txt.read()

print "Type the filename again:"
#Set the variable 'file_again' to be that of the raw input
file_again = raw_input("> ")

#Open the file described in the variable 'filee_again'
txt_again = open(file_again)

#Display the contents of the file described in the variable 'file_again'
print txt_again.read()