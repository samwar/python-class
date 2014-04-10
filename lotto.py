#!/usr/bin/env python2
# -*- coding: utf-8 -*-

DRAWS_PER_YEAR = 104
RANDOM_MIX = 20
DEFAULT_NUM_BALLS = 54
DEFAULT_YEARS = 1
DEFAULT_NUM_PICKS = 6


class InvalidSelectionCount(object):
    pass


class InvalidSelectionType(object):
    pass


class InvalidSelectionRange(object):
    pass


class LotteryDrawing(object):
    def __init__(self, max_ball_number, years, picks):
        self.max_ball_number = max_ball_number
        self.years = years
        self.picks = picks
        self.elapsed = 0.0
        self.results = {}
        self.drawings = years * 104
        self.quick_pick = False

    def _pick_numbers(self):
        import random

        random.seed()
        return random.sample(range(1, self.max_ball_number + 1), len(self.picks))

    def run_simulation(self):
        for i in range(self.drawings + 1):
            import time

            start_time = time.time()
            lotto_picks = set(self._pick_numbers())
            matching_balls = len(lotto_picks.intersection(self.picks))

            # self.results.update(matching_balls)
            self.results[matching_balls] += 1
            self.elapsed = time.time() - start_time

    @staticmethod
    def _calc_odds(max_num_balls=DEFAULT_NUM_BALLS, num_picks=DEFAULT_NUM_PICKS):
        rng = []
        for i in range(num_picks):
            rng.append(max_num_balls - i)
        odds = reduce(lambda a, b: a * b, rng)
        return odds

    def print_results(self, lottery_drawing):
        # import string
        picks = lottery_drawing.picks
        picks_length = len(picks)
        odds = self._calc_odds(lottery_drawing.max_ball_number, picks_length)
        # picks = string.join(map(str, pick_info["picks"]), ", ")
        picks_str = ", ".join([str(val) for val in picks])
        percentage = []

        for k, v in lottery_drawing.results.iteritems():
            percentage.append(v * 100.0 / lottery_drawing.drawings)

        print "Results for {0} - {1} out of {4}\n" \
              "Selected numbers: {3}\n" \
              "Odds of matching all numbers 1 in {2}\n" \
              "\n" \
              "# Matches   Count    Percentage\n" \
              "=========   =====    ==========".format(lottery_drawing.drawings,
                                                       picks_length,
                                                       odds,
                                                       picks_str,
                                                       lottery_drawing.max_ball_number)

        for i in range(len(picks)):
            print "   {0}         {1:>2}       {2:>6.3f}" \
                .format(i,
                        lottery_drawing.results.get(i),
                        percentage[i])

        print "\nRan {1} simulations in {2:.3f} seconds\n" \
              "For a twice-a-week lotto system, that would be the equivalent\n" \
              "of {0:.2f} years of drawings\n" \
            .format(lottery_drawing.year, lottery_drawing.drawings, lottery_drawing.elapsed)
