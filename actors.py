from abc import ABC, abstractmethod
from tasks import Task

class Actor(ABC):
    @abstractmethod
    def step(self, state,entity_map):
        pass


class User(Actor):
    def __init__(self, name = 'User : '):
        self.name = name
        self.all_user_states = {
            'user_greetings': Task(variations_file_name='greetings.txt'),
            'user_greetings_with_name': Task(variations_file_name='greetings_with_name.txt'),
            'user_free_plan_purchase' : Task(variations_file_name='purchase.txt'),
            'user_give_full_name' : Task(variations_file_name='give_full_name.txt'),
            'user_ask_clarification_for_full_name' : Task(variations_file_name='clarification_for_fullname.txt'),
            'user_give_correct_email_id' : Task(variations_file_name='give_correct_email_id.txt'),
            'user_give_incorrect_email_id' : Task(variations_file_name='give_incorrect_email_id.txt'),
            'user_ask_clarification_for_email_id' : Task(variations_file_name='clarification_for_email_id.txt'),
            'user_give_correct_mobile_number' : Task(variations_file_name='give_correct_mobile_number.txt'),
            'user_give_incorrect_mobile_number' : Task(variations_file_name='give_incorrect_mobile_number.txt'),
            'user_ask_clarification_for_mobile_number' : Task(variations_file_name='clarification_for_mobile_number.txt'),
            'user_give_company_name' : Task(variations_file_name='give_company_name.txt'),
            'user_give_company_website' : Task(variations_file_name='give_company_website.txt'),
            'user_give_correct_num_users' : Task(variations_file_name='give_correct_num_users.txt'),
            'user_give_incorrect_num_users' : Task(variations_file_name='give_incorrect_num_users.txt'),
            'user_give_incorrect_password' : Task(variations_file_name='give_incorrect_password.txt'),
            'user_give_correct_password' : Task(variations_file_name='give_correct_password.txt'),
        }

    def step(self,state,entity_map):
        # state = state_manager.current_state
        if state not in self.all_user_states:
            raise ValueError(f"Invalid State {state} not present in list of all user states")
        current_task = self.all_user_states[state]
        utterance, new_entity_map = current_task.generate(entity_map=entity_map,actor_type='user')
        return utterance, new_entity_map

class Bot(Actor):
    def __init__(self, name = 'Assistant : '):
        self.name = name 
        self.all_bot_states = {
            'bot_greetings': Task(variations_file_name='greetings.txt'),
            'bot_greetings_with_name': Task(variations_file_name='greetings_with_name.txt'),
            'bot_ask_full_name':Task(variations_file_name='ask_full_name.txt'),
            'bot_give_clarification_for_fullname':Task(variations_file_name='give_clarification_for_fullname.txt'),
            'bot_ask_email_id':Task(variations_file_name='ask_email_id.txt'),
            'bot_give_clarification_for_email':Task(variations_file_name='give_clarification_for_email.txt'),
            'bot_ask_for_correct_email_id_again':Task(variations_file_name='ask_again_for_correct_email.txt'),
            'bot_ask_mobile_number':Task(variations_file_name='ask_mobile_number.txt'),
            'bot_give_clarification_for_mobile_number':Task(variations_file_name='give_clarification_for_mobile_number.txt'),
            'bot_ask_for_correct_mobile_number_again':Task(variations_file_name='ask_again_for_correct_mobile_number.txt'),
            'bot_ask_company_name':Task(variations_file_name='ask_company_name.txt'),
            'bot_ask_company_website': Task(variations_file_name='ask_company_website.txt'),
            'bot_ask_num_users': Task(variations_file_name='ask_num_users.txt'),
            'bot_ask_correct_num_users': Task(variations_file_name='ask_correct_num_users.txt'),
            'bot_ask_create_password': Task(variations_file_name='ask_create_password.txt'),
            'bot_ask_correct_create_password': Task(variations_file_name='ask_correct_password.txt'),
            'bot_create_verify_message' : Task(variations_file_name='create_verify_message.txt'),
        }

    def step(self,state,entity_map):
        # state = state_manager.current_state
        if state not in self.all_bot_states:
            raise ValueError(f"Invalid State {state} not present in list of all bot states")
        current_task = self.all_bot_states[state]
        utterance, new_entity_map = current_task.generate(entity_map=entity_map,actor_type='bot')
        return utterance, new_entity_map

