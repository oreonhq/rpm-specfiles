#!/usr/bin/python3
# -*- coding: utf-8 -*-

import struct
import tarfile
from argparse import ArgumentParser
from binascii import hexlify, unhexlify
from contextlib import ExitStack, redirect_stderr
from enum import Enum, unique
from hashlib import sha1
from io import BytesIO
from itertools import chain
from os import devnull
from pathlib import Path
from sys import exit, stderr
from tempfile import TemporaryFile
from traceback import format_exc
from urllib.parse import urlparse

from fontTools.ttLib import TTLibError
from fontTools.ttLib.ttFont import TTFont
from requests import get
from tqdm import tqdm


@unique
class Tristate(Enum):
    NO = 0
    YES = 1
    MAYBE = 2


UPSTREAM = (
    "https://github.com/khaledhosny/ots/archive/"
    "v{version}/ots-{version}.tar.gz"
)

# We use SHA1 checksums to enumerate manually-examined files because the test
# font files are generally already named by their SHA1 checksums. Note that
# SHA1 has substantial cryptographic weaknesses, but a cryptographically-strong
# checksum is not required here.

# Manually-validated OK fonts
MANUAL_YES = {
    #
    # The following are corrupt, but are recognizably derived from the Google
    # Noto font family, which is OFL-licensed.
    #
    "051d92f8bc6ff724511b296c27623f824de256e9",
    "1679504907c14c2f27119135bd5da57f8713dd05",
    "16a8e02ff1373539ca818da4f70e9b8573563f29",
    "1acb1be6d45ca77a1b734e3892b823a34634d38e",
    "1e665cdc2796a76d8fd46232566795aa890991b1",
    "2069628b7b2ff2f8367f46c366f010c4f5a6295e",
    "226bc2deab3846f1a682085f70c67d0421014144",
    "2393b84159bd84138529dd136ba6bf45a7addd79",
    "27539eee6487a75cc1ddf8c80b8e3f863ee540c3",
    "29ca0fe494750bb483ed291cffa89d55279d3ac9",
    "3857535d8c0d2bfeab7ee2cd6ba5e39bcb4abd90",
    "39e15202b9fa9700438dbae6343ad8b21b359a68",
    "3b1f374416818644fa5cdb1d592659e502506888",
    "44a458acc6abfe78166e99c5ec9ec0fcf46182af",
    "45855bc8d46332b39c4ab9e2ee1a26b1f896da6b",
    "5028afb650b1bb718ed2131e872fbcce57828fff",
    "52a846621453e288b657f84ef423ff3f832b6c0c",
    "5614290438dcf671fcc1f2858ac9127e45f500bb",
    "56cfd0e18d07f41c38e9598545a6d369127fc6f9",
    "5dfad7735c6a67085f1b90d4d497e32907db4c78",
    "5dfcc2260fa1a08c72655c18885e50260703c863",
    "6466d38c62e73a39202435a4f73bf5d6acbb73c0",
    "6830389bba9787db7da796f364aa47b951e658ae",
    "6c1506d68d00e95a065d97e30964857e0d91c5a1",
    "6e43399b43162dedd7054e00ae97e7b0a71bf72d",
    "6eb6ce1f3930892d42a24d9fe955585c40a59cc0",
    "706c5d7b625f207bc0d874c67237aad6f1e9cd6f",
    "71eca05729f14607e81e9476dce804fe3bafc086",
    "72106114384cb564d4691bd3ea38960b0148f00b",
    "73bf759cd86e12788cd3571daffedeb391fad078",
    "757ebd573617a24aa9dfbf0b885c54875c6fe06b",
    "757ebd573617a24aa9dfbf0b885c54875c6fe06b",
    "7a37dc4d5bf018456aea291cee06daf004c0221c",
    "7e14e7883ed152baa158b80e207b66114c823a8b",
    "7e14e7883ed152baa158b80e207b66114c823a8b",
    "8099955657a54e9ee38a6ba1d6f950ce58e3cc25",
    "814e2e2e76682ab9a518493b475b23565993a4df",
    "8a8dc0703e7a9d14427ceadcea275dfda6a7f844",
    "9192ffc3ddba8dc44a21ccac20bf743593642241",
    "94895e7495f726fa316ca3f2a03c98b86dc20560",
    "9883c9ae58c5dd598ab2fdc142e2dacbc0ad1cb3",
    "99e872a7478a9f7f7f2a183d623f2a5ebaff72ad",
    "a0ca212e069702964aba80ab9c28bcb8aabae782",
    "b9e2aaa0d75fcef6971ec3a96d806ba4a6b31fe2",
    "b9e2aaa0d75fcef6971ec3a96d806ba4a6b31fe2",
    "bb0c53752e85c3d28973ebc913287b8987d3dfe8",
    "c64aff5250ea7360a18154e58678ab14a8e6fee9",
    "cc5f3d2d717fb6bd4dfae1c16d48a2cb8e12233b",
    "ccfc10b31bad1fb3ae508a332c7914c6db037188",
    "d343af630ddff2ed15ae72d9bb4949bb384a8e03",
    "d3ee8b9422e66a4dc827a15a65667bd5eab9ce5f",
    "d4eaf020145c14e2cd76c49353da1fdff8e4f62f",
    "d629e7fedc0b350222d7987345fe61613fa3929a",
    "d69ecb7001e46df61c33e2ec74fdcdd32e018db3",
    "d77f5dd2f02db900f5d568349dc6ed58683a00a9",
    "dcacf960143aecbc692471b2a658c8dc42c9613e",
    "e207635780b42f898d58654b65098763e340f5c7",
    "e31aa13e4a7b565c68e4822d2ef7d16069f8ffab",
    "e9e765985a2beed45d8c4c4666d94a2acede9d48",
    "ee39587d13b2afa5499cc79e45780aa79293bbd4",
    "f293a7cc0c9fad957df4904e8ce5e366e7cab93c",
    "f499fbc23865022234775c43503bba2e63978fe1",
    "f9b1dd4dcb515e757789a22cb4241107746fd3d0",
    "fbb6c84c9e1fe0c39e152fbe845e51fd81f6748e",
    "fc4263389f1a48dd3d1c793dff6b1e0cf8bccd33",
    "fcdcffbdf1c4c97c05308d7600e4c283eb47dbca",
    "ffa0f5d2d9025486d8469d8b1fdd983e7632499b",
    #
    # The following are corrupt, but are recognizably derived from the Lohit
    # project font families (Lohit Bengali, Lohit Kannada, Lohit Malayalam),
    # which are OFL-licensed.
    #
    "1c2fb74c1b2aa173262734c1f616148f1648cfd6",
    "270b89df543a7e48e206a2d830c0e10e5265c630",
    "442a5b09fc1d847eb353b9e219e26067df8b9fb8",
    "57a9d9f83020155cbb1d2be1f43d82388cbecc88",
    "82fae690a786b2d96af7d4845206b528381fa109",
    "908810fd6350c87a62c2dc4bb623e54ddd8aa042",
    "995ca3cf99525e11fcdfeb5ba9f45a6cc602fcfb",
    "9a6305f950f8e3960618b78fca6ba7d7abf3b231",
    "9c3c16ff5fb0e0adef3344f011b5bbb1469f2fd4",
    "bac8d8c1ad2b8a50bf10853c9aeca4fca6c3bf3e",
    #
    # The following are corrupt, but are recognizably derived from the DejaVu
    # Sans font family, which is under the Bitstream Vera license.
    #
    "1c04a16f32a39c26c851b7fc014d2e8d298ba2b8",
    "3fef5bc4d1567fea803c815a0d53d6d7bfa9bdf7",
    "43ef465752be9af900745f72fe29cb853a1401a5",
    "884801ab66022b60168010261438a4ed983ea9a7",
    "a69118c2c2ada48ff803d9149daa54c9ebdae30e",
    "d32823ca92b0443465c07625325bb64a7d78f47d",
    "d4acbc69d72d4ed528367718f022708070ec9635",
    #
    # The following are corrupt, but are recognizably derived from the Lobster
    # font family, which is OFL-licensed.
    #
    "4af3c3b1bf2882e84f25b30bc4aedae2a0b5f98a",
    "a98e908e2ed21b22228ea59ebcc0f05034c86f2e",
    "b2093e804590557247aa7bc2070757c26344c565",
    #
    # The following are corrupt, but are recognizably derived from the Padauk
    # font family, which is OFL-licensed.
    #
    "56bf9590c3f7587a632539b74a7aa0a04dbaadd3",
    "bb9473d2403488714043bcfb946c9f78b86ad627",
    "d8df0f95c805bf3986671a5f39d4e1ce1ef278ce",
    #
    # The following have no apparent license or copyright information, but are
    # recognizably derived from version 1.003 of Aref Ruqaa
    # (https://github.com/aliftype/aref-ruqaa/tree/v1.003), which is
    # OFL-licensed.
    #
    "257a9ccbda162eec44796987d8e20fca32288029",
    #
    # The following have a copyright statement but no license information;
    # however, the copyright statement indicates they are from Raqq
    # (github.com/aliftype/raqq), which is licensed under the AGPLv3.0; the
    # upstream repository makes it clear that the proper SPDX expression is
    # AGPL-3.0-or-later.
    #
    "bcb95ceaa9bad402a1a2b620c153a6bc792bf167",
}

# Manually-rejected filtered fonts
MANUAL_NO = {
    #
    # The following have no apparent license or copyright information, or are
    # too badly malformed to decode it.
    #
    "00ac7a910785ea3a30655fe386d4cb02b39719aa",
    "011facefb10ee4f813117eae60bb5940a280ae30",
    "013d9956e40d1ea194c4d7817fbf220d6be9c33b",
    "02d99e81593bcabce56b6a589254e8bc77e00208",
    "0509e80afb379d16560e9e47bdd7d888bebdebc6",
    "05a7abc8e4c954ef105d056bd6249c6fda96d4a8",
    "07165649b488b700585197b1d1083f94ac61d525",
    "078400f5718f84841fc43a04fd28d946ddad5e37",
    "07f054357ff8638bac3711b422a1e31180bba863",
    "080a26ad508861558f5f69836881bb0b8e8842c2",
    "0a228b7430d18283b6564822c06e8521dac93407",
    "0e4a70a10a82f7f4d63865006e81a445de26d3d1",
    "0f4f4a8e4a247694370ff11ae8b129395eca85fd",
    "0fce4352e04a156a1cb8d4bc344cd2be1dfe7177",
    "103ad354e517994c447b9c5c6914a290517cb5ed",
    "103b47d389cb700e76893677f51f7b74d09d08d5",
    "173c4c23291c983fead3d734afd8a4de504f508e",
    "17cbd36aad32fe96dfb6dc49ceaaed54553c9189",
    "18052b7fc1ca5c188b54864f163bebf80f488811",
    "1a6f1687b7a221f9f2c834b0b360d3c8463b6daf",
    "1c2c3fc37b2d4c3cb2ef726c6cdaaabd4b7f3eb9",
    "1d5090bfad0eeb11c88882085d4a195f73926327",
    "1ef2c4e95428d382ed8653c6657bdb66eb0f415d",
    "205edd09bd3d141cc9580f650109556cc28b22cb",
    "205edd09bd3d141cc9580f650109556cc28b22cb",
    "217a934cfe15c548b572c203dceb2befdf026462",
    "23b2a3316b3797bf9a61acdf36cf63d10ab3342e",
    "251a4ffb5418b336217a9e7958941192b5a20137",
    "2a124fa3e39a294280d406c4790398726bdc66ca",
    "2d80771036e065b9cd582b769d0388a0de90f84f",
    "2edb1d50d2b8f4ccf8b7d56e7f354dd86be081f9",
    "315da578ec2c7e391a93ed484786b5cc93dc2739",
    "335e7e5a354010624679dfb52609652c4a7f6fc8",
    "3511ff5c1647150595846ac414c595cccac34f18",
    "35159513f8d8422ff1a880a039ad68c857660cdd",
    "361ce9ae6e20175595cac0cb82addcb184e20953",
    "3684bc52f9aa06e9e6de67d80b626d44ca2bccf5",
    "375d6ae32a3cbe52fbf81a4e5777e3377675d5a3",
    "3b9bcfd57f7f18dd4c45ba51e77b23b3895faa9f",
    "3ba5737414924ed17800ff60ff21a524a513e111",
    "3bfa96a443c19de63f28554b748bf84e57ee51c3",
    "410761bc1115173bad3f6b0d3d72103e1dc32f67",
    "41c14459f0f134a81fc5f4051b861bae8503c87b",
    "42e947856c0ee90faf78051ffc41e527a8ee8be9",
    "43979b90b2dd929723cf4fe1715990bcb9c9a56b",
    "457227a3d4dbf6dd062d251b2ae0c8b31f14c9b8",
    "4765a8901e377d1e767f67e1cc768ae3c9207bd1",
    "494f40cf28ec4c2753aa907941fe48b7d15f6b04",
    "4a7b3505f054f426efc6057fd0adc27f6c16c41b",
    "4c8e7bcd6b657941c4e846f6e48bb714fb3faf92",
    "4cce528e99f600ed9c25a2b69e32eb94a03b4ae8",
    "4d29ba6a49fcba83c9a0cb91835b8e5e9fbe2e0b",
    "4d9ba653319ad56fa13a724e6d2c357ff948c2ea",
    "52053c2de32349ee09bbb6a4e755c2b3e85b9821",
    "558661aa659912f4d30ecd27bd09835171a8e2b0",
    "55c321d6932942d22555ff9b985e905eb472d4d1",
    "58b7bd1ebd3396d226c5a777098d115a2fc9f56f",
    "58c575a08b375e51c9776275c5f877396ddf552b",
    "5a5daf5eb5a4db77a2baa3ad9c7a6ed6e0655fa8",
    "5c67809a0d4b9a16d9eba881282f920153b761eb",
    "60adec4d200651dbf91e7c373789bbc2a2c4b46b",
    "641bd9db850193064d17575053ae2bf8ec149ddc",
    "65932a3c0a5ebcbc1ac55267e98506e9dedf41a5",
    "68bfc9f9233e34db2c5ecb5fb966bf205f92079a",
    "692df3e4b35e0b83cc8991a19ae29e434e705124",
    "6d2cc2870fabdc4fa686b66accd404759349e4a8",
    "7043d3c69c50da8eba1a0ad627b9f6de70e832e5",
    "7304e91492c3ba14030446c92f084f8fb031e8e8",
    "7522970cb3bb80a698c206cfa61f8418767c1704",
    "7bd0df7f6f234108e1f87f45bcde74931dc16efc",
    "7c8eefff708b374fffbce135ba28a4565766e560",
    "81942d3ea419539b69990ba98f824a8a46dcb951",
    "8240789f6d12d4cfc4b5e8e6f246c3701bcf861f",
    "8240789f6d12d4cfc4b5e8e6f246c3701bcf861f",
    "8330c9816493e1adccc0500b414455b85088d7d1",
    "83670edbe0a52e2e84b4454b1a828c44b6692c63",
    "85d903c71a429ed98a012e742a700cbe2fef005c",
    "8668cff491460e4c5cd03142b87e9710fd4b5588",
    "8a97d860fcbd1294be09f2d0aebb764f2c12f69c",
    "8edb1c6072ff63478456cc93601b77b0eb3432e7",
    "8faaf7e0d92db057ff26cf5af44a44e873c054cb",
    "90d60863109aab420257ee10577f2673cb91b3e7",
    "92520e16995b11b01f56b3834f200416f656161d",
    "94bdbcb520c5301750167dc433803ac7933da028",
    "96813142f8614d945222afa529815dd1213e2b3d",
    "9682ce841ae16214afca9b5e584162611f88dfff",
    "985de319c172b29bd9e651b093271a8939c35f13",
    "9cb9bb35205cb4a7588a5a2b8e35fc4be856fc95",
    "9f553001b12ed154a54de011828fd78138c66113",
    "a34a7b00f22ffb5fd7eef6933b81c7e71bc2cdfb",
    "a34a9191d9376bda419836effeef7e75c1386016",
    "a37166581403c1fda5e5689d4e027a085e3186e8",
    "a64a622a50d6400592a9590c003afb02e9e4436d",
    "a80d45906af055b269d6e81eeae9e91d5c26ef27",
    "a919b33197965846f21074b24e30250d67277bce",
    "aca5f8ef7bc0754b0b6fd7a1abd4c69ca7801780",
    "aef6783789cb40fd037e26f2b299b9088adce089",
    "b48e5042d1f1f6cec531b73abf15c8ee4f2afc63",
    "b6acef662e0beb8d5fcf5b61c6b0ca69537b7402",
    "b927e6af295696a2307641eb9679d0832dd7c22d",
    "b9ea4b9b671307bc0f9745dd684e1e4f6e48191d",
    "bad5283f2b80a5669e03313446c962c50897adb0",
    "bd5ee794425c2809f262b4bc6e3c0b33008fca73",
    "bdb9d23d51966a2544da5a66fd8727f1e0654a73",
    "c69c27b17d332fbf33dbc8f25baa0a0a461293a2",
    "c7d76de613012ce941785c387eb6570d905bc6a7",
    "ca0e0bca764d78f46d533b11bb66466f5b489220",
    "cff4306f450b3b433adca6872ff1c928a6ede2c6",
    "d4e4a9508c6b9e73c514b8af27b56918f45c3f9e",
    "d7aec40dfc478e1adb022406decaadfd46e61f89",
    "dc2b2ffc9fc5318fea924276dc8298f2b06f26ab",
    "dcc4f3316f90bc8a4c05e0086d2b49fddd3a059b",
    "e071a5082117ad5a64dc3db1bfcd0a31d6db93ae",
    "e88c339237f52d21e01c55f01b9c1b4cc14a0467",
    "ea8c4b1d5178ae184ffd0346f12fd426850729cc",
    "eaeb6d903b14ee184f887aa8a0a81b917e252da9",
    "f1dba4340ce94f5359fa4434debc7efcfd1b521f",
    "f22416c692720a7d46fadf4af99f4c9e094f00b9",
    "f4bcb76e745d6390bdf0447f2128db19686c432d",
    "f457d1f9504dbf206f50ea8ae7ab1bc4c51b95c0",
    "f518eb6f6b5eec2946c9fbbbde44e45d46f5e2ac",
    "f5ff6aaa96256b0e2c1abfdebf592c0987a1637a",
    "fab39d60d758cb586db5a504f218442cd1395725",
    #
    # The following have a copyright statement but no license information; or,
    # they are corrupt but have a recognizable font name corresponding to an
    # intact font file with a copyright statement but no license information.
    #
    "01ae09f3a2ca8f33035e6261d09e9fe06b919174",
    "024ad17b23e4298f1d80246b63d63d8e54c76e3d",
    "08b3b69027fc071fa71910cc7857833b7e5f4534",
    "092da87de7e293efee8be43f531b5bf0612693a5",
    "0c60702ee5003855555fee931a2da7daa917a1ef",
    "0e4a70a10a82f7f4d63865006e81a445de26d3d1",
    "10531f9105aa03bf6e0f9754ec8af33ed457ad5c",
    "13124b99e25a379efbdd1c3820b1484f842e1ad5",
    "15dfc433a135a658b9f4b1a861b5cdd9658ccbb9",
    "191826b9643e3f124d865d617ae609db6a2ce203",
    "1de19636832bb7ebb45680fb09b44227f19a96ce",
    "2abab3950432f64f17882a6517a9b7d2fb2dafe7",
    "2f74c3cb404c60d9a46e883c88d6c10dc3562fad",
    "322aa2ac0a3916d3a5cb1e7789ca355de0a6bc76",
    "3b4a0f922a35acba59502ba042f35cafbff1865f",
    "41542b89c620cc3159dc2f29bd335d48136478da",
    "49331b1dd031e95ca803d632f69404d09ee6f592",
    "4fcaec74137a83b5304d7d5f830b81c9abed73e5",
    "56d013275a9626c7b10b677fba1d5d4752eec51f",
    "5733cd9ca76aead50df6240b6b42d466e78240b2",
    "83de2fc102dbe5e1738710655787d736e51f5b56",
    "89166e0ffdfdac0309d31012d1d5c1de8fe65a52",
    "9227eefacd215fee911b7c4f935e0bad9bde5772",
    "ad455c8c531334cf470a98901cbe86a378895c14",
    "af434603052be497e74415f2f160df0d6989aded",
    "c6c0f06e6819b04a2eacca8e20dc0882a21bc312",
    "cb5656f950377ad5de2c7a6df0a659fbb7065ffe",
    "cbc1d3e183f8138f94b788baa397413d7863eb07",
    "cf6934b8e2d100b495e219d1b079fa2c34133d08",
    "d052cc5e62def2facb5772d1b38112779539ef0a",
    "eb44137aa49ccb9ea7aad127a8fdc6e155f20565",
    "fd62f786684b29020b46c40ae4cacfbd044fc7ab",
    #
    # The following have possible license information but it is corrupt, uses a
    # non-Unicode encoding that is difficult to figure out, or is in a language
    # other than English.
    #
    "bd4c6cd00c8b7de49831f2153414c49902da973c",
    #
    # The following are:
    #
    #   The Ahem font belongs to the public domain. In jurisdictions that do
    #   not recognize public domain ownership of these files, the following
    #   Creative Commons Zero declaration applies:
    #   http://labs.creativecommons.org/licenses/zero-waive/1.0/us/legalcode
    #
    # Since CC0-1.0 is not currently an allowed license for fonts in Fedora, we
    # err on the side of excluding these.
    #
    "e502b70bfa49d3f497b2a15093a3765e29ccfdcc",
    #
    # The following have no apparent license or copyright information, but are
    # recognizably derived from the test fonts in
    # https://github.com/googlefonts/color-fonts, which are under the
    # Apache-2.0 license. This license would require including the text with
    # copies, but this is not done.
    #
    "5b376d5ec538bc3c86749e13a815661c7f5d9528",
    "c58d4e63655652bc74153333cd91f190a6e6671e",
    #
    # The following are MIT:
    #   Copyright (c) 2010 Philip Taylor.
    #   Released under the MIT License:
    #   http://www.opensource.org/licenses/mit-license.php
    # This license would require including the text with copies, but this is
    # not done.
    "aabe188315aa874a8e3ad3531efd3f62de10c67e",
}

MANUAL_NO, MANUAL_YES = (
    set(map(unhexlify, _)) for _ in (MANUAL_NO, MANUAL_YES)
)


def main():
    args = parse_args()
    needs_review = set()
    with ExitStack() as stack:
        upstream_tarball = stack.enter_context(TemporaryFile())
        download(upstream_tarball, args.version)
        upstream_tarball.seek(0)

        source = stack.enter_context(
            tarfile.open(fileobj=upstream_tarball, mode="r|*", errorlevel=2)
        )
        destination = stack.enter_context(
            tarfile.open(
                Path(__file__).parent / f"ots-{args.version}-filtered.tar.xz",
                mode="w|xz",
                errorlevel=2,
                format=tarfile.PAX_FORMAT,
            )
        )
        filtered_list = stack.enter_context(
            open(
                Path(__file__).parent
                / f"ots-{args.version}-excluded-font-checksums.txt",
                "w",
            )
        )

        print("Filtering contents:", file=stderr)
        for info in source:
            path, data = Path(info.name), source.extractfile(info)
            if not is_in_target_path(path):
                print(f"{path}: OK (not in tests/fonts)", file=stderr)
            elif data is None:
                print(f"{path}: OK (no data)", file=stderr)
            else:
                data = data.read()
                hasher = sha1()
                hasher.update(data)
                digest = hasher.digest()
                data = BytesIO(data)

                if digest in MANUAL_YES:
                    ok, message = Tristate.YES, "manually validated"
                elif digest in MANUAL_NO:
                    ok, message = Tristate.NO, "manually rejected"
                else:
                    ok, message = identify(data)

                if ok == Tristate.YES:
                    print(f"{path}: OK ({message})")
                elif ok == Tristate.NO:
                    print(f"{path}: FILTERED ({message})")
                    print(
                        f"{hexlify(digest).decode('ascii')}",
                        file=filtered_list,
                    )
                    continue
                else:
                    assert ok == Tristate.MAYBE
                    print(f"{path}: FILTERED, NEEDS REVIEW ({message})")
                    print(
                        f"{hexlify(digest).decode('ascii')}",
                        file=filtered_list,
                    )
                    # Generally, the same as the file basename
                    print(f"SHA1: {hexlify(digest)}")
                    print(f"Try: fonttools ttx -t name {path}\n")
                    needs_review.add(path)
                    continue
            destination.addfile(info, data)

    if needs_review:
        print(
            """
WARNING:

The following {files_need} manual review, and were filtered as a precaution:
{filtered}
""".format(
                files_need=(
                    "file needs" if len(needs_review) == 1 else "files need"
                ),
                filtered="\n".join(sorted(map(str, needs_review))),
            )
        )


def is_in_target_path(path):
    parts = path.parts
    subsequence = ("tests", "fonts")
    starts = range(len(parts) - len(subsequence) - 1)
    return any(
        path.parts[i : i + len(subsequence)] == subsequence for i in starts
    )


def identify(data):
    try:
        with TTFont(data) as tt:
            return identify_tt(tt)
    except (TTLibError, struct.error, AssertionError):
        # Possible corrupt/bad font
        return Tristate.MAYBE, "Bad, corrupt, or unsupported font format"
    finally:
        data.seek(0)


# https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fstype
FSTYPE_PROBLEM_BITS = {
    1: "Restricted License embedding",
    2: "Preview & Print embedding",
    3: "Editable embedding",
    8: "No subsetting",
    9: "Bitmap embedding only",
}

LICENSE_STRINGS = {
    "OFL": ["SIL OPEN FONT LICENSE", "Open Font License"],
    "GPLv2+": [
        "GNU General Public License as published by the Free Software "
        "Foundation; either version 2 of the License, or (at your option) "
        "any later version"
    ],
    "ASL 2.0": ["Apache License, Version 2.0"],
    "BSD": ["License same as MutatorMath", "BSD 3-clause"],
}

LICENSE_URLS = {
    k: list(chain(*((f"http://{url}", f"https://{url}") for url in v)))
    for k, v in {
        "OFL": ["scripts.sil.org/OFL", "opensource.org/licenses/OFL-1.1"],
        "ASL 2.0": ["www.apache.org/licenses/LICENSE-2.0"],
        # No URL for GPL for now, since the URL does not encode the version and
        # affected fonts will be detected via LICENSE_STRINGS
        "MIT": [
            "github.com/behdad/fonttools/blob/master/LICENSE.txt",
            "http://www.opensource.org/licenses/mit-license.php",
        ],
    }.items()
}

LICENSE_STATUS = {
    # This is a great font license.
    "OFL": Tristate.YES,
    # This is an Allowed License in Fedora but not specifically an Allowed Font
    # License. It should be safe enough to ship it in the source RPM.
    "GPLv2+": Tristate.YES,
    # These licenses require that the license text be included (not just
    # linked) with all copies, something we have not seen in any of the sample
    # fonts.
    "MIT": Tristate.NO,
    "ASL 2.0": Tristate.NO,
    "BSD": Tristate.NO,
}

for url_list in LICENSE_URLS.values():
    for url in list(url_list):
        if url.startswith("http://"):
            url_list.append(url.replace("http://", "https://"))


def identify_tt(tt):
    try:
        with open(devnull, "w+") as null, redirect_stderr(null):
            os2 = tt["OS/2"]
    except KeyError:
        pass
    except Exception:
        return Tristate.MAYBE, f"error decoding OS/2 table:\n{format_exc()}"
    else:
        for bit, meaning in FSTYPE_PROBLEM_BITS.items():
            if os2.fsType & (1 << bit) != 0:
                return (
                    Tristate.NO,
                    (
                        f"potentially non-free fsType: bit {bit} is set "
                        f"(“{meaning}”)"
                    ),
                )

    try:
        with open(devnull, "w+") as null, redirect_stderr(null):
            name = tt["name"]
    except KeyError:
        pass
    except Exception:
        return Tristate.MAYBE, f"error decoding name table:\n{format_exc()}"
    else:
        for n in name.names:
            # https://docs.microsoft.com/en-us/typography/opentype/spec/name
            if n.nameID in (0, 13):
                # (Copyright notice, License Description)
                string_data = LICENSE_STRINGS
            elif n.nameID == 14:
                # "License Info URL"
                string_data = LICENSE_URLS
            else:
                continue

            content = n.toStr("replace")
            for license_name, strings in string_data.items():
                if any(substring in content for substring in strings):
                    return LICENSE_STATUS[license_name], license_name

    return Tristate.MAYBE, "no recognized license was found"


def parse_args():
    parser = ArgumentParser(
        description="Filter impermissible content from the upstream tarball",
        epilog="""

Writes the source tarball in the current working directory after filtering out
impermissible content (test fonts with unknown or inappropriate licenses). The
result will be something like ots-${VERSION}-filtered.tar.xz.
""",
    )
    parser.add_argument("version", metavar="VERSION")
    return parser.parse_args()


def download(destfile, version):
    url = UPSTREAM.format(version=version)
    print(
        f"Downloading {urlparse(url).path.rsplit('/', 1)[-1]}:", file=stderr
    )
    response = get(url, stream=True)
    total = int(response.headers.get("content-length", 0))
    with tqdm(total=total, unit="iB", unit_scale=True) as progress:
        for chunk in response.iter_content(0x10000):
            progress.update(len(chunk))
            destfile.write(chunk)
    print("Done.", file=stderr)


if __name__ == "__main__":
    exit(main())
