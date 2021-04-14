from time import sleep


class TrafficLight:
    __color = ['КРАСНЫЙ', 'ЖЕЛТЫЙ', 'ЗЕЛЕНЫЙ']

    def running(self):
        while True:
            print(f'На светофоре {TrafficLight.__color[0]} сигнал')
            for i in range(7):
                sleep(1)
                print(i)
            print(f'На светофоре {TrafficLight.__color[1]} сигнал')
            for i in range(2):
                sleep(1)
                print(i)
            print(f'На светофоре {TrafficLight.__color[2]} сигнал')
            for i in range(10):
                sleep(1)
                print(i)


TL = TrafficLight()
TL.running()