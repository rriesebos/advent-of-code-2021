# https://adventofcode.com/2021/day/16

from math import prod


def parse_literal(packet: str):
    i, literal = 0, ''
    while True:
        nibble = packet[i+1:i+5]
        literal += nibble

        i += 5
        if packet[i - 5] == '0':
            break

    return packet[i:], int(literal, 2)


version_sum = 0


def parse_packet(packet: str):
    global version_sum

    version, type_id = packet[:3], packet[3:6]
    packet = packet[6:]

    version_sum += int(version, 2)

    if int(type_id, 2) == 4:
        packet, result = parse_literal(packet)
    else:
        packet, result = parse_operator(packet, int(type_id, 2))

    return packet, result


def parse_operator(packet: str, operator_type: int):
    length_type_id = packet[0]
    packet = packet[1:]
    result = []

    if length_type_id == '0':
        sub_packet_length = int(packet[:15], 2)
        packet = packet[15:]
        old_packet = packet
        while len(old_packet) - len(packet) != sub_packet_length:
            packet, sub_result = parse_packet(packet)
            result.append(sub_result)
    elif length_type_id == '1':
        sub_packet_count = int(packet[:11], 2)
        packet = packet[11:]
        for i in range(sub_packet_count):
            packet, sub_result = parse_packet(packet)
            result.append(sub_result)

    # Add operator type as string
    result.append(str(operator_type))

    return packet, result


with open('input.txt') as f:
    lines = f.readlines()
    transmission_hex = lines[0].strip()

    # Convert transmission from hex to binary, stripping 0b prefix and adding zero padding at the start
    transmission = bin(int(transmission_hex, 16))[2:].zfill(len(transmission_hex) * 4)

    # Parse transmission, returning the parsed expression
    _, parsed_expression = parse_packet(transmission)


# Part 1
print(version_sum)


# Part 2
OPERATOR_MAP = {
    '0': lambda li: sum(li),
    '1': lambda li: prod(li),
    '2': lambda li: min(li),
    '3': lambda li: max(li),
    '5': lambda li: 1 if li[0] > li[1] else 0,
    '6': lambda li: 1 if li[0] < li[1] else 0,
    '7': lambda li: 1 if li[0] == li[1] else 0
}


def evaluate_expression(expression: list):
    stack = []
    for token in expression:
        if isinstance(token, list):
            # Evaluate sub-expression
            result = evaluate_expression(token)
            stack.append(result)
        elif isinstance(token, str):
            # Perform operation
            operation = OPERATOR_MAP[token]
            result = operation(stack)
            stack.clear()
            stack.append(result)
        else:
            # Add integer
            stack.append(token)

    return stack[0]


print(evaluate_expression(parsed_expression))
