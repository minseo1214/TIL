#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include<turtlesim/Pose.h>
#include <std_msgs/String.h>
#include <std_msgs/Float64.h>

using namespace std;

ros::Publisher vel_pub;
ros::Subscriber pose_sub;
turtlesim::Pose turtlesim_pose;

int stop=0;

void move(double speed, double distance, bool isForward);
void chatterCallback(const std_msgs::Float64::ConstPtr& msg);
void poseCallback(const turtlesim::Pose::ConstPtr & pose_message);

int main(int argc, char **argv){
	ros::init(argc, argv, "turtlesim_move_straight");
	ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("dis_chatter", 1000, chatterCallback);
	vel_pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);
	pose_sub = nh.subscribe("/turtle1/pose", 10, poseCallback);
	ROS_INFO("---STARTING----\n");
	move(0.3, 3, 1);
    //speed distance isForward
	ros::Rate loop_rate(10);
	loop_rate.sleep();
	ros::spin();
	return 0;
}

void chatterCallback(const std_msgs::Float64::ConstPtr& msg)
{
  ROS_INFO("I heard: [%f]", msg->data);
  ROS_INFO("stop: [%d]", stop);
  if((msg->data)<30){
    stop=1;
    move(0.3, 3, 1);
  }
  else{
    stop=0;
    move(0.3, 3, 1);
  }
}


void move(double speed, double distance, bool isForward){
	geometry_msgs::Twist vel_msg;
	if(isForward){
		vel_msg.linear.x = abs(speed);
	}
	else
		vel_msg.linear.x = -abs(speed);
    
	double current_distance = 0.0;
	double t0 = ros::Time::now().toSec();
	ros::Rate rate(100);
	while (!stop){
		vel_pub.publish(vel_msg);
		double t1 = ros::Time::now().toSec();
		current_distance = speed * (t1 - t0);
		ros::spinOnce();
		rate.sleep();
	}
	vel_msg.linear.x = 0.0;
	vel_pub.publish(vel_msg);
}

void poseCallback(const turtlesim::Pose::ConstPtr & pose_message){
	turtlesim_pose.x = pose_message -> x;
	turtlesim_pose.y = pose_message -> y;
	turtlesim_pose.theta = pose_message -> theta;
}
