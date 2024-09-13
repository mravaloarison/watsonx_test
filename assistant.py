from ibm_watson import AssistantV2, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

from dotenv import load_dotenv
import os

from datetime import date

load_dotenv()

API_KEY = os.getenv("WATSONX_API_KEY")
URL = os.getenv("WATSONX_URL")
ENV_ID = os.getenv("WATSONX_ENV_ID")
SKILL_ID = os.getenv("WATSONX_SKILL_ID")

curent_date = date.today().strftime("%Y-%m-%d")

authenticator = IAMAuthenticator(API_KEY)
assistant = AssistantV2(
    version=curent_date,
    authenticator=authenticator
)

assistant.set_service_url(URL)

session_id = assistant.create_session(
    assistant_id=ENV_ID
).get_result()["session_id"]

def watsonx_get(text):
    try: 
        response = assistant.message(
            ENV_ID,
            session_id,
            input={ "text": text }
        ).get_result()

        return json.dumps(response, indent=2)
    
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message
    
def bulk_watsonx_get():
    try:
        response=assistant.bulk_classify(
            skill_id=SKILL_ID,
            input=[{'text': 'I want to order some coffee'}]
        ).get_result()

        return json.dumps(response, indent=2)
    
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

print(bulk_watsonx_get())