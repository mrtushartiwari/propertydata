
# coding: utf-8

# In[1]:


import time
start = time.clock()
import pandas as pd
from sklearn.externals import joblib


# In[2]:


house_model_DT = joblib.load('DTmodel.pkl')


# In[3]:


house_model_RF = joblib.load('RFmodel.pkl')


# In[4]:


X = pd.read_pickle('X_for_final')


# ## Query based use case

# In[5]:



numeric_col = ['area','bathroom','balconies','Lift Available','Car Parking','Power Backup','24 X 7 Security',
          'Children\'s play area','Vaastu Compliant','Club House','Gymnasium','Swimming Pool','Sports Facility',
          'Indoor Games','Jogging Track','Maintenance Staff','Intercom','Golf Course','Cafeteria','Rain Water Harvesting',
          'Staff Quarter','Multipurpose Room','Landscaped Gardens','Shopping Mall','School','Hospital','ATM','AC',
           'Wardrobe','TV','Refrigerator','Sofa','Washing Machine','Wifi','Microwave','Dining Table','Gas connection',
           'BED','pricepersquare','roadfaceing','opensides','totalfloor',]

X = X.drop('price',axis = 1)


# In[6]:


#querydf = [area ,bhk, carpetarea, pricepersquare,
#           Vaastu_Compliant,locality, neworold,facing, floor,additionalrooms,possesiondate,status]
Lift_Available=Car_Parking=Power_Backup= Security=Childrens_play_area=None
Vaastu_Compliant=Club_House=Gymnasium=Swimming_Pool=Sports_Facility=None
Indoor_Games=Jogging_Track=Maintenance_Staff=Intercom=Golf_Course=None
Cafeteria=Rain_Water_Harvesting=Staff_Quarter=Multipurpose_Room=None
Landscaped_Gardens=Shopping_Mall=School=Hospital=ATM=AC=Wardrobe=None
TV=Refrigerator=Sofa=Washing_Machine=Wifi=Microwave=Dining_Table=None
Gas_connection=BED=pricepersquare=roadfaceing=opensides=totalfloor = None


# In[7]:


import json

with open('data2.json') as json_data:
    data2json = json.load(json_data)
    print(data2json["area1"])


area = int(data2json["area1"])
bhk = data2json["bhk1"]
carpetarea = int(data2json["carpetarea1"])
pricepersquare = int(data2json["pricepersquare1"])
Vaastu_Compliant = data2json["Vaastu_Compliant1"]
locality = data2json["locality1"]
neworold = data2json["neworold1"]
facing = data2json["facing1"]
floor = int(data2json["floor1"])
additionalrooms = data2json["additionalrooms1"]
possesiondate = data2json["possesiondate1"]
status = data2json["status1"]
print(type(carpetarea))    # integer becoming str in json convert them


# In[8]:


with open('data3.json') as json_data:
    data3json = json.load(json_data)
    print(data3json["overlooking1"])
bathroom = int(data3json["bathroom1"])
balconies = int(data3json["balconies1"])
opensides = int(data3json["opensides1"])
overlooking = (data3json["overlooking1"])
ownership = data3json["ownership1"]
roadfaceing = data3json["roadfaceing1"]
age = data3json["age1"]
totalfloor = int(data3json["totalfloor1"])


# In[9]:


import re
roadfaceing = data3json["roadfaceing1"]
roadfaceing = re.sub(' feet','',roadfaceing)
roadfaceing


# In[10]:


with open('data4.json') as json_data:
    data4json = json.load(json_data)
    print(data4json["Security1"])
Lift_Available = data4json["Lift_Available1"]
Car_Parking = data4json["Car_Parking1"]
Power_Backup = data4json["Power_Backup1"]
Security = data4json["Security1"]
Childrens_play_area1 = data4json["Childrens_play_area1"]
Club_House = data4json["Club_House1"]
Gymnasium = data4json["Gymnasium1"]
Swimming_Pool = data4json["Swimming_Pool1"]
Sports_Facility = data4json["Sports_Facility1"]
Indoor_Games = data4json["Indoor_Games1"]
Jogging_Track = data4json["Jogging_Track1"]
Maintenance_Staff = data4json["Maintenance_Staff1"]
Intercom = data4json["Intercom1"]
Golf_Course = data4json["Golf_Course1"]
Cafeteria = data4json["Cafeteria1"]
Rain_Water_Harvesting = data4json["Rain_Water_Harvesting1"]
Staff_Quarter = data4json["Staff_Quarter1"]
Multipurpose_Room = data4json["Multipurpose_Room1"]
Landscaped_Gardens = data4json["Landscaped_Gardens1"]
Shopping_Mall = data4json["Shopping_Mall1"]
Washing_Machine = data4json["Washing_Machine1"]
Wardrobe = data4json["Wardrobe1"]
Gas_connection = data4json["Gas_connection1"]
Refrigerator = data4json["Refrigerator1"]
Sofa1 = data4json["Sofa1"]
AC = data4json["AC1"]
TV = data4json["TV1"]
wifi = data4json["wifi1"]
Microwave = data4json["Microwave1"]
Dining_Table = data4json["Dining_Table1"]
BED = data4json["BED1"]
Shopping_Mall = data4json["Shopping_Mall1"]
School = data4json["School1"]
Hospital = data4json["Hospital1"]
ATM = data4json["ATM1"]


# In[11]:


# caught u tushar  
# always make a key  a string  in dictonary
query = [{'area' : 2500
,'bhk' : '3 BHK Apartment'
,'carpetarea' : 1000
,'pricepersquare' : 8500
,'Vaastu_Compliant' : 1
,'locality' : 'Lulla Nagar'
,'neworold' : 'New'
,'facing' : 'NorthEast'
,'floor' : 2
,'additionalrooms' : '1 rooms( study room )'
,'possesiondate' : 'Dec 2018'
,'Lift_Available': 'Yes'
,'status' : 'Under Construction,Unfurnished'}]


# In[12]:


print(area)


# In[13]:


# This is for features encoded using one hot encoding
# bhk,age,locality,neworold,additionalrooms,facing,overlooking,ownership,possesiondate
bhk = '3 BHK Apartment'                                  
bhk = 'bhk_' + bhk + ' '                                    #done
locality = 'Aditya Birla Hospital Marg'
locality = 'locality_' + locality                           #done
possesiondate = 'Sep 2021'
possesiondate = 'possesiondate_' + possesiondate            #done
age = '10 - 11 years'
age = 'age_' + age                                          #done

neworold = 'Resale'
neworold = 'neworold_' + neworold                           #done
additionalrooms = '1 rooms( study room )'
additionalrooms = 'additionalrooms_' + additionalrooms        #done
facing = 'NorthEast'
facing = 'facing_' + facing                                  #done

overlooking = 'Corner, Garden View, Pool View'
overlooking = 'overlooking_' + overlooking                 #done
ownership = 'Co-Operative Society'
ownership = 'ownership_' + ownership                    #done
facing 


# In[14]:


if roadfaceing is None:
    roadfaceing = 999
if opensides is None:
    opensides = 1    
if totalfloor is None:
    totalfloor = 0


# In[15]:


# this cell refer file amenity.py for expanded version of code
#bathroom,balconies,pricepersquare,roadfaceing,opensides,totalfloor these are direct numeric values
  
# for ameineties
if Lift_Available is None:
    Lift_Available = 0
else:
    if Lift_Available == 'Yes':
        Lift_Available = 1
    else:
        Lift_Available = 0
    
if Car_Parking is None:
    Car_Parking = 0
else:
    if Car_Parking == 'Yes':
        Car_Parking = 1
    else:
        Car_Parking = 0

if Power_Backup is None:
    Power_Backup = 0
else:
    if Power_Backup == 'Yes':
        Power_Backup = 1
    else:
        Power_Backup = 0

if Security is None:
    Security = 0
else:
    if Security == 'Yes':
        Security = 1
    else:
        Security = 0
        
if Childrens_play_area is None:
    Childrens_play_area = 0
else:
    if Childrens_play_area == 'Yes':
        Childrens_play_area = 1
    else:
        Childrens_play_area = 0

if Vaastu_Compliant is None:
    Vaastu_Compliant = 0
else:
    if Vaastu_Compliant == 'Yes':
        Vaastu_Compliant = 1
    else:
        Vaastu_Compliant = 0

if Club_House is None:
    Club_House = 0
else:
    if Club_House == 'Yes':
        Club_House = 1
    else:
        Club_House = 0
        
        
if Gymnasium is None:
    Gymnasium = 0
else:
    if Gymnasium == 'Yes':
        Gymnasium = 1
    else:
        Gymnasium = 0
        
if Swimming_Pool is None:
    Swimming_Pool = 0
else:
    if Swimming_Pool == 'Yes':
        Swimming_Pool = 1
    else:
        Swimming_Pool = 0
        
if Sports_Facility is None:
    Sports_Facility = 0
else:
    if Sports_Facility == 'Yes':
        Sports_Facility = 1
    else:
        Sports_Facility = 0
        
if Indoor_Games is None:
    Indoor_Games = 0
else:
    if Indoor_Games == 'Yes':
        Indoor_Games = 1
    else:
        Indoor_Games = 0
        
if Jogging_Track is None:
    Jogging_Track = 0
else:
    if Jogging_Track == 'Yes':
        Jogging_Track = 1
    else:
        Jogging_Track = 0
        
if Maintenance_Staff is None:
    Maintenance_Staff = 0
else:
    if Maintenance_Staff == 'Yes':
        Maintenance_Staff = 1
    else:
        Maintenance_Staff = 0
        
if Intercom is None:
    Intercom = 0
else:
    if Intercom == 'Yes':
        Intercom = 1
    else:
        Intercom = 0
        
if Golf_Course is None:
    Golf_Course = 0
else:
    if Golf_Course == 'Yes':
        Golf_Course = 1
    else:
        Golf_Course = 0
        
if Cafeteria is None:
    Cafeteria = 0
else:
    if Cafeteria == 'Yes':
        Cafeteria = 1
    else:
        Cafeteria = 0
        
if Rain_Water_Harvesting is None:
    Rain_Water_Harvesting = 0
else:
    if Rain_Water_Harvesting == 'Yes':
        Rain_Water_Harvesting = 1
    else:
        Rain_Water_Harvesting = 0
        
if Staff_Quarter is None:
    Staff_Quarter = 0
else:
    if Staff_Quarter == 'Yes':
        Staff_Quarter = 1
    else:
        Staff_Quarter = 0
        
if Multipurpose_Room is None:
    Multipurpose_Room = 0
else:
    if Multipurpose_Room == 'Yes':
        Multipurpose_Room = 1
    else:
        Multipurpose_Room = 0
        
if Landscaped_Gardens is None:
    Landscaped_Gardens = 0
else:
    if Landscaped_Gardens == 'Yes':
        Landscaped_Gardens = 1
    else:
        Landscaped_Gardens = 0
        
if Shopping_Mall is None:
    Shopping_Mall = 0
else:
    if Shopping_Mall == 'Yes':
        Shopping_Mall = 1
    else:
        Shopping_Mall = 0
        
if School is None:
    School = 0
else:
    if School == 'Yes':
        School = 1
    else:
        School = 0
        
if Hospital is None:
    Hospital = 0
else:
    if Hospital == 'Yes':
        Hospital = 1
    else:
        Hospital = 0
        
if ATM is None:
    ATM = 0
else:
    if ATM == 'Yes':
        ATM = 1
    else:
        ATM = 0
        
if AC is None:
    AC = 0
else:
    if AC == 'Yes':
        AC = 1
    else:
        AC = 0
        
if Wardrobe is None:
    Wardrobe = 0
else:
    if Wardrobe == 'Yes':
        Wardrobe = 1
    else:
        Wardrobe = 0
        
if TV is None:
    TV = 0
else:
    if TV == 'Yes':
        TV = 1
    else:
        TV = 0
        
if Refrigerator is None:
    Refrigerator = 0
else:
    if Refrigerator == 'Yes':
        Refrigerator = 1
    else:
        Refrigerator = 0
        
if Sofa is None:
    Sofa = 0
else:
    if Sofa == 'Yes':
        Sofa = 1
    else:
        Sofa = 0
        
if Washing_Machine is None:
    Washing_Machine = 0
else:
    if Washing_Machine == 'Yes':
        Washing_Machine = 1
    else:
        Washing_Machine = 0
        
if Wifi is None:
    Wifi = 0
else:
    if Wifi == 'Yes':
        Wifi = 1
    else:
        Wifi = 0
        
if Microwave is None:
    Microwave = 0
else:
    if Microwave  == 'Yes':
        Microwave  = 1
    else:
        Microwave  = 0
        
if Dining_Table is None:
    Dining_Table = 0
else:
    if Dining_Table == 'Yes':
        Dining_Table = 1
    else:
        Dining_Table = 0
        
if Gas_connection is None:
    Gas_connection = 0
else:
    if Gas_connection == 'Yes':
        Gas_connection = 1
    else:
        Gas_connection = 0
        
if BED is None:
    BED = 0
else:
    if BED == 'Yes':
        BED = 1
    else:
        BED = 0


# In[17]:


rowlist =list()
for i in range(len(X.columns)):
    rowlist.append(0)


# In[18]:


# making new dataframe for query
querydf = pd.DataFrame(columns = X.columns)       # clinically done
querydf


# In[19]:


# just to add an empty row in data frame
querydf.loc[0] = rowlist


# In[20]:


querydf.loc[0, 'area'] = area
querydf.loc[0, 'bathroom'] = bathroom
querydf.loc[0, 'pricepersquare'] = pricepersquare
querydf.loc[0, 'roadfaceing'] = roadfaceing
querydf.loc[0, 'opensides'] = opensides
querydf.loc[0, 'totalfloor'] = totalfloor


# In[21]:


querydf.loc[0, 'area'] = area
querydf.loc[0, 'bathroom'] = bathroom
querydf.loc[0, 'Lift Available'] = Lift_Available
querydf.loc[0, 'Car Parking'] = Car_Parking
querydf.loc[0, 'Power Backup'] = Power_Backup
querydf.loc[0, '24 X 7 Security'] = Security
querydf.loc[0, "Children's play area"] = Childrens_play_area
querydf.loc[0, 'Vaastu Compliant'] = Vaastu_Compliant
querydf.loc[0, 'Club House'] = Club_House
querydf.loc[0, 'Gymnasium'] = Gymnasium
querydf.loc[0, 'Swimming Pool'] = Swimming_Pool
querydf.loc[0, 'Car Parking'] = Car_Parking
querydf.loc[0, 'Sports Facility'] = Sports_Facility
querydf.loc[0, 'Indoor Games'] = Indoor_Games
querydf.loc[0, "Jogging Track"] = Jogging_Track
querydf.loc[0, 'Maintenance Staff'] = Maintenance_Staff

querydf.loc[0, 'Intercom'] = Intercom
querydf.loc[0, 'Golf Course'] = Golf_Course
querydf.loc[0, 'Cafeteria'] = Cafeteria
querydf.loc[0, 'Car Parking'] = Car_Parking
querydf.loc[0, 'Rain Water Harvesting'] = Rain_Water_Harvesting
querydf.loc[0, 'Staff Quarter'] = Staff_Quarter
querydf.loc[0, "Multipurpose Room"] = Multipurpose_Room
querydf.loc[0, 'Vaastu Compliant'] = Vaastu_Compliant
querydf.loc[0, 'Landscaped Gardens'] = Landscaped_Gardens
querydf.loc[0, 'Shopping Mall'] = Shopping_Mall
querydf.loc[0, 'School'] = School
querydf.loc[0, 'Hospital'] = Hospital
querydf.loc[0, 'ATM'] = ATM
querydf.loc[0, 'AC'] = AC
querydf.loc[0, "Wardrobe"] = Wardrobe
querydf.loc[0, 'TV'] = TV

querydf.loc[0, 'Refrigerator'] = Refrigerator
querydf.loc[0, 'Sofa'] = Sofa
querydf.loc[0, 'Washing Machine'] = Washing_Machine
querydf.loc[0, 'Wifi'] = Wifi
querydf.loc[0, 'Microwave'] = Microwave
querydf.loc[0, 'Dining Table'] = Dining_Table
querydf.loc[0, "Gas connection"] = Gas_connection
querydf.loc[0, 'BED'] = BED
querydf.loc[0, 'pricepersquare'] = pricepersquare
querydf.loc[0, 'roadfaceing'] = roadfaceing
querydf.loc[0, 'opensides'] = opensides
querydf.loc[0, 'totalfloor'] = totalfloor


querydf


# In[22]:


if bhk in X:
    querydf[bhk] = 1    
if possesiondate in X:
    querydf[possesiondate] = 1 # Assign that column in X data frame to 1
if locality in X:
    querydf[locality] = 1 # Assign that column in X data frame to 1
if age in X:
    querydf[age] = 1 # Assign that column in X data frame to 1
if neworold in X:
    querydf[neworold] = 1 # Assign that column in X data frame to 1
    
if additionalrooms in X:
    querydf[additionalrooms] = 1 # Assign that column in X data frame to 1
if facing in X:
    querydf[facing] = 1 # Assign that column in X data frame to 1
if overlooking in X:
    querydf[overlooking] = 1 # Assign that column in X data frame to 1
if ownership in X:
    querydf[ownership] = 1 # Assign that column in X data frame to 1
    
    


# In[24]:


#df.columns
#X = df2[price_predictors]


# In[25]:


val_predictions = house_model_DT.predict(querydf)
val_predictions


# In[26]:


val_predictions = house_model_RF.predict(querydf)
val_predictions


# In[27]:


result = int(val_predictions)
with open('result.json', 'w+') as outfile:
    json.dump(result, outfile)


# In[28]:


result


# In[29]:


print(time.clock() - start)

