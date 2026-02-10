#####
marks = [58,25,63,94,48]
extra_marks =[58,255,645,258]
# 
print(marks)
print(extra_marks)

######
marks.append(0000)
extra_marks.append(0000)
#
print(marks)
print(extra_marks)

#####
marks.pop()
extra_marks.pop()
#
print(marks)
print(extra_marks)

#####
marks.extend(extra_marks)
extra_marks.extend(marks)
#
print(marks)
print(extra_marks)