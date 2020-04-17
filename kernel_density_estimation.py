# Name: KernelDensity_Ex_02.py
# Description: Calculates a magnitude per unit area from point or polyline 
#    features using a kernel function to fit a smoothly tapered 
#    surface to each point or polyline.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "E:/GitHub/kernelDensityEstimation/data"

#TODO: READ FROM CSV FILE

# Set local variables
inFeatures = "rec_sites.shp"
populationField = "NONE"
cellSize = 60
searchRadius = 2500

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute KernelDensity
outKernelDensity = KernelDensity(inFeatures, populationField, cellSize,
                                 searchRadius, "SQUARE_KILOMETERS")

# Save the output 
outKernelDensity.save("C:/sapyexamples/output/kerneldout")
