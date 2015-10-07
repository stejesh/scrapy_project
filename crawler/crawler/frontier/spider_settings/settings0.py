from distributed_frontera.settings.default_settings import MIDDLEWARES

#MAX_REQUESTS = 0
MAX_NEXT_REQUESTS = 128     # Should be consistent with MAX_NEXT_REQUESTS set for Frontera worker

MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

#--------------------------------------------------------
# Crawl frontier backend
#--------------------------------------------------------
BACKEND = 'distributed_frontera.backends.remote.KafkaOverusedBackend'
KAFKA_LOCATION = 'localhost:9092'       # Your Kafka service location
SPIDER_PARTITION_ID = 0                 # Partition ID assigned

#--------------------------------------------------------
# Logging
#--------------------------------------------------------
LOGGING_ENABLED = True
LOGGING_EVENTS_ENABLED = True
LOGGING_MANAGER_ENABLED = True
LOGGING_BACKEND_ENABLED = True
LOGGING_DEBUGGING_ENABLED = True






# Frontera settings


SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'

RANDOMIZE_DOWNLOAD_DELAY = False