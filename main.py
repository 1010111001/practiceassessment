import easygui


comics = {
    "Superman": 
    {
        'Start Date': 1939, 
        'Latest Issue #': 100, 
        '# of Issues': 77, 
        'Series Value': 9500
    },

    "Batman": 
    {
        'Start Date': 1940, 
        'Latest Issue #': 64, 
        '# of Issues': 54, 
        'Series Value': 18100
    },

    "Captain America":
    {
        'Start Date': 1941 , 
        'Latest Issue #': 78, 
        '# of Issues': 62, 
        'Series Value': 8300
    },

    "Wonder Woman": 
    {
        'Start Date': 1941, 
        'Latest Issue #': 98, 
        '# of Issues': 38, 
        'Series Value': 3600
    },

    "Archie Comics": 
    {
        'Start Date': 1942, 
        'Latest Issue #': 81, 
        '# of Issues': 59, 
        'Series Value': 5200
    },

    "Flash": 
    {
        'Start Date': 1939, 
        'Latest Issue #': 3, 
        '# of Issues': 3, 
        'Series Value': 1400 
    },
    "Amazing Spiderman": 
    {
        'Start Date': 1962, 
        'Latest Issue #': 302, 
        '# of Issues': 240, 
        'Series Value': 23500
    },

    "X-Men": 
    {
        'Start Date': 1963, 
        'Latest Issue #': 141, 
        '# of Issues': 92, 
        'Series Value': 7600
    },

    "Iron Man": 
    {
        'Start Date': 1968, 
        'Latest Issue #': 44, 
        '# of Issues': 31, 
        'Series Value': 2800 
    }
}
def check(dict1, dict2):
    for x in dict1:
        
        if dict1[x] == dict2:
            return True
        else:
            return False

def get_input():
    

def add(dictionary):
    while True:
        try:
            series_name = easygui.enterbox('What is the name of the menu: ')
        except:
            print('Invalid input: input a string. Try again :(')
        else:
            break
    final = {f"{series_name}": {}}
    satisfied = False
    while satisfied == False:
            # rewrite
            #menu = easygui.enterbox('Item 1 format: input (name, price): ')
            #x = menu.split()
            #final[f"{menuname}"][x[0]] = float(x[1])
            #menu = easygui.enterbox('Item 2 format(name, price): ')
            #x = menu.split()
            #final[f"{menuname}"][x[0]] = float(x[1])
            #menu = easygui.enterbox('Item 3 format(name, price): ')
            #x = menu.split()
            #final[f"{menuname}"][x[0]] = float(x[1])


            happy = easygui.enterbox('Are you happy with the final menu (y, n): ')
            if happy == 'y':
                copy = check(dictionary, final)
                if copy == True:
                    easygui.msgbox(f"Already exists!")
                    copy == True
                    satisfied = False
                else:
                    easygui.msgbox(f"All good!")
                    return final
                    
            else:
                pass

def add_comics(dictionary) :
    pass
def search(dictionary, comic):
    is_cpy = check(dictionary, comic)



def delete(dictionary, comic):
    #choices = all comic series
    easygui.buttonbox('DELETE: ', choices=[])

def output():
    pass