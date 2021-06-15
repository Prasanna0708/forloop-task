dict5 = {'may_batch':{
        'Student':{
            "Name": "Mike",
            "marks":{
            'python': 95,
            'math': 88,
            'full stack' : 90
            }
     }
    }
}

print(dict5)
#accessing Name Mike
print(dict5['may_batch']['Student']['Name'])
#accessing math Value
print(dict5['may_batch']['Student']['marks']['math'])
#Changing Name Prasanna instead of Mike
dict5['may_batch']['Student']['Name'] = "prasanna"
print(dict5)
#adding Science = 80
dict5['may_batch']['Student']['marks']['Science'] = 80
print(dict5)
#adding English = 93
dict5['may_batch']['Student']['marks']['English'] = 93
print(dict5)
