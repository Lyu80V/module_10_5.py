import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            line = file.readline()
            all_data.append(line[0:-1])


filenames = [f'./module_10_5 file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
'''read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])'''
for name in filenames:
    read_info(name)
finish = datetime.datetime.now()
print(finish - start, ' Линейный вызов')  # Линейный вызов

if __name__ == '__main__':

    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    finish = datetime.datetime.now()

    print(finish - start, ' Многопроцессный вызов')  # Многопроцессный вызов

    '''start = datetime.datetime.now()
    p1 = multiprocessing.Process(target=read_info, args=filenames[0])
    p2 = multiprocessing.Process(target=read_info, args=filenames[1])
    p3 = multiprocessing.Process(target=read_info, args=filenames[2])
    p4 = multiprocessing.Process(target=read_info, args=filenames[3])

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    finish = datetime.datetime.now()
    print(finish - start, ' Многопроцессный вызов')  # Многопроцессный вызов'''

