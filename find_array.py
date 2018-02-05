to_be_found = [1, 3, 4]


def is_array_inside(in_array, to_be_found):
    tries = len(to_be_found) - 1  # why?
    while in_array:
        try:
            pos = in_array.index(to_be_found[0])
            for i in range(tries):
                pos += 1
                if in_array[pos] == to_be_found[i+1]:
                    if i < tries:
                        continue
                    else:
                        return True
                else:
                    in_array = in_array[pos:]
                    break
        except ValueError:
            return False


def is_array_inside2(in_array, to_be_found):
    tries = len(to_be_found) - 1  # why?
    while in_array:
        try:
            pos = in_array.index(to_be_found[0])
            for i in range(tries):
                if in_array.index(to_be_found[i+1]) == i + 1:
                    continue
                else:
                    in_array = in_array[pos+1:]
                    break
        except ValueError:
            return False


def find_array(sub, in_arr):
    """Return True if array `sub` appears in sequence in array `in_arr`.

    Otherwise return False.
    """
    while in_arr:
        res = []
        for item in sub:

            try:
                res.append(in_arr.index(item))
            except ValueError:
                return False

        if res == range(res[0], res[-1]+1):
            return True
        else:
            in_arr = in_arr[sub[0]:]
    return False
