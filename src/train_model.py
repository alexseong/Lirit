from miditransform import midiToStateMatrix
from model import model, n_steps
import numpy as np


def statematrixtoarray(statematrix):
    arr = [[[entry for note in state for entry in note]
            for state in statematrix]]
    arr = np.array(arr)
    return arr


def train(midifile):
    statematrix = midiToStateMatrix(midifile)
    return _train(statematrix)


def _train(statematrix):
    neuralnet = model()
    train = statematrixtoarray(statematrix[0: n_steps])
    test = statematrixtoarray(statematrix[1: n_steps + 1])
    neuralnet.fit(train, test)
    return neuralnet

if __name__ == '__main__':
    neuralnet = train('../data/train/mozart/mz_311_1_format0.mid')