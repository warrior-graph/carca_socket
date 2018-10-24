from server import CarcaServer
from carca_socket import CarcaSocket
import utils

def main():
    data = "abcdefghijklmnopqrstuvxz"
    server_address = ('localhost', 6000)
    socket = CarcaSocket()
    server = CarcaServer(socket, data)
    server.listen(server_address)
    encoded_data = server.receive_data()
    encoded_data = utils.string_from_segments(encoded_data)
    encoded_data = utils.parse_from_string(encoded_data)
    print(encoded_data)
    
if __name__ == '__main__':
    main()

