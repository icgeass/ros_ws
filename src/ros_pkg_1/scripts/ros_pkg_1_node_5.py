#! /usr/bin/env python

import rospy
import actionlib
import time

from ros_pkg_1.msg import *
from std_msgs.msg import *

ros_pkg_1_node_5_log_prefix = 'ros_pkg_1_node_5'

wait_seconds = 0.0

all_wait_seconds = 10


class DoDishesServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, self.execute, False)
        self.server.start()

    def execute(self, goal):
        # Do lots of awesome groundbreaking robot stuff here
        rospy.loginfo('%s receive dishwasher_id=%s', ros_pkg_1_node_5_log_prefix,
                      self.server.current_goal.get_goal().dishwasher_id)
        global wait_seconds
        while wait_seconds != all_wait_seconds:
            wait_seconds = wait_seconds + 1
            time.sleep(0.5)
            self.server.publish_feedback(DoDishesFeedback(percent_complete=wait_seconds / all_wait_seconds * 100))
        rospy.loginfo('%s actionlib execute completed!', ros_pkg_1_node_5_log_prefix)
        self.server.set_succeeded(result=DoDishesResult(total_dishes_cleaned=wait_seconds), text='all dishes done!')

    def processing(self):
        return wait_seconds


if __name__ == '__main__':
    rospy.init_node('do_dishes_server')
    server = DoDishesServer()
    rospy.loginfo('%s Ready!', ros_pkg_1_node_5_log_prefix)
    rospy.spin()
