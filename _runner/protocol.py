import binascii
import struct

class AsciiProtocol(BaseProtocol):
    def send(self, test_id, mission, test_input):
        data = (':'.join([str(mission), test_input])).encode()
        self.driver_.write(data + b'\n')
        self.driver_.flush()

    def recv(self):
        try:
            line = self.driver_.readline()
            if line:
                if line[-1] == 0xa:
                    line = line[:-1]
                return line.decode('utf')
        except RuntimeError as e:
            self.driver_.error('Réponse invalide', e)

        self.driver_.error('Aucune réponse reçue')

