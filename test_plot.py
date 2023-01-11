from noaawc import plot_global
import matplotlib.pyplot as plt

indice= 13

plt.style.use('dark_background')
#data_j = dn.get_data_from_point(point=(-9.41,-40.5))['tmpsig995']-273
#temp_j = float(data_j[indice])
#plt.style.use('dark_background')

#text=f'Juazeiro - BA\n{temp_j:.1f}°C',
#            text_size=9,text_color='white',annotate='*',pos_annotate=(-9.4168,-40.5035),
#            annotate_color='white'

pg = plot_global(path='juazeiro_wind.png',title=f'Preciptações',key_noaa='tmpsfc',
            indice=indice,loc_focus=(-20.41,-40.5),text_cb='°C',alpha=.7,author='@gpftc | @reinanbr_')

pg.cmap =plt.cm.jet

pg.date = '10/01/2023'
pg.render(show=True)