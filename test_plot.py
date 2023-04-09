from noaawc.plot import plot_global
from noawclg.main import get_noaa_data as gnd
import matplotlib.pyplot as plt

plt.style.use('dark_background')
cmap = 'inferno'

date_base = '06/04/2023'
dn = gnd(date=date_base)
indice = 5



pg = plot_global(dn=dn)
pg.path=f'{cmap}_juazeiro_wind_focus1.png'
pg.title=f'Temperatura dos Jatos de Ventos'
pg.key_noaa='tmpmwl'
pg.indice=indice

pg.loc_focus=(-9.43847,-40.5052)
pg.zoom(1,-1,-1,1)

pg.text_cb='°C'
pg.author='@gpftc | @reinanbr_'
pg.cmap = cmap

pg.resolution = 'l'
pg.level_data = 40
pg.line_states = .3
pg.render(show=True)
