

# GBA wav format is unsigned 8 bits
def s16_frame_to_gba(halfword):
    return (int.from_bytes(halfword, 'little', signed=True) // 256 + 128).to_bytes(1, 'little')


def s8_frame_to_gba(byte):
    return (int.from_bytes(byte, 'little', signed=True) + 128).to_bytes(1, 'little')


def convert_data_to_gba(signed_data, sample_width):
    function = (s8_frame_to_gba, s16_frame_to_gba)[sample_width - 1]
    unsigned_data = b''
    for i in range(0, len(signed_data), sample_width):
        unsigned_data += function(signed_data[i:i + sample_width])
    return unsigned_data


