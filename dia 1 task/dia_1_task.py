import matplotlib.pyplot as plt
import numpy as np

title = "Данные о ИТ безопасности с сайта "

fig, ( ax2) = plt.subplots(ncols=1)
fig.canvas.set_window_title(title)
fig.suptitle(title +
                 "https://www.stat.ee")
fig.set_figwidth(10)

ax2.set_xlabel("Количество ")
ax2.set_ylabel("Описание ")


    # https://www.yuripetrov.ru/edu/python/ch_12_01.html#module-matplotlib
fail=open("dannie.txt","r")
mas1=[] #description
mas2=[] #numbers
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()
ax2.barh ( mas1, mas2, height=0.7, color="#ffa500")

plt.show()

