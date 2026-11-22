'''
Question: The LOL Detector
Your friend sends you a bunch of messages. Write a function that collects every message containing "lol".
messages = [    "bro that was hilarious",    "LOL WHAT",    "i am tired",    "lol same",    "this is not funny"]
Expected output:
["LOL WHAT", "lol same"]
'''

def lol_detector(l):
    result=[]
    for i in l:
        if "lol" in i.lower():
            result.append(i)

    return result

print(lol_detector([    "bro that was hilarious",    "LOL WHAT",    "i am tired",    "lol same",    "this is not funny"]))


#I HAVE BEEN USING LOL WAY TOO MUCH, lol. moving on :p
    