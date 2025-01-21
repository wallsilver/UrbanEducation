from datetime import datetime
import multiprocessing


def read_info(name):
    all_data=[]
    with open(name, 'r') as file:
         all_data = [line for line in file]

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time_l = datetime.now()
for i in filenames:
    read_info(i)
end_time_l = datetime.now() - start_time_l
print(f'{end_time_l} (линейное)')


# Многопроцессный

if __name__ == '__main__':
  #  processes = [Process(target=read_info, args=(filenames[i],)) for i in range(4)]
  #  for process in processes:
   #     process.start()
    start_time_m = datetime.now()
    pool = multiprocessing.Pool()
    processes = pool.map(read_info, filenames)

    end_time_m = datetime.now() - start_time_m
    print(f'{end_time_m} (многопроцессный)')
