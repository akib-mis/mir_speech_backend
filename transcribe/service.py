from typing import Union, List
from transcribe.utils import LangType
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize
import os

class TranscribeService:
    def __init__(self, sentence: str, lang: Union[LangType, None]= LangType.en):
        self.lang = lang
        self.sentence = sentence
        self.model_path = os.path.abspath("models")
        self.output = ""

    def _transcribe_bn(self):
        bn_model_path = os.path.join(self.model_path, "cse_buet_bangla_t5")
        tokenizer = AutoTokenizer.from_pretrained(bn_model_path, use_fast=False)
        model = AutoModelForSeq2SeqLM.from_pretrained(bn_model_path)
        input_ids = tokenizer(normalize(self.sentence), return_tensors="pt").input_ids
        generated_tokens = model.generate(input_ids)
        decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]
        self.output = decoded_tokens
        return self.output
    # /home/akib/Desktop/AI_projects/Mir_speech_backend/models/cse_buet_bangla_t5
    
    def _transcribe_en(self):
        en_model_path = os.path.join(self.model_path, "t5-base")
        tokenizer = AutoTokenizer.from_pretrained(en_model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(en_model_path)
        input_ids = tokenizer(self.sentence, return_tensors="pt").input_ids
        generated_tokens = model.generate(input_ids)
        decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]
        self.output = decoded_tokens
        return self.output
    
    def transcribe(self):
        if self.lang == LangType.en:
            self._transcribe_en()
        else:
            self._transcribe_bn()
        
        return self.output