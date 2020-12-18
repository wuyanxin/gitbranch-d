
import os

def delete():
  """
  交互式删除
  """

  branches = os.popen('git branch').readlines()

  if len(branches) < 2:
    done(0)
    return

  count = 0
  for b in branches:
    b = str.strip(b)
    if len(b) == 0:
      continue
    if b[0] == '*': # current branch
      continue

    sure = areYouSure(input("\ndeleting branch " + b + ", procceed (y/[n])? "))
    if not sure:
      print("except", b)
      continue

    print(os.popen('git branch -D ' + b).read())
    count += 1

  done(count)


def areYouSure(y_or_n):
  return y_or_n == 'y' or y_or_n == 'Y'

def done(delcount):
  """
  docstring
  """
  print("\n", delcount, "branch(es) deleted\n")
