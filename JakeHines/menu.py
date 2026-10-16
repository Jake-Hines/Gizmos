import nuke
import os

HERE = os.path.dirname(os.path.abspath(__file__))
nuke.pluginAddPath(os.path.join(HERE, "icons"))

toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Jake Hines", icon="Jake_Hines_Icon.png")

m.addCommand("AutoKey_Keymix", "nuke.createNode(\"AutoKey_Keymix\")", icon="AutoKey_Keymix_Icon.png")
