print(2 + 2)
def greet():
    print('hello')

greet()

blockchain = [1, 2]

print(type(blockchain))

print(max(blockchain))

def add_value():
    blockchain.append([blockchain[-1], 5.3])
    print(blockchain)

add_value()

print("""
Hello World
This is me saying hi on many levels
Bonjour, le Monde
""")


number = 100000000000000
print(f"{number:,}")
