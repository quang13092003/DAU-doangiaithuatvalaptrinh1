class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start

        path = sum(distance[start:destination])
        total = sum(distance)

        return min(path, total - path)