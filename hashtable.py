from itertools import islice
import time
import psutil


# initial size of hashtable
hashTable = [[] for _ in range(10)]

def readdata():
    file_name = 'rand.txt'

    data = []

    #time at the start of program is noted
    start = time.time()
  
    #keeps a track of number of lines in the file
    with open(file_name, mode='r') as datafile:
        while True:
            next_n_lines = list(islice(datafile, 10000))
            if not next_n_lines:
                break
            data.extend([int(line.rstrip()) for line in next_n_lines])
      
    #time at the end of program execution is noted
    end = time.time()
  
    # total time taken to print the file
    print("Time of reading data in seconds: ",(end - start))
    print("Size of data: ",len(data))
    return data


def hashFunction(key):
    return key % len(hashTable)


# Function to display hashtable
def displayHashTable(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " |")
        
        count = 0
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
            count += 1

            # just print first 10 columns
            if count > 10:
                print("......", end = "")
                break
              
        print()

        # just print first 20 rows
        if i > 20:
            print("......")
            break


def insertData(key, value):
    index = hashFunction(key)
    hashTable[index].append(value)


def contains(key):
    index = hashFunction(key)
    iterationCount = 0
    for data in hashTable[index]:
        iterationCount += 1
        if data == key:
            print("iteration times: ", iterationCount)
            return True
        
    print("iteration times: ", iterationCount)

    return False

# def removeData(key):
#     index = hashFunction(key)
#     for data in hashTable[index]:
#         if data == key:
#             data == -1;



def main():
    print('cpu % used at start: ', psutil.cpu_percent())
    print(psutil.virtual_memory())  # physical memory usage
    print('memory % used:', psutil.virtual_memory()[2])

    data = readdata()

    # insert data into hashtable
    start = time.time()
    for number in data:
        insertData(number, number)
    end = time.time()
    print("Time of inserting data into hashtable: ", (end - start))
    print()
    # displayHashTable(hashTable)

    # should print true:
    searchValues1 = [522821228, 426088780, 717686692, 652705375, 207855228]

    # should print false:
    searchValues2 = [0, 100000000, 300000000, 600000000, 1000000000]

    for value in searchValues1 + searchValues2:
        print("searching for value: ", value)
        start = time.time()
        result = contains(value)
        end = time.time()
        print("Time of searching value in seconds: ", (end - start))
        if result:
            print("value found!", end = '\n\n')
        else:
            print("value not found!", end = '\n\n')
        
        
    print('cpu % used in the end: ', psutil.cpu_percent())
    print(psutil.virtual_memory())  # physical memory usage
    print('memory % used:', psutil.virtual_memory()[2])


if __name__ == "__main__":
    main()