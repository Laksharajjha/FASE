import customtkinter
import tkinter

class SuggestionBox:

    def __init__(self,root,x,y,widget,options,textsize):

        self.root = root
        self.widget = widget

        self.width = widget.cget('width')
        self.height = widget.cget('height')

        self.x = x
        self.y = y

        self.text_size = textsize

        self.priorinput = ''
        self.suggestions = []
        self.suggestion_labels = []
        self.options = options

    def delete_suggestions(self,input):

        if (input != self.priorinput):
            
            for suggestion in self.suggestions:
                self.suggestions.remove(suggestion)
            
            for suggestion_label in self.suggestion_labels:
                suggestion_label.destroy()

            del self.suggestion_labels
            self.suggestion_labels = []

    def update_suggestions(self):

        input = self.widget.get()

        self.delete_suggestions(input)
        
        if(input != '') and (input != self.priorinput):

            self.suggcounter = 0
            for option in self.options:

                if (input in option) and (option not in self.suggestions):

                    self.suggestions.append(option)
                    suggestion_label = customtkinter.CTkButton(self.root, text = option, fg_color='white',anchor='center',width = self.width,corner_radius=1,border_color='gray',text_color='black',height=self.height,border_width=1,command = lambda : self.click(self.suggcounter), font = ('Arial',self.text_size))
                    suggestion_label.place(x = self.x, y = self.y + self.height + self.suggcounter * self.height)
                    self.suggcounter += 1
                    self.suggestion_labels.append(suggestion_label)

        for option in self.options:

            if option in input:
                self.delete_suggestions(input)

                    
        self.suggcounter = 0
        self.priorinput = input
        self.root.after(10,self.update_suggestions)

    def click(self,suggcounter):

        self.widget.delete(0, customtkinter.END)
        self.widget.insert(0,self.suggestions[suggcounter])

def main():

    root = customtkinter.CTk()
    root.geometry('400x400')

    countries = ['India','United States','United Kingdom','UAE']

    combo = customtkinter.CTkComboBox(root,width = 200,height = 20)
    combo.place(y = 0, x = 100)


    S = SuggestionBox(root,100,0,combo,countries)
    S.update_suggestions()



    root.mainloop()


if __name__ == '__main__':
    main()
