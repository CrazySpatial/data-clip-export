#Name: data_extraction
#Purpose: This tool is designed to run in the python module in arc. Add any and all features inside  the layer panel and then create a feature class 
#                   named study_area. All features will export to a path designated by the user.

import arcpy
from arcpy import env
from arcpy import mapping

mxd = arcpy.mapping.MapDocument("CURRENT")  # Uses your currently open MXD
df = arcpy.mapping.ListDataFrames(mxd, '')[0] # Chooses the first dataframe

destPath = r"D:/output" # Set your destination folder path

for lyr in arcpy.mapping.ListLayers(mxd, '', df): # Loop through layers
    # Output layer to shapefile
        if lyr.name == 'study_area'
            clip_area = lyr

    arcpy.FeatureClassToFeatureClass_conversion(lyr, destPath, "{}.shp".format(lyr), "", "", "")