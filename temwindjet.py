from noaawc.animate import Create_plot_gif as Cpf
from noawclg.main import get_noaa_data as gnd


def test_render():
    dn = gnd(date='21/09/2023') 

    point_jua = (-9.43847,-40.5052)
    cmap = 'CMRmap'

    gif = Cpf(dn=dn,fps=7) 
    gif.key_noaa = 'tmpmwl'

    gif.title = 'Temperatura dos Jatos de Ventos na Atmosfera'

    gif.color_line_states = 'black'
    gif.loc_focus = point_jua
    gif.annotate_data_focus = ('. Juazeiro: %(data)sºC')
    gif.zoom = (2,-2,-2,2)
    gif.fps = 7

    gif.cmap = cmap
    gif.author = '@gpfc_ | @reinanbr_' 
    gif.text_cb = 'ºC' 
    gif.subtr_data = 273

    gif.tracing()
    gif.render_cache()
    gif.render_mp4('jet_wind_temp.mp4')
    
    
    
test_render()