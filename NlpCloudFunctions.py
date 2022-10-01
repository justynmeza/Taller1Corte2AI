from typing_extensions import Self
import nlpcloud as nlp

class NlpCloudFunctions:
    
    def __init__(self):
        self.token = "f1419ff838969dc7a5fa8f48dc9506a1acdf633a"

    def QuestionAnswer(self, question, textContext):
        client = nlp.Client("roberta-base-squad2", self.token)
        answer = client.question(question, textContext)
        return answer["answer"]
        

    def TextGeneration(self, question):
        client = nlp.Client("finetuned-gpt-neox-20b", self.token, gpu=True)
        answer = client.generation(question, max_length=500, min_length=200,)
        return answer["generated_text"]


    def SentimentAnalysis(self, userText):
        client = nlp.Client("distilbert-base-uncased-finetuned-sst-2-english", self.token)
        answer = client.sentiment(userText)
        return answer

    def Translation(self, userText):
        client = nlp.Client("nllb-200-3-3b", self.token)
        answer = client.translation(userText,'spa_Latn', 'eng_Latn')
        return answer["translation_text"]

    def LanguageDetection(self, userText):
        client = nlp.Client("python-langdetect", self.token)
        answer = client.langdetection(userText)
        fullAnswer = str(answer["languages"])[3:5]
        return fullAnswer

    def windows1(self, userText):
        translate = str(self.Translation(userText=userText))
        sentiment = str(self.SentimentAnalysis(userText=translate))

    def windows2(self, question):
        answer = str(self.TextGeneration(question=question))
        summary = str(self.QuestionAnswer(question=question, textContext=answer))
        return "Answer:\n"+str(answer)+"\nSummary:\n"+str(summary)


app = NlpCloudFunctions().windows1(userText="Me gusta donar sangre!")
print(app)