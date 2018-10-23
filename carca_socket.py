from carca_packet import CarcaPacket
from socket import socket, AF_INET, SOCK_DGRAM
import utils


class CarcaSocket(socket):
    def __init__(self *args, **kwargs):
        super(CarcaSocket, self).__init__(AF_INET, SOCK_DGRAM, *args, **kwargs)

    def sendto(self, packet, address):
        return super(CarcaSocket, self).sendto(utils.serialize_to_string(packet), address)

    def recvfrom(self, buffer):
        data, _ = super(CarcaSocket, self).recvfrom(buffer)
        return utils.parse_from_string(data), address
