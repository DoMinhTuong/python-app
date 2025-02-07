class HocSinh():
    def __init__(self, hovaten, diachi, chieucao, cannang, hocluc):
        self.hovaten = hovaten
        self.diachi = diachi
        self.chieucao = chieucao
        self.cannang = cannang
        self.hocluc = hocluc
    def chuyennha(self):
        self.diachi = input("Nhập địa chỉ nhà mới: ")
    def khamsuckhoe(self):
        self.chieucao = input("Nhập chiều cao mới: ")
        self.cannang = input("Nhập cân nặng mới: ")
    def xuatthongtin(self):
        print(self.hovaten, self.diachi, self.chieucao, self.cannang, self.hocluc)