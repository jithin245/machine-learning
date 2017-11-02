#!/usr/bin/python
import itertools

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    straighten = lambda data: list(itertools.chain.from_iterable(data))
    error_lambda = lambda pred, net_worth: (pred-net_worth)**2
    ### your code goes here

    parsed_data = [(age, net_worth, error_lambda(pred, net_worth)) 
                         for pred, age, net_worth in 
                            zip(straighten(predictions), straighten(ages), straighten(net_worths))]

    cleaned_data_len = int(0.9*len(predictions))
    cleaned_data =  sorted(parsed_data, key=lambda data: data[2])[:cleaned_data_len]
    return cleaned_data

