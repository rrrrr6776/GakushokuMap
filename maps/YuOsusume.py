from maps.AbstractGakushoku import AbstractGakushoku

class YuOsusume(AbstractGakushoku):

    def get_menu(self):
        return "すき家の味噌汁"
    
    def get_summary(self):
        return "大多数の日本人に馴染みのあるホッとする味"
    
    def get_author(self):
        return "なかむら"