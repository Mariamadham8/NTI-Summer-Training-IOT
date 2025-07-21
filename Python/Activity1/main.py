from my_sites import dic, open_site

print("Welcome to Website Show")
print("------------------------")
print("Websites Avilable : ")
for key in dic:
    print(key)

name = input("Choose a name ")
open_site(dic[name])

while True:
    print("Do You Want con. ?")
    ans = input()
    if ans == 'yes' or ans == 'Yes':
        name = input("Choose a name ")
        open_site(dic[name])
    else:
        print("tnx for visiting webshow")
        exit()
