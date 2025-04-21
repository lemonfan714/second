#класс лифт, этажи, наш этаж, методы:вверх, вниз по 1 этажу, макс, мин
class Elevator:
    def __init__(self, current_floor, amount_floors):
        self.amount_floors = amount_floors
        self.current_floor = None
        self.min_floor = 1
        self.set_current_floor(current_floor)
        self.is_fire = False

    def set_current_floor(self, current_floor):
        if current_floor > self.amount_floors:
            self.current_floor = self.amount_floors
        else:
            self.current_floor = current_floor

    def up(self):
        if not self.is_fire:
            if self.current_floor != self.amount_floors:
                self.current_floor += 1
                print('I get up')
            else:
                print('cant go up')
        else:
            print('FIRE')


    def down(self):
        if not self.is_fire:
            if self.current_floor != self.min_floor:
                self.current_floor -= 1
                print('I get down')
            else:
                print('Cant go down')
        else:
            print('FIRE')

    def get_current_floor(self):
        print(self.current_floor)

    def goto_selected_floor(self, selected_floor):
        if not self.is_fire:
            if selected_floor <= self.amount_floors:
                steps = selected_floor - self.current_floor
                if steps == 0:
                    print('already there')
                elif steps > 0:
                    for i in range(steps):
                        self.up()
                elif steps < 0:
                    for i in range(abs(steps)):
                        self.down()
            else:
                print('Beyond borders')
        else:
            print('FIRE')
    def fire_block(self):
        self.is_fire =  True


elevator = Elevator(5, 10)
elevator.goto_selected_floor(7)
elevator.get_current_floor()
elevator.fire_block()
elevator.up()
elevator.get_current_floor()