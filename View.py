from cgitb import text
from distutils.cmd import Command
from email import message
import json
from msilib.schema import ListBox
import tkinter as tk
from turtle import right
import openai
import NlpCloudFunctions as nlp

class View:

    def __init__(self):
        self.user = ""
        self.data = {}
        self.data ['Data'] = []
        self.service = ""
        self.input = []
        self.output = []

        self.login = tk.Tk()
        self.login.title("LOGIN")
        self.login.geometry("360x392")
        self.centrar(self.login, 360, 360)
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.login.iconphoto(False, self.iconImage)

        self.lblLogin = tk.Label(self.login, text="LOGIN")
        self.lblLogin.place(x=150, y=60)

        self.userName = tk.StringVar()
        self.userName.set("")

        self.lblUser = tk.Label(self.login, text="Input your UserName")
        self.lblUser.place(x=110, y=100)
        self.txtUser = tk.Entry(self.login, textvariable=self.userName)
        self.txtUser.place(x=110, y=140)
        self.btnUser = tk.Button(self.login, text="LOGIN", command=self.PrincipalWindowView)
        self.btnUser.place(x=150, y=180)

        self.login.mainloop()
    

    #Pricipal window

    def PrincipalWindowView(self):
        self.user = self.userName
        self.login.destroy()

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

    #Opinion
    def Opinion(self):
        self.windows_one = tk.Toplevel()
        self.windows_one.geometry("1000x700")
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.windows_one.iconphoto(False, self.iconImage)
        self.centrar(self.windows_one)
        
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
        self.service = "Translation_and_sentimentAnalysis-NlpCloud"
        self.input.append(self.UserAnswer.get())
        textOpinion = nlp.NlpCloudFunctions()
        textOpinion.setUserText(userText=str(self.UserAnswer.get()))
        self.UserAnswer.set("")
        opinion = textOpinion.Opinion()
        self.output.append(opinion)
        self.lblOpinion = tk.Label(self.windows_one, text=opinion)
        self.lblOpinion.grid(row=3,column=0)
        self.dataJson()

    #Preguntas y respuestas
    def Questions(self):
        self.windows_two = tk.Toplevel()
        self.windows_two.geometry("1000x700")
        self.windows_two.title("Question and Answers")
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.windows_two.iconphoto(False, self.iconImage)
        self.centrar(self.windows_two)

        self.logoImage1 = tk.PhotoImage(file="./Img/logo_rojofull.png")
        self.logo1 = tk.Label(self.windows_two, image=self.logoImage1)
        self.logo1.grid(row=0, column=0)

        self.userQuestion = tk.StringVar()
        self.userQuestion.set("")
        self.txtQuestionW2 = tk.Entry(self.windows_two, textvariable=self.userQuestion)
        self.txtQuestionW2.grid(row=1, column=0)
        self.btnSubmit1 = tk.Button(self.windows_two, text="SUBMIT", command=self.SendQuestion)
        self.btnSubmit1.grid(row=1, column=1)

    def SendQuestion(self):
        self.service = "TextGeneration_and_QuestionAnswer-NlpCloud"
        self.input.append(self.userQuestion.get())
        textQuestion = nlp.NlpCloudFunctions()
        textQuestion.setQuestion(question=str(self.userQuestion.get()))
        self.userQuestion.set("")
        question = textQuestion.Questions()
        self.output.append(question)
        self.lblAnswer = tk.Label(self.windows_two, text=question)
        self.lblAnswer.grid(row=2,column=0)
        self.dataJson()

    #CHAT BOT WITH AI (OPENAI)

    def ChatBotWindows(self):
        self.windows_three = tk.Toplevel()
        self.windows_three.geometry("1000x700")
        self.windows_three.resizable(0,0)
        self.windows_three.title("Chat Bot")
        self.iconImage = tk.PhotoImage(file="./Img/favicon_Corarojofull-copy.png")
        self.windows_three.iconphoto(False, self.iconImage)
        self.centrar(self.windows_three)
        
        self.logoImage1 = tk.PhotoImage(file="./Img/logo_rojofull.png")
        self.logo1 = tk.Label(self.windows_three, image=self.logoImage1)
        self.logo1.place(x=350, y=0)
        
        self.lblNameW3 = tk.Label(self.windows_three, text = "Chat Bot")
        self.lblNameW3.place(x=350, y=100)

        self.conversation = "Me: Hello, who are you?\nAI: What do you want to know about donating blood?"
        self.me = []
        self.Ai = []

        self.msgFrame = tk.Frame(self.windows_three, height=35, width=50)
        self.msgFrame.place(x=350, y=200)
        self.msgChat = tk.StringVar()
        self.msgChat.set("")

        self.msgList = tk.Listbox(self.msgFrame, height=20, width=50)
        self.msgList.grid(row=0, column=0)
        self.msgList.insert(tk.END, "Me: Hello, who are you?")
        self.msgList.insert(tk.END, "AI: I am an AI, What do you want to know about donating blood?")
        self.msgList.insert(tk.END, "AI: If you want finish the conversation, write bye :)")
        self.scrollBar = tk.Scrollbar(self.msgFrame)
        self.scrollBar.place(in_=self.msgList, relx=1, relheight=1, bordermode="outside")

        self.frameField = tk.Frame(self.windows_three)
        self.frameField.place(x=350, y=600)
        self.txtField = tk.Entry(self.frameField, textvariable=self.msgChat, width=40)
        self.txtField.bind("<Return>", "")
        self.txtField.grid(row=0,column=0)
        self.sendButton = tk.Button(self.frameField, text="SUBMIT", command=self.Send)
        self.sendButton.grid(row=0,column=1)

    def Send(self):
        self.message = self.msgChat.get()
        if (("bye" in self.message.lower()) or ("thanks" in self.message.lower())):
            self.msgChat.set("")
            self.msgList.insert(tk.END, "Me: " + self.message)
            self.msgList.insert(tk.END, "AI: Ok, Good Bye!")
            self.me.append(self.message)
            self.Ai.append("Ok, Good Bye!")
            self.input.append(self.me)
            self.output.append(self.Ai)
            print(self.input)
            print(self.output)
            self.dataJson()
        else:
            self.service = "ChatBot-OpenAi"
            self.me.append(self.message)
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
        self.Ai.append(self.answer)
        self.msgList.insert(tk.END, self.answer)

    #Desings

    def centrar(self, r, al = 700, an = 1000):
        altura = al
        anchura = an
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla = r.winfo_screenwidth()
        x = (anchura_pantalla // 2) - (anchura//2)
        y = (altura_pantalla//2) - (altura//2)
        r.geometry(f"+{x}+{y}")


    #JSON

    def verifyFile(self): #Comprueba si existe el historial
        try:
            with open ("data.json") as File:
                return True     
        except FileNotFoundError as e:
            return False

    def fillJson(self):
        idFile = self.autoIncrementId()
        dictionary = {
            'id': idFile,
            'user': str(self.user.get()),
            'service': str(self.service),
            'input': str(self.input),
            'output': str(self.output)
        }
        self.service = ""
        self.input = []
        self.output = []
        return dictionary

    def dataJson(self):
        fileJson = self.fillJson()
        
        if self.verifyFile() == True:
            with open ("data.json") as File:
                self.data = json.load(File)
            self.data['Data'].append(fileJson)

            with open("data.json", 'w') as newFile:
                json.dump(self.data, newFile)
        else:
            with open("data.json", 'w') as newFile:
                self.data['Data'].append(fileJson)
                json.dump(self.data, newFile)

    def autoIncrementId(self):
        if (self.verifyFile()):
            with open ("data.json") as File:
                    datos = json.load(File)
                    for key in datos:
                        value = datos[key]
                        return (len(value)+1)
        else:
            return 1

