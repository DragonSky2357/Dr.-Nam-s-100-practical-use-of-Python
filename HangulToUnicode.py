'''
한글 = ((초성 * 21)+중성)*28+종성+44032

초성 = ((x-44032)/28)/21
중성 = ((x-44032)/28)%21
종성 = (x-44032)%28
'''
CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
       "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
        "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ",
        "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅌ", "ㅍ", "ㅎ"]


def break_korean(string):
    word_list = list(string)
    break_word = []

    for data in word_list:
        if ord(data) >= ord("가") and ord(data) <= ord("힣"):
            # 유니코드상 인덱스
            char_index = ord(data)-ord('가')

            # 초성 = ((x-44032)/28)/21
            index = int((char_index/28)/21)
            break_word.append(CHO[index])

            # 중성 = ((x-44032)/28)%21
            index = int((char_index/28) % 21)
            break_word.append(JUNG[index])

            # 종성 = (x-44032)%28
            index = int(char_index % 28)

            if index > 0:
                break_word.append(JONG[index])
        else:
            break_word.append(data)

    return break_word
