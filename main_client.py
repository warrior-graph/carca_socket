from client import CarcaClient
from carca_socket import CarcaSocket


def main():
    server_address = ('localhost', 6000)
    socket = CarcaSocket()
    client = CarcaClient(socket)
    client.request_data(server_address)
    print('Passei')
    client.receive_data()


if __name__ == '__main__':
    main()
