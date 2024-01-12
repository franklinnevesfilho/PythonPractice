import numpy as np

frame = np.zeros([5,5], dtype=np.uint8) # 5 x 5 matrix - unsigned int 8 bits

print(frame)

frame[:,:] = 1 # all set to 1

print('All are 1','\n', frame)