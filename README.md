Assuming all the kafka topics/partitions are created as per the docs prior to these steps

Get into the directory
`cd scrapy_project`

Run the DB & SW worker

```sh
python -m distributed_frontera.worker.main --config crawler.crawler.frontier.worker_settings
python -m distributed_frontera.worker.score --config crawler.crawler.frontier.strategy_list.strategy0 --strategy crawler.crawler.frontier.strategy_list.strategy0
```

Run the spider with distributed_frontera
`scrapy crawl CustomSpider -s FRONTERA_SETTINGS=crawler.frontier.spider_settings.settings0`

Run the spider with frontera mode

`scrapy crawl CustomSpider`

On my side, the frontera mode is much much faster, (crawling and scraping data fill up the terminal fast)

on distributed_frontera however, it is very very slow, a single link a second, and it halts suddenly giving a "finished" message.

I Hope there's something in there to tweak.

