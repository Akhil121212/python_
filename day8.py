"""file = open('youtube.txt','w')

try:
    file.write('My project ')
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write('My project')"""


import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            print(test)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(vedios):
    with open('youtube.txt','w') as file:
        json.dump(vedios, file)        
        
    

def list_all_vedios(vedios):
     print("\n")
     print(" * " * 70)
     for index, vedios in enumerate(vedios, start=1):
        print(f"{index}. {vedio['name']},
        Duration:{vedio{'time'}}")
    print("\n")
     print(" * " * 70)
        
    

def add_vedios(vedios):
    name = input("Enter the vedio name:")
    time =  input("Enter the vedio time:")
    vedios.append({'name': name,'time':time})
    save_data_helper(vedios)

    

def update_vedio(vedios):
    list_of_vedios(vedios)
    index = int(input("Enter the vedio number to update"))
    if i<= index <= len(vedios):
        name = input("Enter the new vedio name")
        time = input("Enter the new vedio time")
        vedios[index-1] = {'name': name, 'time':time}
        save_data_helper(vedios)
    else:
        print("Incalid index selected")


def delete_vedio(vedios):
    list_all_vedios(vedios)
    index = int(input("Enter the vedio number to deleted"))

    if i<= index <= len(vedios):
        del vedios[index-1]
        save_data_helper(vedios)
    else:
        print("Invalid index selected")    

def main():
    vedios = []

    while True:
        print("\n Youtube Manager")    
        print("1.List all favorite vedios")
        print("2.Add a youtube vedio")
        print("3.Update a youtube vedio  details" )
        print("4.Delete a youtube vedio")
        print("5.Exit the app")
        choice = input("Enter your choice")
        #print(vedios)   

        match choice:
            case '1':
                list_all_vedios(vedios)
            case '2':
                add_vedios(vedios)

            case '3':
                update_vedios(vedios)

            case '4':
                delete_vedio(vedios)    

            case '5':
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()

