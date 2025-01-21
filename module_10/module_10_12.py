from datetime import datetime
from multiprocessing import Process, Pool


def read_info(name):
    all_data=[]
    with open(name, 'r') as file:
         all_data = [line for line in file]


# Линейный вызов
filenames = [f'./file {number}.txt' for number in range(1, 5)]
start_time_l = datetime.now()
for i in filenames:
    read_info(i)
end_time_l = datetime.now() - start_time_l
print(f'{end_time_l} (линейное)')


# Многопроцессный
start_time_m = datetime.now()
if __name__ == '__main__':
    processes = [Process(target=read_info, args=(filenames[i],)) for i in range(4)]
    for process in processes:
        process.start()

    with Pool() as p:
        p.map(read_info(filenames[i]),range(4))
        # Do something else while tasks are running
        p.close()
        p.join()

end_time_m = datetime.now() - start_time_m
print(f'{end_time_m} (многопроцессный)')
