from server import CarcaServer
from carca_socket import CarcaSocket

def main():
	address = ('localhost', 6000)
	socket = CarcaSocket()
	data = "abcdefghijklmnopqrstuvxz"
	server = CarcaServer(data, socket)
	server.listen(address)
	server.accept_cnn()
	
if __name__ == '__main__':
	main()

