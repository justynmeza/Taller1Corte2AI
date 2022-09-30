from email import message
import tkinter as tk
import openai


class View:
    
    def __init__(self):
        self.principalWindows = tk.Tk()
        self.principalWindows.geometry("500x500")
        self.principalWindows.attributes('-fullscreen', True)
        self.principalWindows.title("BANCO NACIONAL DE SANGRE")
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.principalWindows.iconphoto(False, self.iconImage)

        self.menuPpal = tk.Menu(self.principalWindows)
        self.principalWindows.config(menu = self.menuPpal)
        self.options = tk.Menu(self.menuPpal)
        self.options.add_command(label="Module 1", command=self.windows1)
        self.options.add_command(label="Module 2", command=self.windows2)
        self.options.add_command(label="Module 3", command=self.chatBotWindows)
        self.options.add_command(label="Exit", command=self.principalWindows.destroy)
        self.menuPpal.add_cascade(label="Options", menu=self.options)

        self.logoImage = tk.PhotoImage(file="./Img/logo_rojofull.png")
        self.logo = tk.Label(self.principalWindows, image=self.logoImage)
        self.logo.grid(row=0, column=0)

        #Description
        self.lblTitle1 = tk.Label(self.principalWindows, text="Banco Nacional de Sangre")
        self.lblTitle1.grid(row=2, column=1)
        self.lblDescription = tk.Label(self.principalWindows, text="Sómos un banco de sangre sin ánimo de lucro con tecnología de\npunta y personal altamente calificado, sensible y ético al servicio de\ntodos.")
        self.lblDescription.grid(row=3, column=1)

        self.principalWindows.mainloop()
    
    #Area psicologica
    def windows1(self):
        self.windows_one = tk.Toplevel()
        self.windows_one.geometry("400x200")
        self.windows_one.title("Windows One")
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.windows_three.iconphoto(False, self.iconImage)
        
        self.logoImage1 = tk.PhotoImage(file="./Img/logo_rojofull.png")
        self.logo1 = tk.Label(self.windows_three, image=self.logoImage1)
        self.logo1.grid(row=0, column=0)

        self.lblQuestionW1 = tk.Label(self.windows_one, text= "Write your opinion about the donated blood")
        self.lblQuestionW1.grid(row=1, column=0)
        self.UserAnswer = tk.StringVar()
        self.UserAnswer.set("")
        self.txtAnswerW1 = tk.Entry(self.windows_one, textvariable=self.UserAnswer)
        self.txtAnswerW1.grid(row=2, column=0)
        



    def windows2(self):
        self.windows_two = tk.Toplevel()
        self.windows_two.geometry("400x200")
        self.windows_two.title("Windows Two")
        self.lblNameW2 = tk.Label(self.windows_two, text = "Windows 2")
        self.lblNameW2.grid(row = 0, column=0)



    #CHAT BOT WITH AI (OPENAI)

    def chatBotWindows(self):
        self.windows_three = tk.Toplevel()
        self.windows_three.title("Chat Bot")
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.windows_three.iconphoto(False, self.iconImage)
        
        self.logoImage1 = tk.PhotoImage(file="./Img/logo_rojofull.png")
        self.logo1 = tk.Label(self.windows_three, image=self.logoImage1)
        self.logo1.grid(row=0, column=0)
        
        self.lblNameW3 = tk.Label(self.windows_three, text = "Chat Bot")
        self.lblNameW3.grid(row = 0, column=1)

        self.msgFrame = tk.Frame(self.windows_three)
        self.msgFrame.grid(row=1,column=0)
        self.msgChat = tk.StringVar()
        self.msgChat.set("")
        self.scrollBar = tk.Scrollbar(self.msgFrame)

        self.msgList = tk.Listbox(self.msgFrame, height=25, width=50, yscrollcommand=self.scrollBar.set)
        self.msgList.grid(row=1,column=0)
        self.msgList.insert(tk.END, "Me: Hello, who are you?")
        self.msgList.insert(tk.END, "AI: I am an AI, What do you want to know about donating blood?")

        self.conversation = "Me: Hello, who are you?\nAI: What do you want to know about donating blood?"

        self.txtField = tk.Entry(self.windows_three, textvariable=self.msgChat)
        self.txtField.bind("<Return>", "")
        self.txtField.grid(row=2,column=0)
        self.sendButton = tk.Button(self.windows_three, text="SUBMIT", command=self.send)
        self.sendButton.grid(row=2,column=1)


    def send(self):
        self.message = self.msgChat.get()
        self.msgChat.set("")
        self.msgList.insert(tk.END, "Me: " + self.message)
        self.conversation += "\nMe: " + self.message
        self.openAi()

    def openAi(self):
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=self.conversation,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Me:", " AI:"]
        )
        self.answer = response.choices[0].text.strip()
        self.conversation += "\n" + self.answer
        self.msgList.insert(tk.END, self.answer)

