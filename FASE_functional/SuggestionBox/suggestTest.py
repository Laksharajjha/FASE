# This program is to figure out the exact method of implementing suggestion for FASE

import customtkinter
import tkinter

global combo
global root
global suggestions

countries = ['India','United States','United Kingdom']
suggestions = []
suggestion_labels = []

global priorinp
priorinp = ''

def update_suggestions():
    
    global priorinp
    global suggestions
    input = combo.get()

    if (input != priorinp):

        for suggestion in suggestions:
               print("Removed " + str(suggestion))
               suggestions.remove(suggestion)
               print("Total : ",end = '')
               print(suggestions)
        
        for suggestion_label in suggestion_labels:
                suggestion_labels.remove(suggestion_label)
                suggestion_label.destroy()


    if(input != ''):

        for country in countries:
            if (input in country) and (country not in suggestions):
                suggestions.append(country)
                print("Added " + str(country))
                print("Total : ",end = '')
                print(suggestions)
                
                suggestion_label = customtkinter.CTkLabel(root, text = country, fg_color='pink')
                suggestion_label.pack()
                suggestion_labels.append(suggestion_label)
                priorinp = input

    
    root.after(10,update_suggestions)

def hey(string):

    print('hey ' + string)

def main():

    global combo
    global root

    root = customtkinter.CTk()
    root.geometry('400x400')
    root.title('Suggestion Test')

    combo = customtkinter.CTkComboBox(root, width = 300, height = 6, command=hey)
    combo.pack()

    update_suggestions()
    
    root.mainloop()

if __name__ == '__main__':
    main()