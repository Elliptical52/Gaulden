def read(start : str, key : str, write : str = None):
    if write is None:
        with open('D:/Gaulden/root/system/env/env.txt') as file:
            data = file.read().split('\n')
            file.close()
        i = data.index(f'&&{start}')
        current_key = ':'
        while current_key.split(':')[0] != key and data[i] != f'##{start}':
            i += 1
            current_key = data[i]
        
        line = data[i].split(':')
        return line[1]
    else:
        with open('D:/Gaulden/root/system/env/env.txt') as file:
            data = file.read().split('\n')
            file.close()
        
        with open('D:/Gaulden/root/system/env/env.txt', 'w') as file:
            i = data.index(f'&&{start}')
            current_key = ':'
            while current_key.split(':')[0] != key and data[i] != f'##{start}':
                i += 1
                current_key = data[i]
            data[i] = f'{current_key.split(':')[0]}:{write}'
            file.write('\n'.join(data))
            file.close()
        return data[i].split(':')[1]

