class Router:
    def __init__(self, name: str):
        self.name = name
        self.connected_devices = [25]
    def start(self, status: str, battery_level: int):
        print(f"{self.name} is {status} with a battery level of {battery_level}%.")
    def display_status(self, temperature: int, signal_strength: int):
        print (f"{self.name} is connected to {len(self.connected_devices)} devices.")
    def increase_speed(self, speed: int):
        print(f"{self.name} is increasing speed to {speed} Mbps.")
    def decrease_speed(self, speed: int):
        print(f"{self.name} is decreasing speed to {speed} Mbps.")
    def stop(self, location: str):
        print(f"{self.name} is stopping at {location}.")


router= Router("Cisco Router")
router.start("active", 80)
router.display_status(26, 80)
router.increase_speed(100)
router.decrease_speed(50)
router.stop("Living Room")


