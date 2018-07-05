Chris scripts to use Discourse API ( https://docs.discourse.org/ )

  - ```get_user_email.py```.
    Python 3 script to get user names and emails from the Discourse site.
    Needs an API key ( see - /admin/api/keys at Discourse site ).
    Some sites also need valid web based login _t cookie.
    Both these are passed from environment variables set external
    to script. These are privileged access keys so don't store them in github by mistake! 
    The API key can be revoked online, the _t cookie can be revoked by logging out of
    the web session.

   - ```get_categories.py```. Python 3 script to list categories from a site and their descriptions.
   
   - ```get_tags.py```. Python 3 script to list tags from a site.
   
   - ```get_topics.py```. Python 3 script to list topics and topic ids for topics with a specific tag ```zeta:launch-ready```!

 All the Discourse API scripts need environment variables set as listed below. 

   -   ```export DISCOURSE_AUTH=??????????????????????????????????????????????```. This variable
       specifies the API key from the Discourse site.

   -   ```export DISCOURSE_ROOT=a.b.c```. This is the web address (aka DOMAIN NAME) of the Discourse
       site.

   -   ```export DISCOURSE_SESS=?????????????????????????????```. This is a session key that will
       be used to set a cookie (called _t). The cookie needs to come from an active web session
       that is logged in to the Discourse site.

