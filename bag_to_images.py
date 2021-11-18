#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2016 Massachusetts Institute of Technology

"""Extract images from a rosbag.
"""

import os
import argparse

import cv2

import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from sensor_msgs.msg import PointCloud2
import pypcd
import rospy
import sensor_msgs.point_cloud2 as pc2



def save_img(msg, output_dir, counter):
    cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
    cv2.imwrite(os.path.join(output_dir, "image%06i.png" % counter), cv_img)

def save_scan(msg, output_dir, counter):
    pc = pypcd.PointCloud.from_msg(msg)
    pc.save(os.path.join(output_dir, "points%06i" % count))

def main():
    """Extract a folder of images from a rosbag.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file", help="Input ROS bag.")
    parser.add_argument("-output_dirs",  nargs='+', help="Output directories.")
    parser.add_argument("-input_topics", nargs='+', help="Topics to save.")
    parser.add_argument("-topic_type", nargs='+', help="Type of topics specified in ""input_topics"". 0 = image, 1 = laser_scan")

    args = parser.parse_args()


    topic_counter = [0] * len(args.input_topics)

    counter_dict = dict(zip(args.input_topics, topic_counter))

    bag = rosbag.Bag(args.bag_file, "r")
    #bridge = CvBridge()
    count = 0

    for topic, msg, time in bag.read_messages(topics=args.input_topics):
        #print topic 
        
        for (t, t_type, out_dir) in zip(args.input_topics, args.topic_type, args.output_dirs):
            if topic == t:
                if int(t_type) == 0:
                    save_img(msg, out_dir, counter_dict[t])
                    print "Written topic " + t + " " + str(counter_dict[t])
                if t_type == 1:
                    save_scan(msg, out_dir, counter_dict[t])
                counter_dict[t] += 1

    bag.close()


    return

if __name__ == '__main__':
    bridge = CvBridge()
    main()
