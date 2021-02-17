# blendeRos

blendeRos is a blender addon to extract joint positions from a rigged/simulated robot 
wip: blenderROS is intended to feature a communication to ROS using roslibpy (and rosbridge_server)

---

the addon will insert a sidebar panel (shortcut 'N') where IK can be enabled dissabled
joint positions can be visualized in both modes in degrees
there is a 'reset to rest position' and a strem button to trigger the streaming operator

the streaming funcionality uses roslibpy 1.2.0, which has to be installed 
 * either using blenders bundles python (using pip)
 * removing blender's python and using system's python (untested)

---

TODO

currently the addon looks for a specific model (staubli's tx60)
currently the streaming functionality is a stub
tx60 streaming to ROS is not supported by the [staubli_val3_driver](http://wiki.ros.org/staubli_val3_driver) so a followJointTrajectoryGoal action interface is being developed

---

a blender demo file is included. the file contains a tx60 rigged module with the iTaSC solver configured
limits are not set but can easily set up under bone constrains
