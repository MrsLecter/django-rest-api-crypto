def getAverageCurrencyRate(arr):
    avg = arr[0]
    for item in arr:
        for key in item:
            if (key != 'timestamp') & (key != 'id'):
                avg[key] = float(avg[key]) + float(item[key])
                if key == arr[len(arr)-1]:
                    avg[key] = ( '%.5f' % (float(avg[key])/(len(arr))))

    return avg