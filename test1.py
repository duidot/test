class GFG:
    def __init__(self):
        self.key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        self.key1 = [0] * 8
        self.key2 = [0] * 8
        self.IP = [2, 6, 3, 1, 4, 8, 5, 7]
        self.EP = [4, 1, 2, 3, 2, 3, 4, 1]
        self.P4 = [2, 4, 3, 1]
        self.IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
        self.S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
        self.S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    def key_generation(self):
        key_ = [self.key[self.P10[i] - 1] for i in range(10)]
        Ls, Rs = key_[:5], key_[5:]
        Ls_1, Rs_1 = self.shift(Ls, 1), self.shift(Rs, 1)
        key_ = Ls_1 + Rs_1
        self.key1 = [key_[self.P8[i] - 1] for i in range(8)]
        Ls_2, Rs_2 = self.shift(Ls, 2), self.shift(Rs, 2)
        key_ = Ls_2 + Rs_2
        self.key2 = [key_[self.P8[i] - 1] for i in range(8)]
        print("Your Key-1 :", self.key1)
        print("Your Key-2 :", self.key2)

    def shift(self, ar, n):
        return ar[n:] + ar[:n]

    def encryption(self, plaintext):
        arr = [plaintext[self.IP[i] - 1] for i in range(8)]
        arr1 = self.function_(arr, self.key1)
        after_swap = self.swap(arr1, len(arr1) // 2)
        arr2 = self.function_(after_swap, self.key2)
        ciphertext = [arr2[self.IP_inv[i] - 1] for i in range(8)]
        return ciphertext

    def binary_(self, val):
        return format(val, '02b')

    def function_(self, ar, key_):
        l, r = ar[:4], ar[4:]
        ep = [r[self.EP[i] - 1] for i in range(8)]
        ar = [key_[i] ^ ep[i] for i in range(8)]
        l_1, r_1 = ar[:4], ar[4:]
        row, col = int(f"{l_1[0]}{l_1[3]}", 2), int(f"{l_1[1]}{l_1[2]}", 2)
        str_l = self.binary_(self.S0[row][col])
        row, col = int(f"{r_1[0]}{r_1[3]}", 2), int(f"{r_1[1]}{r_1[2]}", 2)
        str_r = self.binary_(self.S1[row][col])
        r_ = [int(str_l[i]) for i in range(2)] + [int(str_r[i]) for i in range(2)]
        r_p4 = [r_[self.P4[i] - 1] for i in range(4)]
        l = [l[i] ^ r_p4[i] for i in range(4)]
        return l + r

    def swap(self, array, n):
        return array[n:] + array[:n]

    def decryption(self, ar):
        arr = [ar[self.IP[i] - 1] for i in range(8)]
        arr1 = self.function_(arr, self.key2)
        after_swap = self.swap(arr1, len(arr1) // 2)
        arr2 = self.function_(after_swap, self.key1)
        decrypted = [arr2[self.IP_inv[i] - 1] for i in range(8)]
        return decrypted

if __name__ == "__main__":
    obj = GFG()
    obj.key_generation()
    plaintext = [0, 1, 1, 1, 0, 0, 1, 0]
    print("Your plain Text is :", plaintext)
    ciphertext = obj.encryption(plaintext)
    print("Your cipher Text is :", ciphertext)
    decrypted = obj.decryption(ciphertext)
    print("Your decrypted Text is :", decrypted)