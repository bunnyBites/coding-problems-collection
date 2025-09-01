def prepare_sorted_square_array(array):
  arrLen = len(array)
  answer = [0] * arrLen

  start = 0
  end = arrLen - 1

  for idx in reversed(range(arrLen)):
    print (idx)
    startValue = abs(array[start])
    endValue = abs(array[end])

    if startValue > endValue:
      answer[idx] = startValue ** 2
      start += 1
    else:
      answer[idx] = endValue ** 2
      end -= 1

  return answer
