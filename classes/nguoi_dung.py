
class NguoiDung:
    def __init__(self, id, ho_ten, username, password, vai_tro):
        self.id = id
        self.ho_ten = ho_ten
        self.username = username
        self.password = password
        self.vai_tro = vai_tro

    def dang_nhap(self, username, password):
        return (
            self.username == username
            and self.password == password
        )
