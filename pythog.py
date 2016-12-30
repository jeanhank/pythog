import discogs_client
import pprint as pp
import requests
import json

class Discotrek:

	#credentials

	consumer_key = 'vMilUVRineJJXVFNzPxd'
	consumer_secret = 'BITsKKSjaXyQlFdPNJHpDCuhFpDRvZVe'
	request_token_URL = 'https://api.discogs.com/oauth/request_token'
	authorize_URL = 'https://www.discogs.com/oauth/authorize'
	access_token_URL = 'https://api.discogs.com/oauth/access_token'

	user_agent = 'DiscotrekApp/0.1'

	client = discogs_client.Client(user_agent)

	def __init__(self):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.request_token_URL = request_token_URL
		self.authorize_URL = authorize_URL
		self.access_token_URL = access_token_URL
		self.client = client