class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        catchers = []
        people = []

        for index, value in enumerate(team):
            if value == 1:
                catchers.append(index)
            else:
                people.append(index)

        i = j = caught = 0

        while i < len(catchers) and j < len(people):
            if abs(catchers[i] - people[j]) <= dist:
                caught += 1
                i += 1
                j += 1
            elif people[j] < catchers[i]:
                j += 1
            else:
                i += 1

        return caught


