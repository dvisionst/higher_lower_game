import art
import random
import game_data
import os

def comp_dict(dictionary1):
    return f"Compare A: {dictionary1['name']}, a {dictionary1['description']}, from {dictionary1['country']}."
def item_removal(index_number,rolling_list):
    rolling_list.pop(index_number)
    return rolling_list

def vers_dict(dictionary2):
    return f"Against B: {dictionary2['name']}, a {dictionary2['description']}, from {dictionary2['country']}."
def account_total(account_dictionary):
    return account_dictionary['follower_count']

still_play = True
while still_play == True:
    copy_list = game_data.data
    print(art.logo)
    a_rand_number = random.randint(0,len(copy_list)-1)
    a_compare_item = copy_list[a_rand_number]
    item_removal(a_rand_number,copy_list)
    score = 0
    user_still_right = True

    while user_still_right == True:
        b_rand_number = random.randint(0,len(copy_list)-1)
        b_compare_item = copy_list[b_rand_number]
        item_removal(b_rand_number,copy_list)
        print(comp_dict(a_compare_item))
        print(art.vs)
        print(vers_dict(b_compare_item))
        a_comp = account_total(a_compare_item)
        b_comp = account_total(b_compare_item)
        user_decision = input(f"Who has more followers? Type 'A' or 'B': \n")
        if user_decision == 'A' and a_comp > b_comp :
            score +=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You're right! Current score {score}")
        elif user_decision == 'B' and b_comp > a_comp:
            score +=1
            a_compare_item = b_compare_item
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You're right! Current score {score}")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Sorry, that's wrong. Final score: {score}")
            user_still_right = False
    play_decision = input(f"Type 'y' to play again, type 'n' to stop: \n")
    if play_decision == 'n':
        still_play = False
    
    

