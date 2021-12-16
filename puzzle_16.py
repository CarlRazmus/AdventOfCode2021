import operator
from functools import reduce


def part_1(packet):
    parse_packet(packet=packet)
    print(packet_versions)

def part_2(packet):
    _, value = parse_packet(packet)
    print(value)

def parse_packet(packet):
    global packet_versions
    packet_versions += int(packet[:3], base=2)
    type_id = packet[3:6]
    packet = packet[6:]

    if type_id == "100": #literal value
        value = ""
        while packet[0] == "1":
            value += packet[1:5]
            packet = packet[5:]
        #add the last value marked with 0 as start bit
        value += packet[1:5]
        packet = packet[5:]
        return packet, int(value, base=2)

    return_values = []
    len_type_id = packet[0]
    packet = packet[1:]
    if len_type_id == "0":
        sub_packages_bit_length = int(packet[:15], 2)
        spent_bit_length = 0
        packet = packet[15:]
        while spent_bit_length < sub_packages_bit_length:
            new_packet, value = parse_packet(packet)
            return_values.append(value)
            spent_bit_length += len(packet) - len(new_packet)
            packet = new_packet
    else:
        nr_sub_packages = int(packet[:11], 2)
        packet = packet[11:]
        for _ in range(nr_sub_packages):
            packet, value = parse_packet(packet)
            return_values.append(value)
    return packet, calc_value(type_id, return_values)

def calc_value(type_id, values):
    if len(values) == 1:
        return_val = values[0]
    elif type_id == "000":
        return_val = sum(values)
    elif type_id == "001":
        return_val = reduce((lambda x, y: x * y), values)
    elif type_id == "010":
        return_val = min(values)
    elif type_id == "011":
        return_val = max(values)
    elif type_id == "101":
        return_val = 1 if operator.gt(values[0], values[1]) else 0
    elif type_id == "110":
        return_val = 1 if operator.lt(values[0], values[1]) else 0
    elif type_id == "111":
        return_val = 1 if operator.eq(values[0], values[1]) else 0
    return return_val

def hex_to_bin(hex_string):
    return "".join(["{0:04b}".format(int(s, 16)) for s in hex_string])


if __name__ == "__main__":
    with open("input_16.txt") as f:
        hex_packet = f.read().strip()
    bin_packet = hex_to_bin(hex_packet)
    packet_versions = 0

    part_1(packet=bin_packet)
    part_2(packet=bin_packet)
