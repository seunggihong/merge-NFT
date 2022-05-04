import os
from PIL import Image
import re
import random
import json
from collections import OrderedDict
from datetime import datetime

# file list import
def fileLink(background_img_link, bodys_img_link, eyes_img_link, mouths_img_link, effects_img_link):
    # background file list create
    background_file_list = os.listdir(background_img_link)
    background_file_list_png = [file for file in background_file_list if file.endswith(".png")]
    background_img = []
    for i in background_file_list_png:
        # find img weight
        try:
            found = re.search("_(.+?).", i).group(1)
            background_img.append([i,int(found)])
        except AttributeError:
            pass
    #bodys file list create
    bodys_file_list = os.listdir(bodys_img_link)
    bodys_file_list_png = [file for file in bodys_file_list if file.endswith(".png")]
    bodys_img = []
    for i in bodys_file_list_png:
        # find img weight
        try:
            found = re.search("_(.+?).", i).group(1)
            bodys_img.append([i,int(found)])
        except AttributeError:
            pass
    # eyes file list create
    eyes_file_list = os.listdir(eyes_img_link)
    eyes_file_list_png = [file for file in eyes_file_list if file.endswith(".png")]
    eyes_img = []
    for i in eyes_file_list_png:
        # find img weight
        try:
            found = re.search("_(.+?).", i).group(1)
            eyes_img.append([i,int(found)])
        except AttributeError:
            pass
    # mouths file list create
    mouths_file_list = os.listdir(mouths_img_link)
    mouths_file_list_png = [file for file in mouths_file_list if file.endswith(".png")]
    mouths_img = []
    for i in mouths_file_list_png:
        # find img weight
        try:
            found = re.search("_(.+?).", i).group(1)
            mouths_img.append([i,int(found)])
        except AttributeError:
            pass
    # effects file list create
    effects_file_list = os.listdir(effects_img_link)
    effects_file_list_png = [file for file in effects_file_list if file.endswith(".png")]
    effects_img = []
    for i in effects_file_list_png:
        # find img weight
        try:
            found = re.search("_(.+?).", i).group(1)
            effects_img.append([i,int(found)])
        except AttributeError:
            pass
    
    return background_img, bodys_img, eyes_img, mouths_img, effects_img # return [img name, weight]
# random choice
def randomChoice(img_list,input_cnt):
    weight = []
    # if empty image list
    flag = False
    if not img_list :
        none_file = os.listdir("./img/none")
        choice_list = [[none_file[0], 1] for i in range(input_cnt)]
        return choice_list, flag
    else:
        flag = True
        for i in range(len(img_list)):
            weight.append(img_list[i][1])
        choice_list = random.choices(img_list,weights=weight,k=input_cnt)
        return choice_list, flag
# json name create
def naming(name_list):
    name = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(12):
        name += random.choice(alpha)
    if name in name_list:
        return naming(name_list)
    return name
# create new directory
def createDir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except:
        print("Error")
# img list merge
def imgMerge(input_cnt=10):
    name_list = []
    background_list, bodys_list, eyes_list, mouths_list, effects_list = fileLink("./img/background","./img/bodys","./img/eyes","./img/mouths","./img/effects")

    background_random_img, backgournd_f = randomChoice(background_list,input_cnt)
    bodys_random_img, bodys_f = randomChoice(bodys_list, input_cnt)
    eyes_random_img, eyes_f = randomChoice(eyes_list,input_cnt)
    mouths_random_img, mouths_f = randomChoice(mouths_list,input_cnt)
    effects_random_img, effects_f = randomChoice(effects_list,input_cnt)

    for count in range(input_cnt):
        if backgournd_f:
            background = Image.open("./img/background/{}".format(str(background_random_img[count][0])))
        else:
            background = Image.open("./img/none/{}".format(str(background_random_img[count][0])))
        
        if bodys_f:
            bodys = Image.open("./img/bodys/{}".format(str(bodys_random_img[count][0])))
        else:
            bodys = Image.open("./img/none/{}".format(str(bodys_random_img[count][0])))

        if eyes_f:
            eyes = Image.open("./img/eyes/{}".format((str(eyes_random_img[count][0]))))
        else:
            eyes = Image.open("./img/none/{}".format((str(eyes_random_img[count][0]))))

        if mouths_f:
            mouths = Image.open("./img/mouths/{}".format((str(mouths_random_img[count][0]))))
        else:
            mouths = Image.open("./img/none/{}".format((str(mouths_random_img[count][0]))))
        
        if effects_f:
            effects = Image.open("./img/effects/{}".format((str(effects_random_img[count][0]))))
        else:
            effects = Image.open("./img/none/{}".format((str(effects_random_img[count][0]))))
        
        # img paste
        paste_img = [background,bodys,eyes,mouths,effects]

        # img size check
        flag = True
        size = background.size[0]*background.size[1]
        for img in paste_img:
            x,y = img.size[0],img.size[1]
            if size != x*y:
                flag = False
        
        name = naming(name_list)
        # json file
        json_f = OrderedDict()
        json_f["name"] = str(name)
        json_f["time"] = str(datetime.now())
        # img paste
        if flag == True:
            new_img = background
            for index in range(1,5):
                # image paste
                new_img.paste(paste_img[index],(0,0),paste_img[index])   
                # json create
                json_f["config"] = {
                    'background' : str(background_random_img[count][0]), 
                    'eyes' : str(eyes_random_img[count][0]), 
                    'bodys' : str(bodys_random_img[count][0]), 
                    'mouth' : str(mouths_random_img[count][0]),
                    'effect' : str(effects_random_img[count][0])
                }     
            json_f['number'] = str(count+1)
            createDir("./new/img")
            createDir("./new/json")
            # new image file create
            new_img.save("./new/img/{}.png".format(str(count+1)),"PNG")
            # new json file create
            with open('./new/json/{}.json'.format(str(count+1)), 'w', encoding="utf-8") as make_file:
                json.dump(json_f, make_file, ensure_ascii=False, indent="\t")
            print("make new image : {}.png".format(str(count+1)))

        else:
            print("Error : Images must be the same size.")