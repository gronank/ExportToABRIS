## Rotorhead to ABRIS
### Run script
* Create a dirctory
* Run the RotorheadsToABRIS script, give the created directory as argument. You may need to surround your arguments with "" if it contains whitespaces. Without argument the working directory is used
* Running the script creates a Database folder in your selected directory containing the files ADDITIONAL.lua and NAVIGATION.lua
### Setup Dcs
* Open the file <Dcs Install directory>/Mods/aircraft/Ka-50/Cockpit/Scripts/Devices_specs/ABRIS.lua
* Go to the line default_path = get_terrain_related_data("ABRIS_data_path")
* Append "or <path to directory containing the Database folder>", remember that only forward slashes can be used.
