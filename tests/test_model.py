# -*- coding: utf-8 -*-

import pytest
import superEEG as se
import numpy as np
import scipy
import pandas as pd
from superEEG._helpers.stats import get_expanded_corrmat, rbf
import seaborn as sns
from sklearn import datasets

# load example model to get locations
locs = se.load('example_locations')

# number of timeseries samples
n_samples = 1000

# number of subjects
n_subs = 5

# number of electrodes
n_elecs = 10



# simulate correlation matrix
data = [se.simulate_model_bos(n_samples=10000, sample_rate=1000, locs=locs, sample_locs = n_elecs) for x in range(n_subs)]


# make tests for attributes



def test_create_model_1bo():
    model = se.Model(data=data[0], locs=locs)
    assert isinstance(model, se.Model)

def test_create_model_2bo():
    model = se.Model(data=data[0:2], locs=locs)
    assert isinstance(model, se.Model)

def test_create_model_superuser():
    locs = np.random.multivariate_normal(np.zeros(3), np.eye(3), size=10)
    numerator = scipy.linalg.toeplitz(np.linspace(0,10,len(locs))[::-1])
    denominator = np.random.multivariate_normal(np.zeros(10), np.eye(10), size=10)
    model = se.Model(numerator=numerator, denominator=denominator, locs=locs, n_subs=2)
    assert isinstance(model, se.Model)

def test_model_predict():
    model = se.Model(data=data[0:2], locs=locs)
    bo = model.predict(data[0])
    assert isinstance(bo, se.Brain)

def test_update():
    model = se.Model(data=data[0:2], locs=locs)
    mo = model.update(data[0])
    assert isinstance(mo, se.Model)

### need to finish this test I think and put it in test helpers
# def test_expand_corrmat():
#     R = scipy.linalg.toeplitz(np.linspace(0, 1, 3)[::-1])
#     model_locs = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
#     subject_locs = np.array([[0,0,3], [0,0,4]])
#     weights = rbf(np.vstack([model_locs, subject_locs]), model_locs, width=2)
#     fit_num, fit_denom = get_expanded_corrmat(R, weights)
