# In[524]:


import pandas as pd
import numpy as np


# In[525]:


# read first dataset
pymoli_1= 'Resources/purchase_data.json'
pymoli_1 =pd.read_json(pymoli_1)
pymoli_1


# In[526]:


# read second dataset
pymoli_2='Resources/purchase_data2.json'
pymoli_2=pd.read_json(pymoli_2)
pymoli_2


# In[527]:


# combine two dataset
pymoli = pd.concat([pymoli_1, pymoli_2])
pymoli


# In[539]:


#Player Count
total_player =len(pymoli['SN'].unique())
total_player_df = pd.DataFrame({'Total Players': total_player}, index=[0])
total_player_df


# In[540]:


#Purchasing Analysis(Total)
unique_item = len(pymoli['Item Name'].unique())
average_price = pymoli['Price'].mean()
average_price="${:.2f}".format(average_price)
num_purchase = pymoli.shape[0]
total_revenue = pymoli['Price'].sum()
total_revenue = "${:.2f}".format(total_revenue)
purchasing_analysis_df=pd.DataFrame({'Number of Unique Items':unique_item,'Average Price':average_price,'Numer of Purchase':num_purchase, 'Total Revenue':total_revenue},index=[0])
purchasing_analysis_df


# In[541]:


#Create a cleaned dataframe with unique players
u_player = pymoli['SN'].unique()
u_gender = [list(pymoli['Gender'].loc[pymoli['SN'] == str(i)]) for i in u_player]
u_gender = [item[0] for item in u_gender]
u_pymoli_df = pd.DataFrame({'Player':u_player, 'Gender':u_gender})
u_pymoli_df


# In[542]:


#Gender Demographics
male = len(u_pymoli_df.loc[u_pymoli_df['Gender'] == 'Male'])
female = len(u_pymoli_df.loc[u_pymoli_df['Gender'] == 'Female'])
other = len(u_pymoli_df.loc[u_pymoli_df['Gender'] ==  'Other / Non-Disclosed'])
m_percent = "{:.2f}%".format(male/total_player*100)
f_percent = "{:.2f}%".format(female/total_player*100)
other_percent = '{:.2f}%'.format(other/total_player*100)
gender_df = pd.DataFrame({'Percentage of Player':[m_percent, f_percent, other_percent], 'Total Count':[male, female, other]},index = ['Male','Female','Other / Non-Disclosed'])
gender_df


# In[543]:


#Purchasing Analysis(Gender)


# In[544]:


#purchase count
male_purchase = len(pymoli.loc[pymoli['Gender']=='Male'])
female_purchase = len(pymoli.loc[pymoli['Gender']=='Female'])
other_purchase = len(pymoli.loc[pymoli['Gender']=='Other / Non-Disclosed'])
total_purchase = male_purchase+female_purchase+other_purchase


# In[545]:


#groupby gender - avg price
avg_price_gender = pymoli.groupby('Gender').mean()


# In[546]:


#male and female avg price
m_avg_price = avg_price_gender['Price']['Male']
f_avg_price = avg_price_gender['Price']['Female']
other_avg_price = avg_price_gender['Price']['Other / Non-Disclosed']
total_avg_price = m_avg_price+f_avg_price+other_avg_price


# In[547]:


#total value
total_value_gender = pymoli.groupby('Gender').sum()
m_total_value = total_value_gender['Price']['Male']
f_total_value = total_value_gender['Price']['Female']
other_total_value = total_value_gender['Price']['Other / Non-Disclosed']
total_value = m_total_value+f_total_value+other_total_value


# In[548]:


#normalized total
m_normalized = total_value/male_purchase
f_normalized = total_value/female_purchase
other_normalized = total_value/other_purchase


# In[549]:


other_purchase = "${:.2f}".format(other_purchase)
m_avg_price = "${:.2f}".format(m_avg_price)
f_avg_price = "${:.2f}".format(f_avg_price)
other_avg_price = "${:.2f}".format(other_avg_price)
m_total_value = "${:.2f}".format(m_total_value)
f_total_value = "${:.2f}".format(f_total_value)
other_total_value = "${:.2f}".format(other_total_value)
m_normalized = "${:.2f}".format(m_normalized)
f_normalized = "${:.2f}".format(f_normalized)
other_normalized = "${:.2f}".format(other_normalized)


# In[550]:


gender_purchasing_df = pd.DataFrame({'Purchase Count':[male_purchase, female_purchase, other_purchase], 'Average Purchase Price':[m_avg_price,f_avg_price,other_avg_price ], 'Total Purchase Value':[m_total_value,f_total_value,other_total_value],'Normalized Totals':[m_normalized,f_normalized,other_normalized]}, index = ['Male','Female','Other / Non-Disclosed'])
gender_purchasing_df


# In[551]:


#Age Demographics
min_age = pymoli['Age'].min()
max_age = pymoli['Age'].max()
min_age


# In[552]:


max_age


# In[553]:


bins = np.linspace(6,46,10,dtype = int)
bins


# In[554]:


labels = ['<=10','11-14','15-19','20-23','24-28','29-32','33-37','38-41','42+']


# In[555]:


pymoli['Age Range'] = pd.cut(pymoli['Age'], bins=bins, labels=labels)
pymoli


# In[556]:


age_grouped_df = pymoli.groupby('Age Range')
age_grouped_df.max()


# In[557]:


age_purchasing = age_grouped_df ['Price'].count()
age_purchasing


# In[558]:


avg_price_age = age_grouped_df ['Price'].mean()
total_value_age = age_grouped_df ['Price'].sum()
total_value_age


# In[559]:


normalized_totals_age = total_value_age/age_purchasing


# In[560]:


avg_price_age = avg_price_age.map('${:.2f}'.format)
total_value_age = total_value_age.map('${:.2f}'.format)
normalized_totals_age = normalized_totals_age.map('${:.2f}'.format)


# In[561]:


age_purchasing_df = pd.DataFrame()
age_purchasing_df['Purchase Count'] = age_purchasing
age_purchasing_df['Average Purchase Price'] = avg_price_age
age_purchasing_df['Total Purchase Value'] = total_value_age
age_purchasing_df['Normalized Totals'] = normalized_totals_age
age_purchasing_df


# In[562]:


#Top Spenders
top_total_value = pymoli['Price'].groupby(pymoli['SN']).sum().nlargest(5)
top_purchase_count = pymoli['Price'].groupby(pymoli['SN']).count()
top_avg = pymoli['Price'].groupby(pymoli['SN']).mean()
top_total_value = top_total_value.map('${:.2f}'.format)
top_total_value


# In[563]:


top_spenders_df = pd.DataFrame()
top_spenders_df['Total Purchase Value'] = top_total_value
top_spenders_df


# In[564]:


top_index = list(top_spenders_df.index)
top_index


# In[565]:


top_s_purchase_count = [top_purchase_count[element] for element in top_index]
top_s_avg = [top_avg[element] for element in top_index]


# In[566]:


top_spenders_df = pd.DataFrame()
top_spenders_df['Total Purchase Value'] = top_total_value
top_spenders_df['Purchase Count'] = top_s_purchase_count
top_spenders_df['Average Purchase Price'] = top_s_avg
top_spenders_df['Average Purchase Price'] = top_spenders_df['Average Purchase Price'].map('${:.2f}'.format)
top_spenders_df


# In[617]:


popular_grouped = pymoli.groupby(['Item ID','Item Name']).count().sort_values(['Price'], ascending=False)
p_purchase_value  = pymoli.groupby(['Item ID','Item Name']).sum()
p_avg = pymoli.groupby(['Item ID','Item Name']).mean()
p_count = pymoli.groupby(['Item ID','Item Name']).count()


# In[618]:


p_index = list(popular_grouped.index)
p_index


# In[619]:


p_total = [p_purchase_value['Price'][element] for element in pop_index]
p_avg_price = [p_avg['Price'][element] for element in pop_index]
p_purchase_count = [p_count['Price'][element] for element in pop_index]


# In[620]:


popular_grouped['Purchase Count'] = p_purchase_count
popular_grouped['Item Price'] = p_avg_price
popular_grouped['Total Purchase Value'] = p_total
popular_grouped = popular_grouped [['Purchase Count','Item Price','Total Purchase Value']]
popular_grouped['Item Price'] = popular_grouped['Item Price'].map('${:.2f}'.format)
popular_grouped['Total Purchase Value'] = popular_grouped['Total Purchase Value'].map('${:.2f}'.format)
popular_grouped.head()


# In[621]:


#Most Profitable Item
profitable_grouped = pymoli.groupby(['Item ID','Item Name']).sum().sort_values(['Price'], ascending=False)
profitable_ct  = pymoli.groupby(['Item ID','Item Name']).count()
profitable_avg = pymoli.groupby(['Item ID','Item Name']).mean()
profitable_total = pymoli.groupby(['Item ID','Item Name']).sum()
profitable_grouped


# In[622]:


profitable_index = list(profitable_grouped.index)
profitable_index


# In[623]:


pro_total = [profitable_total['Price'][element] for element in profitable_index]
pro_avg = [profitable_avg['Price'][element] for element in profitable_index]
pro_purchase_count = [profitable_ct['Price'][element] for element in profitable_index]


# In[628]:


profitable_grouped['Purchase Count'] = pro_purchase_count
profitable_grouped['Item Price'] = pro_avg
profitable_grouped['Total Purchase Value'] = pro_total
profitable_grouped = profitable_grouped[['Purchase Count','Item Price','Total Purchase Value']]
profitable_grouped['Item Price'] = profitable_grouped['Item Price'].map('${:.2f}'.format)
profitable_grouped['Total Purchase Value'] = profitable_grouped['Total Purchase Value'].map('${:.2f}'.format)
profitable_grouped.head()
