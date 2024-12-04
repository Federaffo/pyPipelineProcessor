import yaml
from pypipeliner.modules import EntityExtractor, TextCleaner, TextGenerator, DocumentGenerator
from pypipeliner.pipeline import Pipeline

available_modules = {
    "TextCleaner": TextCleaner,
    "TextGenerator": TextGenerator,
    "DocumentGenerator": DocumentGenerator,
    "EntityExtractor": EntityExtractor
}

# Initialize empty pipeline
pipeline = Pipeline("pipeline.yaml", available_modules)

input_text = "Hi, I am Federico"
output = pipeline.process(input_text)

print(output)