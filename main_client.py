from client import CarcaClient
from carca_socket import CarcaSocket


def main():
    address = ('localhost', 7000)
    socket = CarcaSocket()
    client = CarcaClient(socket)
    client.request_data()
    print('Passei')
    client.receive_data()


if __name__ == '__main__':
    main()
