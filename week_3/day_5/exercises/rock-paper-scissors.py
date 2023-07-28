from game import Game

def get_user_menu_choice():
    while True:
        print("Menu")
        choice = input(" Play a new game (N) or Show scores or Quit (Q)").lower()
        if choice in ['n','q']:
            return choice
        print("Invalid")

def print_results(results):
    print(f"Total wins : {results['win']}")
    print(f"Total losses : {results['loss']}")
    print(f"Total draws : {results['draw']}")
    print(f"Total Rounds : {sum(results.values())}")

def main():
    results = { 'win' : 0, 'loss' : 0, 'draw' : 0}
    while True:
        choice = get_user_menu_choice()

        if choice == 'n':
            game = Game()
            output = game.play()
            results[output] += 1
        elif choice == "q":
            print_results(results)
            break

if __name__ == '__main__':
    main()
        
