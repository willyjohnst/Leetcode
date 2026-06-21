class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # So need to remove minimum intervals 
        # Since its minimum intervals to be non-overlapping I can safely ignore all non-overlapping
        # But that requires a full pass so seems wrong

        # So I have intervals between -5*10^4 and 5*10^4 
        # and need to remove enough so they are non-overlapping

        # so if j = [j_start, j_end] and i = [i_start, i_end]
        # if j_start > i_start and j_start < i_end then its overlapping
        # if j_end > i_start and j_end < i_end
        # if both above are true, its entirely inside the other so remove the larger one
        
        # above is bandage, edge case solution. Need to think in terms of algorithm
        # Can I do two pointers? 
        # Go over list get edges of intervals, move in?
        # No, I think actually, making it a graph problem is the move 
        # So imagining having a graph where we group the intervals over a certain space in a node
        # then sub nodes until we get to just that interval
        # Seems needlessly complex not the solution

        # The problem is some portion of the intervals overlap and need to remove them
        # How can I frame the problem to examine that
        # Thinking mentally of number lines, series' of number lines
        # Can I just keep a counter of # intervals overlapped for each interval
        # Then when we remove one, decrement those intervals?
        # Rather, keep a list for each interval
        # So a dict of lists for each interval of what they overlap with
        # Then on decrementing, remove that item
        # So for [[1,2],[2,3],[3,4],[1,3]]
        # {(1,2):[[1,3]], (2,3):[[1,3]], (3,4):[], (1,3):[[1,2],[2,3]]}
        # Since len((1,3)) = 2 > len((1,2)), len((2,3))

        # So this requires us to increment over this each time, bit inefficient
        # Rather, could keep a list of [(tuple), # overlaps], then the dict to get the overlaps?
        # And this list is sorted.
        # So we just greedily remove the list elements with the most overlap until list.top is 0
        # Acutally don't like removing elements, creates new list, so maybe just pointer = 0?

        # So just need some way to update this list now
        # I like a dict, can I get sorted key:value pairs? sorted by len list?
        # So sorted(dict.values, key=len) then start at top and update other tuples in the list, then resort list?

        # All this resorting seems incredibly wasteful 
        # I need a way to remove the items then know which one is next without sorting
        # Idk, can maybe just drop all 0's from list but thats just trimming not good enough. Algorithm seems wrong

        intervals.sort(key = lambda x: x[1])

        out_intervals = [intervals[0]]

        for interval in intervals:
            if out_intervals[-1][1] <= interval[0]:
                out_intervals.append(interval)

        print(out_intervals)
        return len(intervals) - len(out_intervals)

        # this is correct, but a bit silly. The question asks for only the number of intervals we need to remove, 
        # so we don't need to keep all of this
        # instead, we should just keep track of the intervals_removed


        def eraseOverlapIntervalsOptimal(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])

        intervals_removed = 0
        curr_highest = intervals[0][1]

        for interval in intervals[1:]:
            # if the start is after the end of the highest we are keeping
            if curr_highest <= interval[0]:
                curr_highest = interval[1]
            else: 
                intervals_removed += 1

        return intervals_removed
