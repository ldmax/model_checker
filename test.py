#!/usr/bin/env python3

import pandas as pd

df = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6]
})

print(df)


def add(param_a, param_b):
    """some random function
    """
    return param_a + param_b
