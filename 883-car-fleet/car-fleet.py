class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]

        fleet = []
        for p, s in sorted(cars) [::-1]:
            fleet.append((target - p) / s)

            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        
        return len(fleet)