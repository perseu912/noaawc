from noaawc.animate import Create_plot_gif as Cpf
from noawclg.main import get_noaa_data as gnd


def test_render():
    dn = gnd(date='13/05/2023') 

    point_init=[-9.43,-89] 
    point_jua = [-9.43,-40.50] 
    cmap = 'inferno'


    gif = Cpf(dn=dn) 

    gif.path_save=f'spin_rain.gif' 
    gif.key_noaa = 'acpcpsfc' 

    gif.title='precipitação de chuvas (acumuladas)'

    gif.point_init=point_init 
    gif.point_end=point_jua

    gif.lon_stop=-39

    gif.cmap = cmap

    gif.author = '@gpfc_ | @reinanbr_' 

    gif.text_cb = 'kg/m^2' 
    gif.subtr_data = 0


    gif.tracing()
    gif.render_cache()
    gif.render_mp4('test.mp4')
    
test_render()