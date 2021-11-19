def parce_dump_file(message):
    with open(f'{message}', 'r') as file:
        can_id = []
        dlc = []
        data = []
        for x in file:

            if x.find('Tx') > 0:
                data_frame = []
                data_from_file = x.split(' ')
                data_from_file = ' '.join(data_from_file).split()
                data_from_file = data_from_file[8:]
                for y in range(0, len(data_from_file)):

                    if y == 0:
                        can_id.append(int(data_from_file[y], 16))
                    elif y == 1:
                        dlc.append(int(data_from_file[y], 16))
                    else:
                        data_frame.append(int(data_from_file[y], 16))
                data.append(data_frame)
            else:
                pass
        return can_id, dlc, data
