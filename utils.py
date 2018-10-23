import pickle


def serialize_to_string(data_object):
    return pickle.dumps(data_object)


def parse_from_string(byte_string):
    return pickle.loads(byte_string)


def string_to_segments(byte_string, mss):
    segments = []
    for i in range(0, len(byte_string), mss):
        segments.append(byte_string[i: i + mss])
    return segments


def string_from_segments(seg_list):
    return b''.join(seg_list)
