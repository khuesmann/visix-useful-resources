import argparse
import os


def create_vvd(path, file, dimensions, offset, spacing):
    vvd = open('./vvd_template').read()
    vvd = vvd.format(
        x=dimensions[0], y=dimensions[1], z=dimensions[2],
        filename=file,
        offset_x=offset[0], offset_y=offset[1], offset_z=offset[2],
        spacing_x=spacing[0], spacing_y=spacing[1], spacing_z=spacing[2],
    )
    vvd_path = os.path.join(path, file + '.vvd')
    vvd_file = open(vvd_path, "w")
    vvd_file.write(vvd)
    vvd_file.close()


def main(args):
    print(f'Creating vvd files in path {args.path}.')
    files = os.listdir(args.path)
    for file in files:
        if file.endswith('.vvd'):
            continue
        create_vvd(args.path, file, args.dimensions, args.offset, args.spacing)
    print(f'Done. Created {len(files)} vvd files.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create awesome results_bkup.')
    parser.add_argument('-p', '--path', required=True, type=str)
    parser.add_argument('-d', '--dimensions', help='-d [x|int] [y|int] [z|int]', required=True, nargs='+')
    parser.add_argument('-o', '--offset', help='-o [x|int] [y|int] [z|int]', default=[0, 0, 0], nargs='+')
    parser.add_argument('-s', '--spacing', help='-s [x|int] [y|int] [z|int]', default=[1, 1, 1], nargs='+')
    args = parser.parse_args()

    main(args)
