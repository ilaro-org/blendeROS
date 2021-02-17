'''
BlendeRos allows to simulte a 6dof serial link robot.
This addon uses the iTaSC IK solver and roslibpy to interface to ros
------------------------------------------------------------------------------

Design and developed by Pratipo Instruments / ilaro.org
Inpired by the ideas and work Alex Rössler https://machinekoder.com/
------------------------------------------------------------------------------

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "BlendeRos",
    "author": "info @ ilaro.org",
    "version": (0, 1),
    "blender": (2, 83, 0),
    "location": "View3D > Sidebar > tx60",
    "description": "tx60 control and stream to ROS",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"}


import bpy
from bpy.utils import (register_class, unregister_class)
from bpy.props import PointerProperty

from . Globals import Controls
from . Robot_Joints import JointsHandler
from . Robot_Joints import ROBOT_OT_reset
from . Stream import ROS_OT_stream
from . Stream import Stream
from . Panel import ROBOT_PT_tx60


# ------------------------------------------------------------------------
#    un/register
# ------------------------------------------------------------------------
classes = (
    Controls,
    ROBOT_PT_tx60,
    ROBOT_OT_reset,
    ROS_OT_stream,
)

def register():
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.controls = PointerProperty(type=Controls)

    bpy.app.handlers.depsgraph_update_post.append(JointsHandler)

def unregister():

    bpy.app.handlers.depsgraph_update_post.remove(JointsHandler)

    del bpy.types.Scene.controls

    for cls in reversed(classes):
        unregister_class(cls)
