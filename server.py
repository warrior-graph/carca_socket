from carca_socket import CarcaSocket
from carca_packet import CarcaPacket
import utils
from random import randint


class CarcaServer():
    def __init__(self, data, carca_socket):
        self._data = data
        self._socket = carca_socket
        self._send_base = 0
        
    def listen(self, server_address):
        self._socket.bind(server_address)
        
    def accept_cnn(self):
        while True:
            client_packet, client_address = self._socket.recvfrom(4096)
            if client_packet._SYN == 1:
                byte_string = utils.serialize_to_string(self._data)
                segment_list = utils.string_to_segments(
                    byte_string, client_packet._mss)
                packet = CarcaPacket(seq_number=randint(0, 1000),
                                     ack_number=client_packet._seq_number + 1,
                                     mss=client_packet._mss, payload=segment_list[0])
                #print(packet._seq_number)
                #print(packet._ack_number)
                self._socket.sendto(packet, client_address)
            else:
                print("recebi SYN 0")
                segment_list.pop(0)
                self._send_base = client_packet._ack_number
                self.send_segment(segment_list, client_packet, client_address)
                break

    def send_segment(self, seg_list, to_send_packet, client_address):
        self._socket.sendto(to_send_packet, client_address)
        while True:
            #client_packet, _ = self._socket.recvfrom(4096)
            for seg in seg_list:
                client_packet, _ = self._socket.recvfrom(4096)
                while client_packet._ack_number <= self._send_base:
                    #packet = CarcaPacket(seq_number=client_packet._ack_number,
                    #                     ack_number=client_packet._seq_number + 1)
                    self._socket.sendto(client_packet, client_address)
                self._send_base = client_packet._ack_number
                to_send_packet = CarcaPacket(seq_number=client_packet._ack_number,
                           ack_number=client_packet._seq_number + 1)
                self._socket.sendto(to_send_packet, client_address)
