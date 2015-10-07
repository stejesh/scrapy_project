from urlparse import urlparse
from frontera.contrib.canonicalsolvers.basic import BasicCanonicalSolver
from distributed_frontera.backends.hbase import _state
from distributed_frontera.worker.strategy.base import BaseCrawlingStrategy



SCORING_PARTITION_ID = 0
BACKEND = 'distributed_frontera.backends.hbase.HBaseBackend'
KAFKA_LOCATION = 'localhost:9092'
FRONTIER_GROUP = 'scrapy-crawler'
INCOMING_TOPIC = 'frontier-done'    # Topic used by spiders where to send fetching results
OUTGOING_TOPIC = 'frontier-todo'    # Requests that needs to be downloaded is written there
SCORING_GROUP = 'scrapy-scoring'
SCORING_TOPIC = 'frontier-score'
HBASE_DROP_ALL_TABLES = True


from urlparse import urlparse
from frontera.contrib.canonicalsolvers.basic import BasicCanonicalSolver
from distributed_frontera.backends.hbase import _state
from pprint import pprint


class CrawlingStrategy(BaseCrawlingStrategy):
    def __init__(self):
        print "$$ inside init"
        self.canonicalsolver = BasicCanonicalSolver()

    def add_seeds(self, seeds):
        scores = {}
        for seed in seeds:
            if seed.meta['state'] is None:
                url, fingerprint, _ = self.canonicalsolver.get_canonical_url(seed)
                scores[fingerprint] = 1.0
                seed.meta['state'] = _state.get_id('QUEUED')

        print "$$ inside add_seeds : seeds -> {0}, scores -> {1}".format(seeds, scores)
        print "$$ printing seed.meta"
        for seed in seeds:
            print seed.meta

        return scores

    def page_crawled(self, response, links):
        scores = {}
        response.meta['state'] = _state.get_id('CRAWLED')
        for link in links:
            if link.meta['state'] is None:
                url, fingerprint, _ = self.canonicalsolver.get_canonical_url(link)
                scores[fingerprint] = self.get_score(url)
                link.meta['state'] = _state.get_id('QUEUED')
        print "$$ inside page_crawled : value -> {0}, links -> {1}".format(response.url,links)
        return scores

    def page_error(self, request, error):
        url, fingerprint, _ = self.canonicalsolver.get_canonical_url(request)
        request.meta['state'] = _state.get_id('ERROR')
        print "$$ inside page_error : url -> {0}, error_reason -> {1}".format(request.url, error)
        return {fingerprint: 0.0}

    def get_score(self, url):
        url_parts = urlparse(url)
        path_parts = url_parts.path.split('/')
        print "$$ inside get_score : url -> {0}".format(url)
        return 1.0 / (max(len(path_parts), 1.0) + len(url_parts.path)*0.1)

    def finished(self):
        print "$$ inside finished"
        pass