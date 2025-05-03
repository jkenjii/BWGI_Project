
import io, os

def last_lines(filename, buffer_size=io.DEFAULT_BUFFER_SIZE):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    caminho_absoluto = os.path.join(base_dir, filename)

    with open(caminho_absoluto, 'rb') as f:
        f.seek(0, os.SEEK_END)
        size = f.tell()
        buffer = bytearray()
        pointer = size
        while pointer > 0:
            read_size = min(buffer_size, pointer)
            pointer -= read_size
            f.seek(pointer)
            data = f.read(read_size)
            buffer = data + buffer
            while b'\n' in buffer:
                idx = buffer.rfind(b'\n')
                line = buffer[idx+1:]
                yield line.decode('utf-8', errors='ignore') + '\n'
                buffer = buffer[:idx]
        if buffer:
            yield buffer.decode('utf-8', errors='ignore') + '\n'
