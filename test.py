import subprocess

# Octave を呼び出して MATLAB スクリプトを実行
subprocess.run(["octave", "./config/get_params_value.m"])
