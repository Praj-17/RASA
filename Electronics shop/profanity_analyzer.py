import imp

from importlib_metadata import requires
from rasa.nlu.components import Component 
from rasa.nlu import utils
from rasa.nlu.model import Metadata
from profanity_filter import ProfanityFilter
class ProfanityAnalyzer(Component):
    "A pre-trained sentiment component"
    name = "profanity_analyzer"
    provides = ["entities"]
    requires = []
    defaults = []
    language_list=  ["en"]
    
    def __init__(self, component_config = None):
        super(ProfanityAnalyzer, self). __init__(component_config)
    def train(slef, training_data, cfg,**kwargs):
        pass
        
    def convert_to_rasa(self, value, confidence): 
        "convert model output into the Rasa NLU Compatible output format"  
        entity = { "value": value,
                  "confidence":confidence,"entity": "profane_word",
                  "extractor":"profanity_extractor"}
                  
            
        
    def process(self, message, **kwargs):
        pf = ProfanityFilter()
        text  = message.text()
        
        #is profane is used to check weather the message is a proper sentece or not
        value ="na"
        confidence = 0
        if pf.is_profane(text):
            tokens = text.split()
            for token in tokens:
                if pf.is_prfane(token):
                    value = token
                    confidence = 100
        if value != 'na':        
            entity= self.convert_to_rasa(value,confidence)
            message.set("entities", [entity], add_to_output = True)
        else:
            pass
    
    def persist(self, model_dir):
        pass