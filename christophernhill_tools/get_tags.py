import os
import requests
import pprint

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

url_tags_list='https://%s/%s?%s'%(uroot,'tags.json',uauth)
cookies=dict(_t=usess)

r=requests.get(url_tags_list,cookies=cookies)
pp = pprint.PrettyPrinter(indent=1)
# pp.pprint(r.json())
# exit()
for t in r.json()['tags']:
 print('"%s"'%(t['text']))

# {'category_list': {'can_create_category': True,
#                    'can_create_topic': True,
#                    'categories': [{'can_edit': True,
#                                    'color': '3AB54A',
#                                    'default_top_period': 'all',
#                                    'default_view': '',
#                                    'description': 'Questions about Slurm, Sun '
#                                                   'GridEngine, LSF, PBS and '
#                                                   'other schedulers',
#                                    'description_excerpt': 'Questions about '
#                                                           'Slurm, Sun '
#                                                           'GridEngine, LSF, '
#                                                           'PBS and other '
#                                                           'schedulers',
#                                    'description_text': 'Questions about Slurm, '
#                                                        'Sun GridEngine, LSF, '
#                                                        'PBS and other '
#                                                        'schedulers',
#                                    'has_children': False,
#                                    'id': 5,
#                                    'minimum_required_tags': 0,
#                                    'name': 'Schedulers',
