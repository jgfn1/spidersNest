# spidersNest
A webcrawler application with Scrapy, Zyte and MongoDB Atlas.

## Websites crawled
  * [Boletim Econômico](https://boletimeconomico.com.br/)
  * [InfoMoney](https://www.infomoney.com.br/)
  * [Uol Economia](https://economia.uol.com.br/)

## Setup your MongoDB
  Docs: [MongoDB Docs](https://docs.mongodb.com/manual/)
  
  After MongoDB is set, initialize the connection at a database.py file in the same folder of pipelines.py.
  
  #### E.g. with MongoDB Atlas:
    #database.py
    import pymongo
    dbClient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<cluster>.i3n8n.mongodb.net/<db_name>?retryWrites=true&w=majority")
    
## Run 
  ```{bash}
  $ scrapy crawl boletimEconomico
  $ scrapy crawl infoMoney
  $ scrapy crawl uolEconomia
  ```
## Run & dump to JSON Line file
  ```{bash}
  $ scrapy crawl boletimEconomico -o boletimEconomico.jl
  $ scrapy crawl infoMoney -o infoMoney.jl
  $ scrapy crawl uolEconomia -o uolEconomia.jl 
```
## Deploy
   Docs: [Zyte Docs (former Scrapy Cloud)](https://support.zyte.com/support/solutions/22000084243)  
   #### E.g.:
   
   After creating your account, project in Zyte and setting up dependencies:
   
   ```{bash}
    $ pip install shub
    $ shub login
       API key: <api_key>
    $ shub deploy <project_id>
   ```
