from typing_extensions import Self
import nlpcloud as nlp

class NlpCloudFunctions:
    
    def __init__(self):
        self.token = "2d60236792da4dbb4f13a91ce677a0ee0c6f9550"

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
        return answer["label"]

    def Translation(self, userText, language):
        client = nlp.Client("nllb-200-3-3b", self.token)
        answer = client.translation(userText, language, 'en')
        return answer["translation_text"]

    def LanguageDetection(self, userText):
        client = nlp.Client("python-langdetect", self.token)
        answer = client.langdetection(userText)
        fullAnswer = str(answer["languages"])[3:5]
        return fullAnswer

    def windows1(self, userText):
        language = str(self.LanguageDetection(userText=userText))
        if (language != "en"):
            translate = str(self.Translation(userText=userText, language=language))
        else:
            translate = userText
        sentiment = str(self.SentimentAnalysis(userText=translate))

    def windows2(self, question):
        answer = str(self.TextGeneration(question=question))
        summary = str(self.QuestionAnswer(question=question, textContext=answer))
        return "Answer:\n"+str(answer)+"\nSummary:\n"+str(summary)


app = NlpCloudFunctions().windows2(question="What needed for donated blood?")
print(app)