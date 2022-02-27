from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        
    def get_points(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._points
    
    def set_points(self):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        if self._text == 'O':
            self._points = -25
        elif self._text == '*':
            self._points = 25
    
    