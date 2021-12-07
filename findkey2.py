from sys import argv
from collections import Counter


def lungimea(bytearr, maxlen):
    shifted_arrs = []
    for shift in range(1, maxlen + 1):
        shifted_arrs.append(shiftare(bytearr, shift))
    matches = [[0, 0]]
    for shift in range(1, maxlen + 1):
        matches.append([potriviri(bytearr, shifted_arrs[shift - 1]), shift])
    matches.sort(reverse=True)

    prob_lens_rep = []
    prev_prc = 0
    for match in matches[1:]:
        curr_prc = match[0]
        if curr_prc < prev_prc * 0.8:
            break
        prob_lens_rep.append(match)
        prev_prc = curr_prc

    prob_lens_rep.sort(key=lambda prob_lens_rep: prob_lens_rep[1])
    prob_lens = [prob_lens_rep[0]]
    for len1 in prob_lens_rep[1:]:
        tg = True
        for len2 in prob_lens:
            if len1[1] % len2[1] == 0: tg = False
        if tg:
            prob_lens.append(len1)
    return sorted(prob_lens, reverse=True)


def shiftare(bytearr, shift):
    return bytearr[shift:] + bytearr[:shift]


def potriviri(source, shifted):
    cnt = 0
    for i in range(len(source)):
        if source[i] == shifted[i]: cnt += 1
    return int(cnt / len(source) * 1000) / 10


def parola(text, key_len, most_common_byte=32):
    key = bytearray([0] * key_len)
    for st_idx in range(key_len):
        keyspace_text = []
        keyspace_dict = {}
        for idx in range(st_idx, len(text), key_len):
            keyspace_text.append(text[idx])
        most_common_found = Counter(keyspace_text).most_common(1)[0][0]
        key[st_idx] = most_common_byte ^ most_common_found
    return key

input_file = None
maxlen = None
keylen = None
key = None
most_frequent = 32

i = 0
while i < len(argv):
    arg = argv[i]
    if arg in ("-i", "--input-file"):
        i += 1
        input_file = argv[i]
    if arg in ("-m", "--maxlen"):
        i += 1
        maxlen = int(argv[i])
    if arg in ("-f", "--most-frequent"):
        i += 1
        most_frequent = int(argv[i])
    i += 1

source_text = open(input_file, 'rb').read()

if maxlen:
    prob_lens = lungimea(source_text, maxlen)
    print("Probable key lengths: ")
    for prc, length in prob_lens:
        print("   ", length, " - ", prc, "%", sep='')
    keylen = prob_lens[0][1]
if keylen:
    key = parola(source_text, keylen, most_frequent)
    print("Found a key:", key.decode("utf-8"))



