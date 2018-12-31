class Logger:

    def __init__(self, active=True):
        self.active = active

    def error(self, header, exception):
        if self.active:
            print("[ERROR] ", header, str(exception))

    def info(self, message, args=None):
        if self.active:
            print("[INFO] ", message)
            if args is not None:
                print(args)
