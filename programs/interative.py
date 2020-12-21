
import os
import subprocess

def delete():
  """
  交互式删除
  """

  getBranches = os.popen('git branch')
  print(getBranches.stdout.read())

