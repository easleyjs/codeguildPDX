"""
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    """
    >>> print(peaks(data))
    [6, 14]
    """
    return [i for i in range(1, len(data)-1) if (data[i] > data[i-1]) & (data[i] > data[i+1])]


def valleys(data):
    """
    >>> print(valleys(data))
    [9, 17]
    """
    return [i for i in range(1, len(data)-1) if (data[i] < data[i-1]) & (data[i] < data[i+1])]


def peaks_and_valleys(data):
    """
    >>> print(peaks_and_valleys(data))
    [6, 9, 14, 17]
    """
    return sorted(peaks(data) + valleys(data))


def printGraph(data):
    """
    """
    graphString = ""
    for i in range(max(data), 0, -1):
        for j in data:
            if j >= i:
                graphString += "X "
            else:
                graphString += "  "
        graphString += "\n"
    return graphString
