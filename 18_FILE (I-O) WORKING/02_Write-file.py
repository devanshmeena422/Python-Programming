#Write to a file claled  John Doe.txt
#It should contain data about John Doe

f = open("John Doe.txt" , "w")
string = '''
John Doe is a nice guy . He lives in Nyc and he works with python
His favourite   food is daal baati
'''
f.write(string)
f.close()