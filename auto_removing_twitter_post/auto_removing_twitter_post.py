
# coding: utf-8

# In[ ]:


import twitter
import pandas as pd


# In[ ]:


df = pd.read_csv('keys.csv', index_col=0)


# In[ ]:


CONSUMER_KEY = df.loc['CONSUMER_KEY', 'value']
CONSUMER_SECRET = df.loc['CONSUMER_SECRET', 'value']
ACCESS_TOKEN = df.loc['ACCESS_TOKEN', 'value']
ACCESS_SECRET = df.loc['ACCESS_SECRET', 'value']


# In[ ]:


api = twitter.Api(consumer_key=CONSUMER_KEY,
                         consumer_secret=CONSUMER_SECRET,
                         access_token_key=ACCESS_TOKEN,
                         access_token_secret=ACCESS_SECRET)


# In[ ]:


my_id = api.VerifyCredentials().id


# In[ ]:


statuses = api.GetUserTimeline(user_id=my_id,
                                                count=200,
                                                include_rts=False,
                                                exclude_replies=True)

for s in statuses:
     if '52.193.110.195' in s.text:
        print(s.text + ' '+ str(s.id))
        api.DestroyStatus(s.id)

max_id = statuses[len(statuses)-1].id


# In[ ]:


for i in range(5):
    statuses = api.GetUserTimeline(user_id=my_id,
                                                    max_id=max_id,
                                                    count=200,
                                                    include_rts=False,
                                                    exclude_replies=True)
    
    for s in statuses:
        if '過去記事定期' in s.text:
            print(s.text + ' '+ str(s.id) + ' ')
            api.DestroyStatus(s.id)

    next_max_id = statuses[len(statuses)-1].id
    if max_id == next_max_id:
        max_id = next_max_id
    else:
        break

