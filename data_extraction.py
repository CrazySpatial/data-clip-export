#Name: data_extraction
#Purpose: This tool is designed to run in the python module in arc. Add any and all features inside  the layer panel and then create a feature class 
#                   named study_area. All features will export to a path designated by the user.
import os, arcpy
arcpy.env.overwriteOutput = True

in_clip_layer = r"L:/2016/test/study_area.shp" #Select  location of the study_area
out_gdb = r"D:/output/" #Define a location to dump the files

mxd_obj = arcpy.mapping.MapDocument("CURRENT") # This will create a object for the current map document in which y ou will use for you for loop

for lyr in arcpy.mapping.ListLayers(mxd_obj):
    arcpy.AddMessage(lyr)
    out_layer = os.path.join(out_gdb,lyr.name)
    arcpy.Clip_analysis(lyr,in_clip_layer,out_layer)