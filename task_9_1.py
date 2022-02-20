from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(2)
            elif i == 1:
                sleep(3)
            elif i == 2:
                sleep(4)
            i += 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()