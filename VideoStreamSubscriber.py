import imagezmq
import threading
import traceback

class VideoStreamSubscriber:

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self._stop = False
        self._data = {}
        self._data_ready = threading.Event()
        self._thread = threading.Thread(target=self._run, args=())
        self._thread.daemon = True
        self._thread.start()

    def receive(self, timeout=15.0):
        flag = self._data_ready.wait(timeout=timeout)
        if not flag:
            raise TimeoutError(
                f"Timeout while reading from subscriber tcp://{self.hostname}:{self.port}")
        self._data_ready.clear()
        return self._data


    def _run(self):
        try:
            receiver = imagezmq.ImageHub(f"tcp://{self.hostname}:{self.port}", REQ_REP=False)
            while not self._stop:
                data = receiver.recv_jpg()
                self._data[data[0]] = data[1]
                self._data_ready.set()
            receiver.close()

        except Exception:
            print("unhandled exception")
            traceback.print_exc()

    def close(self):
        self._stop = True