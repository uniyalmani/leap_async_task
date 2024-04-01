import dramatiq

from dramatiq.brokers.redis import RedisBroker

#RedisBroker(host="127.0.0.1", port=6379, db=0, password="hunter2")
#RedisBroker(url="redis://127.0.0.1:6379/0")

def configure_redis_broker(redis_url):
    redis_broker = RedisBroker(url=redis_url, db=0,
                         namespace='sfa-queue')
    dramatiq.set_broker(redis_broker)
