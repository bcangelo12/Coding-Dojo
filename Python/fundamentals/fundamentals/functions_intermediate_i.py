#1
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["last_name"] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
(z[0]["y"]) = 30
print(z)

#2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(list):
    for x in range(0, len(list)):
        y = ""
        for k,v in list[x].items():
            y += f" {k} - {v},"
        print(y)
iterateDictionary(students)

#3
def iterateDictionary2(k_name, list):
    for x in range(0, len(list)):
        for k,v in list[x].items():
            if k == k_name:
                print(v)
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(list):
    for k,v in list.items():
        print("")
        print(f"{len(v)} {k.upper()}")
        for x in range(0, len(v)):
            print(v[x])
printInfo(dojo)
