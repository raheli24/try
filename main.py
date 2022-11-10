from utils import load_random_word
from player import Player

data_source = "https://api.npoint.io/ef74ba12e461bc3c9cf5"


if __name__ == '__main__':

    print("Введите имя игрока")
    user_name = input()

    player = Player(user_name)
    print(f"Привет, {player.name}!")

    basic_word = load_random_word(data_source)

    print(f"Составьте {basic_word.count_sub_words()} слов из слова {basic_word.word}")
    print("Слова должны быть не менее 3 букв")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?')

    while player.count_used_words() < basic_word.count_sub_words():

        user_input = input().strip().lower()

        if user_input in ["stop", "стоп"]:
            break

        elif len(user_input) < 3:
            print("Слишком короткое слово")
            continue

        elif not basic_word.has_sub_word(user_input):
            print("неверно")

        elif player.is_word_used(user_input):
            print("уже использовано")

        else:
            print("верно")
            player.add_word(user_input)

    print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")

