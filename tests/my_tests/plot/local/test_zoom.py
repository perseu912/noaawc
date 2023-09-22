from noaawc.plot import plot_global
from noawclg.main import get_noaa_data as gnd
import matplotlib.pyplot as plt

cmap = 'inferno'

date_base = '16/05/2023'
dn = gnd(date=date_base)
indice = 5



pg = plot_global(dn=dn,fps=7)
pg.path=f'geralplot.png'
pg.title=f'Temperatura dos Jatos de Ventos'
pg.key_noaa='tmpmwl'
pg.indice=indice


pg.loc_focus=(-9.43847,-40.5052)
pg.annotate_data_focus('. Juazeiro: %(data)sºC')
pg.annotate_color_focus = 'white'
pg.zoom(2,-2,-2,2)


pg.text_cb='°C'
pg.author='@gpftc | @reinanbr_'
pg.cmap = cmap



pg.render(show=False)
