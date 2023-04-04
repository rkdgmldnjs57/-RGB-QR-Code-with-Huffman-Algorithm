import cv2                                                                  #opencv 영상처리 라이브러리
import numpy as np
import Huffman_Quinary_4_RGBQR as hq                                        #직접 제작한 5진 허프만 코드 라이브러리?

NOTATION = '0123456789ABCDEF'
def numeral_system(number, base):                                           #5진수 변환용
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

def red(x, y) :                                                             #해당 픽셀 색 설정
    img.itemset((y, x, 2), 255)

def green(x, y) :
    img.itemset((y, x, 1), 255)

def blue(x, y) :
    img.itemset((y, x, 0), 255)

def black(x, y) :
    pass

def white(x, y) :
    img.itemset((y, x, 0), 255)
    img.itemset((y, x, 1), 255)
    img.itemset((y, x, 2), 255)

def zeroadd(num ,string) :
    while(len(string)<num) :
        string = '0' + string
    return string

sentence = input()
(dict, encode) = hq.Huffman_encode(sentence)                                #문자열 입력받아 허프만 인코드 함수 호출

maxlen = 0
minlen = 10
Data = []
DivData = []
dictstr = ''

for (key, val) in dict.items() :
    if key == '' :
        continue
    if maxlen < len(val) :
        maxlen = len(val)
    if minlen > len(val) :
        minlen = len(val)

dictstr = dictstr + str(maxlen) + str(minlen)
for (char, code) in dict.items() :                                          #허프만 코드 딕셔너리 부분을 QR코드 앞부분에 저장
    if char == '' :
        continue
    charQ = numeral_system(ord(char)-32, 5)                                 #char의 ASCII 값을 5진수로 변환, 4자리
    dictstr = dictstr + zeroadd(3, charQ)
    dictstr = dictstr + zeroadd(maxlen, code)

string = dictstr + zeroadd(3+maxlen,'0') + encode                             #딕셔너리 입력 후 0000000으로 경계 표시하고 뒤의 5진 인코드 문자열까지 합침
length = len(string)
size = int(length**0.5+1)
print(string)
f = open("save.txt", 'w')                                                   #영상처리 능력이 딸려서 QR코드 해독 대신 문자열로 저장..
f.write(string)
f.close()

#opencv 시작
img = np.zeros((size, size, 3), np.uint8)                                   #qr코드 담을 빈 넘파이 배열 생성
cnt = 0

for y in range(size) :                                                      #배열 전체 돌며 픽셀 별 데이터 입력
    for x in range(size) :                 
        if cnt<length :                                                     #초과 입력 방지
            color = int(string[cnt])
            cnt+=1
        else :
            break
        if color == 0 :
            black(x, y)
        elif color == 1 :
            white(x, y)
        elif color == 2 :
            red(x, y)
        elif color == 3 :
            green(x, y)
        elif color == 4 :
            blue(x, y)
    
if size**2 < length :
    print('Size error')
bigimg = cv2.resize(img, dsize = (500, 500), interpolation = cv2.INTER_NEAREST)     #qr 코드 (500, 500) 으로 확대
cv2.imwrite('images/save.png', bigimg)                                              #.png 저장
cv2.imshow('Image', bigimg)                                                         #qr코드 표시

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/save.png', bigimg)                                              #.png 저장
print('Saved')