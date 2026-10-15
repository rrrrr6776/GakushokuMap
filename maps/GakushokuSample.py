from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):

    def get_menu(self):
        return "すき家のチーズ牛丼"
    
    def get_summary(self):
        return "すき家のチーズ牛丼は、ジューシーな牛肉ととろけるチーズが絶妙に組み合わさった人気のメニューです。ご飯の上にたっぷりの牛肉とチーズがのせられ、特製のタレがかかっており、食欲をそそります。手軽に楽しめる一品で、忙しい日やランチタイムにぴったりです。"
    
    def get_author(self):
        return "貴斗"