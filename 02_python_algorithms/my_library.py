import math
import pandas as pd


def wuzzle(number):
    """
    The wuzzle function manipulates a number in a magic way and returns the result.
    """

    import math

    return math.sqrt(number * 1.2)


def square(number):
    """
    Squares a number by multiplying it with itself  and returns its result.
    """

    return number * number


def euclidean_distance_1d(p, q):
    """
    Takes tuples of points as input and calculates the distance between them in a
    pairwise fashion. Then returns a pandas dataframe containing the original points
    data and the euclidean distance between them
    """

    distance_dict = {"point_p": [], "point_q": [], "Euc_distance": []}

    for point_p, point_q in zip(p, q):
        distance = math.sqrt(pow((point_p - point_q), 2))
        distance_dict["point_p"].append(point_p)
        distance_dict["point_q"].append(point_q)
        distance_dict["Euc_distance"].append(distance)

    distance_df = pd.DataFrame(distance_dict)

    return distance_df
