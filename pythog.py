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

	#temporary token just to see. need to implement OAuth
	my_user_token = 'FUVJEoiYuwgeuLGgPUEqvlYiGCEnyymAHtKbtSrw'

	user_agent = 'DiscotrekApp/0.1'

	client = discogs_client.Client(user_agent, user_token = my_user_token)