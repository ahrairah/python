from datetime import date

last_id = 0


class Plant:
    def __init__(self, name, plant_type, earth_humidity=0, slot=0, **kwargs):
        self.name = name
        self.plant_type = plant_type
        self.last_watered = ""
        global last_id
        last_id += 1
        self.id = last_id
        self.earth_humidity = earth_humidity
        self.slot = slot
        pass

    def match(self, filter_str):
        """Nach Pflanzenbezeichnung oder -typ suchen.
        :param filter_str:
        """
        return filter_str in self.name or filter_str in self.plant_type


class WindowShelf:
    def __init__(self):
        self.plants = []

    def new_plant(self, name, plant_type=''):
        self.plants.append(Plant(name, plant_type))

    def _find_plant(self, plant_id):
        for plant in self.plants:
            if str(plant.id) == str(plant_id):
                return plant
        return None

    def modify_plant_name(self, plant_id, name):
        plant = self._find_plant(plant_id)
        if plant:
            plant.name = name
            return True
        return False

    def modify_plant_type(self, plant_id, plant_type):
        plant = self._find_plant(plant_id)
        if plant:
            plant.plant_type = plant_type
            return True
        return False

    def search(self, search_str):
        return [plant for plant in self.plants if plant.match(search_str)]


class WateringSystem:
    def __init__(self):
        pass

    def trigger_water(self, slot):
        """Sollte gegebenen Anschluss wässern.
        :param slot:
        """
        pass

    def water_plants(self):
        for plant in WindowShelf.plants:
            if plant.earth_humidity < 50:
                self.trigger_water(plant.slot)
                plant.last_watered = date.today()
