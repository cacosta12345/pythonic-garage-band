class Band:
    """
    Represents a musical band.
    """
    instances = []

    def __init__(self, name, members):
        """
        Initializes a Band object.

        Args:
            name (str): The name of the band.
            members (list): A list of Musician objects representing the members of the band.
        """
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        """
        Plays solos for each member of the band.

        Returns:
            list: A list containing the solos played by each member.
        """
        return [member.play_solo() for member in self.members]
    
    @classmethod
    def to_list(cls):
        """
        Gets a list of all Band instances.

        Returns:
            list: A list containing all Band instances.
        """
        return cls.instances
    
    def __str__(self):
        """
        Returns a string representation of the band.

        Returns:
            str: A string representation of the band.
        """
        return f"{self.name} band with {len(self.members)} members"
        
class Musician():
    """
    Represents a musician.
    """
    def __init__(self, name):
        """
        Initializes a Musician object.

        Args:
            name (str): The name of the musician.
        """
        self.name = name

    def __str__(self):
        """
        Returns a string representation of the musician.

        Returns:
            str: A string representation of the musician.
        """

        return f"My name is {self.name}"

    def get_instrument(self):
        """
        Gets the instrument played by the musician.

        Returns:
            str: The instrument played by the musician.
        """
        pass

    def play_solo(self):
        """
        Plays a solo.

        Returns:
            str: A string representing the solo played by the musician.
        """
        pass
        

class Guitarist(Musician):
    """
    Represents a guitarist, a type of musician.
    """
    
    def __str__(self):
        """
        Returns a string representation of the guitarist.

        Returns:
            str: A string representation of the guitarist.
        """
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        """
        Returns a string representation of the guitarist for debugging purposes.

        Returns:
            str: A string representation of the guitarist.
        """

        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        """
        Gets the instrument played by the guitarist.

        Returns:
            str: The instrument played by the guitarist.
        """
        return "guitar"
    
    def play_solo(self):
        """
        Plays a guitar solo.

        Returns:
            str: A string representing the guitar solo.
        """
        return "face melting guitar solo"

    

class Bassist(Musician):
    """
    Represents a bassist, a type of musician.
    """
 
    def __str__(self):
        """
        Returns a string representation of the bassist.

        Returns:
            str: A string representation of the bassist.
        """

        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        """
        Returns a string representation of the bassist for debugging purposes.

        Returns:
            str: A string representation of the bassist.
        """
        return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        """
        Gets the instrument played by the bassist.

        Returns:
            str: The instrument played by the bassist.
        """
        return "bass"
    
    def play_solo(self):
        """
        Plays a bass solo.

        Returns:
            str: A string representing the bass solo.
        """
        return "bom bom buh bom"


class Drummer(Musician):
    """
    Represents a drummer, a type of musician.
    """
    
    def __str__(self):
        """
        Returns a string representation of the drummer.

        Returns:
            str: A string representation of the drummer.
        """
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        """
        Returns a string representation of the drummer for debugging purposes.

        Returns:
            str: A string representation of the drummer.
        """
        return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        """
        Gets the instrument played by the drummer.

        Returns:
            str: The instrument played by the drummer.
        """
        return "drums"
    
    def play_solo(self):
        """
        Plays a drum solo.

        Returns:
            str: A string representing the drum solo.
        """
        return "rattle boom crash"
