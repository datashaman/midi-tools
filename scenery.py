import mido

with mido.open_input() as input_port:
    with mido.open_output() as output_port:
        for input_message in input_port:
            if input_message.type == 'program_change':
                print(input_message)
