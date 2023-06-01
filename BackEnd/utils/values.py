# Setting host and port values
host = "0.0.0.0"
port = 5000

# Pin values
pins = { "rooms": { "Sala": 2, "Cuarto 1": 3, "Cuarto 2": 4, "Cocina": 17, "Comedor": 27 }, 
            "doors": { "1": 23, "2": 24, "3": 20, "4": 21 } }

# Setting status values constants
low = 0
high = 1

# Library path
ourLib = "/lib/libgpioman.so.0"

# Setting input and output modes to read and send info
iMode = 0
oMode = 1

# If the command was completed correctly
error = -1
complete = 0