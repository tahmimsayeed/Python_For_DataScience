readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]
clean = []
for read in readings:
 if read in readings == None and read>=50:
    continue
 else:
   clean = read

print("Clean list: ",clean)