
from programs import interative

programList = [
  interative.delete,
]


programNo = input("\n 0. 交互式删除 \n 1. 只保留master \n 2. 输入保留分支，其它都删除 \n 请输入编号选择（默认0）：")
if programNo == '':
  programNo = 0

program = programList[programNo]

program()