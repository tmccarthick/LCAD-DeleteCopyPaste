##Delete, copy, paste for SA@LCAD geodatabase

import arcpy
import sys
import os
import getpass
import datetime

### Set workspace
###newFGDB = r"U:\LCAD\Geodatabases\Testing"
##
### Set local variables
##out_folder_path = r"U:\LCAD\Geodatabases\Testing"
##out_name = "{}".format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
##
##
### Execute CreateFileGDB
##arcpy.CreateFileGDB_management(out_folder_path, out_name)
##
###Set path for local FGDB
##newDB = os.path.join(out_folder_path, out_name) 
##
##print "Created File Geodatabase{} ".format(newDB)

# Set workspace with data to delete
delete_workspacePartOne = r"U:\LCAD\Geodatabases\Testing"
delete_workspacePartTwo = r"CitySept2017copy.gdb"
deleteDataBase = os.path.join(delete_workspacePartOne, delete_workspacePartTwo)


#Delete old data THIS WORKS
for gdb, datasets, features in arcpy.da.Walk(deleteDataBase):
    print gdb
    print datasets
    print features
    for feature in features:       
        arcpy.Delete_management(os.path.join(deleteDataBase,feature))
        print "Delete {} complete".format(feature)


#Allow script to overwrite 
#arcpy.env.overwriteOutput = True

####Copy data
#Set copy workspace
copy_workspacePartOne = r"U:\LCAD\Geodatabases\Testing"
copy_workspacePartTwo = r"CityOct2017copy.gdb"
copyDataBase = os.path.join(copy_workspacePartOne, copy_workspacePartTwo)

for gdb, datasets, features in arcpy.da.Walk(copyDataBase):
    print gdb
    print datasets
    print features
    for feature in features:
        if str(arcpy.Describe(os.path.join(copyDataBase,feature))) == "Table":
            acrpy.TableToGeodatabase_conversion(
        arcpy.CopyFeatures_management((os.path.join(copyDataBase,feature)),
                                       (os.path.join(deleteDataBase,feature)))
        print "Copy {} complete".format(feature)

print "Copy Complete"     

##OrionData does not exist or is not supported (table?)
        
### Set local variables
##out_folder_path = r"U:\LCAD\Geodatabases"
##out_name = "{}".format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
##
##
### Execute CreateFileGDB
##arcpy.CreateFileGDB_management(out_folder_path, out_name)
##
###Set path for local FGDB
##newDB = os.path.join(out_folder_path, out_name)
##
##print "Created File Geodatabase{} ".format(newDB)
##
####Set workspace to LCAD database connection
##arcpy.env.workspace = r"C:\Users\161477\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\Viewer@LCAD.sde"
##workspacePartOne = r"S:\gisds\Projects\LCAD\ftp\CitySept2017"
##workspacePartTwo = r"CitySept2017\CitySept2017.gdb"
##arcpy.env.workspace = os.path.join(workspacePartOne, workspacePartTwo)
##
   
##
