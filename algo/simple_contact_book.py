# ✅ 9. Simple Contact Book (Dictionary Practice)
# Let the user store names and phone numbers, and retrieve them on demand.
# python
# CopyEdit
# Input: Add John - 09012345678
# Input: Get John
# Output: 09012345678


phoneBook  = {}
stop = False

while stop == False:
    queryString = input("Input query parameter : \n")
    queries = queryString.split(" ")
    print(f"Your Query String is : {queryString} \n")
    
    if(queries[0] == "Add") :
        phoneBook[queries[1]] = queries[2]
        print(f"Phone book updated:  {phoneBook} \n")
    elif queries[0] == "Get" :
        print(f"This is {queries[1]}'s contact : {phoneBook[queries[1]]}")
    else :
        print(f"{queries[0]} is not a valid queries \n")
        stop = True
        
    
 