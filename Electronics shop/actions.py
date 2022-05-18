from rasa_sdk import Action, Tracker

from typing import Any, Text, Dict, List

from rasa_sdk.executor import CollectingDispatcher
import re

#this is how you define one single action the format for all other is as goven below, you need to prepare 2 functions that is name and run , name gives its name and run describes the function

class ActionSearch(Action):
    def name(self) -> Text:
        return "action_search"
    def run(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Calling a DB
        #Calling an API
        # do anything
        # all calculatios are done
        camera = tracker.get_slot('camera')
        ram = tracker.get_slot('ram')
        battery = tracker.get_slot('battery')
        
        dispatcher.utter_messag(text = "Here are your search Results")
        dispatcher.utter_messag(text = "The fearures you entered" + str(camera) + ", " + str(ram) + ", " + str(battery))
        
        return []
class ActionShowLatestNews(Action):
    def name(self) -> Text:
        return "action_show_latest_news"
    def run(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Calling a DB
        #Calling an API
        # do anything
        # all calculatios are done
        dispatcher.utter_messag(text = "Here is the latest news for your category")
        
        return []
class ProductSearchForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "product_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["ram","battery","camera","budget"]

    #def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""


        #return []


    def validate_ram(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        ram_int = int(re.findall(r'[0-9]+',value)[0])
        #Query the DB and check the max value, that way it can be dynamic
        if ram_int < 50:
            return {"ram":ram_int}
        else:
            dispatcher.utter_message(template="utter_wrong_ram")

            return {"ram":None}

    def validate_camera(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        camera_int = int(re.findall(r'[0-9]+',value)[0])
        #Query the DB and check the max value, that way it can be dynamic
        if camera_int < 150:
            return {"camera":camera_int}
        else:
            dispatcher.utter_message(template="utter_wrong_camera")

            return {"camera":None}

    def validate_budget(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        budget_int = int(re.findall(r'[0-9]+',value)[0])
        #Query the DB and check the max value, that way it can be dynamic
        if budget_int < 4000:
            return {"budget":budget_int}
        else:
            dispatcher.utter_message(template="utter_wrong_budget")

            return {"budget":None}

    def validate_battery(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        battery_int = int(re.findall(r'[0-9]+',value)[0])
        #Query the DB and check the max value, that way it can be dynamic
        if battery_int < 50:
            return {"battery":battery_int}
        else:
            dispatcher.utter_message(template="utter_wrong_battery")

            return {"battery":None}


    
    # USED FOR DOCS: do not rename without updating in docs
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(text="Please find your searched items here.........")


        return []