telNo = [input() for _ in range(int(input()))]

def wrapper(f):
    def phone(telNo):
        f(["+91 "+number[-10:-5]+" "+number[-5:] for number in telNo])
    return phone

@wrapper
def phone(telNo):
    print(*sorted(telNo), sep='\n')

phone(telNo)
