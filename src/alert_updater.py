from src.common.database import Database
from src.models.alerts.alert import Alert

Database.initialize()

alerts_needing_update = Alert.find_needing_update()

for alert in alerts_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()


'''
db.alerts.insert({ "_id" : "896045e647084cacb37a702f418be707", "price_limit" : 100, "last_checked" : ISODate("2016-02-09T10:35:31.542Z"), "item_id" : "d5527d22c0a74a8199fbbc0aab440463", "user_email" : "mqda0304@gmail.com" })
db.items.insert({"_id": "d5527d22c0a74a8199fbbc0aab440463", "url": "https://www.johnlewis.com/us/great-little-trading-co-cloud-wall-shelf-white/p3414641", "name": "Dexter" })
db.stores.insert({"_id": "a980989112d746a793448e706a6ad976", "query": {"class": "price price--large"}, "tag_name": "p", "name": "John Lewis", "url_prefix": "http://www.johnlewis.com"})
db.users.insert({"_id": "1234", "email": "mqda0304@gmail.com", "password": "$pbkdf2-sha256$7665$WKs1ZkwJ4ZxT6t07R0iplQ$ZKfMMAMzKxH64g.3XwaFONAlVwoZf76dWdqW6uSlQtE"})
'''

