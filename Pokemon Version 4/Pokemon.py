
from array_stack import ArrayStack


class Pokemon():
    #constructor 
    def __init__(self, pokemon):
        self.pokemon = pokemon

    #list of all pokemon sorted
    def pokemonList(self):
        f = open('Pokemon.txt')
        list = f.readlines()
        list = ' '.join(list).replace('\\n', '').split()
        list = ' '.join(list).replace("'", '').split()
        for i in range(len(list)):
            list[i] = list[i].lower()
        return list

    def pokemonChecker(self):
        list = self.pokemonList()
        for i in range(len(list)):
            if self.pokemon == list[i]:
                return True

    #finds specific attributes for a pokemon from an imported file
    def getAttributes(self):
        a = ArrayStack()
        f = open('pokemon_moves.txt.csv')
        temp_string = ''
        attribute_list = []
        user_list = []
        p_list = f.readlines()
        p_list = p_list[1:]
        user_list = ' '.join(p_list).replace('\\n', '').split()
        #series of loops to format and access the nested list required for the specific pokemon
        for i in range(len(p_list)):
            user_list.append(p_list[i].split(','))
        for i in range(len(user_list)):
            if user_list[i][0] == self.pokemon:
                attribute_list = user_list[i]
        for i in range(len(attribute_list)):
            if i == 1:
                attribute_list[i] = int(attribute_list[i])
            elif 3 <= i <= 8:
                attribute_list[i] = int(attribute_list[i])
            if attribute_list[i] == attribute_list[-1]:
                temp_string = attribute_list[i]
                temp_string = temp_string[0:-1]                 #formatted string
                attribute_list[i] = temp_string                 
        for i in range(len(attribute_list)):
            a.push(attribute_list[i])                           #pushes all necessary attributes into stack
        return a

    def movesDisplayer(self):
        #display the user sees when choosing an attack
        self.pokemon.lower()
        displayer = open('pokemonDisplayer.xlsx.csv')
        temp_list = []
        temp_list = displayer.readlines()
        display_list = []
        output = []
        for i in range(len(temp_list)):
            display_list.append(temp_list[i].split(','))
        for _ in range(len(display_list)):
            if display_list[_][0] == self.pokemon:
                output = display_list[_]
        temp_string = output[-1]
        output[-1] = temp_string[0:-1]
        for l in range(len(output)):
            print(output[l])
                    


# def main():
#     p = Pokemon('mewtwo')
#     p.movesDisplayer()


# main()