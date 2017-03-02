def do():
    import subprocess
    subprocess.call("git submodule update --init --recursive --remote".split(" "))