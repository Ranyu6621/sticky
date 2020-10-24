import csv
import datetime
today = datetime.datetime.now()

filename = 'G:\\python\\sticky\\data.csv' 
# type = 번호, 제목, 내용, 날짜, 시간, 고정, 삭제
#         1     ㅈ   ㄴ    ㄴ    ㅅ    t    t
# date = today()
# time = time()
# 고정 = False
# del = false

# 메모리스트 확인
def listmemo():
    f = open(filename ,'r',encoding="utf-8",newline="")
    rdr = csv.reader(f)
    for line in rdr:
        print(line)
    f.close()
# 메모 시리얼 넘버링
def get_index(): 
    f = open(filename,'r',encoding="utf-8",newline="")
    reader = csv.reader(f)
    find_index = []
    for line in reader:
        find_index.append(int(line[0]))
    f.close()
    got_index = int(max(find_index)+1)
    return got_index
# 메모 작성
def writememo(number, title, contents,date,time):
    f = open(filename ,'a',encoding="utf-8",newline="")
    wr = csv.writer(f)
    wr.writerow([number, title, contents,date,time])
    f.close()
def date():
    date = today.strftime('%Y-%m-%d')
    return date
def time():
    time = today.strftime('%H:%M:%S')
    return time

# def delermemo()
# number, title, contents = input().split(",")
# number = int(number)

# print(time())
title = input("제목을 입력하세요 : ")
contents = input("내용을 입력하세요 : ")

writememo(get_index(), title, contents,date(),time())

#문제1 - data.csv가 비어있을 때 입력이 안됨
#해결1 
# if not find_index : -> find_index가 비었으면
#     find_index.append([1])
# else : -> find_index가 비지 않았으면
#         for line in reader:
#         find_index.append(int(line[0]))
#     f.close()
#     got_index = int(max(find_index)+1)
#     return got_index

# 새로운 코멘트
