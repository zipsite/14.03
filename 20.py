from statistics import mean
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return mean(numbers)