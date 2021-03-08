import bpy
import time

from bpy.types import Operator

# try: import roslibpy
# except: print("roslibpy did not load")

import roslibpy

# ------------------------------------------------------------------------

#    Operators
# ------------------------------------------------------------------------
# def Stream():
#     c=bpy.context.scene.controls
#
#     print("ip " + c.ip_address)
#     print("port " + c.ip_port)
#
#
#     client = roslibpy.Ros(host='localhost', port=9090)
#     client.run()
#     publisher = roslibpy.Topic(client, '/arm_controller/command', 'trajectory_msgs/JointTrajectory')
#
#     now_sec = client.get_time().to_sec()
#     pos = [[1.57,0,0,0,0,0], [1.57,1.57,0,0,0,0], [1.57,1.57,1.57,0,0,0]]
#
#     if client.is_connected:
#         for i in range(3):
#             print('Sending message...' + str(i))
#
#             msg = dict(header=roslibpy.Header(seq=i, stamp=roslibpy.Time(now_sec+i, 0), frame_id=''), #roslibpy.Time.now()
#                        joint_names=['joint_1','joint_2','joint_3','joint_4', 'joint_5', 'joint_6'],
#                        points=[dict(
#                                     positions=pos[i],
#                                     #velocities=[1,1,1,1,1,1],
#                                     #accelerations=[1,1,1,1,1,1],
#                                     # effort=[],
#                                     time_from_start=roslibpy.Time(now_sec+i+1, 0)
#                                     )
#                               ],
#                        )
#             publisher.publish(roslibpy.Message(msg))
#             time.sleep(1)
#     publisher.unadvertise()
#     client.terminate()


def Stream():
    c=bpy.context.scene.controls

    print("ip " + c.ip_address)
    print("port " + c.ip_port)


    client = roslibpy.Ros(host='localhost', port=9090)
    client.run()
    publisher = roslibpy.Topic(client, '/arm_controller/command', 'trajectory_msgs/JointTrajectory')

    now_sec = client.get_time().to_sec()
    pos = [[1.57,0,0,0,0,0], [1.57,1.57,0,0,0,0], [1.57,1.57,1.57,0,0,0]]

    if client.is_connected:
        for i in range(3):
            print('Sending message...' + str(i))

            msg = dict(header=roslibpy.Header(seq=i, stamp=roslibpy.Time(now_sec+i, 0), frame_id=''), #roslibpy.Time.now()
                       joint_names=['joint_1','joint_2','joint_3','joint_4', 'joint_5', 'joint_6'],
                       points=[dict(
                                    positions=pos[i],
                                    #velocities=[1,1,1,1,1,1],
                                    #accelerations=[1,1,1,1,1,1],
                                    # effort=[],
                                    time_from_start=roslibpy.Time(now_sec+i+1, 0)
                                    )
                              ],
                       )
            publisher.publish(roslibpy.Message(msg))
            time.sleep(1)
    publisher.unadvertise()
    client.terminate()

class ROS_OT_stream(Operator):
    bl_label = "stream trajectory"
    bl_idname = "ros.stream"
    bl_description = "play and stream joint angles"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        print("streaming!")
        Stream()
        return {'FINISHED'}
