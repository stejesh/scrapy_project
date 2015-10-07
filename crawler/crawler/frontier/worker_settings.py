from distributed_frontera.settings.default_settings import MIDDLEWARES

#MAX_REQUESTS = 0
MAX_NEXT_REQUESTS = 128     # Size of batch to generate per partition, should be consistent with
                            # CONCURRENT_REQUESTS in spider. General recommendation is 5-7x CONCURRENT_REQUESTS
CONSUMER_BATCH_SIZE = 50   # Batch size for updates to backend storage
NEW_BATCH_DELAY = 30.0      # This cause spider to wait for specified time, after getting empty response from
                            # backend

#--------------------------------------------------------
# Url storage
#--------------------------------------------------------
BACKEND = 'distributed_frontera.backends.hbase.HBaseBackend'
HBASE_DROP_ALL_TABLES = False
HBASE_THRIFT_PORT = 9090
HBASE_THRIFT_HOST = 'localhost'
HBASE_QUEUE_PARTITIONS = 2  # Count of spider instances

MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

KAFKA_LOCATION = 'localhost:9092'
FRONTIER_GROUP = 'scrapy-crawler'
INCOMING_TOPIC = 'frontier-done'    # Topic used by spiders where to send fetching results
OUTGOING_TOPIC = 'frontier-todo'    # Requests that needs to be downloaded is written there
SCORING_GROUP = 'scrapy-scoring'
SCORING_TOPIC = 'frontier-score'    # Scores provided by strategy worker using this channel and read by storage
                                    # worker.

#--------------------------------------------------------
# Logging
#--------------------------------------------------------
LOGGING_EVENTS_ENABLED = False
LOGGING_MANAGER_ENABLED = True
LOGGING_BACKEND_ENABLED = True
LOGGING_DEBUGGING_ENABLED = False