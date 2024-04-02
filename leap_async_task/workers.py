import os
import dramatiq
import time
from dramatiq.brokers.redis import RedisBroker
from  django_setup import main as setup_django
import django
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

redis_url = os.getenv('REDIS_URL', 'redis://redis:6379')



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leap_async_task.settings')

setup_django()


# from   .facts.tasks import fetch_fact

def main():
    redis_broker = RedisBroker(url=redis_url, db=0,
                            namespace='sfa-queue')
    dramatiq.set_broker(redis_broker)
    
    from facts.tasks import fetch_fact
    
    redis_broker.emit_after("process_boot")
    
    while True:  
        try:
            worker = dramatiq.Worker(broker=redis_broker, worker_threads=1)
            worker.start()
            logger.info("Worker started")

           
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            logger.info("Stopping worker (KeyboardInterrupt)...")
            worker.stop()
            redis_broker.close()
            logger.info("Worker stopped")
            break  

        except Exception as e:
            logger.exception(f"Unhandled exception: {e}")
            logger.info("Restarting worker...")

if __name__ == "__main__":
    main()