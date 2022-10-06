#!/usr/bin/env python3
from typing import Tuple
from PIL import Image, ImageDraw

# Global parameters for image resolution
WIDTH, HEIGHT = 1200, 2400


class Table:
    """Class containing the specifications of the pool table.

        The Table class is used to instantiate a table used as the
        background of the generated image. The object of this class
        is used to set the image dimensions, and ball scales.

        Attributes:
            width: The short edge length of the pool table in centimeters.
            height: The long edge length of the pool table in centimeters.
            scale: The relative scale of the table to the standard 99-by-198.
            radii: The radius of the balls in centimeters.
    """

    def __init__(self, width: float = 99, radii: float = 5.7 / 2) -> None:
        """Initiates the Table class.

        Args:
            width (float): The width of the pool table in centimeters.
            radii (float): The radius of the balls in centimeters.

        Yields:
            An object instance of the Table class.
        """
        self.width = width
        self.height = self.width * 2
        self.scale = self.width / 99
        self.radii = radii * self.scale

    def set_width(self, width: float = 99) -> None:
        """Setter for the table width.

        Args:
            width (float): The width of the pool table in centimeters.

        Returns:
            None
        """
        self.width = width

    def set_height(self, height: float = 198) -> None:
        """Setter for the table height.

        Args:
            height (float): The height of the pool table in centimeters.

        Returns:
            None
        """
        self.height = height

    def set_scale(self, scale: float = 1) -> None:
        """Setter for the table scale.

        Args:
            scale (float): The relative scale of the table to the standard 99-by-198.

        Returns:
            None
        """
        self.scale = scale

    def set_radii(self, radii: float = 5.7 / 2) -> None:
        """Setter for the ball radius.

        Args:
            radii (float): The radius of the balls in centimeters.

        Returns:
            None
        """
        self.radii = radii

    def get_width(self) -> float:
        """Getter for the table width.

        Returns:
            The width of the pool table in centimeters.
        """
        return self.width

    def get_height(self) -> float:
        """Getter for the table height.

        Returns:
            The height of the pool table in centimeters.
        """
        return self.height

    def get_scale(self) -> float:
        """Getter for the table scale.

        Returns:
            The relative scale of the table to the standard 99-by-198.
        """
        return self.scale

    def get_radii(self) -> float:
        """Getter for the ball radius.

        Returns:
            The radius of the balls in centimeters.
        """
        return self.radii

    def __repr__(self) -> str:
        """Creates the string representation of the Table object.

        Returns:
            String representation of the Table object.
        """
        return 'Table {\n' \
               + '    width:  {}\n'.format(self.width) \
               + '    height: {}\n'.format(self.height) \
               + '    scale:  {}\n'.format(self.scale) \
               + '    radii:  {}\n'.format(self.radii) \
               + '}\n'


class Ball:
    """Parent class containing the specifications of the pool balls.

        The Ball class is used as the parent class inherited by
        specific ball classes, containing the general properties
        of the pool balls.

        Attributes:
            color: The RGBA color of the pool ball.
            coordinates: The coordinates of the ball on the pool table.
            scale: The relative scale of the table to the standard 99-by-198.
    """

    def __init__(self, color: (int, int, int, int) = (255, 255, 255, 255),
                 coordinates: (float, float) = (0, 0),
                 scale: float = 1) -> None:
        """Initiates the Ball class.

        Args:
            color (tuple(int, int, int, int): The RGBA color of the pool ball.
            coordinates (tuple(float, float): The coordinates of the ball on the pool table.
            scale (float): The relative scale of the table to the standard 99-by-198.

        Yields:
            An object instance of the Ball class.
        """
        self.color = color
        self.coordinates = (coordinates[0] * scale, coordinates[1] * scale)

    def set_color(self, color: (int, int, int, int) = (255, 255, 255, 255)) -> None:
        """Setter for the ball color.

        Args:
            color (tuple(int, int, int, int): The RGBA color of the pool ball.

        Returns:
            None
        """
        self.color = color

    def set_coordinates(self, coordinates: (float, float) = (0, 0)) -> None:
        """Setter for the ball coordinates.

        Args:
            coordinates (tuple(float, float): The coordinates of the ball on the pool table.

        Returns:
            None
        """
        self.coordinates = coordinates

    def get_color(self) -> Tuple[int, int, int, int]:
        """Getter for the ball color.

        Returns:
            The RGBA color of the pool ball.
        """
        return self.color

    def get_coordinates(self) -> Tuple[float, float]:
        """Getter for the ball coordinates.

        Returns:
            The coordinates of the ball on the pool table.
        """
        return self.coordinates

    def get_xy(self, radius: float = 5.7 / 2) -> Tuple[float, float, float, float]:
        """Calculates the xy parameter for drawing an ellipse.

        Args:
            radius (float): The radius of the balls in centimeters.

        Returns:
            The xy parameter for drawing an ellipse.
        """
        return (self.coordinates[0] - radius, self.coordinates[1] - radius,
                self.coordinates[0] + radius, self.coordinates[1] + radius)

    def get_trajectory(self, target: (float, float) = (0, 0)) -> Tuple[float, float, float, float]:
        """Calculates the xy parameter for drawing a line.

        Args:
            target (tuple(float, float)): The coordinates of the intended destination of
                                          the ball on the pool table.

        Returns:
            The xy parameter for drawing a line.
        """
        return self.coordinates[0], self.coordinates[1], target[0], target[1]

    def __repr__(self) -> str:
        """Creates the string representation of the Ball object.

        Returns:
            String representation of the Ball object.
        """
        return 'Ball {\n' \
               + '    coordinates:  {}\n'.format(self.coordinates) \
               + '    color: {}\n'.format(self.color) \
               + '}\n'


class CueBall(Ball):
    """Class containing the specifications of the cue ball.

        The CueBall class inherits from the Ball class to
        house the specifications of the cue ball.

        Attributes:
            coordinates: The coordinates of the ball on the pool table.
    """

    def __init__(self, coordinates: (int, int) = (0, 0)) -> None:
        """Initiates the CueBall class using the predetermined white color.

        Args:
            coordinates (tuple(float, float): The coordinates of the ball on the pool table.

        Yields:
            An object instance of the CueBall class.
        """
        super().__init__((255, 255, 255, 255), coordinates)


class GhostBall(Ball):
    """Class containing the specifications of the ghost ball.

        The GhostBall class inherits from the Ball class to
        house the specifications of the ghost ball.

        Attributes:
            coordinates: The coordinates of the ball on the pool table.
    """

    def __init__(self, coordinates: (int, int) = (0, 0)) -> None:
        """Initiates the GhostBall class using the predetermined shadow color.

        Args:
            coordinates (tuple(float, float): The coordinates of the ball on the pool table.

        Yields:
            An object instance of the GhostBall class.
        """
        super().__init__((255, 255, 255, 2), coordinates)


class CalledBall(Ball):
    """Class containing the specifications of the called ball.

        The CalledBall class inherits from the Ball class to
        house the specifications of the red ball.

        Attributes:
            coordinates: The coordinates of the ball on the pool table.
    """

    def __init__(self, coordinates: (int, int) = (0, 0)) -> None:
        """Initiates the CalledBall class using the predetermined red color.

        Args:
            coordinates (tuple(float, float): The coordinates of the ball on the pool table.

        Yields:
            An object instance of the CalledBall class.
        """
        super().__init__((255, 0, 0, 255), coordinates)


class Pocket(Ball):
    """Class containing the specifications of the pocket.

        The Pocket class inherits from the Ball class to
        house the specifications of the pocket.

        Attributes:
            coordinates: The coordinates of the pocket on the pool table.
    """

    def __init__(self, coordinates: (int, int) = (0, 0)) -> None:
        """Initiates the CalledBall class using the predetermined black color.

        Args:
            coordinates (tuple(float, float): The coordinates of the pocket on the pool table.

        Yields:
            An object instance of the Pocket class.
        """
        super().__init__((0, 0, 0, 255), coordinates)


def parse(_representation: str, _scale: float) -> [CueBall, GhostBall, CalledBall, Pocket]:
    """Parses the string representation of the drill, and instantiates objects to be drawn on the image.

    Args:
        _representation (str): The string representation of the drill.
        _scale (float): The relative scale of the table to the standard 99-by-198.

    Returns:
        The object instances of cue, ghost, called balls, and the pocket.
    """
    # Parse representation string into a list of tuples (float, float)
    # where each tuple represents an object's x-y coordinates.
    parameters = [tuple(float(p) * _scale for p in parameter.split(',')) for parameter in _representation.split(';')]

    # Instantiate objects using appropriate parameters.
    return CueBall(parameters[0]), GhostBall(parameters[1]), CalledBall(parameters[2]), Pocket(parameters[3])


def generate(_table: Table, _cue: CueBall, _ghost: GhostBall, _called: CalledBall, _pocket: Pocket) -> Image:
    """Generates the projection image using the instantiated objects.

    Args:
        _table (Table): The pool table object.
        _cue (CueBall): The cue ball object.
        _ghost (GhostBall): The ghost ball object.
        _called (CalledBall): The called ball object.
        _pocket (Pocket): The pocket object.

    Returns:
        The generated image.
    """
    # The predetermined coefficients for perspective warping a straight image to a 2:1 orthogonal.
    coefficients = [2.00000000e+00, 2.50000000e-01, -6.00000000e+02, 1.06814613e-13,
                    2.00000000e+00, -7.45505545e-12, 7.49741597e-18, 4.16666667e-04]

    # Instantiate the image
    img = Image.new(mode='RGBA', size=(WIDTH, HEIGHT), color=(21, 88, 67, 255))
    # Create the draw object
    draw = ImageDraw.Draw(img)

    # Iterator for the objects
    itemList = [_cue, _ghost, _called, _pocket]
    # Iterate over the objects to be drawn,
    # excluding the pocket
    for i, item in enumerate(itemList[:-1]):
        # Draw the object
        draw.ellipse(xy=item.get_xy(radius=_table.radii), fill=item.get_color())
        # Draw the line between the current object and the next
        draw.line(xy=item.get_trajectory(itemList[i + 1].get_coordinates()), fill='white')

    # Perspective warp the image
    img = img.transform((WIDTH, HEIGHT), Image.PERSPECTIVE, coefficients, Image.BICUBIC)

    return img


def run(string: str) -> None:
    """Drives the image generation script.

        Args:
            string (str): The string representation of the drill.

        Returns:
            None
    """
    # Instantiate Table object
    table = Table(width=WIDTH)
    # Parse string representation to obtain drill parameters
    cue, ghost, called, pocket = parse(string, table.get_scale())
    # Generate image
    image = generate(table, cue, ghost, called, pocket)
    # Save image
    image.save('drill.png')


if __name__ == '__main__':
    run('072.4188,166.2855;031.2016,035.1107;027.4153,030.8499;000.0,000.0;00120025')
