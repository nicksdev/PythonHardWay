from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") + "\n"
line2 = raw_input("line 2: ") + "\n"
line3 = raw_input("line 3: ") + "\n"

print "I'm going to write these to the file."

target.write(line1 + line2 + line3)
#target.write(line2)
#target.write(line3)


#target.write
print "And finally, we close it."
target.close()