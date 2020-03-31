'''
printing is slow
comment out cluster printing to test code
set turtle to fastest

.read() returns a string of "everything" (from pointer to end)

.readline() returns a string of the one line

.readlines() returns a list of strings, reads "everything" so pointer is at end

fileob.writelines(list)

close files:
    can't accidently modify a file you are done with
    limit on # of files you can have open at once
    when you write to a file it gets a buffer until you close the file the buffer might not finish


*****************************************************************    
Hint: coding part on final may involve opening and reading a file
*****************************************************************


try:
    {protected by except block
except:
    {what to do in case of an error/exception in try block
built-in
helps you handle errors
error is class/"type": Exception
errors aren't always fatal so they aren't all errors so they're called exceptions
examples for use:
    files that don't exist
    arithmetic issues
        WANT to handle
    bad user input
***can't catch syntax errors***

