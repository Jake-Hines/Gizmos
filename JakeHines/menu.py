import nuke
import os

toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Jake Hines", icon="Jake_Hines_Icon.png")

m.addCommand("AutoKey_Merges", "nuke.createNode(\"AutoKey_Merges\")", icon="AutoKey_Merges_Icon.png")
