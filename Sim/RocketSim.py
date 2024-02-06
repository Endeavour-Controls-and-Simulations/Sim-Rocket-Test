import matplotlib.pyplot as plt
from dep.ADA import Rocket_Data


Rocket = Rocket_Data()
'''
    For initializing Rocket_Data, you can pass the **Process Noise** Matrix and
    **Sensor Noise** Matrix as: np.array([[alt Var, vel Var, Acc Var]]).T.

    When passing in Sensor Noise Matrix, go crazy it just affects your readings but...
    don't go crazy with the process noise as it makes the system act unrealistically (you can try)
'''


alt =[]
for i in range(5000):
    Rocket.update(0.01)
    alt.append(Rocket.SensorReading()[0])


print(max(alt))
plt.plot(alt)
plt.show()    
