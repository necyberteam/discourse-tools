import os
import requests
import pprint

# see - https://meta.discourse.org/t/reading-topics-in-a-forum-with-javascript/23042/3
# for notes on getting topics
# Main thing is to get categories from sites first, and then enumerate over topics in
# each category.

# print(os.environ['DISCOURSE_AUTH'])
# print(os.environ['DISCOURSE_ROOT'])
# print(os.environ['DISCOURSE_SESS'])

# Check environment cariables are set

if 'DISCOURSE_AUTH' in os.environ:
 uauth=os.environ['DISCOURSE_AUTH']
else:
 print('ERROR: Environment variable DISCOURSE_AUTH not found.')
 print('This is value from https://DOMAIN_NAME/admin/api/keys')
 exit()

if 'DISCOURSE_ROOT' in os.environ:
 uroot=os.environ['DISCOURSE_ROOT']
else:
 print('ERROR: Environment variable DISCOURSE_ROOT not found.')
 print('This is the domain name of the discourse site e.g. https://DOMAIN_NAME')
 exit()

if 'DISCOURSE_SESS' in os.environ:
 usess=os.environ['DISCOURSE_SESS']
else:
 print('ERROR: Environment variable DISCOURSE_SESS not found.')
 print('This is an _t session key from a valid https://DOMAIN_NAME session')
 print('The _t session key is a security "feature" for some discourse installs')
 exit()

# Get site info

url_site_list='https://%s/%s?%s'%(uroot,'site.json',uauth)
cookies=dict(_t=usess)

r=requests.get(url_site_list,cookies=cookies)
pp = pprint.PrettyPrinter(indent=1)
# pp.pprint(r.json())
# exit()

# Iterate over categories from site
for c in r.json()['categories']:
 url_category_list='https://%s/c/%d.json?%s'%(uroot,c["id"],uauth)
 rr=requests.get(url_category_list,cookies=cookies)
 tl=rr.json()["topic_list"]["topics"]

 # Iterate over topic list returned for each category and match ready tag
 for t in tl:
  if 'zeta:launch-ready' in t['tags']:
   print('Ready_topic ', t['id'], t['title'])
