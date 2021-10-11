import mido

INPUT = None
OUTPUT = None
CHANNEL = 15
TYPE = 'program_change'

SCENES = {
    0: [
        mido.Message('program_change', channel=0, program=1),
    ],
}

def scene_index(message):
    if input_message.channel == CHANNEL and input_message.type == TYPE:
        return message.program

with mido.open_input(INPUT) as input_port:
    with mido.open_output(OUTPUT) as output_port:
        for input_message in input_port:
            index = scene_index(input_message)

            if index is None:
                # print('ignored %s on %s' % (input_message, input_port))
                continue

            print('received %s on %s scene %s' % (input_message, input_port, index))

            if index not in SCENES:
                print('not found %s on %s scene %s' % (input_message, input_port, index))
                continue

            output_messages = SCENES[index]
            for output_message in output_messages:
                output_port.send(output_message)
                print('sent %s on %s scene %s' % (output_message, output_port, index))
