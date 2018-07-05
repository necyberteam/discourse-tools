import os
import requests
import pprint
import string
import secrets
import json

#
#  Create a whole load of accounts at Discourse using API
#  Primarily for migrating from one site to another
#  
#  Program reads a file with records like below
#
#  # 2 christophernhill XXXXXXXXXXXXXXXX@YYYYY.com Christophernhill
#  # 6 chrishill-regular XXXXX@ZZZZ.edu Christopher Hill
#  62 zoe.braiterman XXXXXXXX@BBBBB.com Zoe Braiterman
#
#  for lines that don't begin with '#' it requests an account
#  creation with the username from the second field.
#
#  Since this is for migrating users we avoid spamming them 
#  with activate account email by sending activate account
#  emails to an address in the variable email_template.
#
#  A 33 character random string of alphabetic and number characters is used as a password.
#
# Subsequent to this running program, and ACKing activate emails, we run another
# program to set emails to correct values.
#


# print(os.environ['DISCOURSE_AUTH'])
# print(os.environ['DISCOURSE_ROOT'])
# print(os.environ['DISCOURSE_SESS'])

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

url_user_create='https://%s/%s?%s'%(uroot,'users.json',uauth)
cookies=dict(_t=usess)

fname="current_source_site_emails.txt"
with open(fname) as f:
    content = f.read().splitlines()

# In actual use this needs to be replaced with a real value
email_template="XXXXXXXXXXXXXXXX+rcfaq-%s@YYYYYYYY.com"

for c in content:
 if c[:1] != '#':
  cs=c.split(" ")
  N=33
  pw=''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(N))
  pl={'name':"", 'email':email_template%(cs[1]), 'password':pw, 'username':cs[1]}
  print(json.dumps(pl))
  print(url_user_create)
  r=requests.post(url_user_create,cookies=cookies,json=pl)
  print(r.text)
  # exit()


# print(content)

# r=requests.post(url_tags_list,cookies=cookies)
# pp = pprint.PrettyPrinter(indent=1)
# pp.pprint(r.json())
# exit()
# for t in r.json()['tags']:
#  print('"%s"'%(t['text']))
