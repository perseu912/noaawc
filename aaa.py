import noawclg.main as main
from noawclg.main import get_noaa_data as gnd
from noawclg.plot import plot_data_from_place as pdp
import matplotlib.pyplot as plt


date_base = '21/05/2023'
main.set_date(date_base)
data_noaa = gnd()

place = 'juazeiro BA'

jua_pet = pdp(place=place,data=data_noaa)
jua_pet.path_file='plot_wind100m.png'

jua_pet.key_noaa='tmp80m'
jua_pet.title='Temperatura do Ar\nPetrolina-PE/Juazeiro-BA'
jua_pet.ylabel='°C'
jua_pet.xlabel='Dias'

def fmt_data(data): return data-273
jua_pet.fmt_data =  fmt_data

jua_pet.render()

