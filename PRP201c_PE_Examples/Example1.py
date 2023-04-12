print("Nhập vào số N cần đảo ngược: ")

# Lấy dữ liệu
n = int(input())

# In ra số đảo ngược
while (n != 0):
    print(n % 10, end="")
    n = n // 10