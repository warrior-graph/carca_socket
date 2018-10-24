from carca_socket import CarcaSocket
from carca_packet import CarcaPacket
from random import randint
from time import sleep


class CarcaClient():
    def __init__(self, carca_socket, mss=2):
        self._socket = carca_socket
        self._last_byte_read = 0
        self._mss = mss
        self._byte_list = []

    def request_data(self, server_address):
        client_packet = CarcaPacket(ack_number=0,seq_number=randint(0, 1000), SYN=1, mss=self._mss)
        #print(client_packet._seq_number)
        #print(client_packet._ack_number)
        while True:
            self._socket.sendto(client_packet, server_address)
            server_packet, _ = self._socket.recvfrom(4096)
            print("Recebi primeiro pacote")
            if server_packet._ack_number > self._last_byte_read:
                self._byte_list.append(server_packet._payload)
                self._last_byte_read = server_packet._ack_number
                #print(server_packet._seq_number)
                #print(server_packet._ack_number)
                confirm_packet = CarcaPacket(ack_number=server_packet._seq_number + self._mss,
                                             seq_number=server_packet._ack_number, SYN=0)
                #print(confirm_packet._SYN)
                self._socket.sendto(confirm_packet, server_address)
                #print(confirm_packet._seq_number)
                #print(confirm_packet._ack_number)
                break

    def receive_data(self):
        #byte_list = []
        while True:
            server_packet, server_address = self._socket.recvfrom(4096)
            print("cheguei aqui")
            data = server_packet._payload   
            if server_packet._ack_number > self._last_byte_read:
                self._last_byte_read = server_packet._ack_number
                self._byte_list.append(data)
                confirm_packet = CarcaPacket(ack_number=server_packet._seq_number + self._mss,
                                             seq_number=server_packet._ack_number)
            else:
                confirm_packet = CarcaPacket(ack_number=self._last_byte_read)
            self._socket.sendto(confirm_packet, server_address)
