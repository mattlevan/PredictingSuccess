
# coding: utf-8

# # Crunchbase Snapshot © 2013 Data Analysis Notebook

# In[1]:

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import pandas
from pandas import DataFrame as df
import numpy as np
# import sklearn as sk
import plotly as py
from plotly.graph_objs import *
import igraph as ig

# CSS files for more aesthetically pleasing inline tables.
from IPython.core.display import HTML
css = open('css/style-table.css').read() + open('css/style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# ## Import Crunchbase 2013 Snapshot CSV files.

# In[2]:

cb_acquisitions = df.from_csv('csv/cb_acquisitions.csv').reset_index('id')
cb_funding_rounds = df.from_csv('csv/cb_funding_rounds.csv').reset_index('id')
cb_funds = df.from_csv('csv/cb_funds.csv').reset_index('id')
cb_investments = df.from_csv('csv/cb_investments.csv').reset_index('id')
cb_ipos = df.from_csv('csv/cb_ipos.csv').reset_index('id')
cb_milestones = df.from_csv('csv/cb_milestones.csv').reset_index('id')
cb_objects = df.from_csv('csv/cb_objects.csv').reset_index('id')
cb_offices = df.from_csv('csv/cb_offices.csv').reset_index('id')
cb_people = df.from_csv('csv/cb_people.csv').reset_index('id')
cb_relationships = df.from_csv('csv/cb_relationships.csv').reset_index('id')


# ## Visualize data frames.

# In[3]:

cb_acquisitions.iloc[70:73]
# cb_funding_rounds.head(1)
# cb_funds.head(1)
# cb_investments.head(1)
# cb_ipos.head(1)
# cb_milestones.head(1)
# cb_objects.head(1)
# cb_offices.head(1)
# cb_people.head(1)
# cb_relationships.head(1)


# ## Build igraph networks.

# #### Acquisitions

# In[4]:

# Declare an empty graph for acquisitions.
acquisitions = ig.Graph(directed = True)

# Remove rows that report companies who've acquired themselves...
cb_acquisitions = cb_acquisitions[(cb_acquisitions['acquiring_object_id'] != cb_acquisitions['acquired_object_id'])].reset_index(drop = True)

# Calculate the number of unique acquirers and acquirees
unique_acquirers = cb_acquisitions['acquiring_object_id'].unique()
unique_acquirees = cb_acquisitions['acquired_object_id'].unique()
# Append both acquirers and acquirees into one np.array and remove duplicates.
unique_nodes = np.unique(np.append(unique_acquirers, unique_acquirees))

# Add appropriate number of vertices to the acquisitions graph.
acquisitions.add_vertices(len(unique_nodes))

# Declare and initialize vertex attributes with company ids.
acquisitions.vs['id'] = unique_nodes

# Initialize edges.
for i in range(0, len(cb_acquisitions)):
    # Get (already existing) node integer indices.
    acquired = acquisitions.vs.find(id = cb_acquisitions.get_value(i, 'acquired_object_id')).index
    acquiring = acquisitions.vs.find(id = cb_acquisitions.get_value(i, 'acquiring_object_id')).index
    
    # Get edge attributes.
    price_amount = cb_acquisitions.get_value(i, 'price_amount')
    price_currency_code = cb_acquisitions.get_value(i, 'price_currency_code')
    acquired_at = cb_acquisitions.get_value(i, 'acquired_at')
    source_url = cb_acquisitions.get_value(i, 'source_url')
    source_description = cb_acquisitions.get_value(i, 'source_description')
    
    # Draw edge between both nodes; direction: acquiring <- acquired.
    acquisitions.add_edge(acquired, acquiring, price_amount = price_amount, 
                                               price_currency_code = price_currency_code, 
                                               acquired_at = acquired_at, 
                                               source_url = source_url, 
                                               source_description = source_description)


# In[ ]:

layout = acquisitions.layout('kk')
ig.plot(acquisitions, layout = layout)


# In[ ]:




# In[ ]:




# ## Visualize networks with plotly.

# In[7]:

# Relationships


# In[11]:

# Average number of relationships per company.
avg_relationships = np.average(cb_objects[(cb_objects.relationships.notnull())].relationships)
"Average relationships: {:,.2}".format(avg_relationships)


# In[121]:

# Visualize number of relationships in companies, only those with 5x average.
x = cb_objects[(cb_objects.relationships > avg_relationships * 5)]
x = x.sort_values(by = 'relationships', ascending = True)
x = x.plot(x = 'name', y = 'relationships', kind = 'barh', title = 'Relationships')

# Save as an image.
# plt.savefig('plots/avg_relationships.png', format='png', bbox_inches='tight', dpi=1000)


# In[ ]:

### FUNDS


# In[138]:

# Average funds per company.
avg_funding = np.average(cb_objects[(cb_objects.funding_total_usd.notnull())].funding_total_usd)
avg_funding
"Average funding: {:,}".format(avg_funding)


# In[150]:

# Visualize funds per company, only showing companies with at least 3x average.
x = cb_objects[(cb_objects.funding_total_usd > avg_funding * 3)]
x = x.sort_values(by = 'funding_total_usd', ascending = True)
x = x.plot(x = 'name', y = 'funding_total_usd', kind = 'barh', title = 'Funds')


# In[146]:




# In[ ]:




# In[ ]:




# In[ ]:



