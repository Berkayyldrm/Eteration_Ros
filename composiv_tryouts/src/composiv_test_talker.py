#!/usr/bin/env python

import unittest
from std_msgs.msg import String
import time
import rostest
import rospy

class TalkerTestCase(unittest.TestCase):
    check_talker = False
    
    def callback(self, data):
        self.check_talker = True

    def test_talker(self):
        rospy.init_node("test_talker")
        rospy.Subscriber("Topic", String, self.callback)

        counter = 0
        while not rospy.is_shutdown() and counter < 5 and (not self.check_talker):
            time.sleep(1)
            counter += 1

        self.assertTrue(self.check_talker)

if __name__ == "__main__":
    rostest.rosrun("compolsiv_tryouts", "composiv_test_talker", TalkerTestCase)