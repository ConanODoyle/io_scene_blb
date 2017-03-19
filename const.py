# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
"""
Various constants used in multiple modules.

@author: Demian Wright
"""

from decimal import Decimal
from enum import Enum, IntEnum
from math import pi

# The BLB file extension.
BLB_EXT = ".blb"

# The log file extension.
LOG_EXT = ".log"

# One log indent level.
LOG_INDENT = "  "

# Generic.
X = 0
Y = 1
Z = 2

# Blockland does not accept bricks that are wide/deeper than 64 bricks or taller than 256 plates.
MAX_BRICK_HORIZONTAL_PLATES = 64
MAX_BRICK_VERTICAL_PLATES = 256

# FIXME: Use more enums.


class BLBQuadSection(IntEnum):
    """The quad sections in the correct order for writing to a BLB file. Indexed from 0 to 6."""
    TOP = 0
    BOTTOM = 1
    NORTH = 2
    EAST = 3
    SOUTH = 4
    WEST = 5
    OMNI = 6

# A tuple of valid brick textures in alphabetical order.
VALID_BRICK_TEXTURES = ("bottomedge", "bottomloop", "print", "ramp", "side", "top")

# BLB file strings.
BLB_BRICK_TYPE_SPECIAL = "SPECIAL"
BLB_SECTION_SEPARATOR = "---------------- {} QUADS ----------------"
BLB_HEADER_COVERAGE = "COVERAGE:"
BLB_PREFIX_TEXTURE = "TEX:"
BLB_HEADER_POSITION = "POSITION:"
BLB_HEADER_UV = "UV COORDS:"
BLB_HEADER_COLORS = "COLORS:"
BLB_HEADER_NORMALS = "NORMALS:"

# The default coverage value = no coverage. (Number of plates that need to cover a brick side to hide it.)
# The maximum area a brick's side can cover is 64 * 256 = 16384 plates.
DEFAULT_COVERAGE = 99999

# Brick grid symbols.
GRID_INSIDE = "x"  # Disallow building inside brick.
GRID_OUTSIDE = "-"  # Allow building in empty space.
GRID_UP = "u"  # Allow placing bricks above this plate.
GRID_DOWN = "d"  # Allow placing bricks below this plate.
GRID_BOTH = "b"  # Allow placing bricks above and below this plate.

# Maximum number of decimal places to write to file.
MAX_FP_DECIMALS_TO_WRITE = 16

# The width and height of the default brick textures in pixels.
BRICK_TEXTURE_RESOLUTION = 512

# The UV coordinates are a single point in the middle of the image = no uv coordinates.
# The middle of the image is used instead of (0,0) due to the way Blockland brick textures are designed.
DEFAULT_UV_COORDINATES = ((0.5, 0.5),) * 4

# Often used Decimal values.
DECIMAL_HALF = Decimal("0.5")

# Useful angles in radians.
RAD_45_DEG = pi * 0.25
RAD_135_DEG = pi - RAD_45_DEG
RAD_225_DEG = pi + RAD_45_DEG
RAD_315_DEG = pi + RAD_135_DEG

TWO_PI = 2.0 * pi


class Axis3D(Enum):
    """An enum with values representing each axis in three-dimensional space, indexed as follows:
           0: POS_X
           1: NEG_X
           2: POS_Y
           3: NEG_Y
           4: POS_Z
           5: NEG_Z
    """
    POS_X = 0
    NEG_X = 1
    POS_Y = 2
    NEG_Y = 3
    POS_Z = 4
    NEG_Z = 5

    def index(self):
        """Determines the index of this three-dimensional axis.

        Returns:
            The index 0, 1, or 2 for the axes X, Y, and Z respectively.
        """
        if self == Axis3D.POS_X or self == Axis3D.NEG_X:
            return X
        elif self == Axis3D.POS_Y or self == Axis3D.NEG_Y:
            return Y
        else:
            return Z

    def is_positive(self):
        """Determines if this three-dimensional axis is positive or negative.

        Returns:
            True if this value represents a positive axis.
        """
        return self == Axis3D.POS_X or self == Axis3D.POS_Y or self == Axis3D.POS_Z


class AxisPlane3D(Enum):
    """An enum with values representing each axis-aligned plane in three-dimensional space, indexed as follows:
           0: XY-plane
           1: XZ-plane
           2: YZ-plane
    """
    XY = 0
    XZ = 1
    YZ = 2
