import math

def get_sets(_data: str):
    _sets = []
    sets_count = math.ceil(len(data) / SET_SIZE)
    for i in range(0, sets_count):
        if i == sets_count - 1:
            _sets.append(_data[i*SET_SIZE..len(data)])
        _sets.append(_data[i*SET_SIZE..(i+1)*SET_SIZE])
    return _sets

SET_SIZE = 8

data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ut arcu tincidunt, pharetra massa sed, " \
       "dictum nibh. Nunc mattis ipsum vel. "
sets = get_sets(data)
