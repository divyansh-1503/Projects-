#pip install cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
projection=ccrs.PlateCarree()
fig,ax=plt.subplots(subplot_kw={'projection':projection})
ax.set_extent([-180,180,-90,90], crs=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND,facecolor="RED")

ax.add_feature(cfeature.OCEAN,facecolor="BLACK")

plt.show()