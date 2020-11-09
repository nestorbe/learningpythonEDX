def calcStamp(price, available, count=0):
    index = 0

    if price == 0:
        return count

    else:
        if price < available[-1]:
            index -= 1
            return calcStamp(price, available[:index], count)

        else:
            if price >= available[index - 1]:
                price -= available[index - 1]
                count += 1
                return calcStamp(price, available, count)

            else:
                index -= 1

            return calcStamp(price, available[:-1], count)


print(calcStamp(11, [1, 2, 5, 12, 14, 18]))