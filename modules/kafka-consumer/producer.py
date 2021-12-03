from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
person_msg = dict({'first_name':'Jane','last_name':'Dorsey','company_name':'Vodacom'})
# location_msg = dict({'id':70,'person_id':30 , 'creation_time':'2020-04-07 11:47:12.000000', 'latitude' : '-122.290883','longitude':'37.55363'})
producer.send('udaconnecttopic', bytes(str(person_msg), 'utf-8'))
# .send('location', bytes(str(location_msg), 'utf-8'))
producer.flush()
