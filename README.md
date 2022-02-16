# rasa-chat-bot-for-university-expertise-recomender
The chatbot is be able to greet you. b. A user would ask about a topic he might want help with, and relevant professor with expertise should be recommended not more than 3 at any time. c. Recommendation can be based on expertise list in profile or from descriptions etc.
* Rasa 3.0 is used in this project.
* In this project there is some files under "scrapping-and-mongodb" folder "Scrapper.py" is responcible for extrating the information(Professor Information) from https://www.swansea.ac.uk/staff/engineering/#associate-professors=is-expanded&lecturers-and-tutors=is-expanded&professors=is-expanded&readers=is-expanded&senior-lecturers=is-expanded
this website using web scrapping. For web Scrapping "Beautiful Soup" is used.
* After getting the information the results are stored in a csv file
* Then the csv file with all prof. information is stored in the mongo db.
* After all those stuffs the RASA chat bot is trined

## This are some following eg. of commands which the bot understands for the information retrival for the Prof. Information
   * I need help for [mechanical performance](topic)
   * show me the results for [mechanical performance](topic) this topic
   * help me with [mechanical performance](topic) topic
   * help me with [Fluid Dynamics](topic) topic
   * show me results for [mechanical performance](topic) topic
   * help me with [High temperature characterisation of ceramic matrix c](topic) topic
   * help me with [Fluid Dynamics](topic) topic
   * help me with [Crack initiation and growth mechanisms](topic) topic
   * I need help for[Crack initiation and growth mechanisms](topic)
 With those extra commands the 'nlu.yml' is trained
 
 ### Now stories.yml

stories:
- story: search info happy path
  steps: 
  - intent: greet
  - action: utter_how_can_i_help
  - intent: ask_for_help
    entities:
      - topic: mechanical performance
  - slot_was_set:
      - topic: mechanical performance
  - action: action_info_search
  - intent: goodbye
  - action: utter_goodbye

This is an extra addition with the existing one.

### Custom Action for information retrival from mongo db
```
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
        
```
### Here is a screenshot of a mongo db instance
![Screenshot (647)](https://user-images.githubusercontent.com/67363661/154317780-8ad466ff-b9ff-47d7-b6f2-8d8e2f2884b3.png)
 
### Here is some screenshot chatting with RASA

![Screenshot (645)](https://user-images.githubusercontent.com/67363661/154316929-ad3abbd0-8b3f-4dcc-b29f-55e2986b48d7.png)

