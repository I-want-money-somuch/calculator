#计算机
import subprocess
print('仅支持两个数字加减乘除')
print('按1选择加法,按2选择减法,按3选择乘法,按4选择除法')
while True:
    try:
        a = int(input())
        if a in [1,2,3,4]:
            break
        else:
            print('请输入1-4去选择')
    except ValueError:
        print('请输入数字')
if a == 1:
    print('请输入第一个数字')
    while True:
        try:
            fir= float(input())
            break
        except ValueError:
            print('请输入数字')
    print('请输入第二个数字')
    while True:
        try:
            sec= float(input())
            break
        except ValueError:
            print('请输入数字')
    print('好了正在运行中')
    ans=fir+sec
    ans=str(ans)
    ans='答案是'+ans
    print(ans)
if a == 2:
    print('请输入第一个数字')
    while True:
        try:
            fir= float(input())
            break
        except ValueError:
            print('请输入数字')
    print('请输入第二个数字')
    while True:
        try:
            sec= float(input())
            break
        except ValueError:
            print('请输入数字')
    print('好了正在运行中')
    ans=fir-sec
    ans=str(ans)
    ans='答案是'+ans
    print(ans)
if a == 3:
    print('请输入第一个数字')
    while True:
        try:
            fir= float(input())
            break
        except ValueError:
            print('请输入数字')
    print('请输入第二个数字')
    while True:
        try:
            sec= float(input())
            break
        except ValueError:
            print('请输入数字')
    print('好了正在运行中')
    ans=fir*sec
    ans=str(ans)
    ans='答案是'+ans
    print(ans)
if a == 4:
    print('请输入第一个数字')
    while True:
        try:
            fir= float(input())
            if fir ==0:
                print('0不能作为除数，请重新输入')
            else:
                break
        except ValueError:
            print('请输入数字')
    print('请输入第二个数字')
    while True:
        try:
            sec= float(input())
            if sec ==0:
                print('0不能作为除数，请重新输入')
            else:
                break
        except ValueError:
            print('请输入数字')
    print('好了正在运行中')
    print('你要不要余数(1=要,2=不要)')
    while True:
        try:
            Y = int(input())
            if Y > 2 or Y < 1:
                print('请输入1-2来选择')
            else:
                break
        except ValueError:
            print('请输入整数字')
    if Y == 1:
        ans=fir//sec
        R=fir%sec
        ans=str(ans)
        if R == 0:
            print('没有余数')
            ans = '答案是'+ans
            print(ans)
        else:
            R=str(R)
            ans='答案是'+ans+'余'+R
            print(ans)
    elif Y == 2:
        ans=fir/sec
        ans=str(ans)
        ans = '答案是'+ans
        print(ans)
subprocess.run(["python","restart.py"])
#这个代码用来运行同目录的另一个代码
