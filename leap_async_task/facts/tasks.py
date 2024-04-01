import requests
import dramatiq 
from models import CatFact# Import the Dramatiq instance

FETCH_FACT_ENDPOINT = "https://cat-fact.herokuapp.com/facts"
broker = dramatiq.get_broker()




@dramatiq.actor(broker=broker)
def fetch_fact():
    try:
        response = requests.get(FETCH_FACT_ENDPOINT)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        first_fact_text = data[0]['text']
        user_id = data[0]['user']

        CatFact.objects.create(
            text=first_fact_text,
            user_id=user_id
        )
        return True, "Successfully fetched and saved the cat fact."

    except requests.RequestException as e:
        return False, f"Error fetching data: {e}"
    except (KeyError, IndexError) as e:
        return False, f"Error processing data: {e}"
    except Exception as e:  # Catch any other unexpected exceptions
        return False, f"An error occurred: {e}" 




        
        

