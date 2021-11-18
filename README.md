# ros_bag_to_file
Python script to extract images and laser scans from a rosbag and save them as individual files.


USAGE:

Arguments:

-bag_file: (Relative) Path to bag file from which you wish to extract.
-output_dirs: (Abolute) Directories in which you wish to write images / scans, there must be one for each topic. N.B. you cannot write two different image topic to the same directory as it is impossible to use the topic name as the base name for files as ROS topics include '/' which is an invalid character for file names.
-input_topics: List of topics you would like to extract
-topic_type: List of same length as -input_topics specifiying whether each topic is either an image (0) or laser scan (1)

Example:
python bag_to_images.py 2021-11-04-11-09-25.bag output_dirs /home/james/right /home/james//left /home/james/scans input_topics /stereo/right/image_raw /stereo/left/image_raw /rslidar_points topic_type 0 0 1

This will write all of the messages contained in topics /stereo/right/image_raw, /stereo/left/image_raw and /rslidar_points to the corresponding /left/, /right/ and /scans directories. 
