import bpy
from math import (radians, degrees)

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

from bpy.types import Operator

# ------------------------------------------------------------------------
#    Handlers
# ------------------------------------------------------------------------

def JointsHandler(scene):
    controls = bpy.context.scene.controls

    if bpy.context.scene.controls.ik_control:
        # get join rotations in inverse kinematics mode
        b0 = bpy.data.objects['staubliTX60'].pose.bones["base_link"]
        b1 = bpy.data.objects['staubliTX60'].pose.bones["joint_1"]
        b2 = bpy.data.objects['staubliTX60'].pose.bones["joint_2"]
        b3 = bpy.data.objects['staubliTX60'].pose.bones["joint_3"]
        b4 = bpy.data.objects['staubliTX60'].pose.bones["joint_4"]
        b5 = bpy.data.objects['staubliTX60'].pose.bones["joint_5"]
        b6 = bpy.data.objects['staubliTX60'].pose.bones["joint_6"]

        controls.j1 = degrees((b0.matrix.inverted()@b1.matrix).to_euler()[1])
        controls.j2 = degrees((b1.matrix.inverted()@b2.matrix).to_euler()[2])
        controls.j3 = degrees((b2.matrix.inverted()@b3.matrix).to_euler()[2])
        controls.j4 = degrees((b3.matrix.inverted()@b4.matrix).to_euler()[1])
        controls.j5 = degrees((b4.matrix.inverted()@b5.matrix).to_euler()[2])
        controls.j6 = degrees((b5.matrix.inverted()@b6.matrix).to_euler()[1])
        #print("IK > j1: "+str(j1)+"     j2: "+str(j2)+"     j3: "+str(j3)+"     j4: "+str(j4)+"     j5: "+ str(j5)+"     j6: "+str(j6))

    else:
        # get join rotations in fordware kinematics mode
        controls.j1 = degrees(bpy.data.objects['staubliTX60'].pose.bones["joint_1"].matrix_basis.to_euler()[1])
        controls.j2 = degrees(bpy.data.objects['staubliTX60'].pose.bones["joint_2"].matrix_basis.to_euler()[2])
        controls.j3 = degrees(bpy.data.objects['staubliTX60'].pose.bones["joint_3"].matrix_basis.to_euler()[2])
        controls.j4 = degrees(bpy.data.objects['staubliTX60'].pose.bones["joint_4"].matrix_basis.to_euler()[1])
        controls.j5 = degrees(bpy.data.objects['staubliTX60'].pose.bones["joint_5"].matrix_basis.to_euler()[2])
        controls.j6 = degrees(bpy.data.objects['staubliTX60'].pose.bones["joint_6"].matrix_basis.to_euler()[1])
        #print("FK > j1: "+str(j1)+"     j2: "+str(j2)+"     j3: "+str(j3)+"     j4: "+str(j4)+"     j5: "+ str(j5)+"     j6: "+str(j6))


class ROBOT_OT_reset(Operator):
    bl_label = "rest position"
    bl_idname = "robot.reset"
    bl_description = "restore rest position set all the joints to zero"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        controls = context.scene.controls
        robot = bpy.data.objects['staubliTX60']

        if not controls.ik_control:
            print("ik not enabled")
            robot.pose.bones["joint_1"].rotation_euler[1] = 0
            robot.pose.bones["joint_2"].rotation_euler[2] = 0
            robot.pose.bones["joint_3"].rotation_euler[2] = 0
            robot.pose.bones["joint_4"].rotation_euler[1] = 0
            robot.pose.bones["joint_5"].rotation_euler[2] = 0
            robot.pose.bones["joint_6"].rotation_euler[1] = 0
        else:
            print("ik is enabled")

        return {'FINISHED'}
