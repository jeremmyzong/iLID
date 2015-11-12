import os
import subprocess
import sys


def get_audio_length(f):
  print f 
  command = "soxi -D %s" % f
  return float(subprocess.check_output(command, shell=True))

if __name__ == '__main__':
  target_dir = sys.argv[1]
  files = os.listdir(target_dir)
  print files
  total = sum([get_audio_length(os.path.join(target_dir, f)) for f in files])
  print total / 60. / 60.