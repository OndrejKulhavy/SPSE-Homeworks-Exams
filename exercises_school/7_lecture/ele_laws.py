import math

class OhmLaw:
    """
    The OhmLaw class provides methods for calculating various electrical quantities
    using Ohm's Law.

    Ohm's Law describes the relationship between voltage (V), current (I), and
    resistance (R) in an electrical circuit:

    - V = I * R (Voltage is equal to current multiplied by resistance)
    - I = V / R (Current is equal to voltage divided by resistance)
    - R = V / I (Resistance is equal to voltage divided by current)
    """

    @staticmethod
    def calculate_voltage(current, resistance):
        """
        Calculate voltage using Ohm's Law.

        Args:
            current (float): The current in the circuit (in amperes).
            resistance (float): The resistance in the circuit (in ohms).

        Returns:
            float: The voltage in the circuit (in volts).
        """
        return current * resistance

    @staticmethod
    def calculate_current(voltage, resistance):
        """
        Calculate current using Ohm's Law.

        Args:
            voltage (float): The voltage in the circuit (in volts).
            resistance (float): The resistance in the circuit (in ohms).

        Returns:
            float: The current in the circuit (in amperes).
        """
        return voltage / resistance

    @staticmethod
    def calculate_resistance(voltage, current):
        """
        Calculate resistance using Ohm's Law.

        Args:
            voltage (float): The voltage in the circuit (in volts).
            current (float): The current in the circuit (in amperes).

        Returns:
            float: The resistance in the circuit (in ohms).
        """
        return voltage / current


class CoulombsLaw:
    COULOMBS_CONSTANT = 8.99e9

    @staticmethod
    def calculate_force(charge_1, charge_2, distance, epsilon_r=1):
        """
        Calculate the electrostatic force between two charges.

        Parameters:
        charge_1 (float): The magnitude of the first charge in coulombs (C).
        charge_2 (float): The magnitude of the second charge in coulombs (C).
        distance (float): The distance between the two charges in meters (m).
        epsilon_r (float, optional): The relative permittivity of the medium (default is 1).

        Returns:
        float: The electrostatic force in newtons (N).
        """
        force = CoulombsLaw.COULOMBS_CONSTANT * abs(charge_1 * charge_2) / (distance ** 2) / epsilon_r
        return force

    @staticmethod
    def calculate_charge(force, distance, epsilon_r=1):
        """
        Calculate the charge required to produce a given electrostatic force.

        Parameters:
        force (float): The electrostatic force in newtons (N).
        distance (float): The distance between the two charges in meters (m).
        epsilon_r (float, optional): The relative permittivity of the medium (default is 1).

        Returns:
        float: The magnitude of the charge in coulombs (C).
        """
        charge = force * (distance ** 2) * epsilon_r / CoulombsLaw.COULOMBS_CONSTANT
        return charge

    @staticmethod
    def calculate_distance(force, charge_1, charge_2, epsilon_r=1):
        """
        Calculate the distance between two charges that produce a given electrostatic force.

        Parameters:
        force (float): The electrostatic force in newtons (N).
        charge_1 (float): The magnitude of the first charge in coulombs (C).
        charge_2 (float): The magnitude of the second charge in coulombs (C).
        epsilon_r (float, optional): The relative permittivity of the medium (default is 1).

        Returns:
        float: The distance between the two charges in meters (m).
        """
        distance = math.sqrt(CoulombsLaw.COULOMBS_CONSTANT * abs(charge_1 * charge_2) / (force * epsilon_r))
        return distance

    @staticmethod
    def calculate_epsilon_r(force, charge_1, charge_2, distance):
        """
        Calculate the relative permittivity (epsilon_r) of the medium based on electrostatic force and charges.

        Parameters:
        force (float): The electrostatic force in newtons (N).
        charge_1 (float): The magnitude of the first charge in coulombs (C).
        charge_2 (float): The magnitude of the second charge in coulombs (C).
        distance (float): The distance between the two charges in meters (m).

        Returns:
        float: The relative permittivity (epsilon_r) of the medium.
        """
        epsilon_r = CoulombsLaw.COULOMBS_CONSTANT * abs(charge_1 * charge_2) / (force * (distance ** 2))
        return epsilon_r

    @staticmethod
    def calculate_charge(force, charge, distance, epsilon_r=1):
        """
        Calculate the magnitude of the second charge to produce a given electrostatic force.

        Parameters:
        force (float): The electrostatic force in newtons (N).
        charge (float): The magnitude of the first charge in coulombs (C).
        distance (float): The distance between the two charges in meters (m).
        epsilon_r (float, optional): The relative permittivity of the medium (default is 1).

        Returns:
        float: The magnitude of the second charge in coulombs (C).
        """
        charge_2 = force * (distance ** 2) * epsilon_r / (CoulombsLaw.COULOMBS_CONSTANT * charge)
        return charge_2

