import ntpath
from fs import open_fs


class open:
    # f = ''
    # def __new__(cls, target, mode='r'):
    #     print('in new')
    #     import ntpath
    #     fs_name = ntpath.dirname(target)
    #     file_name = ntpath.basename(target)
    #     fs = open_fs(fs_name)
    #     f = fs.open(file_name, mode)
    #     print(type(f))
    #     return f

    def __init__(self, target, mode='rt'):
        self.fs_name = ntpath.dirname(target)
        self.file_name = ntpath.basename(target)
        self.fs = open_fs(self.fs_name)
        self.f = self.fs.open(self.file_name, mode)

    def __call__(self, *args, **kwargs):
        return self.f

    def write(self, text):
        self.f.write(text)

    def read(self, size=-1):
        return self.f.read(size)

    def close(self, close_fs=True):
        # option to only close the file and not the fs. This is useful when we want to perform os.remove on the file, keeping the fs open
        self.f.close()
        if close_fs:
            self.fs.close()

    def __iter__(self):
        return self.f

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()
        self.fs.close()
