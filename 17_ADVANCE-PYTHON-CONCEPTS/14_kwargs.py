def marks(**kwargs):
    
    #**kwargs is a dictoinary with all the key value pairs which were passed to marks

    # for items in kwargs.keys():
    #     print(kwargs[items])


    for item in kwargs.keys():
        print(f"The marks obtained by {item} is : " , kwargs[item])

marks(shubham = 98 , priya = 77 , darshana = 23 , motu = 89)