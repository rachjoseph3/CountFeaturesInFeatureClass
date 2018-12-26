#script to count features in a feature class

#12/26/2018

import arcpy

fc = r" " #path to feature class

count = 0

with arcpy.da.SearchCursor(fc, ("OBJECTID")) as cursor:
    for item in cursor:
        print item
        count += 1

del cursor

print("Number of features in feature class: {}".format(count))
