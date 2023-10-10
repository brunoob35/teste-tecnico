class Device:
    def __init__(self, _id, name, serialNumber, points=None):
        self._id = _id
        self.name = name
        self.serialNumber = serialNumber
        self.points = points if points is not None else []

    def add_point(self, point):
        self.points.append(point)