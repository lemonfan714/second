class Finger:
    def __init__(self, is_existing=True, is_ill=False, functionality=1):
        self.is_existing = is_existing
        self.is_ill = is_ill
        self.functionality = functionality
        self._is_bended = False

    def bend_finger(self):
        if self.functionality >= 0.3 and self.is_existing and not self.is_ill:
            self._is_bended = True
    def unbend_finger(self):
        self._is_bended = False
    def print_info(self):
        if self.is_existing:
            print('is_Ill', self.is_ill)
            print('functionality', self.functionality)
            print('is_bended', self._is_bended)
            print('\n')
        else:
            print('no finger here')
    def finger_must_die(self):
        self.is_existing = False
        self.bastards_they_killed_finger()
    def bastards_they_killed_finger(self):
        if not self.is_existing:
            self.functionality = 0




class Arm:
    _amount_fingers = 5
    fingers = [Finger() for i in range(_amount_fingers)]
    def __init__(self, is_ill = False, is_existing = True):
        self.is_ill = is_ill
        self.is_existing = is_existing
        self._is_bended = False

    def print_info(self):
        print('\nARM\n')
        print('is_ill', self.is_ill)
        print('is_existing', self.is_existing)
        print('_is_bended', self._is_bended)
        print('\n FINGERS \n')
        for i in range(len(self.fingers)):
            print(f'FINGER NUMBER - {i+1}\n')
            self.fingers[i].print_info()
    def unbend_fingers(self):
        for finger in self.fingers:
            finger.unbend_finger()
    def bend_arm(self):
        if self.is_existing and not self.is_ill:
            self._is_bended = True
    def unbend_arm(self):
        self._is_bended =  False
    def bend_amount_fingers(self, count_fingers):
        if 0<count_fingers<=5:
            for i in range(count_fingers):
                self.fingers[i].bend_finger()
    def bend_selected_fingers(self, *finger_nums):
        for num in finger_nums:
            if 1<=num<=5:
                self.fingers[num-1].bend_finger()
            else:
                print(f'cant_bend! - {num} finger\n')

class Leg:
    def __init__(self, is_ill = False, is_existing = True):
        self.is_ill = is_ill
        self.is_existing = is_existing
        self._is_bended = False
        self._amount_fingers = 5
        self.fingers = [Finger() for i in range(self._amount_fingers)]
    def bend_leg(self):
        if self.is_existing and not self.is_ill:
            self._is_bended = True
    def unbend_leg(self):
        self._is_bended = False

    def print_info(self):
        print('\nLEG\n')
        print('is_ill', self.is_ill)
        print('is_existing', self.is_existing)
        print('_is_bended', self._is_bended)
        print('\n FINGERS \n')
        for i in range(len(self.fingers)):
            print(f'FINGER NUMBER - {i+1}\n')
            self.fingers[i].print_info()

    def unbend_fingers(self):
        for finger in self.fingers:
            finger.unbend_finger()

    def bend_amount_fingers(self, count_fingers):
        if 0<count_fingers<=5:
            for i in range(count_fingers):
                self.fingers[i].bend_finger()

    def bend_selected_fingers(self, finger_nums):
        for num in finger_nums:
            if 1<=num<=5:
                self.fingers[num-1].bend_finger()
            else:
                print(f'cant_bend! - {num} finger\n')
class CPU:
    def __init__(self, color, smartness=0.75):
        self.color = color
        self.smartness = smartness
        self._is_bended = [False, None]
    def bend_head(self, direction: str|None):
        if self.smartness > 0.1:
            self._is_bended[0] = True
            self._is_bended[1] = direction
    def unbend(self):
        if self.smartness > 0.1:
            self._is_bended[0] = False
            self._is_bended[1] = None
    def logic(self, operator: str, *args):
        if operator.lower() == 'not':
            if args[0] == 0:
                print('0 was inputed \n1 is a result')
                return 1
            elif args[0] == 1:
                print('1 was inputed \n0 is a result')
                return 0
            else:
                print('YOU CAN ONLY TYPE 0 OR 1!')
        elif operator.lower() == 'and':
            flare = False
            for i in args:
                if i != 0 and i!=1:
                    flare = True
            if not flare and ((args[0] == args[1]) and (args[0] != 0 and args[1] != 0)):
                print(f'{args[0]} and {args[1]} was inputed \n1 is a result')
                return 1
            elif not flare:
                print(f'{args[0]} and {args[1]} was inputed \n0 is a result')
                return 0
            else:
                print('YOU CAN ONLY TYPE 0 OR 1!')
        elif operator.lower() == 'or':
            flare = False
            for i in args:
                if i != 0 and i != 1:
                    flare = True
            if not flare and ((args[0]==1 or args[1]==1) and (args[0]!=0 or args[1] != 0)):
                print(f'{args[0]} and {args[1]} was inputed \n1 is a result')
                return 1
            elif not flare:
                print(f'{args[0]} and {args[1]} was inputed \n0 is a result')
                return 0
            else:
                print('YOU CAN ONLY TYPE 0 OR 1!')
    def print_info(self):
        print('CPU')
        print(f'color:{self.color} \nsmartness:{self.smartness} \nis_bended:{self._is_bended}')

class Amalgam:
    parts = {
        'head':CPU('groovy'), 'hands':[Arm() for i in range(4)], 'legs':tuple([Leg() for i in range(2)])
    }

    def print_info(self):
        self.parts['head'].print_info()
        for hand in self.parts['hands']:
            hand.print_info()
        for leg in self.parts['legs']:
            leg.print_info()

copepod = Amalgam()
copepod.parts['legs'][0].fingers[3].finger_must_die()
copepod.parts['legs'][0].print_info()
copepod.parts['head'].logic('or', 0, 1)
copepod.parts['legs'][1].fingers[0].bend_finger()
copepod.parts['hands'][3].bend_selected_fingers(1, 3, 8)