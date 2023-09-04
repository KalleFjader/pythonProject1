import tkinter as tk
from timeit import default_timer as timer
from random import randint

window = tk.Tk()
window.geometry("900x500+700+400")
end = 0
start = 0

ordlista = []                                                   # List of words to be written

a_file = open("wordlist.txt", "r")                              # txt of all words
content = a_file.readlines()
lines_to_read = []


for i in range(9):
    value = randint(0, 2900)                                    # 9 RNG numbers
    lines_to_read.append(value)
    print(value)

for i in range(9):                                              # Adding those specific lines to ordlista
    ordlista.append(content[lines_to_read[i]].rstrip())

print(ordlista)
print(lines_to_read)



def Take_input(event=None):                                     # Checking if correct input
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if (INPUT == " ".join(ordlista)):
        global end
        end = timer()
        sluttid = str((60/(end-start)*9))                       # Calculating WPM
        result.insert(tk.END, '\nWords per minute = '+ sluttid)


def starta(event=None):                                         # Starting the timer
    global start
    start = timer()

def startmeddelande(event=None):
    result.insert(tk.END, 'Running...')

label2 = tk.Label(window, text="__________________________________________________")
label2.config(font=("Arial", 24))

label1 = tk.Label(window, text="Typing Speed Test")
label1.config(font=("Arial", 24))

label = tk.Label(window, text=ordlista)
label.config(font=("Arial", 18))



inputtxt = tk.Text(window, height=10, width=600, bg="light yellow")

result = tk.Text(window, height=5, width=350, bg="light cyan")

knapp = tk.Button(window, height=4, width=25, text="Press enter when finished", command=lambda:Take_input())
startknapp = tk.Button(window, height=4, width=20, text="Start", command=lambda:[starta(), startmeddelande()])




inputtxt.bind('<Return>',Take_input)

label1.pack()
label2.pack()
label.pack()
inputtxt.pack()
result.pack()
startknapp.pack()
knapp.pack()



window.mainloop()

