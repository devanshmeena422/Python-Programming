#Append to an existing file called John Doe.txt
#It should add data about John Doe Hometown

f = open("John Doe.txt" , "a")
string = '''
John doe want to be a good proggramer in future and want to start a new company of his own
'''
f.write(string)
f.close()