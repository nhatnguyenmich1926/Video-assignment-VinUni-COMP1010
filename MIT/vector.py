from math import sqrt

class Vector:
    def __init__(self, vector_x, vector_y):
        self.vectorX = vector_x
        self.vectorY = vector_y

    def distance(self, other):
        """Distance between two Vector objects."""
        return sqrt((other.vectorX - self.vectorX)**2 +
                    (other.vectorY - self.vectorY)**2)

def main():
    # First vector
    x1 = float(input("Enter vector 1 X: "))
    y1 = float(input("Enter vector 1 Y: "))
    v1 = Vector(x1, y1)

    # Second vector
    x2 = float(input("Enter vector 2 X: "))
    y2 = float(input("Enter vector 2 Y: "))
    v2 = Vector(x2, y2)

    # Compute distance between v1 and v2
    dist = Vector.distance(v1,v2)
    print(f"Distance = {dist}")

if __name__ == "__main__":
    main()
