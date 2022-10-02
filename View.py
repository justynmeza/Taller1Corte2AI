from cgitb import text
from email import message
import json
import tkinter as tk
import openai
import NlpCloudFunctions as nlp

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
        self.options.add_command(label="Module 1", command=self.Opinion)
        self.options.add_command(label="Module 2", command=self.Questions)
        self.options.add_command(label="Module 3", command=self.ChatBotWindows)
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
    def Opinion(self):
        self.windows_one = tk.Toplevel()
        self.windows_one.geometry("400x200")
        self.windows_one.title("Area Psicologica")
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.windows_one.iconphoto(False, self.iconImage)
        
        self.logoImage1 = tk.PhotoImage(file="./Img/logo_rojofull.png")
        self.logo1 = tk.Label(self.windows_one, image=self.logoImage1)
        self.logo1.grid(row=0, column=0)

        self.lblQuestionW1 = tk.Label(self.windows_one, text= "Write your opinion about the donated blood")
        self.lblQuestionW1.grid(row=1, column=0)
        self.UserAnswer = tk.StringVar()
        self.UserAnswer.set("")
        self.txtAnswerW1 = tk.Entry(self.windows_one, textvariable=self.UserAnswer)
        self.txtAnswerW1.grid(row=2, column=0)
        self.btnSubmit = tk.Button(self.windows_one, text="SUBMIT", command=self.SendOpinion)
        self.btnSubmit.grid(row=2, column=1)

    def SendOpinion(self):
        textOpinion = nlp.NlpCloudFunctions()
        textOpinion.setUserText(userText=str(self.UserAnswer.get()))
        self.UserAnswer.set("")
        self.lblOpinion = tk.Label(self.windows_one, text="Your opinion is: "+ textOpinion.Opinion())
        self.lblOpinion.grid(row=3,column=0)

    #Preguntas y respuestas
    def Questions(self):
        self.windows_two = tk.Toplevel()
        self.windows_two.geometry("400x200")
        self.windows_two.title("Question and Answers")
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.windows_two.iconphoto(False, self.iconImage)

        self.logoImage1 = tk.PhotoImage(file="./Img/logo_rojofull.png")
        self.logo1 = tk.Label(self.windows_two, image=self.logoImage1)
        self.logo1.grid(row=0, column=0)

        self.userQuestion = tk.StringVar()
        self.userQuestion.set("")
        self.txtQuestionW2 = tk.Entry(self.windows_two, textvariable=self.userQuestion)
        self.txtQuestionW2.grid(row=1, column=0)
        self.btnSubmit1 = tk.Button(self.windows_two, text="SUBNIT", command=self.SendQuestion)
        self.btnSubmit1.grid(row=2, column=1)

    def SendQuestion(self):
        textQuestion = nlp.NlpCloudFunctions()
        textQuestion.setQuestion(userText=str(self.UserAnswer.get()))
        self.userQuestion.set("")
        self.lblAnswer = tk.Label(self.windows_two, text= textQuestion.Questions())
        self.lblAnswer.grid(row=3,column=0)

    #CHAT BOT WITH AI (OPENAI)

    def ChatBotWindows(self):
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
        self.sendButton = tk.Button(self.windows_three, text="SUBMIT", command=self.Send)
        self.sendButton.grid(row=2,column=1)


    def Send(self):
        self.message = self.msgChat.get()
        self.msgChat.set("")
        self.msgList.insert(tk.END, "Me: " + self.message)
        self.conversation += "\nMe: " + self.message
        self.OpenAi()

    def OpenAi(self):
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

