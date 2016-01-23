from subprocess import Popen, PIPE
import re
import sys
import protocol
import mission

class RunnerError(Exception):
    pass

class Driver:
    def __init__(self, command):
        self.test_id_ = 0
        self.protocol_ = None
        self.popen_ = Popen(args=command, shell=True, stdin=PIPE, \
                            stdout=PIPE, stderr=PIPE, bufsize=0)
        self.protocol_flags = b''

    def write(self, data):
        return self.popen_.stdin.write(data)

    def read(self, size):
        return self.popen_.stdout.read(size)

    def readline(self):
        return self.popen_.stdout.readline()

    def flush(self):
        return self.popen_.stdout.flush()

    def error(self, msg, e=None, raise_ex=True):
        fmt = '\n[Erreur] ' + msg + '\n'
        sys.stderr.write(fmt)
        if e:
            import traceback
            traceback.print_exc()

        msg = ''
        try:
            _, stderr = self.popen_.communicate(timeout=1)
            msg = stderr.decode('utf')
        except:
            pass

        if msg:
            sys.stderr.write('\nErreur du programme (stderr):\n{}\n'.format(stderr.decode('utf')))
        if raise_ex:
            raise RunnerError()

def run(target, test_file, include=None):
    driver = Driver(target)
    missions = mission.MissionManager(driver, include)
    missions.load(test_file)
    try:
        missions.protocol_ = protocol.AsciiProtocol(missions)
        missions.run()
    except KeyboardInterrupt:
        driver.error('Ctrl-C: Arrêt du programme.', raise_ex=False)
    except RunnerError as e:
        pass
    except Exception:
        import traceback
        traceback.print_exc()
        pass
    missions.print_score()

