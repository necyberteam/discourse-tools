Chris scripts to use Discourse API ( https://docs.discourse.org/ )

  - get_user_email.py
    Python 3 script to get user names and emails from the Discourse site.
    Needs an API key ( see - /admin/api/keys at Discourse site ).
    Some sites also need valid web based login _t cookie.
    Both these are passed from environment variables set external
    to script. These are privileged access keys so don't store them in github by mistake! 
    The API key can be revoked online, the _t cookie can be revoked by logging out of
    the web session.
