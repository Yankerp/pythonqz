print("foo功能开始运行了.........")

__all__ = ["x"]
x = 10000000
def get():
    print(x)

def change():
    global x
    x = 20000000


if __name__ == '__main__':
    get()
    change()
