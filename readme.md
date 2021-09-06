## Rotorhead to ABRIS
Rotorhead to ABRIS is an application that will read the current state of the Rotorheads DCS [dynamic server](http://rotorheads.ddns.net/) and imports that data into the Ka-50's ABRIS system.
![ABRIS](https://user-images.githubusercontent.com/5412638/125851711-176c6035-4881-4440-a1ed-b298f235beb6.png)

Information such as disposition of friendly and hostile troops, enemy AA batteries, JTAC locations et.c is available. In the Russian fashion, blue denotes hostile and red friendlies.

### Usage
1. Go to The [release page](https://github.com/gronank/RotorheadToABRIS/releases) to get the latest version of the application
2. Unpack the zip into your saved games/DCS directory (You should end up with a RotorheadsToABRIS folder in your DCS directory)
3. Open the file \<DCS install directory\>/Mods/aircraft/Ka-50/Cockpit/Scripts/Devices_specs/ABRIS.lua
4. Go to the line **default_path = get_terrain_related_data("ABRIS_data_path")** (line 42 as of writing) and replace it with **default_path = get_terrain_related_data("ABRIS_data_path") or lfs.writedir().."RotorheadToABRIS/"**
5. Run the RotorheadsToABRIS.exe inside the newly unpacked folder. A Database folder will appear. Running the application again updates the data available to ABRIS

### Notes
* This does not take into account what mission you're actually running. All Ka-50 missions will show the rotorheads data unless you restore the lua or delete the Database folder.
* The database will be loaded when the module is first loaded, i.e. when you first enter the Ka-50 slot.

### Command line arguments
The application can be supplied various arguments to modify the result
* **-nocsar** Removes csar symbols
* **-noobj** Removes objective markers
* **-nosam** Removes the sam markers
* **-nofarp** Removes farp markers (the ones added by the game still remains)
* **-nojtac** Removes jtac symbols
