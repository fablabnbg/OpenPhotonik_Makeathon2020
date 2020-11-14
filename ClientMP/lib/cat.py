# cat.py
import sys

def cat(fn):
    with open(fn, 'w') as fh:
        sys.stdin  = fh
        for line in sys.stdin:
            try:
                print(line, end='')
            except BrokenPipeError:
                sys.stderr.close()

### main
if __name__ == "__main__":
    cat()


