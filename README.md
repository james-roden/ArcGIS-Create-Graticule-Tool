# ArcGIS-Create-Graticule-Tool
*Written by James M Roden*

An ArcGIS tool that uses the users current MXD dataview extent to create a graticule at a specified interval of their desired degrees, minutes, seconds.

[DOWNLOAD](https://github.com/GISJMR/ArcGIS-Create-Graticule-Tool/raw/master/ArcGIS-Create-Graticule.zip)

<div>
<img style="float;" right src="https://github.com/GISJMR/ArcGIS_Create_Graticule_Tool/blob/master/imgs/Map.png" alt="Map" width="250" height="250">
<img style="float;" src="https://github.com/GISJMR/ArcGIS_Create_Graticule_Tool/blob/master/imgs/Map_Grat_WGS84.png" alt="Map" width="250" height="250">
<img style="float;" src="https://github.com/GISJMR/ArcGIS_Create_Graticule_Tool/blob/master/imgs/Map_Grat_UTM36N.png" alt="Map" width="250" height="250">
</div>

*(Left)Initial map extent. (Centre)15 minute (0° 15" 0') created graticule in WGS84 data frame. (Right)The same graticule in UTM36N data frame.*

## Methodology
* Extract extent, lower left, and upper right from MapDocument objects active data frame
* Construct coordinate variables using previous step outputs for Fishnet tool
* Run Fishnet tool to create grid
* Run 2 codeblock functions to label each line either latitude or longitude, and include degrees and direction
* Finally densify so there are enough intermediate vertices to allow graticule lines to 'curve' when projected
