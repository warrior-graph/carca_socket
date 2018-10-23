from server import CarcaServer
from carca_socket import CarcaSocket

def main():
	address = ('localhost', 6000)
	socket = CarcaSocket(address)
	data = "abcdefghijklmnopqrstuvxz"
	server = CarcaServer(data, socket)
	server.listen()


if __name__ == '__main__':
	main()

