from Devices.HP3455A import HP3455A

# Configure this to match the serial Port of the DDM-arduino
port = "/dev/ttyACM0"

# Init and test the connection to the Digital Multimeter
ddm = HP3455A(port, debug=False)

print(ddm.get_reading())

# write your script here