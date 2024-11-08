# import os
# import random

# user_utterances_base_path = './user_utterances'
# variations_file_name = 'greetings.txt'
# variations_with_entities_file_name = 'greetings_with_entities.txt'

# path = os.path.join(user_utterances_base_path,variations_file_name)

# def get_utterance(path):
#     with open(path,'r') as f:
#         utterances = f.readlines()
#     assert f.closed == True
#     return random.choice(utterances)


# import re


# pattern = r'\(([^()]+)\)'
# pattern = r'\{.*?\}'

# # Find all occurrences of the pattern in the text
# matches = re.findall(pattern, text)

# # Print the matches
# for match in matches:
#     print(match)
#     match = match.rstrip('}').lstrip('{')
#     print(match)

# def get_entity_name(text:str)-> list[str]:
#     pattern = r'\{.*?\}'
#     matches = re.findall(pattern, text)
#     if len(matches) == 0:
#         return []
#     entities = [match.rstrip('}').lstrip('{') for match in matches]
#     return entities






# # user_greeting_state = UserGreetingState(state_name='greetings')

# # for i in range(5):
# #     user_greeting_state.get_utterances()
# import random

# entities_file = {
#     'user_name': ['Vaibhav','Rajsekar'],
#     'phone_number' : ['45367','774648']
# }

# entity_map = {'user_name': 'Rajsekar'}
# text = "Hello {user_name} I am xaia. sample phone number {phone_number}"
# entities = get_entity_name(text)

# for entity in entities:
#     if entity in entity_map:
#         continue
#     entity_map.update({entity:random.choice(entities_file[entity])})

# print(entity_map)
# print(text.format_map(entity_map))
# from dataclasses import dataclass, field
# import pandas as pd

# @dataclass
# class Utterance:
#     role: str = ''
#     content: str = ''

# @dataclass
# class Conversation:
#     conversation_id : int = -1
#     interaction : list[Utterance.__dict__] = field(default_factory=list)

# @dataclass
# class Dataset:
#     dataset : list[Conversation] = field(default_factory=list)

# dataset = [Conversation(conversation_id=1, interaction=[{'role': 'user', 'content': 'I am Vel Murugan'}, {'role': 'bot', 'content': 'Hi Vel Murugan. How can I help you'}, {'role': 'user', 'content': 'I am planning on purchasing xaia 1 plan'}, {'role': 'bot', 'content': 'Thanks for choosing xaia 1 plan. To get started may I know your full name for the record?'}, {'role': 'user', 'content': 'why do I need to give my full name?'}, {'role': 'bot', 'content': 'We need your full name for our records as part of the sign up process.'}, {'role': 'user', 'content': 'my name is Rajasekaran Ravi'}, {'role': 'bot', 'content': 'Next, I require your email-id.'}, {'role': 'user', 'content': 'why should I give my email id ?'}, {'role': 'bot', 'content': 'Email id is mandatory for the signup process and required for sending future correspondence.'}, {'role': 'user', 'content': 'this is my email address vaibh @gmaoil.com'}, {'role': 'bot', 'content': 'The email id you provided is not in the correct format. Can you please send it in the correct format? For eg. example@gmail.com'}, {'role': 'user', 'content': 'this is my email address aqWs123@gmail.com'}, {'role': 'bot', 'content': 'May I have your mobile number, please?'}]), Conversation(conversation_id=2, interaction=[{'role': 'user', 'content': 'Hello. My name is Vel Murugan'}, {'role': 'bot', 'content': "Hi Vel Murugan. I am Xaia - Worktual's Assistant. How can I assist you today?"}, {'role': 'user', 'content': 'I am interested in buying xaia 2 lite free'}, {'role': 'bot', 'content': 'Thank you for your interest in the xaia 2 lite free plan. Let me start the signup process for you. To begin with please give me your full name.'}, {'role': 'user', 'content': 'my name is Rajasekaran Ravi'}, {'role': 'bot', 'content': 'Next, could please provide me your email address?'}, {'role': 'user', 'content': 'this is my email address Mlokijnh@worktual.com'}, {'role': 'bot', 'content': 'Please provide me your mobile number'}]), Conversation(conversation_id=3, interaction=[{'role': 'user', 'content': 'Hi This is Rajsekaran'}, {'role': 'bot', 'content': 'Hello Rajsekaran.I am Xaia. How can I help you?'}, {'role': 'user', 'content': 'Can you help me to sign up for xaia 2 lite free plan'}, {'role': 'bot', 'content': 'Thanks for choosing xaia 2 lite free plan. To get started may I know your full name for the record?'}, {'role': 'user', 'content': 'my name is John Doe'}, {'role': 'bot', 'content': 'May I have your email id, please?'}, {'role': 'user', 'content': 'Is my email address necessary?'}, {'role': 'bot', 'content': 'I need your email id for cconfirmation correspondence an dit is mandatory.'}, {'role': 'user', 'content': 'vaibhav1@gmail.com'}, {'role': 'bot', 'content': 'Please provide me your mobile number'}]), Conversation(conversation_id=4, interaction=[{'role': 'user', 'content': 'Hello. My name is Bharathi'}, {'role': 'bot', 'content': 'Hi Bharathi. How can I help you'}, {'role': 'user', 'content': 'Can you help me to sign up for xaia 1 plan'}, {'role': 'bot', 'content': 'Thanks for choosing xaia 1 plan. To get started may I know your full name for the record?'}, {'role': 'user', 'content': 'Rajasekaran Ravi'}, {'role': 'bot', 'content': 'Please provide me your email address'}, {'role': 'user', 'content': 'vchdk bju.com'}, {'role': 'bot', 'content': 'It seems the email you provided is not in the correct format. Could you please re-send it again?'}, {'role': 'user', 'content': 'my email id is Mlokijnh@worktual.com'}, {'role': 'bot', 'content': 'May I have your mobile number, please?'}]), Conversation(conversation_id=5, interaction=[{'role': 'user', 'content': 'Hi This is Rajsekaran'}, {'role': 'bot', 'content': 'Hello Rajsekaran.I am Xaia. How can I help you?'}, {'role': 'user', 'content': 'I am planning on purchasing xaia 1 plan'}, {'role': 'bot', 'content': 'I can help you with the sign up process. First, I need your full name for the record.'}, {'role': 'user', 'content': 'My full name is Rajasekaran Ravi'}, {'role': 'bot', 'content': 'Please provide me your email address'}, {'role': 'user', 'content': 'Is my email address necessary?'}, {'role': 'bot', 'content': 'Email id is mandatory for the signup process and required for sending future correspondence.'}, {'role': 'user', 'content': 'my email id is hcjcUjb@yahoo.co.in'}, {'role': 'bot', 'content': 'Next, could please provide me your mobile number?'}])]
# # print(dataset)
# df = pd.DataFrame()
# for convo in dataset:
#     df_1 = pd.DataFrame(convo.interaction)
#     convo_id = [str(convo.conversation_id)] * (len(df_1)//2)
#     data_1 = {'conversation_id':convo_id,'User': list(df_1[df_1['role']=='user']['content']),'Assistant':list(df_1[df_1['role']=='bot']['content'])}
#     df1 = pd.DataFrame(data_1)
#     df = pd.concat([df,df1])
#     del df1
#     del data_1
#     del convo_id
# print(df)
# df.to_excel("data.xlsx",index=False)
# # for convo in dataset:
# df_1 = pd.DataFrame(dataset[0].interaction)
# df_2 = pd.DataFrame(dataset[1].interaction)
# # print(df[df['role']=='user']['content'])
# convo_id = [str(dataset[0].conversation_id)] * (len(df_1)//2)
# # print(convo_id)

# # data = {'conversation_id':convo_id,'User': list(df[df['role']=='user']['content']),'Assistant':list(df[df['role']=='bot']['content'])}
# data_1 = {'User': list(df_1[df_1['role']=='user']['content']),'Assistant':list(df_1[df_1['role']=='bot']['content'])}
# data_2 = {'User': list(df_2[df_2['role']=='user']['content']),'Assistant':list(df_2[df_2['role']=='bot']['content'])}

# df1 = pd.DataFrame(data_1)
# df2 = pd.DataFrame(data_2)
# df = pd.concat([df1,df2],keys=[dataset[0].conversation_id,dataset[1].conversation_id])
# print(df)

# system_prompt = "My System Prompt"
# instruction = "Set of instructions"

# def format_example(sample):
#     prompt = f"
#     {system_prompt}

#     #### Instruction
#     {instruction}

#     #### Chat History
#     {sample['chat_history']}

#     #### Current User Query
#     User : {sample['user_query']}
#     #### Response
#     Assistant : {sample['bot_response']}
#     ".strip()
#     return prompt
