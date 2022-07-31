import requests
import pandas as pd

col_list = ["Municípios", "Estado"]

df = pd.read_csv("municipios_pr.csv", usecols=col_list)

addresses:list = []

for index, row in df.iterrows():
    try:
        address:dict = {}

        req = requests.get("https://nominatim.openstreetmap.org/search.php?q={}%2C+{}&format=jsonv2".format(row['Municípios'], row['Estado']))
        content = req.json()               

        lat_list = [i['lat'] for i in content if 'lat' in i]        
        lon_list = [j['lon'] for j in content if 'lon' in j] 
   
        lat = lat_list[0]
        lon = lon_list[0]                 

        address["Latitude"] = lat
        address["Longitude"] = lon
       
        addresses.append(address)

    except Exception as ex:
        print("ERRO" + str(ex))

new_df = pd.DataFrame(addresses)
new_df.to_csv("output.csv", index=False)

