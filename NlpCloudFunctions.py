from typing_extensions import Self
import nlpcloud as nlp

class NlpCloudFunctions:
    
    def __init__(self):
        self.token = "b5674efe3b606da7fd766064bfe6e7ede2e59775"

    def QuestionAnswer(self, question, textContext):
        client = nlp.Client("roberta-base-squad2", self.token)
        answer = client.question(question, textContext)
        return answer["answer"]
        

    def TextGeneration(self, question):
        client = nlp.Client("finetuned-gpt-neox-20b", self.token, gpu=True)
        answer = client.generation(question, min_length=100, max_length=500)
        return answer["generated_text"]


    def SentimentAnalysis(self, userText):
        client = nlp.Client("distilbert-base-uncased-finetuned-sst-2-english", self.token)
        answer = client.sentiment(userText)
        return answer["label"]

    def Translation(self, userText):
        client = nlp.Client("nllb-200-3-3b", self.token)
        answer = client.translation(userText, 'en', 'es')
        return answer["translation_text"]

    def LanguageDetection(self, userText):
        client = nlp.Client("python-langdetect", self.token)
        answer = client.langdetection(userText)
        fullAnswer = str(answer["languages"])[3:5]
        return fullAnswer


    def windows1(self, question):
        return self.QuestionAnswer(question, self.TextGeneration(question))


app = NlpCloudFunctions().Translation("What needed for donated blood?")
print(app)