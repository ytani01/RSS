# RSSリーダー


## install

```
$ cd
$ python3 -m venv env-rss
$ . ~/env-rss/bin/activate
(env-rss)$ cd ~/env-rss
(env-rss)$ git clone https://github.com/ytani01/RSS.git
(env-rss)$ cd RSS
(env-rss)$ pip install -r requirements.txt
```


## usage

```
$ cd ~/env-rss/RSS
$ ./rss.py RSS-URL
```


### URLs

* [Yahoo天気:横浜](https://rss-weather.yahoo.co.jp/rss/days/4610.xml):
  https://rss-weather.yahoo.co.jp/rss/days/4610.xml
* [日テレNEWS24](http://www.news24.jp/rss/index.rdf):
  http://www.news24.jp/rss/index.rdf
