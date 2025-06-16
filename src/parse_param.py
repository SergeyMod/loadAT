import argparse

def parse_param():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-if', '--input_file',
        type=str,
        help='Путь до входного json файла',
        default='src/events.json')

    parser.add_argument(
        '-of', '--output_file',
        type=str,
        help='Путь до json файла для записи в него результата',
        default='src/output.json')
    args = parser.parse_args()
    return args.input_file, args.output_file