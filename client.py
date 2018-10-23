from carca_socket import CarcaSocket
from carca_packet import CarcaPacket
from random import randint
from time import sleep


class CarcaClient():
    def __init__(self, carca_socket, mss=2):
        self._socket = carca_socket
        self._last_byte_read = 0
        self._mss = mss

    def request_data(self):
        packet = CarcaPacket(seq_number=randint(0, 1000), SYN=1, mss=self._mss)
        while True:
            self._socket.sendto(packet)
            print("malucoi")
            packet = self._socket.recvfrom(4096)
            
            if packet._ack_number > self._last_byte_read:
                self._last_byte_read = packet._ack_number
                break

    def receive_data(self):
        byte_list = []
        while True:
            server_packet = self._socket.recvfrom(4096)
            data = server_packet.payload   
            if server_packet.ack_number > self._last_byte_read:
                self._last_byte_read = server_packet.ack_number
                byte_list.append(data)
                confirm_packet = CarcaPacket(ack_number=server_packet._seq_number + self._mss,
                                             seq_number=server_packet._ack_number + 1)
            else:
                confirm_packet = CarcaPacket(ack_number=self._last_byte_read)

                self._socket.sendto(confirm_packet)
