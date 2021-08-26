#!/usr/bin/env python3

import translate as t

try:
    _core_name = t.sys.argv[1]
except IndexError:
    print('Please provide core name!')
    t.sys.exit(1)


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

        print("Getting translations from libretro_core_options_intl.h")
        try:
            with open(t.INTL_FILE_PATH, 'r+', encoding='utf-8') as _intl_file:
                _intl_text = _intl_file.read()
                _err = False
        except OSError:
            print(f'ERROR: Could not find/open {t.INTL_FILE_PATH}!')
            _err = True

        if not _err:
            _hash_n_str_intl = t.get_texts(_intl_text)
            _intl_files = t.create_msg_hash(_core_name, _hash_n_str_intl)
            _intl_jsons = t.h2json(_intl_files)

    except Exception as e:
        print(e)
        print('\nERROR: Something went wrong during synchronisation! Cleaning up...')

    print('\nAll done!')
