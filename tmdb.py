#!/usr/bin/env python3

"""
Quick script to lookup movie description and rating from TMDb
@ankitdaf
"""

import requests
import sys

TMDB_API_URI = 'https://api.themoviedb.org'
TMDB_API_VERSION = '/3'
TMDB_API_SEARCH_PATH = '/search'
TMDB_API_MOVIE_ENDPOINT = '/movie'
TMDB_API_KEY_PARAM =  'api_key'
TMDB_API_QUERY_PARAM = 'query'

TMDB_API_KEY_VALUE = 'YOUR_KEY_HERE'

def movie_lookup(moviename):
	query_payload = {TMDB_API_KEY_PARAM:TMDB_API_KEY_VALUE,TMDB_API_QUERY_PARAM:moviename}
	r = requests.get(TMDB_API_URI+TMDB_API_VERSION+TMDB_API_SEARCH_PATH+TMDB_API_MOVIE_ENDPOINT,params=query_payload)
	response = r.json()
	total_results = response['total_results']
	if  total_results > 0:
		results = response['results'] 
		for movie in results:
			print("Title : " + movie['title'])
			print("Overview : " + movie['overview'])
			print("Popularity : " + str(movie['popularity']))
			print("Vote count : " + str(movie['vote_count']))
			print("Release Date : " + str(movie['release_date']))
			print("---------------")
			print()

if __name__ == "__main__":
	if(len(sys.argv)>1):
		movie_lookup(sys.argv[1])
