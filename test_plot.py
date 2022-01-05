from noaawc import plot_global
import matplotlib.pyplot as plt

indice= 8

plt.style.use('dark_background')
#data_j = dn.get_data_from_point(point=(-9.41,-40.5))['tmpsig995']-273
#temp_j = float(data_j[indice])
#plt.style.use('dark_background')

#text=f'Juazeiro - BA\n{temp_j:.1f}°C',
#            text_size=9,text_color='white',annotate='*',pos_annotate=(-9.4168,-40.5035),
#            annotate_color='white'

plot_global(path='juazeiro_wind.png',title=f'Velocidade dos jatos\nde ventos',key_noaa='apcpsfc',
            indice=indice,loc_focus=(-9.41,-40.5),subtr_data=0,text_cb='mm',alpha=.7)