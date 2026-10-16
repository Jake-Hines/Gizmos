import nuke
import os

toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Jake Hines", icon="Jake_Hines_Icon.png")

m.addCommand("AutoKey_Keymix", "nuke.createNode(\"AutoKey_Keymix\")", icon="AutoKey_Keymix_Icon.png")
