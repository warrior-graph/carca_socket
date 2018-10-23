from carca_socket import CarcaSocket
from carca_packet import CarcaPacket
import utils
from random import randint


class CarcaServer():
    def __init__(self, data, carca_socket):
        self._data = data
        self._socket = carca_socket
        self._send_base = 0

    def listen(self):
        while True:
            client_packet = self._socket.recvfrom(4096)
            print('entrou?')
            if client_packet._SYN == 1:
                print('test')
                byte_string = utils.serialize_to_string(self._data)
                segment_list = utils.string_to_segments(
                    byte_string, client_packet._mss)
                packet = CarcaPacket(seq_number=randint(0, 1000),
                                     ack_number=client_packet._seq_number + 1,
                                     mss=client_packet._mss, payload=segment_list[0])
                print(self._socket._address)
                self._socket.sendto(packet)
            else:
                segment_list.pop(0)
                self._send_base = client_packet._ack_number
                self.send_segment(segment_list)
                break

    def send_segment(self, seg_list):
        while True:
            client_packet = self._socket.recvfrom(4096)
            for seg in seg_list:
                while client_packet._ack_number < self._send_base:
                    packet = CarcaPacket(seq_number=client_packet._ack_number,
                                         ack_number=client_packet._seq_number + 1)
                    self._socket.sendto(packet)
                self._send_base = client_packet._ack_number
