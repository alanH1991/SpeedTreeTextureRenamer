How to run:
- Make sure all files are stored in the same directory.
- Launch SpeedTreeTextureRenamer_MASTER_v001.py and the tool should work.

Why I made this tool:
This tool will open the stmat file (XML format) and referances the textures it needs to rename. It will edit both the texture fil and the stmat so that the nameing lines up.
This will make the import to applications like Houdini simpler when using the speedtree otl.

What Do the other files do:
strUi.py is the the ui that the "Master" files referances.
If you want to edit the UI in QtDesigner the orginal .ui file is included.
The png image is used in the header for the tool in the ui.

Other things:
python Libaries used:
- sys
- os
- glob (eventually remove the need for this)
- re
- shutil
- ElementTree


