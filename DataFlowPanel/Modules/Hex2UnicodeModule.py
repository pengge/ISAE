properties = {
    'name': 'Hex To Unicode',
    'categories': '数据转换',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
    }
}

defaults = {}


def main(inp, settings):
    out = {0: HexStr2Unicode(inp[0])}
    return out


def HexStr2Unicode(Hex_Str):
    Unicde_Str = ""
    for i in range(0, len(Hex_Str) // 4):
        chr(int(Hex_Str[i * 4:i * 4 + 4], 16))
        Unicde_Str += chr(int(Hex_Str[i * 4:i * 4 + 4], 16))
    return Unicde_Str