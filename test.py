import time

def 출력(dian):
    print(dian)

def 변수선언(filename, content):
    f = open(filename +".txt", 'w')
    f.write(content)
    f.close()

def 변수불러오기(filename):
    try:
        f = open(filename +".txt", 'r')
        contents = f.read()
        print(contents)
        f.close()
    except:
        print("")

def setInterval(funname,filename,content,timer):
    if funname == "출력":
        while True:
            출력(content)
            time.sleep(int(timer))
    elif funname == "변수선언":
        while True:
            변수선언(filename, content)
            time.sleep(int(timer))
    elif funname == "변수불러오기":
        while True:
            변수불러오기(filename)
            time.sleep(int(timer))


setInterval("출력", "", "테스트", "2")