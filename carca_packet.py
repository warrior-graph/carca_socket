class CarcaPacket():
    def __init__(self, ack_number=0, seq_number=0, mss=0, ACK=0, FIN=0, SYN=0, payload=b'', *args, **kwargs):
        self._ack_number = ack_number
        self._seq_number = seq_number
        self._mss = mss
        self._ACK = ACK
        self._FIN = FIN
        self._SYN = SYN
        self._payload = payload
