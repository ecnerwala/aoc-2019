# Advent of Code 2019 Speedrun

This is my code from a speedrun on December 28, 2020 of [Advent of Code 2019](https://adventofcode.com/2019),
an Advent calendar of programming puzzles run in December each year. I solved
all 25 days from scratch (with 2 parts per day) in 6 hours, 44 minutes, and 52
seconds. The run was almost blind; I had previously solved the first 4 days and
also have peeked at some of the other problems sometime last year.

You can find a recording of the livestream on [Twitch](https://www.twitch.tv/videos/854280596).

Most of my code is in Python3, but I used C++ for some select problems with
tighter runtimes. I also used a spreadsheet for day 25, replicated here.

These are my final splits. Times were computed using server-side
submission times from the private-leaderboard API, falling back to my splits
and video for the first 4 days. Rank and Score are computed against the public
leaderboard as if I had taken part live.

| Day | Part | Part Time | Day Time | Total Time | Rank | Score |
|:--- |:---- | ----------:| ---------:| -----------:| ----------------:| ------:|
| Day 1 | Part 1 | 00:56 | 00:56 | 00:00:56 | 26 | 75 |
| Day 1 | Part 2 | 01:01 | 01:57 | 00:01:57 | 6 | 95 |
| Day 2 | Part 1 | 06:51 | 06:51 | 00:08:48 | >100 | 0 |
| Day 2 | Part 2 | 03:12 | 10:03 | 00:12:00 | 75 | 26 |
| Day 3 | Part 1 | 03:03 | 03:03 | 00:15:03 | 2 | 99 |
| Day 3 | Part 2 | 01:12 | 04:15 | 00:16:15 | 1 | 100 |
| Day 4 | Part 1 | 02:24 | 02:24 | 00:18:39 | 45 | 56 |
| Day 4 | Part 2 | 00:46 | 03:10 | 00:19:25 | 7 | 94 |
| Day 5 | Part 1 | 10:44 | 10:44 | 00:30:09 | 27 | 74 |
| Day 5 | Part 2 | 03:28 | 14:12 | 00:33:37 | 16 | 85 |
| Day 6 | Part 1 | 04:00 | 04:00 | 00:37:37 | 27 | 74 |
| Day 6 | Part 2 | 02:15 | 06:15 | 00:39:52 | 7 | 94 |
| Day 7 | Part 1 | 03:32 | 03:32 | 00:43:24 | 2 | 99 |
| Day 7 | Part 2 | 13:10 | 16:42 | 00:56:34 | 11 | 90 |
| Day 8 | Part 1 | 02:34 | 02:34 | 00:59:08 | 13 | 88 |
| Day 8 | Part 2 | 02:14 | 04:48 | 01:01:22 | 3 | 98 |
| Day 9 | Part 1 | 06:15 | 06:15 | 01:07:37 | 10 | 91 |
| Day 9 | Part 2 | 00:25 | 06:40 | 01:08:02 | 10 | 91 |
| Day 10 | Part 1 | 03:59 | 03:59 | 01:12:01 | 2 | 99 |
| Day 10 | Part 2 | 08:13 | 12:12 | 01:20:14 | 1 | 100 |
| Day 11 | Part 1 | 09:30 | 09:30 | 01:29:44 | 64 | 37 |
| Day 11 | Part 2 | 01:58 | 11:28 | 01:31:42 | 26 | 75 |
| Day 12 | Part 1 | 08:37 | 08:37 | 01:40:19 | 42 | 59 |
| Day 12 | Part 2 | 08:01 | 16:38 | 01:48:20 | 5 | 96 |
| Day 13 | Part 1 | 03:12 | 03:12 | 01:51:32 | 84 | 17 |
| Day 13 | Part 2 | 10:09 | 13:21 | 02:01:41 | 16 | 85 |
| Day 14 | Part 1 | 14:30 | 14:30 | 02:16:11 | 17 | 84 |
| Day 14 | Part 2 | 01:26 | 15:56 | 02:17:37 | 8 | 93 |
| Day 15 | Part 1 | 12:20 | 12:20 | 02:29:57 | 10 | 91 |
| Day 15 | Part 2 | 00:57 | 13:17 | 02:30:54 | 1 | 100 |
| Day 16 | Part 1 | 06:16 | 06:16 | 02:37:10 | 7 | 94 |
| Day 16 | Part 2 | 11:25 | 17:41 | 02:48:35 | 1 | 100 |
| Day 17 | Part 1 | 06:10 | 06:10 | 02:54:45 | 46 | 55 |
| Day 17 | Part 2 | 26:08 | 32:18 | 03:20:53 | 30 | 71 |
| Day 18 | Part 1 | 39:11 | 39:11 | 04:00:04 | 77 | 24 |
| Day 18 | Part 2 | 05:46 | 44:57 | 04:05:50 | 8 | 93 |
| Day 19 | Part 1 | 02:13 | 02:13 | 04:08:03 | 18 | 83 |
| Day 19 | Part 2 | 22:22 | 24:35 | 04:30:25 | 75 | 26 |
| Day 20 | Part 1 | 17:40 | 17:40 | 04:48:05 | 35 | 66 |
| Day 20 | Part 2 | 10:21 | 28:01 | 04:58:26 | 14 | 87 |
| Day 21 | Part 1 | 12:39 | 12:39 | 05:11:05 | 52 | 49 |
| Day 21 | Part 2 | 26:43 | 39:22 | 05:37:48 | >100 | 0 |
| Day 22 | Part 1 | 09:57 | 09:57 | 05:47:45 | 61 | 40 |
| Day 22 | Part 2 | 06:10 | 16:07 | 05:53:55 | 2 | 99 |
| Day 23 | Part 1 | 05:38 | 05:38 | 05:59:33 | 10 | 91 |
| Day 23 | Part 2 | 07:33 | 13:11 | 06:07:06 | 24 | 77 |
| Day 24 | Part 1 | 05:46 | 05:46 | 06:12:52 | 12 | 89 |
| Day 24 | Part 2 | 11:56 | 17:42 | 06:24:48 | 4 | 97 |
| Day 25 | Part 1 | 19:59 | 19:59 | 06:44:47 | 29 | 72 |
| Day 25 | Part 2 | 00:05 | 20:04 | 06:44:52 | 25 | 76 |
| **Total** |  |  |  | **06:44:52** | **1** | **3754** |
