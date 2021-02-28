import bpy

from bpy.types import Panel
from bpy.props import BoolProperty
from math import (radians, degrees)

# ------------------------------------------------------------------------
#    Panel
# ------------------------------------------------------------------------

class ROBOT_PT_tx60(bpy.types.Panel):
    bl_label = "TX60 panel"
    bl_idname = "ROBOT_PT_tx60control"
    bl_category = "TX60 CONTROL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    degrees: BoolProperty()

    @classmethod
    def poll(cls, context):
        return bpy.data.objects['staubliTX60']

    def draw(self, context):

        global connected

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False # True to show "add keyframe dot · "

        robot = bpy.data.objects['staubliTX60']
        controls = bpy.context.scene.controls


        # layout.prop(self, "degrees", text="r/d")

        layout.prop(controls, "ik_control", text="fk/IK", icon="CON_SPLINEIK")
        box=layout.box()
        s = box.split(factor=0.3)
        c1 = s.column()
        c1.alignment = 'RIGHT'
        for i in range(6):
            c1.label(text="joint" + str(i+1) + "  :  ")
        c2 = s.column()
        c2.label(text=str(degrees(controls.j1)))
        c2.label(text=str(degrees(controls.j2)))
        c2.label(text=str(degrees(controls.j3)))
        c2.label(text=str(degrees(controls.j4)))
        c2.label(text=str(degrees(controls.j5)))
        c2.label(text=str(degrees(controls.j6)))
        # c2.label(text=str((controls.j1)))
        # c2.label(text=str((controls.j2)))
        # c2.label(text=str((controls.j3)))
        # c2.label(text=str((controls.j4)))
        # c2.label(text=str((controls.j5)))
        # c2.label(text=str((controls.j6)))
        layout.operator("robot.reset")
        layout.separator()
        layout.separator()

        # if connected==True :
        layout.prop(controls, "speed", text="overall speed [0 - 1]")
        layout.operator("ros.action")
        layout.separator()
        layout.separator()

        box=layout.box()
        s = box.split(factor=0.7)
        c1 = s.column()
        c1.alignment = 'RIGHT'
        # c1.label(text = "ip")
        c1.prop(controls, "ip_address", text="ip address")
        c2 = s.column()
        # c2.label(text="port")
        c2.prop(controls, "ip_port", text="ip port")
        layout.operator("ros.connect")
