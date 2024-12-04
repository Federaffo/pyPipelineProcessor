
import yaml


class Pipeline:
    def __init__(self, config_path: str, available_modules: dict):
        self.steps = []
        self.available_modules = available_modules
        self.load_config(config_path)
    
    def load_config(self, config_path: str):    
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

        for module in self.config['pipeline']:
            module_name = module['type']
            params = module.get('params', {})
            module_class = self.available_modules.get(module_name, None)
            if not module_class:
                raise ValueError(f"Module type: {module_name} not imported")
            self.add_step(module_class(), params)

    def add_step(self, step, params: dict = {}):
        self.steps.append((step, params))

    def process(self, input_data):
        data = input_data
        for step, params in self.steps:
            data = step.process(data, **params)
        return data

