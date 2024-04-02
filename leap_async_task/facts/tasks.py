import requests
import dramatiq 
import logging
from facts.models import CatFact


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FETCH_FACT_ENDPOINT = "https://cat-fact.herokuapp.com/facts"
broker = dramatiq.get_broker()




@dramatiq.actor(broker=broker)
def fetch_fact():
    try:
        response = requests.get(FETCH_FACT_ENDPOINT)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = response.json()
        if data:
            first_fact = data[0]
            text = first_fact.get('text')
            user_id = first_fact.get('user')
            if text and user_id:
                CatFact.objects.create(text=text, user_id=user_id)
                logger.info("Successfully fetched and saved the cat fact.")
            else:
                logger.error("Missing data in the fetched fact.")
        else:
            logger.error("No data returned from the fetch request.")
    except requests.RequestException as e:
        logger.error(f"Error fetching data: {e}")
    except (KeyError, IndexError) as e:
        logger.error(f"Error processing data: {e}")
    except Exception as e:  # Catch any other unexpected exceptions
        logger.error(f"An error occurred: {e}")


        
        

