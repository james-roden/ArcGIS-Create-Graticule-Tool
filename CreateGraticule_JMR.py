# Create Graticule Tool for ArcGIS
# PEP8 Styling
# Creates graticule of desired resolution. Graticules down to 1 degree are
# widely available to download, use this tool for sub-degree intervals.
# James M Roden (Feb 2017)

try:
    import arcpy
    import sys
    import traceback

    def dms_to_dd(degrees, minutes, seconds):
        '''
        Converts degrees, minutes or seconds into decimal degrees
        '''
        return degrees + (minutes/60.0) + (seconds/3600.0)

    arcpy.env.workspace = r'in_memory'
    arcpy.env.overwriteOutput = True

    # ArcGIS toolbox parameters
    degrees = int(arcpy.GetParameterAsText(0))  # degrees
    minutes = int(arcpy.GetParameterAsText(1))  # minutes
    seconds = int(arcpy.GetParameterAsText(2))  # seconds
    out_feature_class = arcpy.GetParameterAsText(3)  # Output feature class

    # Variables prepared for GP
    mxd = arcpy.mapping.MapDocument("CURRENT")
    data_frame = mxd.activeDataFrame
    sr = data_frame.spatialReference
    arcpy.env.outputCoordinateSystem = sr
    extent = data_frame.extent
    lower_left = extent.lowerLeft
    upper_right = extent.upperRight
    interval_param = dms_to_dd(degrees, minutes, seconds)

    # Construct coordinate variables for Fishnet. Round so that they fall on a
    # line of lat and long.
    origin_coord = str(round(lower_left.X)) + ' ' + str(round(lower_left.Y))
    corner_coord = str(round(upper_right.X)) + ' ' + str(round(upper_right.Y))
    orient_coord = str(round(lower_left.X)) + ' ' + str(round(lower_left.Y
                                                  + 10))
    arcpy.CreateFishnet_management('_grat', origin_coord, orient_coord,
                                interval_param, interval_param, "", "",
                                corner_coord, 0, "", "POLYLINE")

    # Densify so there are enough intermediate vertices so graticule lines
    # 'curve' when projected.
    densify_distance = interval_param/3.00
    arcpy.Densify_edit('_grat', 'DISTANCE', densify_distance)

    arcpy.CopyFeatures_management('_grat', out_feature_class)

except:
    tb = sys.exc_info()[2]  # Traceback object
    tbinfo = traceback.format_tb(tb)[0]  # Traceback string
    # Concatenate error information and return to GP window
    pymsg = ('PYTHON ERRORS:\nTraceback info:\n' + tbinfo + '\nError Info: \n'
            + str(sys.exc_info()[1]))
    msgs = 'ArcPy ERRORS:\n' + arcpy.GetMessage(2) + '\n'
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)

finally:
    # Delete in_memory
    arcpy.Delete_management('in_memory')

# End of script
