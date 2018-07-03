import os
import requests
import pprint

# print(os.environ['DISCOURSE_AUTH'])
# print(os.environ['DISCOURSE_ROOT'])
# print(os.environ['DISCOURSE_SESS'])

if 'DISCOURSE_AUTH' in os.environ:
 uauth=os.environ['DISCOURSE_AUTH']
else:
 print('ERROR: Environment variable DISCOURSE_AUTH not found.'
 print('This is value from https://DOMAIN_NAME/admin/api/keys'
 exit()

if 'DISCOURSE_ROOT' in os.environ:
 uroot=os.environ['DISCOURSE_ROOT']
else:
 print('ERROR: Environment variable DISCOURSE_ROOT not found.'
 print('This is the domain name of the discourse site e.g. https://DOMAIN_NAME'
 exit()

if 'DISCOURSE_SESS' in os.environ:
 usess=os.environ['DISCOURSE_SESS']
else:
 print('ERROR: Environment variable DISCOURSE_SESS not found.'
 print('This is an _t session key from a valid https://DOMAIN_NAME session'
 print('The _t session key is a security "feature" for some discourse installs')
 exit()

url_user_specific_base='https://%s/u/%s/emails.json?%s'
url_user_list='https://%s/%s?%s'%(uroot,'admin/users/list/active.json',uauth)
cookies=dict(_t=usess)

r=requests.get(url_user_list,cookies=cookies)
pp = pprint.PrettyPrinter(indent=1)
for j in r.json():
 if j["id"] >= 2:
  iu='%s %s'%(j["id"],j["username"])
  url_specific_user=url_user_specific_base%(uroot,j["username"],uauth)
  ru=requests.get(url_specific_user,cookies=cookies)
  jj=ru.json()
  if 'email' in jj:
   print(iu, jj['email'])
  else:
   print(iu)
