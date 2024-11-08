# from abc import ABC, abstractmethod
import random
import os
import re

class Task(object):
    def __init__(self,variations_file_name):
        self.variations_file_name = variations_file_name
        self.user_utterances_base_path = './user_utterances'
        self.bot_utterances_base_path = './bot_utterances'
        self.entities_base_path = './entities'

    @staticmethod
    def get_item(path):
        # print(path)
        with open(path,'r') as f:
            utterances = f.readlines()
        assert f.closed == True
        return random.choice(utterances).strip()
    
    @staticmethod
    def get_entity_name(text:str)-> list[str]:
        pattern = r'\{.*?\}'
        matches = re.findall(pattern, text)
        if len(matches) == 0:
            return []
        entities = [match.rstrip('}').lstrip('{') for match in matches]
        return entities
    
    def get_utterances(self,entity_map,utterance_path) -> str:
        # path = os.path.join(self.user_utterances_base_path,variations_file_name)
        
        utterance = self.get_item(utterance_path)
        entities = self.get_entity_name(utterance)
        if len(entities) == 0:
            print(f"Utterance : {utterance}")
            return utterance,entity_map
        for entity in entities:
            if entity in entity_map:
                continue
            file_path = entity + '.txt'
            path = os.path.join(self.entities_base_path,file_path)
            entity_value = self.get_item(path)
            entity_map[entity] = entity_value
        utterance = utterance.format_map(entity_map)
        print(f"Utterance : {utterance}")
        return utterance,entity_map
    
    def generate(self, entity_map, actor_type):
        if actor_type == 'user':
            path = os.path.join(self.user_utterances_base_path,self.variations_file_name)
        else:
            path = os.path.join(self.bot_utterances_base_path,self.variations_file_name)

        new_utterance, updated_entity_map = self.get_utterances(entity_map=entity_map,utterance_path=path)
        return new_utterance, updated_entity_map
