
class BaseComputer:

    serial_number_counter = 0
    
    def __init__(self):

        BaseComputer.serial_number_counter += 1
        self.serial_number = BaseComputer.serial_number_counter


class DesktopComputer(BaseComputer):

    def __init__(self, connection_type):

        super().__init__()
        self.connection = connection_type()
    
    def display_info(self):

        print(f"The desktop computer costs $1000\nSerial Number: {self.serial_number}")
        self.connection.download()


class Laptop(BaseComputer):

    def __init__(self, connection_type):

        super().__init__()
        self.connection = connection_type()
    
    def display_info(self):
        
        print(f"The laptop costs $700\nSerial Number: {self.serial_number}")
        self.connection.download()


class Connection:

    def __init__(self, speed):

        self.speed = speed
    
    def download(self):

        print(f"Downloading at {self.speed}")


class DialUp(Connection):

    def __init__(self):

        super().__init__(speed="9600bit/s")
    
    def download(self):

        print("DialUp connection: Initiating download...")

        super().download()


class ADSL(Connection):

    def __init__(self):

        super().__init__(speed="2Mbit/s")
    
    def download(self):

        print("ADSL connection: Starting download...")

        super().download()


class Ethernet(Connection):

    def __init__(self):

        super().__init__(speed="10Mbit/s")
    
    def download(self):

        print("Ethernet connection: Downloading...")

        super().download()



#computer objects with different connections
dialup_desktop = DesktopComputer(DialUp)

adsl_desktop = DesktopComputer(ADSL)

ethernet_desktop = DesktopComputer(Ethernet)

#____________________________________________________

dialup_laptop = Laptop(DialUp)

adsl_laptop = Laptop(ADSL)

ethernet_laptop = Laptop(Ethernet)

#information and initiating downloads

dialup_desktop.display_info()

adsl_desktop.display_info()

ethernet_desktop.display_info()

#________________________________________________________

dialup_laptop.display_info()

adsl_laptop.display_info()

ethernet_laptop.display_info()
