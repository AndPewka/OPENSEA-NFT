def gen():
    from PIL import Image
    import time
    import time

    import os
    from function import body_with_eye
    massive = [1,2,3,4,5,6,7,8,9]
    from random import choice

    from time import sleep

    add_0 = os.listdir(os.path.join("0"))
    add_1 = os.listdir(os.path.join("1"))
    add_2 = os.listdir(os.path.join("2"))
    add_3 = os.listdir(os.path.join("3"))
    add_4 = os.listdir(os.path.join("4"))
    add_5 = os.listdir(os.path.join("5"))
    add_6 = os.listdir(os.path.join("6"))
    add_7 = os.listdir(os.path.join("7"))
    add_8 = os.listdir(os.path.join("8"))
    add_9 = os.listdir(os.path.join("9"))

    locate_card = os.listdir(os.path.join("new_card"))

    x = int(input("write count's of card --> "))
    start_time = time.time()

    locate_card = os.listdir(os.path.join("new_card"))


    os.system("cls")
    for i in range(x):
        word = ""
        result_word = ""
        
        word = choice(add_0) 
        result_word = result_word + word + "$"
        main = Image.open("0/{}".format(word), 'r')

        word = choice(add_1)
        body = word
        result_word = result_word + word + "$" 
        card = Image.open("1/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        word = choice(add_2)
        result_word = result_word + word + "$" 
        card = Image.open("2/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        word = choice(add_3)
        eye = word
        if body_with_eye(body,eye) == False:
            eye = list(eye)
            eye[2] = body[0]
            eye = "".join(eye)
            word = eye
            
        result_word = result_word + word + "$" 
        card = Image.open("3/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        word = choice(add_4)
        result_word = result_word + word + "$" 
        card = Image.open("4/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        word = choice(add_5)
        result_word = result_word + word + "$" 
        card = Image.open("5/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        word = choice(add_6)
        result_word = result_word + word + "$" 
        card = Image.open("6/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        word = choice(add_7)
        result_word = result_word + word + "$"
        card = Image.open("7/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        word = choice(add_8)
        result_word = result_word + word + "$"
        card = Image.open("8/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        word = choice(add_9)
        result_word = result_word + word
        card = Image.open("9/{}".format(word), 'r')
        main.paste(card,(0,0),card)

        result_word = result_word.replace(".png","")
        result_word = result_word + ".png"
        
        if result_word not in locate_card:
            main.save("new_card/+" + result_word, format="png")
            print("{}/{}    | {}".format(i+1,x,result_word[:]))