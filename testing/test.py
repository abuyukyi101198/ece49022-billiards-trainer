from comm import comm
from DIS import DIS
import time


def comm_accuracy():
    print('\033[95m' + 'TESTING COMM ACCURACY...' + '\033[0m')
    passed, failed = 0, 0
    with open('drills.txt', 'r') as f:
        i = 1
        for string in f.readlines():
            if i > CNT:
                break
            print('TEST {}: '.format(str(i).zfill(3)), end='')
            if comm.run(stream=string):
                print('[' + '\033[92m' + 'PASSED' + '\033[0m' + ']')
                passed += 1
            else:
                print('[' + '\033[91m' + 'FAILED' + '\033[0m' + ']')
                failed += 1
            i += 1

    print('{:>36}'.format('\033[92m' + str(passed) + '\033[0m' + '/' + '\033[91m' + str(failed) + '\033[0m'))
    success = round(passed / (passed + failed) * 100, 0)

    if success > 99:
        print('\033[92m' + '{:>18}'.format(str(success) + '%') + '\033[0m')
    elif success > 95:
        print('\033[93m' + '{:>18}'.format(str(success) + '%') + '\033[0m')
    else:
        print('\033[91m' + '{:>18}'.format(str(success) + '%') + '\033[0m')
    print()


def DIS_runtime():
    TIMEOUT = 4
    print('\033[95m' + 'TESTING DIS RUNTIME...' + '\033[0m')
    passed, failed = 0, 0
    with open('drills.txt', 'r') as f:
        i = 1
        for string in f.readlines():
            if i > CNT:
                break
            print('TEST {}: '.format(str(i).zfill(3)), end='')
            time_start = time.time()
            DIS.run(string=string)
            runtime = time.time() - time_start
            if runtime < TIMEOUT:
                print('[' + '\033[92m' + 'PASSED' + '\033[0m' + ']' + ' {:>3}s'.format(round(runtime, 1)))
                passed += 1
            else:
                print('[' + '\033[91m' + 'FAILED' + '\033[0m' + ']' + ' {:>3}s'.format(round(runtime, 1)))
                failed += 1
            i += 1

    print('{:>36}'.format('\033[92m' + str(passed) + '\033[0m' + '/' + '\033[91m' + str(failed) + '\033[0m'))
    success = round(passed / (passed + failed) * 100, 0)

    if success > 99:
        print('\033[92m' + '{:>18}'.format(str(success) + '%') + '\033[0m')
    elif success > 95:
        print('\033[93m' + '{:>18}'.format(str(success) + '%') + '\033[0m')
    else:
        print('\033[91m' + '{:>18}'.format(str(success) + '%') + '\033[0m')
    print()


if __name__ == '__main__':
    CNT = int(input('Enter number of tests: '))
    print()
    comm_accuracy()
    DIS_runtime()
