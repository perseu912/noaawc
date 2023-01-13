from noaawc.plot import plot_global
import noawclg.main as main
from noawclg.main import get_noaa_data as gnd
import matplotlib.pyplot as plt
indice= 5


plt.style.use('dark_background')



date_base = '13/01/2023'

main.set_date(date_base)
dn = gnd()


cmap = 'jet'
pg = plot_global(dn=dn)
pg.path=f'test_plots/juazeiro_wind_focus.png'
pg.title=f'Temperatura dos Jatos de Ventos'
pg.key_noaa='tmpmwl'
pg.indice=indice
pg.loc_focus=(-9.43847,-40.5052)

pg.annotate_data_focus('. Juazeiro: %(data)sºC')

pg.zoom(4,-4,-.5,6)
pg.text_cb='°C'

pg.author='@gpftc | @reinanbr_'

pg.cmap = cmap

#pg.date = '10/01/2023'
pg.render(show=True)