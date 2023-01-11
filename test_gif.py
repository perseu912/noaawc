from noaawc import create_plot_gif as cpf

point_init=[-9.43,-89]
point_jua = [-9.43,-40.50]

cpf('test.gif',title='temperatura dos jatos de vento',point_init=point_init,point_end=point_jua,lon_stop=-35)