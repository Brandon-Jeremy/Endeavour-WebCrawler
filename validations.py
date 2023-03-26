def validateList(lst:list[list]):
    """
    Count number of items found in matrix
    Function used for the sake of simplifying testing
    and validation
    """
    print(f"Number of threads to divide tasks between: {len(lst)}")
    total_tasks = 0
    for row in lst:
        count = 0
        for column in row:
            count+=1
        total_tasks += count
        print(f"Number of tasks per thread: {count}")
        print(f"Total number of tasks {total_tasks}")
