class OrderedSet(int):

    def __init__(self):
        self.set = []
        self.size = 0

    def add(self, element) -> None:
        if element in self.set:
            print(f"{element} already exists...")
            return
        print(f"Now adding {element}")
        self.set.append(element)
        print(f"{element} has been successfully added!")
        self.size += 1

    def remove(self, element) -> None | str:
        for e in range(len(self.set) - 1, -1, -1):
            if self.set[e] == element:
                print(f"Now removing {element}...")
                del self.set[self.set.index(element)]
                print(f"{element} has been successfully removed!")
                self.size -= 1
                return
        return f"{element} was not found for removal."

    def sorted_union_of(self, some_set) -> list:
        union = []
        for index, element in enumerate(self.set):
            if index >= len(some_set):
                union.append(self.set[index])
                continue
            elif some_set[index] in self.set:
                union.append(element)
                continue
            union.append(some_set[index])
            union.append(self.set[index])
        union.sort()
        return union

    def sorted_intersection_of(self, some_set) -> list:
        intersection = []
        for element in some_set:
            if element in self.set and element not in intersection:
                intersection.append(element)
        intersection.sort()
        return intersection


if __name__ == "__main__":

    heavenly_bodies = OrderedSet()

    print(heavenly_bodies.size)

    heavenly_bodies.add(15)
    heavenly_bodies.add(1)
    heavenly_bodies.add(-4)
    heavenly_bodies.add(18)
    heavenly_bodies.add(32)
    heavenly_bodies.add(28)
    heavenly_bodies.add(100)
    heavenly_bodies.add(-100)
    heavenly_bodies.add(-100)
    heavenly_bodies.add(15)
    heavenly_bodies.add(-4)

    print(heavenly_bodies.size)

    print("\n\nOrdered Set:", heavenly_bodies.set)
    print("Some Set:", [8, -15, 15, 100, 1, 1, 1, 1, 2, 3, 4, 5, 6, 28])
    union_set = heavenly_bodies.sorted_union_of([8, -15, 15, 100, 1, 1, 1, 1, 2, 3, 4, 5, 6, 28])
    print("Union (sorted):", union_set)

    print("\n\nOrdered Set:", heavenly_bodies.set)
    print("Some Set:", [8, -15, 15, 100, 1, 1, 1, 1, 2, 3, 4, 5, 6, 28])
    intersection_set = heavenly_bodies.sorted_intersection_of([8, -15, 15, 100, 1, 1, 1, 1, 2, 3, 4, 5, 6, 28])
    print("Intersection (sorted):", intersection_set)
