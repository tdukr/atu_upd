"""
KOATUU  provides data in UPPERCASE ("UST-CHORNA"). 
Using the *.title function make only the space divided settlements names correct.
However, there are hundreds of settlements have the dash symbol in their names.
Script hadles these occasions and changes "Ust-chorna" to "Ust-Chorna" in the separate field

Open the file from your QGIS Application

Created by Mykola Kozyr
13.07.2017
"""

from PyQt4.QtCore import QVariant

def settl_name_uppercase(feature):
    #define the field with raw values
    raw_name = feature.attribute("nameUA_new")
    #split features with the dash symbol
    split_list = raw_name.split('-')
    if len(split_list) > 3:
        print raw_name #no such values
        return raw_name
    elif len(split_list) == 3:
        name_new =  split_list[0].title() + '-' + split_list[1] + '-' + split_list[2].title()
        return name_new
    elif len(split_list) == 2:
        name_new =  split_list[0][0].title() + split_list[0][1:] + '-' + split_list[1][0].title()+split_list[1][1:]
        return name_new
    elif len(split_list) == 1:
        name_new = raw_name
        return name_new

def add_field(layer):
    #create new column
    layer.dataProvider().addAttributes([QgsField("nameUA_upd", QVariant.String)])
    layer.updateFields()
    
    #add values to new column
    with edit(layer):
        idx = layer.fieldNameIndex( "nameUA_upd" )
        for f in layer.getFeatures():
            print settl_name_uppercase(f) #printing features just for seeing the progress. Recommended to remove this string
            f[idx] = settl_name_uppercase(f)
            layer.updateFeature(f)

#change the layer path
layer = QgsVectorLayer("pathtoyourdata/settl_upd.shp", "settl_upd", "ogr")

add_field(layer)