import numpy as np

def predict_number(number:int=1)->int:
    """Function gueses the number in
    20 tries or less

    Args:
        number (int, optional): Number is between 1 and 100. Defaults to 1.

    Returns:
        : tries count
    """
    min = 1 
    max = 101
    try_count=0
    while True:
        guess=(min+max)//2   
        try_count+=1      
        if guess == number:
            return try_count
        if guess < number:
            min = guess
        if guess > number:
            max = guess

def game_score(predict_number)->int:
    """Calculating score of predict_number function

    Args:
        predict_number (function): function gueses random number

    Returns:
        int: Average tries count
    """
    random_list = np.random.randint(1,101,size=1000)
    np.random.seed(18)
    tries=[]
    for i in random_list:
        tries.append(predict_number(i))
        
    score = int(np.mean(tries))
    return score

if __name__=='__main__':
    print('Your algorithm gueses the number in average try count={}'.format(game_score(predict_number)))

