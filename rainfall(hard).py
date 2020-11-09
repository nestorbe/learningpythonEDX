def accumulation(hills):
    length_hills = len(hills)
    left = [0] * length_hills
    right = [0] * length_hills
    water = 0

    left[0] = hills[0]
    for i in range(1, length_hills):
        left[i] = max(left[i - 1], hills[i])

    right[length_hills-1] = hills[length_hills-1]
    for i in range(length_hills - 2, -1, -1):
        right[i] = max(right[i + 1], hills[i]);

    for i in range(0, length_hills):
        water += min(left[i], right[i]) - hills[i]

    return water


hills = [2, 5, 3, 4, 3, 2, 5, 5, 3, 4, 2, 2, 2]
print(accumulation(hills))

