from maps.AbstractGakushoku import AbstractGakushoku

class RinOsusume(AbstractGakushoku):

    def get_menu(self):
        return "唐揚げ丼"
    
    def get_summary(self):
        return "美味しい"
    
    def get_author(self):
        return "りん"