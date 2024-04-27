from transformers import pipeline
import pandas as pd

class PhishingEmailClassifier:
    def __init__(self, model_name="kamikaze20/phishing-email-detection", max_length=512):
        self.pipe = pipeline("text-classification", model=model_name)
        self.max_length = max_length

    def truncate_text(self, text):
        if len(text) <= self.max_length:
            return text
        truncated_text = text[:self.max_length].rsplit(' ', 1)[0]
        return truncated_text

    def predict_phishing(self, text):
        truncated_text = self.truncate_text(text)
        result = self.pipe(truncated_text, top_k=None)
        return result[0]

