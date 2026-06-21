class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # so last time the solution was to organize by end times and remove the offending intervals
        # since this is merge if there is a conflict = merge?

        def sort_by_end(interval):
            return interval[-1]

        intervals.sort(key=sort_by_end)

        out_intervals = [intervals[0]]  
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] >= intervals[i][0]:

                curr_interval = intervals[i]
                while out_intervals and curr_interval[0] <= out_intervals[-1][1]:
                    start_i = min(out_intervals[-1][0], intervals[i - 1][0], intervals[i][0])
                    curr_interval = [start_i, intervals[i][1]]

                    out_intervals.pop()
                out_intervals.append(curr_interval)
            else:
                out_intervals.append(intervals[i])

        return out_intervals

    # Above is good, but don't need the while loop inside the for loop
    # Need to sort by start times for merge, rather than end times for remove
    def mergeOptimal(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        out_intervals = [intervals[0]]  
        for i in range(1, len(intervals)):
            if intervals[i][0] <= out_intervals[-1][1]:
                end_interval = max(intervals[i][1], out_intervals[-1][1])
                out_intervals[-1][1] = end_interval
            else: 
                out_intervals.append(intervals[i])

        return out_intervals