
from state_manager import StateManager
from dataclasses import dataclass, field
import pandas as pd

@dataclass
class Utterance:
    role: str = ''
    content: str = ''

@dataclass
class Conversation:
    conversation_id : int = -1
    interaction : list[Utterance.__dict__] = field(default_factory=list)

@dataclass
class Dataset:
    dataset : list[Conversation] = field(default_factory=list)

    def format_and_save(self,path):
        df = self.format_dataset()
        df.to_excel(path,index=False)
        return

    def format_dataset(self):
        df = pd.DataFrame()
        for convo in self.dataset:
            df_1 = pd.DataFrame(convo.interaction)
            convo_id = [str(convo.conversation_id)] * (len(df_1)//2)
            data_1 = {'conversation_id':convo_id,'User': list(df_1[df_1['role']=='user']['content']),'Assistant':list(df_1[df_1['role']=='bot']['content'])}
            df1 = pd.DataFrame(data_1)
            df = pd.concat([df,df1])
            del df1
            del data_1
            del convo_id
        return df


def create_dataset(max_num_conversations=1):
    dataset = Dataset()
    for i in range(max_num_conversations):
        print("================================================")
        state_manager = StateManager()
        state_manager.change_state()
        convo = Conversation()
        convo.conversation_id = i+1
        while True:
            # actor = state_manager.current_actor_object
            # print(f"Starting State : {state_manager.current_state}")
            state_manager.current_utterance,state_manager.entity_map = state_manager.current_actor_object.step(state=state_manager.current_state,entity_map=state_manager.entity_map)
            state_manager.update_possible_next_states()
            utterance = Utterance()
            utterance.role = state_manager.current_actor
            utterance.content = state_manager.current_utterance
            convo.interaction.append(utterance.__dict__)
            if state_manager.possible_next_states == []:
                break
            state_manager.change_actor()
            state_manager.change_state()
            # print(f"Ending State : {state_manager.current_state}")
        del state_manager
        dataset.dataset.append(convo)
        print("================================================")
    return dataset


if __name__ == '__main__':
    dataset = create_dataset(20)
    dataset.format_and_save(path = 'mydata.xlsx')