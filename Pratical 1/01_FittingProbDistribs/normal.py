import numpy as np

def normal(X, mu, sigma):
    """Return likelihood of data given parameters"

    Computes the likelihood that the data X have been generated
    from the given parameters (mu, sigma) of the one-dimensional
    normal distribution.

    Args:
        X: vector of point samples
        mu: mean
        sigma: standard deviation
    Returns:
        a scalar likelihood
    """
    likelihoods = [1 / np.sqrt(2 * np.pi * (sigma ** 2)) * np.exp(-0.5 * ((xi - mu) ** 2) / (sigma ** 2)) for xi in X]
    lik = 1.0
    for l in likelihoods:
        lik *= l
    return lik