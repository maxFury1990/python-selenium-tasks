import logging


def substring(s):
    ans, temp = 1, 1
    logging.info("get len of the string and walk through")
    for i in range(1, len(s)):
        logging.info(f"if character {s[i]} is the same as previous increase temp value +1")
        if s[i] == s[i - 1]:
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 1
    logging.info(f"get the biggest number between {ans} and {temp}")
    ans = max(ans, temp)
    return ans


def test_substring():
    print(substring("sdffffqe"))
    print(substring("ddvvrwwwrggg"))

