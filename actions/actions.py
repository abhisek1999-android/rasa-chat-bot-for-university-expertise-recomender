# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import pymongo
import pandas as pd
import csv
from pprint import pprint
from sympy import xfield

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myclient.list_database_names())
mydb = myclient["Prof_Info"]
myCol=mydb['prof_data']

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_info_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topic=tracker.get_slot("topic")
        query={"expertise":{"$regex":topic}}
        mydoc = myCol.find(query,{ "_id": 0, "name": 1, "expertise": 1,"phone":1,"about":1 }).limit(3)

        for x in mydoc:
                dispatcher.utter_message(text=f"Here what I have found: \n {x}")
           

        return []
