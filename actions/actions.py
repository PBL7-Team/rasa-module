from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, UserUtteranceReverted, AllSlotsReset, Restarted

from actions.search import search_wikipedia
from actions.recommend import recommend_place

def name_cap(text):
    tarr = text.split()
    for idx in range(len(tarr)):
        tarr[idx] = tarr[idx].capitalize()
    return ' '.join(tarr)

class ActionSaveCustInfo(Action):
    def name(self):
        return 'action_save_cust_info'

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.current_state()["sender_id"]
        print(user_id)
        cust_name = next(tracker.get_latest_entity_values("cust_name"), None)
        cust_sex = next(tracker.get_latest_entity_values("cust_sex"), None)
        bot_position = "mình"

        if cust_sex is None:
            cust_sex = "bạn"

        if cust_sex in ["anh", "chị"]:
            bot_position = "em"
        elif cust_sex in ["cô", "chú"]:
            bot_position = "cháu"
        elif cust_sex in ["mình", "tớ"]:
            bot_position = "mình"
        elif cust_sex in ["tôi"]:
            bot_position = "tôi"

        if not cust_name:
            return []
        print(cust_name)
        print(name_cap(cust_name))
        return [SlotSet('cust_name', " " + name_cap(cust_name)), SlotSet('cust_sex', name_cap(cust_sex)), SlotSet('bot_position', name_cap(bot_position))]

class ActionSaveMobileNo(Action):
    def name(self):
        return 'action_save_mobile_no'

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.current_state()["sender_id"]
        print(user_id)
        mobile_no = next(tracker.get_latest_entity_values("inp_number"), None)

        if not mobile_no:
            return [UserUtteranceReverted()]

        mobile_no = mobile_no.replace(" ", "")
        return [SlotSet('mobile_no', mobile_no)]

class ActionResetSlot(Action):
    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("transfer_nick", None), SlotSet("transfer_amount", None), SlotSet("transfer_amount_unit", None)]
    
    
class ActionSearchPlaceInfo(Action):
    def name(self):
        return "action_search_place_info"

    def run(self, dispatcher, tracker, domain):
        search_term= next(tracker.get_latest_entity_values("place"), None)
        msg = search_wikipedia(search_term)
        dispatcher.utter_message(msg)
        return []
    
class ActionRecommendPalce(Action):
    def name(self):
        return "action_recommend_place"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message['text']
        num= next(tracker.get_latest_entity_values("number"), None)
        msg = recommend_place(user_message,num)
        dispatcher.utter_message(msg)
        return []

