def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count = [0] * 26
    window_count = [0] * 26
    k = len(s1)

    for i in range(k):
        s1_count[ord(s1[i]) - ord('a')] += 1
        window_count[ord(s2[i]) - ord('a')] += 1

    if s1_count == window_count:
        return True

    for i in range(k, len(s2)):
        window_count[ord(s2[i]) - ord('a')] += 1
        window_count[ord(s2[i-k]) - ord('a')] -= 1

        if s1_count == window_count:
            return True

    return False
