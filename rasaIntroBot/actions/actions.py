from typing import Text, List

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ValidateHealthForm(FormValidationAction):

  def name(self) -> Text:
      return "validate_health_form"

  async def required_slots(
    self,
    slots_mapped_in_domain: List[Text],
    dispatcher: "CollectingDispatcher",
    tracker: "Tracker",
    domain: "DomainDict"
  ) -> List[Text]:
    if tracker.get_slot("confirm_exercise") == True:
      return ["confirm_exercise", "exercise", "sleep", "diet", "stress", "goal"]
    else:
      return ["confirm_exercise", "sleep", "diet", "stress", "goal"]






      '''version: "2.0"

stories:

- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_great
  - action: utter_happy

- story: sad path 1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: affirm
  - action: utter_happy

- story: sad path 2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: deny
  - action: utter_goodbye

- story: ask_roast_friends
  steps:
  - intent: greet
  - action: utter_greet
  - intent: ask_roast_friends
  - action: utter_roast_friends
  
- story: ask_lower_stress
  steps:
  - intent: greet
  - action: utter_greet
  - intent: ask_lower_stress
  - action: utter_lower_stress

- story:  survey happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: affirm
  - active_loop: forms{"name":"health_form"}
  - action: utter_slot_values

- story: Thank you
  steps:
  - intent: thank
  - action: utter_no_worries
  - intent: goodbye
  - action: utter_goodbye

- story: survey_stop
  steps:
  - intent: greet
  - action: utter_greet
  - intent: affirm
  - action: health_form
  - active_loop: forms{"name":"health_form"}
  - intent: out_of_scope
  - action: utter_ask_continue
  - intent: deny
  - action: action_deactivate_form
  - action: utter_goodbye

- story: survey_continue
  steps:
  - intent: greet
  - action: utter_greet
  - intent: affirm
  - action: health_form
  - active_loop: forms{"name":"health_form"}
  - intent: out_of_scope
  - action: utter_ask_continue
  - intent: affirm
  - action: health_form
  - action: utter_slots_values

- story: no survey
  steps:
  - intent: greet
  - action: utter_greet
  - intent: deny
  - action: utter_goodbye

- story: ask health questions form
  steps:
  - intent: greet
  - action: utter_greet
  - intent: affirm
  - action: health_form
  - intent: ask_exercise
  - action: health_form
  - action: utter_goodbye

'''