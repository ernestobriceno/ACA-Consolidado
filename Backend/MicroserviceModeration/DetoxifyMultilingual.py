from detoxify import Detoxify

class DetoxifyMultilingual:
    def __init__(self):
        self.model = Detoxify('multilingual')

    def predict(self, text: str) -> dict:
        return self.model.predict(text)
