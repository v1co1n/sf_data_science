import numpy as np
def random_predict(number:int=1)->int:
    """Guess number randomly

    Args:
        number (int, optional): Number to predict. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count  = 0

    while 1==1:
        answer = np.random.randint(1,500)
        count +=1
        if answer == number:
            return count

def score_game(random_predict)->int:
    """_summary_

    Args:
        random_predict (_type_): _description_

    Returns:
        int: _description_
    """
    try_count_list = []
    #np.random.seed(1)
    random_array = np.random.randint(1,101,size = (1000))
    
    for number in random_array:
        try_count_list.append(random_predict(number))
    
    score = int(np.mean(try_count_list))
    print('Average try count is {}'.format(score))
    return score

if __name__ == '__main__':
    score_game(random_predict)
