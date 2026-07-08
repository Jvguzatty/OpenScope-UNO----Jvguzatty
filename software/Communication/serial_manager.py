import serial


class SerialManager:

    def __init__(self, port="COM3", baudrate=115200):
        self.serial = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=1
        )

    def read_samples(self):

        samples = []

        while True:
            line = self.serial.readline().decode(errors="ignore").strip()

            if line == "BEGIN":
                break

        while True:
            line = self.serial.readline().decode(errors="ignore").strip()

            if line == "END":
                break

            try:
                samples.append(int(line))
            except ValueError:
                pass

        return samples