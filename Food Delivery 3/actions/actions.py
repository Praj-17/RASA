# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import AllSlotsReset
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionFoodOrderForm(FormValidationAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        return "validate_food_order_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["item","location","quantity"]

    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    #     """A dictionary to map required slots to
    #         - an extracted entity
    #         - intent: value pairs
    #         - a whole message
    #         or a list of them, where a first match will be picked"""


    #     return []


    def validate_item(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        food_items = ['sandwich', 'pav bhaji', 'biryani']
        
        if value.lower() in food_items:
            return {"item":value}
        else:
            dispatcher.utter_message(template="utter_wrong_item")

            return {"ram":None}

    def validate_location(
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
        #Query the DB and check the max value, that way it can be dynamic
        try:
            return {"location":str(value)}
        except:
            dispatcher.utter_message(template="utter_wrong_location")

            return {"location":None}

    def validate_quantity(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
       
        quantity = str(value)
        if quantity.isdigit():
            return {"quantity":quantity}
        elif quantity.lower() == 'a' or quantity.lower() == 'an' or quantity.lower() == 'one':
            return {"quantity":1}
        else:
            dispatcher.utter_message(template="utter_wrong_quantity")

            return {"budget":None}

   


    
    # USED FOR DOCS: do not rename without updating in docs
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(template='utter_submit')


        return []

class ActionFoodOrderForm(Action):
    """Example of a custom form action"""

    def name(self) -> Text:
        return "action_order_food"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["item","location","quantity"]
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        item = tracker.get_slot("item")
        location = tracker.get_slot("location")
        quantity = tracker.get_slot("quantity")
        
        print("Item: ",item)
        print("Location: ",location)
        print("Quantity: ",quantity)
        dispatcher.utter_message(template="utter_slots_values")
        dispatcher.utter_message(text= f"Your order for {quantity} {item} at {location} has been placed successfully. Enjoy your meal!")
    

    

   





