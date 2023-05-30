#!/usr/bin/env python
# coding: utf-8

# In[18]:


pip install bokeh


# In[19]:


import pandas as pd
from bokeh.io import output_notebook, show
from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import Select
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers


# In[20]:


df = flowers.copy()
species = iris_df['species'].unique().tolist()


# In[21]:


df.head()


# In[22]:


scatter = figure(title="Iris Dataset", plot_width=500, plot_height=400)
histogram = figure(title="Histogram", plot_width=500, plot_height=400)


# In[23]:


def update_plots(attrname, old, new):
    selected_species = species_select.value

    filtered = df[df['species'] == selected_species]

    scatter.circle(x=filtered['petal_length'],
                        y=filtered['petal_width'],
                        color=Spectral6[0],
                        legend_label=selected_species)

    
    histogram.quad(top=filtered['sepal_length'].value_counts().sort_index().tolist(),
                        bottom=0,
                        left=filtered['sepal_length'].value_counts().sort_index().index.tolist(),
                        right=filtered['sepal_length'].value_counts().sort_index().index.tolist(),
                        fill_color=Spectral6[0],
                        line_color='black')


# In[24]:


species_select = Select(title="Select Species", options=species_list, value=species_list[0])
species_select.on_change('value', update_plots)


# In[25]:


update_plots('value', None, species_list[0])


# In[26]:


output_notebook()


# In[27]:


layout = column(species_select, row(scatter, histogram))


# In[28]:


show(layout)


# In[ ]:




