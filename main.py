
from programs import interative, except_master

programList = [
  interative.delete,
  except_master.delete,
]


# programNo = input("\n 1. 交互式删除 \n 2. 只保留master \n 3. 输入保留分支，其它都删除 \n 请输入编号选择（默认0）：")
programNo = input("\n 1. interative delete (recommanded) \n 2. keep master, delete others \n input number for chosing program (default 1): ")
if programNo == '':
  programNo = 0
else:
  try:
    programNo = int(programNo)
  except Exception:
    print("illegal input")
    exit()

if programNo > len(programList):
  print("illegal input")
  exit()

program = programList[programNo]

program()