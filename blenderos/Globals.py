import bpy

from bpy.props import (BoolProperty,
                       FloatProperty,
                       StringProperty
                       )

from bpy.types import PropertyGroup

# ------------------------------------------------------------------------
#    Data structures
# ------------------------------------------------------------------------

class Controls(PropertyGroup):
    def updateik(self, context):
        bpy.data.objects['staubliTX60'].pose.bones['joint_6'].constraints['IK'].mute = not self.ik_control
        print("todo: copy slf.jX rotations to bone angles when exiting IK to mimin in FK")

    ik_control: BoolProperty(
        name="set ik",
        description="set ik control",
        default = True,
        update=updateik
        )

    j1: FloatProperty(
        name="j1",
        description="j1 rotation",
        default = 0,
        )
    j2: FloatProperty(
        name="j2",
        description="j2 rotation",
        default = 0,
        )
    j3: FloatProperty(
        name="j3",
        description="j3 rotation",
        default = 0,
        )
    j4: FloatProperty(
        name="j4",
        description="j4 rotation",
        default = 0,
        )
    j5: FloatProperty(
        name="j5",
        description="j5 rotation",
        default = 0,
        )
    j6: FloatProperty(
        name="j6",
        description="j6 rotation",
        default = 0,
        )

    ip_address: StringProperty(
        name="ip",
        description="websocket ip",
        default = "localhost",
        )
    ip_port: StringProperty(
        name="port",
        description="websocket port",
        default = "9090",
        )
