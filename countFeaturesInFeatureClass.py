#script to count features in a feature class

#12/26/2018

import arcpy

fc = r"E:\TreeRisk\TreeRiskTools\OtherTestLines\line_t6390\Line_T6390_Outputs\Line_T6390_Hazard_Tree.gdb\TreeRisk_Complete_Hazard_Tree_Cat2" #test Hazard tree cat 2 feature class

count = 0

with arcpy.da.SearchCursor(fc, ("OBJECTID")) as cursor:
    for item in cursor:
        print item
        count += 1

del cursor

print("Number of features in feature class: {}".format(count))
