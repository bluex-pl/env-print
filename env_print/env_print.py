#!/usr/bin/env python3

import os

def main():
    for k, v in os.environ.items():
        print('{k}={v}'.format(**locals())) # todo: f-string

if __name__ == '__main__':
    main()
    
