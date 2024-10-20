import customtkinter
import tkinter
import extrakinter

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
        self.suggestion_buttons = []
        self.options = set(options)

        self.Stop = False
        self.numofoptions = 5

        

    def delete_suggestions(self,userinput):

        if (userinput != self.priorinput):
            
            for suggestion_button in self.suggestion_buttons:
                suggestion_button.destroy()

            del self.suggestion_buttons
            del self.suggestions
            self.suggestions = []
            self.suggestion_buttons = []

    def stop(self):

        self.Stop = True

    def update_suggestions(self):

        if(self.Stop == True):
           return 
        
        userinput = self.widget.get().casefold()
        self.delete_suggestions(userinput)

        
        if(userinput != '') and (userinput != self.priorinput):

            self.suggcounter = 0
            for option in self.options:

                if(self.suggcounter >= self.numofoptions):
                        break

                if (option.startswith(userinput)) and (option not in self.suggestions):

                    self.suggestions.append(option)
                    suggestion_button = customtkinter.CTkButton(self.root, text = ("   " + option).title(), bg_color='white',fg_color='white',
                                                                anchor='w',width = self.width,corner_radius=0,border_color='gray',
                                                                text_color='black',height=self.height/1.5,border_width=1,
                                                                command=lambda option=option: self.click(option),
                                                                font = ('Arial',self.text_size))
                    suggestion_button.place(x = self.x, y = self.y + self.height + self.suggcounter * (self.height - 22))
                    self.suggcounter += 1
                    self.suggestion_buttons.append(suggestion_button)
                    
        for option in self.options:
            if (option == userinput):
                self.delete_suggestions(userinput)
                    
        self.suggcounter = 0
        self.priorinput = userinput
        self.root.after(50,self.update_suggestions)

    def click(self,input):

        self.widget.delete(0, customtkinter.END)
        self.widget.insert(0,input.title())

    def get(self):

        return self.widget.get()


def main():

    root = customtkinter.CTk()
    root.geometry('400x400')

    countries = ['India','United States','United Kingdom','UAE']

    entry = customtkinter.CTkEntry(root,width = 200, height = 20)
    entry.place(y = 0, x = 100)

    S = SuggestionBox(root,100,0,entry,countries,10)
    S.update_suggestions()

    root.mainloop()


if __name__ == '__main__':
    main()
