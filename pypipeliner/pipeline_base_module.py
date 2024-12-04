class PipelineBaseModule:
    input_type = None
    output_type = None
    
    def process(self, data, **params):
        if self.input_type and not isinstance(data, self.input_type):
            raise TypeError(f"{self.__class__.__name__} expects {self.input_type.__name__} input, got {type(data).__name__}")
        
        result = self._process(data, **params)
        
        if self.output_type and not isinstance(result, self.output_type):
            raise TypeError(f"{self.__class__.__name__} should return {self.output_type.__name__}, got {type(result).__name__}")
        
        return result
    
    def _process(self, data, **params):
        raise NotImplementedError()