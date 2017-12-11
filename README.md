# pandassssssss




```python
import pandas as pd
import numpy as np
```


```python
# read first dataset
pymoli_1= 'Resources/purchase_data.json'
pymoli_1 =pd.read_json(pymoli_1)
pymoli_1.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# read second dataset
pymoli_2='Resources/purchase_data2.json'
pymoli_2=pd.read_json(pymoli_2)
pymoli_2.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>Male</td>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>Iloni35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>12</td>
      <td>Dawne</td>
      <td>3.36</td>
      <td>Aidaira26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>Male</td>
      <td>5</td>
      <td>Putrid Fan</td>
      <td>2.63</td>
      <td>Irim47</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>Male</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>2.55</td>
      <td>Irith83</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>Philodil43</td>
    </tr>
  </tbody>
</table>
</div>




```python
# combine two dataset
pymoli = pd.concat([pymoli_1, pymoli_2])
pymoli.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Player Count
total_player =len(pymoli['SN'].unique())
total_player_df = pd.DataFrame({'Total Players': total_player}, index=[0])
total_player_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>612</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis(Total)
unique_item = len(pymoli['Item Name'].unique())
average_price = pymoli['Price'].mean()
average_price="${:.2f}".format(average_price)
num_purchase = pymoli.shape[0]
total_revenue = pymoli['Price'].sum()
total_revenue = "${:.2f}".format(total_revenue)
purchasing_analysis_df=pd.DataFrame({'Number of Unique Items':unique_item,'Average Price':average_price,'Numer of Purchase':num_purchase, 'Total Revenue':total_revenue},index=[0])
purchasing_analysis_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Number of Unique Items</th>
      <th>Numer of Purchase</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.93</td>
      <td>180</td>
      <td>858</td>
      <td>$2514.43</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a cleaned dataframe with unique players
u_player = pymoli['SN'].unique()
u_gender = [list(pymoli['Gender'].loc[pymoli['SN'] == str(i)]) for i in u_player]
u_gender = [item[0] for item in u_gender]
u_pymoli_df = pd.DataFrame({'Player':u_player, 'Gender':u_gender})
u_pymoli_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Player</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Male</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Male</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Male</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Male</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Gender Demographics
male = len(u_pymoli_df.loc[u_pymoli_df['Gender'] == 'Male'])
female = len(u_pymoli_df.loc[u_pymoli_df['Gender'] == 'Female'])
other = len(u_pymoli_df.loc[u_pymoli_df['Gender'] ==  'Other / Non-Disclosed'])
m_percent = "{:.2f}%".format(male/total_player*100)
f_percent = "{:.2f}%".format(female/total_player*100)
other_percent = '{:.2f}%'.format(other/total_player*100)
gender_df = pd.DataFrame({'Percentage of Player':[m_percent, f_percent, other_percent], 'Total Count':[male, female, other]},index = ['Male','Female','Other / Non-Disclosed'])
gender_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Player</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>80.88%</td>
      <td>495</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.65%</td>
      <td>108</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.47%</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis(Gender)
```


```python
#purchase count
male_purchase = len(pymoli.loc[pymoli['Gender']=='Male'])
female_purchase = len(pymoli.loc[pymoli['Gender']=='Female'])
other_purchase = len(pymoli.loc[pymoli['Gender']=='Other / Non-Disclosed'])
total_purchase = male_purchase+female_purchase+other_purchase
```


```python
#groupby gender - avg price
avg_price_gender = pymoli.groupby('Gender').mean()
```


```python
#male and female avg price
m_avg_price = avg_price_gender['Price']['Male']
f_avg_price = avg_price_gender['Price']['Female']
other_avg_price = avg_price_gender['Price']['Other / Non-Disclosed']
total_avg_price = m_avg_price+f_avg_price+other_avg_price
```


```python
#total value
total_value_gender = pymoli.groupby('Gender').sum()
m_total_value = total_value_gender['Price']['Male']
f_total_value = total_value_gender['Price']['Female']
other_total_value = total_value_gender['Price']['Other / Non-Disclosed']
total_value = m_total_value+f_total_value+other_total_value
```


```python
#normalized total
m_normalized = total_value/male_purchase
f_normalized = total_value/female_purchase
other_normalized = total_value/other_purchase
```


```python
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
```


```python
gender_purchasing_df = pd.DataFrame({'Purchase Count':[male_purchase, female_purchase, other_purchase], 'Average Purchase Price':[m_avg_price,f_avg_price,other_avg_price ], 'Total Purchase Value':[m_total_value,f_total_value,other_total_value],'Normalized Totals':[m_normalized,f_normalized,other_normalized]}, index = ['Male','Female','Other / Non-Disclosed'])
gender_purchasing_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>$2.94</td>
      <td>$3.61</td>
      <td>697</td>
      <td>$2052.28</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>$2.85</td>
      <td>$16.88</td>
      <td>149</td>
      <td>$424.29</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$3.15</td>
      <td>$209.54</td>
      <td>$12.00</td>
      <td>$37.86</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Age Demographics
min_age = pymoli['Age'].min()
max_age = pymoli['Age'].max()
min_age
```




    7




```python
max_age
```




    45




```python
bins = np.linspace(6,46,10,dtype = int)
bins
```




    array([ 6, 10, 14, 19, 23, 28, 32, 37, 41, 46])




```python
labels = ['<=10','11-14','15-19','20-23','24-28','29-32','33-37','38-41','42+']
```


```python
pymoli['Age Range'] = pd.cut(pymoli['Age'], bins=bins, labels=labels)
pymoli.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>38-41</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20-23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>33-37</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20-23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20-23</td>
    </tr>
  </tbody>
</table>
</div>




```python
age_grouped_df = pymoli.groupby('Age Range')
age_grouped_df.max()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
    <tr>
      <th>Age Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;=10</th>
      <td>10</td>
      <td>Male</td>
      <td>177</td>
      <td>Woeful Adamantite Claymore</td>
      <td>4.89</td>
      <td>Yarithsurgue62</td>
    </tr>
    <tr>
      <th>11-14</th>
      <td>14</td>
      <td>Other / Non-Disclosed</td>
      <td>183</td>
      <td>Woeful Adamantite Claymore</td>
      <td>4.75</td>
      <td>Undistasta86</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>19</td>
      <td>Male</td>
      <td>183</td>
      <td>Worldbreaker</td>
      <td>4.95</td>
      <td>Zhisrisu83</td>
    </tr>
    <tr>
      <th>20-23</th>
      <td>23</td>
      <td>Other / Non-Disclosed</td>
      <td>183</td>
      <td>Yearning Mageblade</td>
      <td>4.95</td>
      <td>Zontibe81</td>
    </tr>
    <tr>
      <th>24-28</th>
      <td>28</td>
      <td>Other / Non-Disclosed</td>
      <td>182</td>
      <td>Yearning Mageblade</td>
      <td>4.95</td>
      <td>Zhisrisu83</td>
    </tr>
    <tr>
      <th>29-32</th>
      <td>32</td>
      <td>Other / Non-Disclosed</td>
      <td>182</td>
      <td>Yearning Mageblade</td>
      <td>4.95</td>
      <td>Yathecal72</td>
    </tr>
    <tr>
      <th>33-37</th>
      <td>37</td>
      <td>Other / Non-Disclosed</td>
      <td>183</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>4.83</td>
      <td>Wailin72</td>
    </tr>
    <tr>
      <th>38-41</th>
      <td>40</td>
      <td>Male</td>
      <td>181</td>
      <td>Woeful Adamantite Claymore</td>
      <td>4.65</td>
      <td>Yasrisu92</td>
    </tr>
    <tr>
      <th>42+</th>
      <td>45</td>
      <td>Male</td>
      <td>124</td>
      <td>Venom Claymore</td>
      <td>3.81</td>
      <td>Raesurdil91</td>
    </tr>
  </tbody>
</table>
</div>




```python
age_purchasing = age_grouped_df ['Price'].count()
age_purchasing
```




    Age Range
    <=10      37
    11-14     34
    15-19    144
    20-23    295
    24-28    190
    29-32     70
    33-37     54
    38-41     31
    42+        3
    Name: Price, dtype: int64




```python
avg_price_age = age_grouped_df ['Price'].mean()
total_value_age = age_grouped_df ['Price'].sum()
total_value_age
```




    Age Range
    <=10     110.44
    11-14     92.75
    15-19    416.83
    20-23    858.33
    24-28    564.81
    29-32    210.06
    33-37    154.87
    38-41     97.70
    42+        8.64
    Name: Price, dtype: float64




```python
normalized_totals_age = total_value_age/age_purchasing
```


```python
avg_price_age = avg_price_age.map('${:.2f}'.format)
total_value_age = total_value_age.map('${:.2f}'.format)
normalized_totals_age = normalized_totals_age.map('${:.2f}'.format)
```


```python
age_purchasing_df = pd.DataFrame()
age_purchasing_df['Purchase Count'] = age_purchasing
age_purchasing_df['Average Purchase Price'] = avg_price_age
age_purchasing_df['Total Purchase Value'] = total_value_age
age_purchasing_df['Normalized Totals'] = normalized_totals_age
age_purchasing_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;=10</th>
      <td>37</td>
      <td>$2.98</td>
      <td>$110.44</td>
      <td>$2.98</td>
    </tr>
    <tr>
      <th>11-14</th>
      <td>34</td>
      <td>$2.73</td>
      <td>$92.75</td>
      <td>$2.73</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>144</td>
      <td>$2.89</td>
      <td>$416.83</td>
      <td>$2.89</td>
    </tr>
    <tr>
      <th>20-23</th>
      <td>295</td>
      <td>$2.91</td>
      <td>$858.33</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>24-28</th>
      <td>190</td>
      <td>$2.97</td>
      <td>$564.81</td>
      <td>$2.97</td>
    </tr>
    <tr>
      <th>29-32</th>
      <td>70</td>
      <td>$3.00</td>
      <td>$210.06</td>
      <td>$3.00</td>
    </tr>
    <tr>
      <th>33-37</th>
      <td>54</td>
      <td>$2.87</td>
      <td>$154.87</td>
      <td>$2.87</td>
    </tr>
    <tr>
      <th>38-41</th>
      <td>31</td>
      <td>$3.15</td>
      <td>$97.70</td>
      <td>$3.15</td>
    </tr>
    <tr>
      <th>42+</th>
      <td>3</td>
      <td>$2.88</td>
      <td>$8.64</td>
      <td>$2.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Spenders
top_total_value = pymoli['Price'].groupby(pymoli['SN']).sum().nlargest(5)
top_purchase_count = pymoli['Price'].groupby(pymoli['SN']).count()
top_avg = pymoli['Price'].groupby(pymoli['SN']).mean()
top_total_value = top_total_value.map('${:.2f}'.format)
top_total_value
```




    SN
    Undirrala66      $17.06
    Aerithllora36    $15.10
    Saedue76         $13.56
    Sondim43         $13.02
    Mindimnya67      $12.74
    Name: Price, dtype: object




```python
top_spenders_df = pd.DataFrame()
top_spenders_df['Total Purchase Value'] = top_total_value
top_spenders_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Aerithllora36</th>
      <td>$15.10</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Sondim43</th>
      <td>$13.02</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>$12.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_index = list(top_spenders_df.index)
top_index
```




    ['Undirrala66', 'Aerithllora36', 'Saedue76', 'Sondim43', 'Mindimnya67']




```python
top_s_purchase_count = [top_purchase_count[element] for element in top_index]
top_s_avg = [top_avg[element] for element in top_index]
```


```python
top_spenders_df = pd.DataFrame()
top_spenders_df['Total Purchase Value'] = top_total_value
top_spenders_df['Purchase Count'] = top_s_purchase_count
top_spenders_df['Average Purchase Price'] = top_s_avg
top_spenders_df['Average Purchase Price'] = top_spenders_df['Average Purchase Price'].map('${:.2f}'.format)
top_spenders_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>$17.06</td>
      <td>5</td>
      <td>$3.41</td>
    </tr>
    <tr>
      <th>Aerithllora36</th>
      <td>$15.10</td>
      <td>4</td>
      <td>$3.77</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>$13.56</td>
      <td>4</td>
      <td>$3.39</td>
    </tr>
    <tr>
      <th>Sondim43</th>
      <td>$13.02</td>
      <td>4</td>
      <td>$3.25</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>$12.74</td>
      <td>4</td>
      <td>$3.18</td>
    </tr>
  </tbody>
</table>
</div>




```python
popular_grouped = pymoli.groupby(['Item ID','Item Name']).count().sort_values(['Price'], ascending=False)
p_purchase_value  = pymoli.groupby(['Item ID','Item Name']).sum()
p_avg = pymoli.groupby(['Item ID','Item Name']).mean()
p_count = pymoli.groupby(['Item ID','Item Name']).count()
```


```python
p_index = list(popular_grouped.index)
```


```python
p_total = [p_purchase_value['Price'][element] for element in pop_index]
p_avg_price = [p_avg['Price'][element] for element in pop_index]
p_purchase_count = [p_count['Price'][element] for element in pop_index]
```


```python
popular_grouped['Purchase Count'] = p_purchase_count
popular_grouped['Item Price'] = p_avg_price
popular_grouped['Total Purchase Value'] = p_total
popular_grouped = popular_grouped [['Purchase Count','Item Price','Total Purchase Value']]
popular_grouped['Item Price'] = popular_grouped['Item Price'].map('${:.2f}'.format)
popular_grouped['Total Purchase Value'] = popular_grouped['Total Purchase Value'].map('${:.2f}'.format)
popular_grouped.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>12</td>
      <td>$2.45</td>
      <td>$29.34</td>
    </tr>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>10</td>
      <td>$2.32</td>
      <td>$23.22</td>
    </tr>
    <tr>
      <th>44</th>
      <th>Bonecarvin Battle Axe</th>
      <td>9</td>
      <td>$2.67</td>
      <td>$24.04</td>
    </tr>
    <tr>
      <th>154</th>
      <th>Feral Katana</th>
      <td>9</td>
      <td>$2.62</td>
      <td>$23.55</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Profitable Item
profitable_grouped = pymoli.groupby(['Item ID','Item Name']).sum().sort_values(['Price'], ascending=False)
profitable_ct  = pymoli.groupby(['Item ID','Item Name']).count()
profitable_avg = pymoli.groupby(['Item ID','Item Name']).mean()
profitable_total = pymoli.groupby(['Item ID','Item Name']).sum()
profitable_grouped.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Age</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>234</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>222</td>
      <td>33.03</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>154</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>140</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>268</td>
      <td>29.34</td>
    </tr>
  </tbody>
</table>
</div>




```python
profitable_index = list(profitable_grouped.index)
```


```python
pro_total = [profitable_total['Price'][element] for element in profitable_index]
pro_avg = [profitable_avg['Price'][element] for element in profitable_index]
pro_purchase_count = [profitable_ct['Price'][element] for element in profitable_index]
```


```python
profitable_grouped['Purchase Count'] = pro_purchase_count
profitable_grouped['Item Price'] = pro_avg
profitable_grouped['Total Purchase Value'] = pro_total
profitable_grouped = profitable_grouped[['Purchase Count','Item Price','Total Purchase Value']]
profitable_grouped['Item Price'] = profitable_grouped['Item Price'].map('${:.2f}'.format)
profitable_grouped['Total Purchase Value'] = profitable_grouped['Total Purchase Value'].map('${:.2f}'.format)
profitable_grouped.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>9</td>
      <td>$3.67</td>
      <td>$33.03</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>12</td>
      <td>$2.45</td>
      <td>$29.34</td>
    </tr>
  </tbody>
</table>
</div>


