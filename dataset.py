from PIL import Image
import numpy as np


def get_dataset():
    path = "train_data_formatted.png"

    # load img
    img = Image.open(path).convert("L")
    # convert to two dimensional array
    arr = np.array(img)

    size = img.size
    print(size)

    h = size[1]
    w = size[0]


    d2 = []

    for i in range(h):
        row = []
        for j in range(w):
            if arr[i][j] >= 200:
                row.append(1)
            else:
                row.append(0)

        d2.append(row)

    dt = []

    # высота в 10 цифр 0-9
    for h in range(10):
        nums = []
        # ширина в 10 цифр одного типа
        for w in range(10):
            num = []
            # высота в пикселях одного сектора
            for i in range(5):
                row = []
                # ширина в пикселях одного сектора
                for j in range(3):
                    if arr[h * 5 + i][w * 3 + j] == 255:
                        row.append(1)
                    else:
                        row.append(0)

                num.append(row)
            nums.append(num)
        dt.append(nums)

    return dt

if __name__ == '__main__':
    print(get_dataset())
