This program will take the situation from http://rotorheads.ddns.net/ and make it available to the ingame Ka-50 ABRIS system

Instructions:
1. Unpack this zip to your "saved games/DCS" folder (there should exist a "saved games/DCS/RotorheadToABRIS" folder
2. open file <DCS install directory>/Mods/aircraft/Ka-50/Cockpit/Scripts/Devices_specs/ABRIS.lua
3. go to the line "default_path = get_terrain_related_data("ABRIS_data_path")" (line 42 as of writing)
4. to that line, append:
 or lfs.writedir().."RotorheadToABRIS/"
5. run the RotorheadToABRIS.exe program each time you want to update, doing this creates a Database folder

Note:
* This does not take into account what mission you're actually running, ie all Ka-50 missions will get rotorheads data in them unless you restore the lua or delete the Database folder.
* The game will load the ABRIS data when the Ka-50 module is loaded (Th first time it is entered in a mission)

Modifying output:
The application can be supplied various arguments to modify the result

    -nocsar Removes csar symbols
    -noobj Removes objective markers
    -nosam Removes the sam markers
    -nofarp Removes farp markers (the ones added by the game still remains)
    -nojtac Removes jtac symbols
