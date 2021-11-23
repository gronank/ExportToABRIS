## Export to ABRIS
Export to ABRIS is an application that will read the current state of a DCS server such Rotorheads [dynamic server](http://rotorheads.ddns.net/) and imports that data into the Ka-50's ABRIS system.
![ABRIS](https://user-images.githubusercontent.com/5412638/125851711-176c6035-4881-4440-a1ed-b298f235beb6.png)

Information such as disposition of friendly and hostile troops, enemy AA batteries, JTAC locations et.c is available. In the Russian fashion, blue denotes hostile and red friendlies.

### Usage
1. Go to The [release page](https://github.com/gronank/RotorheadToABRIS/releases) to get the latest version of the application
2. Unpack the zip into your saved games/DCS directory (You should end up with a RotorheadsToABRIS folder in your DCS directory)
3. Open the file \<DCS install directory\>/Mods/aircraft/Ka-50/Cockpit/Scripts/Devices_specs/ABRIS.lua
4. Go to the line **default_path = get_terrain_related_data("ABRIS_data_path")** (line 42 as of writing) and replace it with **default_path = get_terrain_related_data("ABRIS_data_path") or lfs.writedir().."ExportToABRIS/"**
5. Run the ExportToABRIS.exe inside the newly unpacked folder by dragging and dropping a serverspec.json file onto the exe. A Database folder will appear. Running the application again updates the data available to ABRIS.

### Notes
* This does not take into account what mission you're actually running. All Ka-50 missions will show data from the exported server unless you restore the lua or delete the Database folder.
* The database will be loaded when the module is first loaded, i.e. when you first enter the Ka-50 slot.
* It is possible to create a shortcut and supply it with command line arguments and the path to your favourite serverspec for ease of use. Dropping a serverspec on a shortcut with command arguments works equally well.

### Command line arguments
The application can be supplied various arguments to modify the result
* **-nocsar** Removes csar symbols
* **-noobj** Removes objective markers
* **-nosam** Removes the sam markers
* **-nofarp** Removes farp markers (the ones added by the game still remains)
* **-nojtac** Removes jtac symbols

### Custom visualization and servers
Export To Abris reads mapbox features from json and converts them to a format readable by DCS. This is defined by serverspec files.
The serverspec files are simple json objects with the following properties.

* **server**: Url to the server from which data is retrieved.
* **dataSources**: A dictionary mapping data source names to the underlying data json path. Path is concatinated with the server url.
* **points**: A list of objects that will be rendered as points. A point object is defined as follows:
  * **sources**: A list of source names reffering to the names in dataSources.
  * **condition**: An object using regexp to determine if a particular feature will we drawn with this symbol. A condition has the following properties:
    * **property**: The name of the property whose value will be matched against.
    * **pattern**: The regex pattern used to match the property value.
  * **symbolType**: The name of the symbol used to visualize the point. Can take any of the following values:
    * referencePoint
	* initialPoint  
	* landmark	  
	* obstacle	  
	* climbPoint	
	* divePoint	 
	* airbase	   
	* farp		  
	* navalbase	 
	* airport	   
	* heliport	  
	* closed_airport
	* common_airport
	* new_airport   
	* vorPoint	   
	* dmePoint	   
	* tacanPoint	 
	* homerPoint	 
	* vorDmePoint	
	* vorTacanPoint  
	* airportHomer   
	* routeMarker	
	* ilsMarker	  
	* unknownHostile 
	* armouredHostile
	* airDefenceHostile
	* otherHostile   
	* dlInitial	  
	* groupMember
  * **name**: An object containing Regex match and replace pattern to set the name of the point visible in ABRIS. Has the following properties:
    * **property**: The name of the property whose value will be matched against.
    * **pattern**: The regex pattern used to match the property value.
    * **replace**: Constructs the string using the parts captured by the pattern.
  * **disable**: The keyword used to disable exporting this particular symbol. Must be listed in disableCategories.json.
* **bufferZones**: A list of buffer zone object. A buffer zone draws an outline around the given point at some distance. The object is defined as follows:
  * **style**: The style of the buffer zone, can take values either "filledHostile" or "line"
  * **color**: The color if the line style is used. Can take "r,g,b" where r, g, and b are color components 0-255 or any of the following values
    * red
    * yellow
    * green
    * white
    * black 
  * **sources**: See above.
  * **condition**: See above.
  * **disable**: See above.
* **lines**: A list of line objects. A line object traces the shortest possible line between point features with the same name (as determined by the name property). The object is defines as follows:
  * **color**: See above.
  * **name**: See above.
  * **sources**: See above.
  * **condition**: See above.
  * **disable**: See above.


