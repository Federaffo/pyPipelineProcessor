from typing import List

from pydantic import BaseModel
from pypipeliner.pipeline_base_module import PipelineBaseModule

class TextCleaner(PipelineBaseModule):
    input_type = str
    output_type = str
    
    def _process(self, data: str, **params) -> str:
        return self.clean(data)
    
    def clean(self, text: str) -> str:
        # rimuove caratteri speciali
        return text.strip()

class EntityExtractor(PipelineBaseModule):
    input_type = str
    output_type = list
    
    def _process(self, data: str, **params) -> list:
        return self.extract_entities(data)

    def extract_entities(self, text: str) -> List[str]:
        # estrae entità dal testo
        return ['entity1', 'entity2']

class SentimentAnalyzer(PipelineBaseModule):
    input_type = str
    output_type = float
    
    def _process(self, data: str, **params) -> float:
        return self.analyze(data)
    
    def analyze(self, text: str) -> float:
        # calcola sentiment score (-1 to 1)
        return 0.8

class TextGenerator(PipelineBaseModule):
    input_type = str
    output_type = str
    
    def _process(self, data: str, **params) -> str:
        max_length = params.get('max_length', None)
        return self.generate(data, max_length)

    def generate(self, prompt: str, max_length: int) -> str:
        # genera testo dato un prompt
        return f"Generated text based on: {prompt}"


class myDocument(BaseModel):
    text: str

class DocumentGenerator(PipelineBaseModule):
    input_type = str
    output_type = myDocument
    
    def _process(self, data: str, **params) -> myDocument:
        max_length = params.get('max_length', None)
        return self.generate(data, max_length)

    def generate(self, prompt: str, max_length: int) -> myDocument:
        # genera documento dato un prompt (restituisce un oggetto myDocument)
        return myDocument(text=f"This is a custom document generated from the prompt: {prompt}")

