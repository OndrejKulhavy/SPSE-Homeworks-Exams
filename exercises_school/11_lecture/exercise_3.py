class Bottle:
    """A bottle with a capacity and a volume of liquid"""

    def __init__(self, capacity_liters: float):
        """
        Initializes a new Bottle object.

        Parameters:
        capacity_liters (float): The maximum capacity of the bottle in liters.

        Attributes:
        isClosed (bool): Indicates if the bottle is closed.
        capacity_liters (float): The maximum capacity of the bottle in liters.
        filled_liters (float): The volume of liquid in the bottle in liters.
        """
        self.isClosed = False
        self.capacity_liters = capacity_liters
        self.filled_liters = 0

    def fill(self, volume_liters: float):
        """
        Fills the bottle with a specified volume of liquid.

        Parameters:
        volume_liters (float): The volume of liquid to be added to the bottle in liters.

        Raises:
        ValueError: If the volume exceeds the bottle's capacity or if the bottle is closed.
        """
        if volume_liters + self.filled_liters > self.capacity_liters:
            raise ValueError("Volume exceeds capacity")
        if self.isClosed:
            raise ValueError("Bottle is closed")
        self.filled_liters = volume_liters + self.filled_liters

    def pour(self, volume_liters: float):
        """
        Pours a specified volume of liquid from the bottle.

        Parameters:
        volume_liters (float): The volume of liquid to be poured from the bottle in liters.

        Raises:
        ValueError: If the volume exceeds the filled liters or if the bottle is closed.
        """
        if self.filled_liters - volume_liters < 0:
            raise ValueError("Volume exceeds filled liters")
        if self.isClosed:
            raise ValueError("Bottle is closed")
        self.filled_liters -= volume_liters

    def get_volume_milliliters(self):
        """
        Returns the volume of liquid in the bottle in milliliters.

        Returns:
        float: The volume of liquid in the bottle in milliliters.
        """
        return self.filled_liters * 1000

    def close(self):
        """
        Closes the bottle, preventing further filling or pouring.
        """
        self.isClosed = True

    def open(self):
        """
        Opens the bottle, allowing filling and pouring.
        """
        self.isClosed = False
