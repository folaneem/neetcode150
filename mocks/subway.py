# London underground,
# swipe in (userId, location, time), swipe out( userId, location, time)
# get average (start, destination) -> avg time between the two stations
# For example, swipe_in(1, liverpool, 20), swipe_out(1, bank, 25), swipe_in(2, liverpool, 10), swipe_out(2, woolich, 25)
# overall_ave = {liverpool : {'bank': (5, 1), woolich:(15, 1) }}}
# overall_ave = {liverpool_bank : (5, 1), liverpool_woolich: (15, 1) }

# swipe_in = {1 :(liverpool, 20)}


class LondonUnderground:
    def __init__(self):
        self.swipes = {}
        self.distances = {}

    def swipe_in(self, user_id, location, time):
        self.swipes[user_id] = (location, time)

    def swipe_out(self, user_id, location, time):
        if user_id not in self.swipes:
            return
        loc, t = self.swipes.get(user_id)
        start_dest = loc + "_" + location
        user_dist = time - t
        if start_dest not in self.distances:
            self.distances[start_dest] = (user_dist, 1)
        else:
            current_total_distance, counts = self.distances[start_dest]
            self.distances[start_dest] = (current_total_distance + user_dist, counts + 1)
        del self.swipes[user_id]

    def get_average(self, start, destination):
        start_dest = start + "_" + destination
        if start_dest not in self.distances:
            return None
        total_distance, counts = self.distances[start_dest]
        return total_distance // counts
# swipes = {1: (livpool, 20)}
# distances = {liverpool_bank: (5, 1)}
# user_id =
# user_DIST = 5
# location = bank
# time =
# loc = liverpppol
# t =  20
# start_dist = liverpool_bank
# start= loiverppo, destiona = bank
# total_distanc = 5, coounts 1
# 5
