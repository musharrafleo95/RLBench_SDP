from pyrep.robots.mobiles.nonholonomic_base import NonHolonomicBase


class HSR(NonHolonomicBase):
    def __init__(self, count: int = 0):
        super().__init__(count, 2, 'HSR')
