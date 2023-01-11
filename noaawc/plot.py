
import numpy as np
#import pygrib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from noawclg import get_noaa_data as gnd
import pandas as pd
from dataclasses import dataclass

#dn = gnd()

#keys = dn.get_noaa_keys()
'''
the function base and more
important from it work
'''
plt.style.use('dark_background')

@dataclass
class plot_global:
    dn:gnd=None
    path:str='plot.png'
    indice:int=0
    date:str=None
    title:str='plot'
    text:str=False
    pos_text:tuple=False
    annotate:str=False
    pos_annotate:tuple=False
    text_color='white'
    text_size=9
    fontweight_text='bold'
    facecolor_text:str='red'
    edgecolor_text:str='black'
    annotate_size:float=9
    annotate_color:str='white'
    loc_focus:tuple=(0,0)
    key_noaa:str='tmpmwl'
    subtr_data:str=273,
    text_cb:str='ºC'
    alpha:str=1
    author:str='@gpftc_ | @reinanbr_'
    level_data:int=25
    keys:str = ''
    fillcontinents_colors:str = ''
    cmap:plt.cm = plt.cm.inferno
    ax:plt.subplot = plt.subplot(111)
    plt:plt=plt
    
    
    
    def mining_data(self):
        
        self.fillcontinents_colors:str = {'color':'coral','lake_color':'aqua'}
        if self.date:
            self.dn = gnd(date=self.date)
            self.keys = self.dn.get_noaa_keys()
            self.data = self.dn[self.key_noaa][self.indice]-self.subtr_data
            self.data1 = self.dn[self.key_noaa][1]-self.subtr_data
        #import pandas as pd 
        self.lat  = self.dn['lat'][:]
        self.lon  = self.dn['lon'][:]
        self.data = self.dn[self.key_noaa][self.indice]-self.subtr_data
        self.data1 = self.dn[self.key_noaa][1]-self.subtr_data
        #print(len(data),len(lat))
        
        #if not self.indice==None:
        self.date_pd=self.dn['time'][self.indice].to_numpy()
        
        
        self.ts = pd.to_datetime(str(self.date_pd)) 
        self.date_text = self.ts.strftime('%d %h %Y\n %H:%M UTC')
        self.min_temp = self.data1.min()
        self.max_temp = self.data1.max()
        self.levels = np.linspace(self.min_temp,self.max_temp,self.level_data)


    def rendering_image(self):
        self.m = Basemap(projection='ortho',
                         lat_0=self.loc_focus[0],
                         lon_0=self.loc_focus[1],
                         resolution='c')
        
        self.x, self.y = self.m(*np.meshgrid(self.lon,self.lat))
        
        self.m.fillcontinents(self.fillcontinents_colors['color'],
                              self.fillcontinents_colors['lake_color'])
        self.cm=self.m.contourf(self.x,self.y,self.data,100,
                                alpha=self.alpha,
                                levels=self.levels,
                                cmap=self.cmap)
        #cm1=plt.contourf(x,y,data1,100,shading='nearest',cmap=plt.get_cmap('inferno'))
        #plt.cla()
        #plt.clf()
        self.cbar=self.plt.colorbar(self.cm,orientation='horizontal',extend='both',fraction=0.07,pad=0.05)
        
        self.m.drawcoastlines()
        #m.drawmapboundary(fill_color='aqua')
        #m.drawrivers(linewidth=0.1)
        self.m.drawcountries(linewidth=0.25)
        self.m.drawcountries(linewidth=0.25)
        
        #m.drawmapboundary(fill_color='aqua')

        self.m.drawmeridians(np.arange(0,360,30))
        self.m.drawparallels(np.arange(-90,90,30))
        #print(dir(m))
        self.m.drawmapboundary(fill_color='aqua')
        
    
    
    def rendering_text(self):
        self.cbar.set_label(self.text_cb,y=0,ha='right',color='white')
        self.cbar.ax.set_title(f'by: {self.author}',fontweight='bold')
        
        #xn2,yn2=m(-9.52,-40.61)
        self.t = self.plt.text(-0.3,0.99,self.date_text, transform=self.ax.transAxes,
                    color='white', fontweight='bold',fontsize=14)
        self.t = self.plt.text(1.1,1,f'*\n{self.key_noaa}:\n{self.keys[self.key_noaa]}',transform=self.ax.transAxes,
                    color='grey', fontweight='bold',fontsize=5)
        self.t = self.plt.text(1.1,0.03,'data: GFS 0.25', transform=self.ax.transAxes,
                    color='white', fontweight='bold',fontsize=8)
        self.t = self.plt.text(1.12,-0.01,'NOAA/NASA', transform=self.ax.transAxes,
                    color='grey', fontweight='bold',fontsize=8)
        #t.set_bbox(dict(facecolor='red', alpha=0.81, edgecolor='black'))
        
        if self.pos_text and self.text:
            self.t = self.plt.text(self.pos_text[0],self.pos_text[1], self.text, transform=self.ax.transAxes,
                        color=text_color, fontweight='bold',fontsize=text_size)
            self.t.set_bbox(dict(facecolor='red', alpha=0.81, edgecolor='black'))
        
        if self.annotate and self.pos_annotate:
            xn,yn=self.m(self.pos_annotate[1],self.pos_annotate[0])
            self.plt.annotate(self.annotate,color=self.annotate_color,xy=(xn,yn),xytext=(xn,yn),xycoords='data',textcoords='data')
        
        
        self.plt.title(self.title,fontweight='bold',fontsize=16)
        
        
        
    def render(self,show=True,save=True):
        self.plt.style.use('dark_background')
        self.mining_data()
        self.rendering_image()
        self.rendering_text()
        if save:
            self.plt.savefig(self.path)
        if show:
            self.plt.show()
        self.plt.cla()
        self.plt.clf()






def old_plot_global(path:str,indice:int=None,date:str=None,title='plot',text:str=False,pos_text:tuple=False,annotate:str=False,
               pos_annotate:tuple=False,text_color='white',text_size=9,fontweight_text='bold',
               facecolor_text:str='red',edgecolor_text:str='black',annotate_size:float=9, 
                annotate_color:str='white',loc_focus:tuple=(0,0),key_noaa='tmpmwl',subtr_data=273,
               text_cb='ºC',alpha=1,author='@gpftc_ | @reinanbr_'):
    
    plt.style.use('dark_background')
    ax = plt.subplot(111)


    lat  = dn['lat'][:]
    lon  = dn['lon'][:]
    data = dn[key_noaa][indice]-subtr_data
    data1 = dn[key_noaa][1]-subtr_data
    print(len(data),len(lat))
    
    if indice and (not date):
        date_pd=dn['time'][indice].to_numpy()
    
    if date and (not indice):
        dn = gnd(date=date)
        data = dn[key_noaa][indice]-subtr_data
        data1 = dn[key_noaa][1]-subtr_data
    #import pandas as pd 
    ts = pd.to_datetime(str(date_pd)) 
    date_text = ts.strftime('%d %h %Y\n %H:%M UTC')
    #print(d)

#     m=Basemap(projection='mill',lat_0=-9.41,lon_0=40,lat_ts=10,llcrnrlon=lon.min(), \
#       urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
#       resolution='l')
    
    m = Basemap(projection='ortho',lat_0=loc_focus[0],lon_0=loc_focus[1],resolution='c')
    # convert the lat/lon values to x/y projections.
    
    x, y = m(*np.meshgrid(lon,lat))
#     x[x>1e20]=np.nan
#     y[y>1e20]=np.nan
    # plot the field using the fast pcolormesh routine 
    # set the colormap to jet.

#     Z = data
#     import numpy.ma as ma

#     Zm = ma.masked_invalid(Z)
    #m.contour(x,y,data,50,cmap=plt.cm.jet)
    min_temp = data1.min()
    max_temp = data1.max()
    levels = np.linspace(min_temp,max_temp,25)
    
    m.fillcontinents(color='coral',lake_color='aqua')
    cm=m.contourf(x,y,data,100,alpha=alpha,levels=levels,cmap=plt.cm.inferno)
    #cm1=plt.contourf(x,y,data1,100,shading='nearest',cmap=plt.get_cmap('inferno'))
    #plt.cla()
    #plt.clf()
    cbar=plt.colorbar(cm,orientation='horizontal',extend='both',fraction=0.07,pad=0.05)
    cbar.set_label(text_cb,y=0,ha='right',color='white')
    cbar.ax.set_title(f'by: {author}',fontweight='bold')
    
    
    #temp_cbar=np.linspace(-40,36,8)
    #cbar.set_ticks([int(i) for i in temp_cbar])
    #cbar.ax.invert_yaxis()
    #cbar.ax.set_yticklabels(["{:2.2f}".format(i) for i in data_cm]) # add the labels

    # Add a coastline and axis values.
    #print(dir(m))
    m.drawcoastlines()
    #m.drawmapboundary(fill_color='aqua')
    #m.drawrivers(linewidth=0.1)
    m.drawcountries(linewidth=0.25)
    m.drawcountries(linewidth=0.25)
    
    #m.drawmapboundary(fill_color='aqua')

    m.drawmeridians(np.arange(0,360,30))
    m.drawparallels(np.arange(-90,90,30))
    #print(dir(m))
    m.drawmapboundary(fill_color='aqua')
    #print(dir(m))
    
    
    
   
#     lats = [-40.5,-40.6,-40.5,-40.6]
#     lons = [-9.41,-9.51,-9.41,-9.51]
#     draw_screen_poly(lats,lons,m)

    #xn2,yn2=m(-9.52,-40.61)
    t = plt.text(-0.3,0.99,date_text, transform=ax.transAxes,
                color='white', fontweight='bold',fontsize=14)
    t = plt.text(1.1,1,f'*\n{key_noaa}:\n{keys[key_noaa]}',transform=ax.transAxes,
                color='grey', fontweight='bold',fontsize=5)
    t = plt.text(1.1,0.03,'data: GFS 0.25', transform=ax.transAxes,
                color='white', fontweight='bold',fontsize=8)
    t = plt.text(1.12,-0.01,'NOAA/NASA', transform=ax.transAxes,
                color='grey', fontweight='bold',fontsize=8)
    #t.set_bbox(dict(facecolor='red', alpha=0.81, edgecolor='black'))
    
    if pos_text and text:
        t = plt.text(pos_text[0],pos_text[1], text, transform=ax.transAxes,
                     color=text_color, fontweight='bold',fontsize=text_size)
        t.set_bbox(dict(facecolor='red', alpha=0.81, edgecolor='black'))
    
    if annotate and pos_annotate:
        xn,yn=m(pos_annotate[1],pos_annotate[0])
        plt.annotate(annotate,color=annotate_color,xy=(xn,yn),xytext=(xn,yn),xycoords='data',textcoords='data')
    
    
    plt.title(title,fontweight='bold',fontsize=16)
    plt.savefig(path)
    #plt.show()




