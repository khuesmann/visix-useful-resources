import xml.etree.ElementTree as ET

import h5py


def get_volume(full_path, field):
    f = h5py.File(full_path, 'r')
    fields = f.keys()
    channel = None
    for fi in fields:
        x = ET.fromstring(f[fi].attrs.get('metaData')).findall('metaData/MetaData/MetaItem')[2].find('value').attrib['value']
        if x == field:
            channel = fi
            break
    volume = f[channel].value
    return volume


if __name__ == "__main__":
    v = get_volume('/data_storage/scivis_contest_2018/ensemble_hdf5/yB11/pv_insitu_300x300x300_06931.hdf5', 'v02')
    print(v.shape)
