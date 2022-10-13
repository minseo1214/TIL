#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include<turtlesim/Pose.h>
#include <sensor_msgs/Range.h>

using namespace std;

ros::Publisher vel_pub;
ros::Subscriber pose_sub;
turtlesim::Pose turtlesim_pose;

class range_HC{
    private:
        double speed=0.3;
        double distance=5;
        double isForward=1;
        int stop=0;
        double angle_radian=5;
	    double angular_speed=50;
	    bool direction=1;
        double current_distance = 0.0;
        double current_angle = 0.0;
    public:
        void move(double speed, double distance, bool isForward);
        void poseCallback(const turtlesim::Pose::ConstPtr & pose_message);
        void rangecallback(const sensor_msgs::Range::ConstPtr& msg);
        

};

void range_HC::rangecallback(const sensor_msgs::Range::ConstPtr& msg){
    ROS_INFO("I heard: [%f]", msg->range);
    ROS_INFO("stop: [%d]", stop);
    if((msg->range)<0.4){
        stop=1;
        move(speed, distance,isForward);
    }
    else{
        stop=0;
        move(speed, distance, isForward);
    }
}

void range_HC::move(double speed, double distance, bool isForward){
	geometry_msgs::Twist vel_msg;
    if(isForward){
	   	vel_msg.linear.x = abs(speed);
    }
   	else
        vel_msg.linear.x = -abs(speed);

    
    double t0 = ros::Time::now().toSec();
    ros::Rate rate(100);

    while (!stop){
       	vel_pub.publish(vel_msg);
       	double t1 = ros::Time::now().toSec();
        ROS_INFO("distance: [%f]", current_distance);
       	current_distance += speed * (t1 - t0);
       	ros::spinOnce();
       	rate.sleep();
        if(current_distance>distance){
            geometry_msgs::Twist vel_msg;
		    vel_msg.angular.z = abs(angular_speed);
	        
	        double t0 = ros::Time::now().toSec();
	        ros::Rate loop_rate(100);
	        while (current_angle < angle_radian){
		        vel_pub.publish(vel_msg);
		        double t1 = ros::Time::now().toSec();
		        current_angle += angular_speed * (t1 - t0);
                ROS_INFO("current: [%f]", current_angle*180/3.14 );
		        ros::spinOnce();
		        loop_rate.sleep();
                current_distance=0.0;
                
	        }
        }
        current_angle=0.0;
       }
    vel_msg.angular.z = 0.0;
	vel_pub.publish(vel_msg);
    vel_msg.linear.x = 0.0;
    vel_pub.publish(vel_msg);
}

void range_HC::poseCallback(const turtlesim::Pose::ConstPtr & pose_message){
    turtlesim_pose.x = pose_message -> x;
    turtlesim_pose.y = pose_message -> y;
    turtlesim_pose.theta = pose_message -> theta;
}

int main(int argc, char **argv){
    ros::init(argc, argv, "range_test");
	ros::NodeHandle nh;
    range_HC turtle;
    
    ros::Subscriber range_sub = nh.subscribe("rangeSonar",1000,&range_HC::rangecallback, &turtle);
    vel_pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);
	pose_sub = nh.subscribe("/turtle1/pose", 10, &range_HC::poseCallback, &turtle);
    ROS_INFO("---STARTING----\n");

	turtle.move(0.3, 3, 1);
	ros::Rate loop_rate(10);
	loop_rate.sleep();
	ros::spin();
	return 0;
}
//make_stars
