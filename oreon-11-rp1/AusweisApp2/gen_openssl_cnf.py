# -*- coding: utf-8 -*-
#
# Generate OpenSSL configuration file for AusweisApp2 from settings found
# in the application's 'config.json' file.
#
# Copyright (c) 2020 Björn Esser <besser82@fedoraproject.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import json, sys


def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)


class _Const(object):
    @constant
    def CONF_OPTIONS():
        return [
                   'ciphers',
                   'ellipticCurves',
                   'signatureAlgorithms',
               ]

    @constant
    def CONF_SECTIONS():
        return [
                   'tlsSettings',
                   'tlsSettingsPsk',
                   'tlsSettingsRemoteIfd',
                   'tlsSettingsRemoteIfdPairing',
                   'tlsSettingsLocalIfd',
               ]

    @constant
    def DEFAULT_CIPHERS_TLS13():
        return [
                   'TLS_AES_256_GCM_SHA384',
                   'TLS_AES_128_GCM_SHA256',
               ]

    @constant
    def KEYSIZE_EC_OPTION():
        return 'Ec'

    @constant
    def KEYSIZE_OPTIONS():
        return [
                   'Rsa',
                   'Dsa',
                   'Dh',
               ]

    @constant
    def KEYSIZE_SECTIONS():
        return [
                   'minKeySizes',
                   'sizesIfd',
               ]

    @constant
    def KEYSIZE_MIN_SECTION():
        return 'min'

    @constant
    def TLS_VERSIONS():
        return {
                   'TlsV1_2': (2, 'TLSv1.2'),
                   'TlsV1_3': (3, 'TLSv1.3'),
               }


CONST = _Const()


def get_min_ssl_sec_level(json_data):
    sec_level = 0
    min_keysize = sys.maxsize
    min_ecsize = sys.maxsize
    for section in CONST.KEYSIZE_SECTIONS:
        if section in json_data:
            for option in CONST.KEYSIZE_OPTIONS:
                if option in json_data[section]:
                    if min_keysize > json_data[section][option]:
                        min_keysize = json_data[section][option]
                elif option in json_data[section][CONST.KEYSIZE_MIN_SECTION]:
                    if min_keysize > json_data[section][CONST.KEYSIZE_MIN_SECTION][option]:
                        min_keysize = json_data[section][CONST.KEYSIZE_MIN_SECTION][option]
            if CONST.KEYSIZE_EC_OPTION in json_data[section]:
                    if min_ecsize > json_data[section][CONST.KEYSIZE_EC_OPTION]:
                        min_ecsize = json_data[section][CONST.KEYSIZE_EC_OPTION]
            elif CONST.KEYSIZE_EC_OPTION in json_data[section][CONST.KEYSIZE_MIN_SECTION]:
                    if min_ecsize > json_data[section][CONST.KEYSIZE_MIN_SECTION][CONST.KEYSIZE_EC_OPTION]:
                        min_ecsize = json_data[section][CONST.KEYSIZE_MIN_SECTION][CONST.KEYSIZE_EC_OPTION]

    if min_keysize >=  1000 and min_ecsize >= 160:
        sec_level = 1
    if min_keysize >=  2000 and min_ecsize >= 224:
        sec_level = 2
    if min_keysize >=  3000 and min_ecsize >= 256:
        sec_level = 3
    if min_keysize >=  7000 and min_ecsize >= 384:
        sec_level = 4
    if min_keysize >= 15000 and min_ecsize >= 512:
        sec_level = 5

    return sec_level


def get_proto_ver(json_data):
    conf_dict = {
                    'minProtocolVersion': list(CONST.TLS_VERSIONS.keys())[-1],
                    'maxProtocolVersion': list(CONST.TLS_VERSIONS.keys())[0],
                }
    for section in CONST.CONF_SECTIONS:
        if section in json_data:
            if 'protocolVersion' in json_data[section]:
                have = conf_dict['minProtocolVersion']
                want = json_data[section]['protocolVersion']
                if CONST.TLS_VERSIONS[want][0] < CONST.TLS_VERSIONS[have][0]:
                    conf_dict['minProtocolVersion'] = want
                have = conf_dict['maxProtocolVersion']
                if CONST.TLS_VERSIONS[want][0] > CONST.TLS_VERSIONS[have][0]:
                    conf_dict['maxProtocolVersion'] = want

    return conf_dict


def get_ssl_cipher_config(json_data):
    conf_dict = dict.fromkeys(CONST.CONF_OPTIONS)
    for option in CONST.CONF_OPTIONS:
        conf_dict[option] = list()
    for section in CONST.CONF_SECTIONS:
        if section in json_data:
            for option in CONST.CONF_OPTIONS:
                if option in json_data[section]:
                    for value in json_data[section][option]:
                        if option == 'ciphers' and value.startswith('TLS_'):
                            if not 'ciphers_tls13' in conf_dict:
                                conf_dict['ciphers_tls13'] = list()
                            if not value in conf_dict['ciphers_tls13']:
                                conf_dict['ciphers_tls13'].append(value)
                        else:
                            if not value in conf_dict[option]:
                                conf_dict[option].append(value)

    return conf_dict


def print_config_file(conf_dict, sec_level):
    max_tls_proto = CONST.TLS_VERSIONS[conf_dict['maxProtocolVersion']][0]
    prelude = (
                  '# This application specific OpenSSL configuration enables all cipher',
                  '# algorithms, elliptic curves, and signature algorithms, which are',
                  '# needed for AusweisApp2 to provide full functionality to the end-user.',
                  '# The order of the algorithms in the list is of no importance, as the',
                  '# application chooses the algorithm used for a connection from a preset',
                  '# list, that is ordered in descending preference.  This configuration',
                  '# also limits the minimum and maximum cryptographic protocol versions',
                  '# to a range needed by AusweisApp2.',
                  '# The settings used to generate this file have been taken from the',
                  '# \'config.json\' file, which can be found in the same directory as this',
                  '# configuration file.',
                  '',
                  'openssl_conf = AusweisApp2_conf',
                  '',
                  '[AusweisApp2_conf]',
                  'ssl_conf = AusweisApp2_OpenSSL',
                  '',
                  '[AusweisApp2_OpenSSL]',
                  'alg_section = AusweisApp2_evp',
                  'system_default = AusweisApp2_ciphers',
                  '',
                  '[AusweisApp2_evp]',
                  'fips_mode = no',
                  '',
                  '[AusweisApp2_ciphers]',
              )
    print('%s' % '\n'.join(prelude))
    print('MinProtocol = %s' % (CONST.TLS_VERSIONS[conf_dict['minProtocolVersion']][1]))
    print('MaxProtocol = %s' % (CONST.TLS_VERSIONS[conf_dict['maxProtocolVersion']][1]))
    if max_tls_proto >= CONST.TLS_VERSIONS['TlsV1_3'][0]:
        if 'ciphers_tls13' in conf_dict:
            print('Cipherlist = %s' % (':'.join(conf_dict['ciphers_tls13'])))
        else:
            print('Cipherlist = %s' % (':'.join(CONST.DEFAULT_CIPHERS_TLS13)))
    print('CipherString = @SECLEVEL=%d:%s' % (sec_level, ':'.join(conf_dict['ciphers'])))
    print('Curves = %s' % (':'.join(conf_dict['ellipticCurves'])))
    print('SignatureAlgorithms = %s' % (':'.join(conf_dict['signatureAlgorithms'])))


def main():
    if not len(sys.argv) == 2:
        sys.exit('Usage: %s <path_to_config.json>' % sys.argv[0])

    with open(sys.argv[1], 'r') as conf_file:
        conf = json.load(conf_file)

    ssl_conf = get_proto_ver(conf)
    ssl_conf.update(get_ssl_cipher_config(conf))

    print_config_file(ssl_conf, get_min_ssl_sec_level(conf))


if __name__ == '__main__':
    main()
