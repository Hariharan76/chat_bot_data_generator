
from actors import User, Bot
import random


class StateManager(object):
    def __init__(self):
        self.current_utterance : str = ''
        self.entity_map : dict = {}
        self.current_state : str = ''
        self.current_actor : str = 'user'
        self.possible_next_states : list = ['user_greetings','user_greetings_with_name']
        self.current_actor_object = self.actor_mapping()
        self.user_state_2_bot_state_mapping = {
            'user_greetings': ['bot_greetings'],
            'user_greetings_with_name': ['bot_greetings_with_name'],
            'user_free_plan_purchase':['bot_ask_full_name'],
            'user_ask_clarification_for_full_name':['bot_give_clarification_for_fullname'],
            'user_give_full_name': ['bot_ask_email_id'],
            'user_ask_clarification_for_email_id' : ['bot_give_clarification_for_email'],
            'user_give_incorrect_email_id': ['bot_ask_for_correct_email_id_again'],
            'user_give_correct_email_id' : ['bot_ask_mobile_number'],
            'user_give_incorrect_mobile_number':['bot_ask_for_correct_mobile_number_again'],
            'user_ask_clarification_for_mobile_number':['bot_give_clarification_for_mobile_number'],
            'user_give_correct_mobile_number': ['bot_ask_company_name'],
            'user_give_company_name' : ['bot_ask_company_website'],
            'user_give_company_website': ['bot_ask_num_users'],
            'user_give_incorrect_num_users': ['bot_ask_correct_num_users'],
            'user_give_correct_num_users': ['bot_ask_create_password'],
            'user_give_incorrect_password': ['bot_ask_correct_create_password'],
            'user_give_correct_password': ['bot_create_verify_message']
        }

        self.bot_state_2_user_state_mapping = {
            'bot_greetings': ['user_free_plan_purchase'],
            'bot_greetings_with_name': ['user_free_plan_purchase'],
            'bot_ask_full_name': ['user_give_full_name','user_ask_clarification_for_full_name'],
            'bot_give_clarification_for_fullname' : ['user_give_full_name'],
            'bot_ask_email_id': ['user_give_correct_email_id','user_give_incorrect_email_id','user_ask_clarification_for_email_id'],
            'bot_give_clarification_for_email' : ['user_give_correct_email_id','user_give_incorrect_email_id'],
            'bot_ask_for_correct_email_id_again' : ['user_give_correct_email_id'],
            'bot_ask_mobile_number': ['user_give_correct_mobile_number','user_give_incorrect_mobile_number','user_ask_clarification_for_mobile_number'],
            'bot_ask_for_correct_mobile_number_again': ['user_give_correct_mobile_number'],
            'bot_give_clarification_for_mobile_number': ['user_give_correct_mobile_number','user_give_incorrect_mobile_number'],
            'bot_ask_company_name' : ['user_give_company_name'],
            'bot_ask_company_website' : ['user_give_company_website'],
            'bot_ask_num_users' : ['user_give_incorrect_num_users','user_give_correct_num_users'],
            'bot_ask_correct_num_users' : ['user_give_correct_num_users'],
            'bot_ask_create_password' : ['user_give_incorrect_password','user_give_correct_password'],
            'bot_ask_correct_create_password' : ['user_give_correct_password'],
            'bot_create_verify_message': []
        }

    def actor_mapping(self):
        return User() if self.current_actor == 'user' else Bot()
    
    def change_actor(self):
        self.current_actor =  'bot' if self.current_actor == 'user' else 'user'
        self.current_actor_object = self.actor_mapping()
        return

    def change_state(self):
        self.current_state = random.choice(self.possible_next_states)
        return
    
    def update_possible_next_states(self):
        if self.current_actor == 'user':
            self.possible_next_states = self.user_state_2_bot_state_mapping[self.current_state]
        else:
            self.possible_next_states = self.bot_state_2_user_state_mapping[self.current_state]
        return


