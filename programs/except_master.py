
import os

def delete():
  """
  只保留master
  """

  checkoutMaster = os.popen('git checkout master').read()
  print(checkoutMaster)
  if checkoutMaster.startswith('error'):
    return

  print("git branch | grep -v 'master' | xargs git branch -D")
  print(os.popen("git branch | grep -v 'master' | xargs git branch -D").read())
  print('done')
