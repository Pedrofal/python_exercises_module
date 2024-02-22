def list_manupulation():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'grape']
    print(f'This is the current list of fruits: {fruits}')
    
    def change_fruit(fruits):
        
        fruit_to_change = input("If you want to change any fruit, please type its name. If you don't press enter: ").lower().strip()
               
        
        if fruit_to_change == '':
            add_to_end_of_list(fruits)
        elif fruit_to_change not in fruits:
            print('The fruit you enter is not on the list, please run the code again with a fruit on the list')
            change_fruit(fruits)
            
        else:
            
            fruit_index = fruits.index(fruit_to_change)
            fruit_change_to = input(f"What fruit do you want to change '{fruit_to_change}' for? ").lower()
            fruits[fruit_index] = fruit_change_to
            print(f'This is the updated list of fruits: {fruits}')
            add_to_end_of_list(fruits)  

    
    def add_to_end_of_list(fruits):
        add_to_end_of_list = input("If you want to add a fruit to the end of the list, please type its name. If you don't press enter: ").lower()
        
        if add_to_end_of_list != '':
            fruits.append(add_to_end_of_list)
            print(f'This is the updated list of fruits: {fruits}')

        
            
    
    change_fruit(fruits)

    def remove_fruit(fruits):
        fruit_to_remove = input("If you want to remove a fruit, please type its name. If you don't press enter: ").lower()
        if fruit_to_remove != '':
            if fruit_to_remove in fruits:
                fruits.remove(fruit_to_remove)
                print(f'You removed "{fruit_to_remove}" from the list. This is the updated list of fruits: {fruits}')
            else:
                print('The fruit you enter is not on the list, please enter a fruit on the list')
                remove_fruit(fruits) 
       
        

        else:
            print(f'This is the current list of fruits: {fruits}') 

    remove_fruit(fruits)







