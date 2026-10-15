from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuTakato(AbstractGakushoku):

    def get_menu(self):
        return "すき家のチーズ牛丼"
    
    def get_summary(self):
        return "すき家のチーズ牛丼は、ボリューム満点で満足感があります。"
    
    def get_author(self):
        return "貴斗"