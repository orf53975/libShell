#!/usr/bin/env python
import urllib

def pastebin(data, expire_time):
	pastebin_vars = {'api_dev_key':'Enter API Key Here','api_option':'paste','api_paste_code':data,'api_paste_expire_date':expire_time}
	response = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(pastebin_vars))
	url = response.read()
	return url
