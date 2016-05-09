# FruitLine

### FruitLine (线线果实，源自《ONEPIECE》堂吉诃德·多弗朗明哥的果实能力)， 是一个分布式爬虫程序。

### 运行环境及依赖
- Python 2.7
- celery
- lxml
- SQLAlchemy
- requests


### 在/config/spider_config.ini中可以配置相关属性如下：
```
[spider]
url = https://segmentfault.com/a/1190000005083953  #抓取的起始链接
threads = 15 #开启的线程数量
filter_rule = https\://segmentfault\.com/a/.* #URL过滤规则（正则表达式）
count = 1000000 #抓取网页的最大上限
spider_model = 0 #抓取的网页是否为动态网页
crawl_policy = 0 #抓取策略

```


