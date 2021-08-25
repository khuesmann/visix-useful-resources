import numpy as np


def mds(d, dimensions=3):
    (n, n) = d.shape
    E = (-0.5 * d ** 2)

    Er = np.mat(np.mean(E, 1))
    Es = np.mat(np.mean(E, 0))

    F = np.array(E - np.transpose(Er) - Es + np.mean(E))

    [U, S, V] = np.linalg.svd(F.astype(np.float64), full_matrices=True, hermitian=True)

    Y = U * np.sqrt(S)

    return (Y[:, 0:dimensions], S[0:dimensions])
