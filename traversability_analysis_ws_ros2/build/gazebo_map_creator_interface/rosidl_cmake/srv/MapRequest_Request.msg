# Define constants
uint8 MAP_2D  = 0
uint8 MAP_3D  = 1

# Request to send for map creation
geometry_msgs/Point   lowerright
geometry_msgs/Point   upperleft
uint8                 skip_vertical_scan 0   # Default is 2d map (e.g .pgm)
float64               resolution 0.01  # smaller the value, higher the resolution
float64               range_multiplier 0.55   # Distance multiplier to check for horizontal collision.
int32                 threshold_2d 255
string                filename "map"
