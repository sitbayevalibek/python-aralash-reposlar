#kinolar ro'yxati bo'yicha kichik dastur
kinolar = []
print("5 ta eng sevimli kinongizni kiriting")
for n in range(5):
   kinolar.append(input(f"{n+1} - sevimli kinolaringizni kiriting: "))
kinolar_str = ", ".join([kino.title() for kino in kinolar[:-1]]) + f" va {kinolar[-1].title()}"
print(f"Sizning sevimli kinolaringiz {kinolar_str} lar.")