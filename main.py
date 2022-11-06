import numpy as np
import dataset

X = [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]

one = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

four = [
    [0, 0, 0],
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1]
]

eight = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

eight2 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

y = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
syn0 = 2 * np.random.random((15, 10)) - 1
syn1 = 2 * np.random.random((10, 10)) - 1

data = dataset.get_dataset()


def train(inps, idls):
    global syn0, syn1

    inps = np.array([sum(inps, [])])

    l1 = 1 / (1 + np.exp(-(np.dot(inps, syn0))))
    l2 = 1 / (1 + np.exp(-(np.dot(l1, syn1))))
    l2_delta = (idls - l2) * (l2 * (1 - l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))

    if (j % 100) == 0:
        print("Error:" + str(np.mean(np.abs(idls - l2))))

    syn1 += l1.T.dot(l2_delta)
    syn0 += inps.T.dot(l1_delta)


print(data[1][0])

for j in range(60):

    for h in range(10):
        y = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        for w in range(10):
            y[0][h] = 1
            train(data[h][w], y)


# input your number
minp = np.array([sum(four, [])])
tl1 = 1 / (1 + np.exp(-(np.dot(minp, syn0))))
tl2 = 1 / (1 + np.exp(-(np.dot(tl1, syn1))))
from PIL import Image
import numpy as np


def get_dataset():
    path = "trainset.png"
    path2 = "/storage/emulated/0/Download/neuralNet/mnist.png"

    p3 = "/storage/emulated/0/Download/neuralNet/1_Ft2rLuO82eItlvJn5HOi9A.png"

    img = Image.open(path).convert("L")

    arr = np.array(img)

    size = img.size
    print(size)

    h = size[1]
    w = size[0]

    data = []

    d2 = []

    for i in range(h):
        row = []
        for j in range(w):
            if arr[i][j] == 255:
                row.append(1)
            else:
                row.append(0)

        d2.append(row)

    dt = []

    for h in range(10):
        nums = []
        for w in range(10):
            num = []
            for i in range(5):
                row = []
                for j in range(3):
                    if arr[h * 5 + i][w * 3 + j] == 255:
                        row.append(1)
                    else:
                        row.append(0)

                num.append(row)
            nums.append(num)
        dt.append(nums)

    return dt


#print(get_dataset())

ml2 = tl2.tolist()
bg = max(ml2[0])
print(bg)
ind = ml2[0].index(bg)
print("your number is: ", ind)
print(ml2)