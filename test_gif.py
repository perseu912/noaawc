from noaawc.animate import Create_plot_gif as Cpf
from noawclg.main import get_noaa_data as gnd

dn = gnd()

point_init=[-9.43,-89]
point_jua = [-9.43,-40.50]

gif = Cpf(dn=dn)
gif.path_save='test.gif'
gif.title='temperatura dos jatos de vento'
gif.point_init=point_init
gif.point_end=point_jua
gif.lon_stop=-35

gif.tracing()
gif.render()