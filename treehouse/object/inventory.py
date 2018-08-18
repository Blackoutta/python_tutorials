class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, *items):
        for item in items:
            self.slots.append(item)


class SortedInventory(Inventory):
    def add_item(self, *items):
        super().add_item(*items)
        self.slots.sort()

