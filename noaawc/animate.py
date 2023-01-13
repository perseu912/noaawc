
'''
Reinan Br <slimchatuba@gmail.com>
5 jan 2022 19:08 (init)
lib: noaawc
license: GPLv3
--------------------------------------------------

'''
import numpy as np
#import pygrib
import psutil as ps
import imageio
import time
import os
from noaawc.plot import plot_global
import matplotlib.pyplot as plt






def create_plot_gif(path_gif='img.gif',size:int=70,path_data='data/img_',title='',key_noaa='vgrdpbl',
                   loc_focus=(0,0),point_init=False,point_end=False,text_cb='°C',lon_stop=False,alpha=1,
                   subtr_data=0,speed_degree_frame=1):

    assert size < 128, print('size of data is max 128!!')
    images = []
    #size = frames
    time_0 = time.time()
    ping_list = np.array([0])
    
    locs_focus = []
    if loc_focus:
        for _ in range(size):
            locs_focus.append(loc_focus)
        
    if point_init and point_end:
        lat_space = (point_init[0],point_end[0])
        lon_space = (point_init[1],point_end[1])
        #print(lon_space)
        
        
        lat_list = np.linspace(lat_space[0],lat_space[1],size)
        
        lon_list = np.linspace(lon_space[0],lon_space[1],size)
        #print('after',lon_list)
        
        if lon_stop:
            print('istop: yes')
            k = speed_degree_frame*size+lon_space[0]-lon_space[1]
            lon_list = np.linspace(lon_space[0],lon_space[1]+k,size)
            lon_list[abs(lon_list)<abs(lon_stop)] = lon_stop 
            #print('before',lon_list)
        locs_focus = list(zip(lat_list,lon_list))
        
    for i in range(size):
        path_img = f'{path_data}_{i}.png'

        time0 = time.time()

        #temp_j = float(data_j[i])
        #print(locs_focus)
        pg = plot_global(path=path_img,title=title,key_noaa=key_noaa,alpha=alpha,
                indice=i,loc_focus=locs_focus[i],subtr_data=subtr_data,text_cb=text_cb)
        
        pg.cmap = plt.cm.jet

        #pg.date = '10/01/2023'
        pg.render(show=False)
        ping = time.time()-time0
        ping_list = np.append(ping_list,[ping])
        ping_m = sum(ping_list)/len(ping_list)
        i_=i+1
        eta = (size-i_)*ping_m
        min_eta = eta//60
        seg_eta = eta%60
        per = (i_/size)*100
        perr = time.time()-time_0
        min_perr = perr//60
        seg_perr = perr%60
        os.system(f'echo "[{i_}/{size} {per:.2f}% | PER :{int(min_perr)}min :{int(seg_perr)}seg / ETA: {int(min_eta)}min :{int(seg_eta)}seg]   [CPU:{ps.cpu_percent()}% | RAM:{ps.virtual_memory().percent}% swap:{ps.swap_memory().percent}%]"')

        images.append(imageio.imread(path_img))

    print('criando gif...')
    imageio.mimsave(path_gif,images)