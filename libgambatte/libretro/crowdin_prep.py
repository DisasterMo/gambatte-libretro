#!/usr/bin/env python3

import core_opt_translation as t

_core_name = 'core_options'


if __name__ == '__main__':
    try:
        _core_name = t.clean_file_name(_core_name)

        print('Getting texts from libretro_core_options.h')
        with open(t.H_FILE_PATH, 'r+', encoding='utf-8') as _h_file:
            _main_text = _h_file.read()
        _hash_n_str = t.get_texts(_main_text)
        if not t.os.path.exists(t.INTL_DIR_PATH):
            t.os.makedirs(t.INTL_DIR_PATH)
        _files = t.create_msg_hash(_core_name, _hash_n_str)

        _source_jsons = t.h2json(_files)

    except Exception as e:
        print(e)
        print('\nERROR: Something went wrong during synchronisation! Cleaning up...')

    print('\nAll done!')
