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

'''
    Also for clarification u can change this stuff. To update the rockets position, u pass the epoch/evolution time to Rocket.update(delta_t)
    Then you read from the sensor using Rocket.SensorReading(). This returns a matrix with [alt, vel, acc].T so u can just index what u want.
    Also I havent added a function to update the airbrake size (will add after) but if u want to change go to dep/Ada.py and go to the openAirBrake function.

    Also to deplot airbrake use Rocket.openAirBrakes(P) where P is a val between [0 - 1].
'''

print(max(alt))
plt.plot(alt)
plt.show()    
