yosh = int(input("Nechchi yoshdasiz?: "))
if yosh<7 or yosh>60:
    j = "Sizga kirish bepul"
elif yosh<18:
    j = "Sizga chipta narxi 5000 so'm"
else:
    j = "Sizga chipta narxi 10000 so'm"
print(j)