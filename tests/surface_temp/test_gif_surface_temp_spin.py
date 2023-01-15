from noaawc.animate import Create_plot_gif as Cpf
from noawclg.main import get_noaa_data as gnd

dn = gnd()

point_init=[-9.43,-89]
point_jua = [-9.43,-40.50]

gif = Cpf(dn=dn)
gif.path_save='tests_gifs/test_spin_temp_surface.gif'
gif.key_noaa = 'tmpsfc'
gif.title='temperatura da superficie'
gif.point_init=point_init
gif.point_end=point_jua
gif.lon_stop=-39

gif.tracing()
gif.render()