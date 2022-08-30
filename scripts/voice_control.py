#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    global pub, order
    rospy.loginfo(msg.data)
    if "hey spot" in msg.data.lower() and "fetch me" in msg.data.lower():
        order_start = msg.data.index("fetch me")
        order = msg.data[order_start + 9:]
        pub.publish("Fetching " + order)

def talker():
    global pub

    rospy.init_node("spot_voice_control", anonymous=True)
    pub = rospy.Publisher("speak", String, queue_size=10)
    rospy.Subscriber("final", String, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
