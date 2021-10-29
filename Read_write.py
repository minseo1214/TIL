import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import *                    # Uses Dynamixel SDK library

# Control table address
ADDR_MX_TORQUE_ENABLE      = 24             # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION      = 30
ADDR_MX_PRESENT_POSITION   = 36

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel


# Default setting
DXL1_ID                     = 3                 # Dynamixel#1 ID : 1
DXL2_ID                     = 4                 # Dynamixel#1 ID : 2

DXL3_ID                     = 6                 # Dynamixel#1 ID : 1
DXL4_ID                     = 7                 # Dynamixel#1 ID : 2

DXL5_ID                     = 9                 # Dynamixel#1 ID : 1
DXL6_ID                     = 10                 # Dynamixel#1 ID : 2

DXL7_ID                     = 1                 # Dynamixel#1 ID : 1
DXL8_ID                     = 8                 # Dynamixel#1 ID : 2

DXL9_ID                     = 2                 # Dynamixel#1 ID : 1
DXL10_ID                     = 5 
BAUDRATE                    = 1000000             # Dynamixel default baudrate : 57600
DEVICENAME                  = '/dev/ttyACM0'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
DXL1_MINIMUM_POSITION_VALUE  = 600           # Dynamixel will rotate between this value
DXL1_MAXIMUM_POSITION_VALUE  = 700            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL2_MINIMUM_POSITION_VALUE  = 350           # Dynamixel will rotate between this value
DXL2_MAXIMUM_POSITION_VALUE  = 450            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL3_MINIMUM_POSITION_VALUE  = 500          # Dynamixel will rotate between this value
DXL3_MAXIMUM_POSITION_VALUE  = 400            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL4_MINIMUM_POSITION_VALUE  = 450           # Dynamixel will rotate between this value
DXL4_MAXIMUM_POSITION_VALUE  = 350            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL5_MINIMUM_POSITION_VALUE  = 340           # Dynamixel will rotate between this value
DXL5_MAXIMUM_POSITION_VALUE  = 440            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL6_MINIMUM_POSITION_VALUE  = 370           # Dynamixel will rotate between this value
DXL6_MAXIMUM_POSITION_VALUE  = 470            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL7_MINIMUM_POSITION_VALUE  = 780           # Dynamixel will rotate between this value
DXL7_MAXIMUM_POSITION_VALUE  = 680            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL8_MINIMUM_POSITION_VALUE  = 950           # Dynamixel will rotate between this value
DXL8_MAXIMUM_POSITION_VALUE  = 850            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL9_MINIMUM_POSITION_VALUE  = 500           # Dynamixel will rotate between this value
DXL9_MAXIMUM_POSITION_VALUE  = 500            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

DXL10_MINIMUM_POSITION_VALUE  = 520           # Dynamixel will rotate between this value
DXL10_MAXIMUM_POSITION_VALUE  = 520            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)


DXL1_MOVING_STATUS_THRESHOLD = 50                # Dynamixel moving status threshold
DXL2_MOVING_STATUS_THRESHOLD = 10                # Dynamixel moving status threshold

index = 0
dxl1_goal_position = [DXL1_MINIMUM_POSITION_VALUE, DXL1_MAXIMUM_POSITION_VALUE]         # Goal position
dxl2_goal_position = [DXL2_MINIMUM_POSITION_VALUE, DXL2_MAXIMUM_POSITION_VALUE]         # Goal position

dxl3_goal_position = [DXL3_MINIMUM_POSITION_VALUE, DXL3_MAXIMUM_POSITION_VALUE]         # Goal position
dxl4_goal_position = [DXL4_MINIMUM_POSITION_VALUE, DXL4_MAXIMUM_POSITION_VALUE]         # Goal position

dxl5_goal_position = [DXL5_MINIMUM_POSITION_VALUE, DXL5_MAXIMUM_POSITION_VALUE]         # Goal position
dxl6_goal_position = [DXL6_MINIMUM_POSITION_VALUE, DXL6_MAXIMUM_POSITION_VALUE]         # Goal position

dxl7_goal_position = [DXL7_MINIMUM_POSITION_VALUE, DXL7_MAXIMUM_POSITION_VALUE]         # Goal position
dxl8_goal_position = [DXL8_MINIMUM_POSITION_VALUE, DXL8_MAXIMUM_POSITION_VALUE]         # Goal position

dxl9_goal_position = [DXL9_MINIMUM_POSITION_VALUE, DXL9_MAXIMUM_POSITION_VALUE]         # Goal position
dxl10_goal_position = [DXL10_MINIMUM_POSITION_VALUE, DXL10_MAXIMUM_POSITION_VALUE]         # Goal position


# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel Torque
dxl1_comm_result, dxl1_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
dxl2_comm_result, dxl2_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)

dxl3_comm_result, dxl3_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
dxl4_comm_result, dxl4_error = packetHandler.write1ByteTxRx(portHandler, DXL4_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)

dxl5_comm_result, dxl5_error = packetHandler.write1ByteTxRx(portHandler, DXL5_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
dxl6_comm_result, dxl6_error = packetHandler.write1ByteTxRx(portHandler, DXL6_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)

dxl7_comm_result, dxl7_error = packetHandler.write1ByteTxRx(portHandler, DXL7_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
dxl8_comm_result, dxl8_error = packetHandler.write1ByteTxRx(portHandler, DXL8_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)

dxl9_comm_result, dxl9_error = packetHandler.write1ByteTxRx(portHandler, DXL9_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
dxl10_comm_result, dxl10_error = packetHandler.write1ByteTxRx(portHandler, DXL10_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)

if dxl1_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl1_comm_result))
elif dxl1_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl1_error))
else:
    print("Dynamixel has been successfully connected")

if dxl2_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl2_comm_result))
elif dxl2_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl2_error))
else:
    print("Dynamixel has been successfully connected")


if dxl3_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl3_comm_result))
elif dxl3_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl3_error))
else:
    print("Dynamixel has been successfully connected")

if dxl4_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl4_comm_result))
elif dxl4_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl4_error))
else:
    print("Dynamixel has been successfully connected")


if dxl5_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl5_comm_result))
elif dxl5_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl5_error))
else:
    print("Dynamixel has been successfully connected")

if dxl6_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl6_comm_result))
elif dxl6_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl6_error))
else:
    print("Dynamixel has been successfully connected")


if dxl7_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl7_comm_result))
elif dxl7_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl7_error))
else:
    print("Dynamixel has been successfully connected")

if dxl8_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl8_comm_result))
elif dxl8_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl8_error))
else:
    print("Dynamixel has been successfully connected")

if dxl9_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl9_comm_result))
elif dxl9_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl9_error))
else:
    print("Dynamixel has been successfully connected")

if dxl10_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl10_comm_result))
elif dxl10_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl10_error))
else:
    print("Dynamixel has been successfully connected")

while 1:
    #print("Press any key to continue! (or press ESC to quit!)")
    #if getch() == chr(0x1b):
    #    break

    # Write goal position
    dxl2_comm_result, dxl2_error = packetHandler.write2ByteTxRx(portHandler, DXL2_ID, ADDR_MX_GOAL_POSITION, dxl2_goal_position[index])
    dxl4_comm_result, dxl4_error = packetHandler.write2ByteTxRx(portHandler, DXL4_ID, ADDR_MX_GOAL_POSITION, dxl4_goal_position[index])
    dxl7_comm_result, dxl7_error = packetHandler.write2ByteTxRx(portHandler, DXL7_ID, ADDR_MX_GOAL_POSITION, dxl7_goal_position[index])
    dxl6_comm_result, dxl6_error = packetHandler.write2ByteTxRx(portHandler, DXL6_ID, ADDR_MX_GOAL_POSITION, dxl6_goal_position[index])
    time.sleep(0.2)
    dxl1_comm_result, dxl1_error = packetHandler.write2ByteTxRx(portHandler, DXL1_ID, ADDR_MX_GOAL_POSITION, dxl1_goal_position[index])
    dxl3_comm_result, dxl3_error = packetHandler.write2ByteTxRx(portHandler, DXL3_ID, ADDR_MX_GOAL_POSITION, dxl3_goal_position[index])
    dxl8_comm_result, dxl8_error = packetHandler.write2ByteTxRx(portHandler, DXL8_ID, ADDR_MX_GOAL_POSITION, dxl8_goal_position[index])
    dxl5_comm_result, dxl5_error = packetHandler.write2ByteTxRx(portHandler, DXL5_ID, ADDR_MX_GOAL_POSITION, dxl5_goal_position[index])
    time.sleep(0.2)
    
    dxl9_comm_result, dxl9_error = packetHandler.write2ByteTxRx(portHandler, DXL9_ID, ADDR_MX_GOAL_POSITION, dxl9_goal_position[index])
    dxl10_comm_result, dxl10_error = packetHandler.write2ByteTxRx(portHandler, DXL10_ID, ADDR_MX_GOAL_POSITION, dxl10_goal_position[index])
    if dxl1_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl1_comm_result))
    elif dxl1_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl1_error))
    if dxl2_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl2_comm_result))
    elif dxl2_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl2_error))

    if dxl3_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl3_comm_result))
    elif dxl3_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl3_error))
    if dxl4_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl4_comm_result))
    elif dxl4_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl4_error))

    if dxl5_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl5_comm_result))
    elif dxl5_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl5_error))
    if dxl6_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl6_comm_result))
    elif dxl6_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl6_error))

    if dxl7_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl7_comm_result))
    elif dxl7_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl7_error))
    if dxl8_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl8_comm_result))
    elif dxl8_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl8_error))

    if dxl9_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl9_comm_result))
    elif dxl9_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl9_error))
    if dxl10_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl10_comm_result))
    elif dxl10_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl10_error))

    while 1:
        # Read present position
        dxl1_present_position, dxl1_comm_result, dxl1_error = packetHandler.read2ByteTxRx(portHandler, DXL1_ID, ADDR_MX_PRESENT_POSITION)
        dxl2_present_position, dxl2_comm_result, dxl2_error = packetHandler.read2ByteTxRx(portHandler, DXL2_ID, ADDR_MX_PRESENT_POSITION)
        
        dxl3_present_position, dxl1_comm_result, dxl1_error = packetHandler.read2ByteTxRx(portHandler, DXL3_ID, ADDR_MX_PRESENT_POSITION)
        dxl4_present_position, dxl2_comm_result, dxl2_error = packetHandler.read2ByteTxRx(portHandler, DXL4_ID, ADDR_MX_PRESENT_POSITION)
        
        dxl5_present_position, dxl1_comm_result, dxl1_error = packetHandler.read2ByteTxRx(portHandler, DXL5_ID, ADDR_MX_PRESENT_POSITION)
        dxl6_present_position, dxl2_comm_result, dxl2_error = packetHandler.read2ByteTxRx(portHandler, DXL6_ID, ADDR_MX_PRESENT_POSITION)
        
        dxl7_present_position, dxl1_comm_result, dxl1_error = packetHandler.read2ByteTxRx(portHandler, DXL7_ID, ADDR_MX_PRESENT_POSITION)
        dxl8_present_position, dxl2_comm_result, dxl2_error = packetHandler.read2ByteTxRx(portHandler, DXL8_ID, ADDR_MX_PRESENT_POSITION)
        
        dxl9_present_position, dxl1_comm_result, dxl1_error = packetHandler.read2ByteTxRx(portHandler, DXL9_ID, ADDR_MX_PRESENT_POSITION)
        dxl10_present_position, dxl2_comm_result, dxl2_error = packetHandler.read2ByteTxRx(portHandler, DXL10_ID, ADDR_MX_PRESENT_POSITION)
        if dxl1_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl1_comm_result))
        elif dxl1_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl2_error))
        if dxl2_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl2_comm_result))
        elif dxl2_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl2_error))

        if dxl3_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl3_comm_result))
        elif dxl3_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl3_error))
        if dxl4_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl4_comm_result))
        elif dxl4_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl4_error))

        if dxl5_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl5_comm_result))
        elif dxl5_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl5_error))
        if dxl6_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl6_comm_result))
        elif dxl6_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl6_error))

        if dxl7_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl7_comm_result))
        elif dxl7_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl7_error))
        if dxl8_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl8_comm_result))
        elif dxl8_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl8_error))

        if dxl9_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl9_comm_result))
        elif dxl9_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl9_error))
        if dxl10_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl10_comm_result))
        elif dxl10_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl10_error))

        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL1_ID, dxl1_goal_position[index], dxl1_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL2_ID, dxl2_goal_position[index], dxl2_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL3_ID, dxl3_goal_position[index], dxl3_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL4_ID, dxl4_goal_position[index], dxl4_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL5_ID, dxl5_goal_position[index], dxl5_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL6_ID, dxl6_goal_position[index], dxl6_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL7_ID, dxl7_goal_position[index], dxl7_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL8_ID, dxl8_goal_position[index], dxl8_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL9_ID, dxl9_goal_position[index], dxl9_present_position))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL10_ID, dxl10_goal_position[index], dxl10_present_position))

        if not abs(dxl1_goal_position[index] - dxl1_present_position) > DXL1_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl2_goal_position[index] - dxl2_present_position) > DXL2_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl3_goal_position[index] - dxl3_present_position) > DXL1_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl4_goal_position[index] - dxl4_present_position) > DXL2_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl5_goal_position[index] - dxl5_present_position) > DXL1_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl6_goal_position[index] - dxl6_present_position) > DXL2_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl7_goal_position[index] - dxl7_present_position) > DXL1_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl8_goal_position[index] - dxl8_present_position) > DXL2_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl9_goal_position[index] - dxl9_present_position) > DXL1_MOVING_STATUS_THRESHOLD:
            break
        if not abs(dxl10_goal_position[index] - dxl10_present_position) > DXL2_MOVING_STATUS_THRESHOLD:
            break

    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0


# Disable Dynamixel Torque
dxl1_comm_result, dxl1_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl1_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl1_comm_result))
elif dxl1_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl1_error))
dxl2_comm_result, dxl2_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl2_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl2_comm_result))
elif dxl2_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl2_error))
dxl3_comm_result, dxl3_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl3_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl3_comm_result))
elif dxl3_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl3_error))
dxl4_comm_result, dxl4_error = packetHandler.write1ByteTxRx(portHandler, DXL4_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl4_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl4_comm_result))
elif dxl4_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl4_error))
dxl5_comm_result, dxl5_error = packetHandler.write1ByteTxRx(portHandler, DXL5_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl5_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl5_comm_result))
elif dxl5_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl5_error))
dxl6_comm_result, dxl6_error = packetHandler.write1ByteTxRx(portHandler, DXL6_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl6_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl6_comm_result))
elif dxl6_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl6_error))
dxl7_comm_result, dxl7_error = packetHandler.write1ByteTxRx(portHandler, DXL7_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl7_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl7_comm_result))
elif dxl7_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl7_error))
dxl8_comm_result, dxl8_error = packetHandler.write1ByteTxRx(portHandler, DXL8_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl8_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl8_comm_result))
elif dxl8_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl8_error))
dxl9_comm_result, dxl9_error = packetHandler.write1ByteTxRx(portHandler, DXL9_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl9_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl9_comm_result))
elif dxl9_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl9_error))
dxl10_comm_result, dxl10_error = packetHandler.write1ByteTxRx(portHandler, DXL10_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl10_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl10_comm_result))
elif dxl10_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl10_error))

# Close port
portHandler.closePort()
