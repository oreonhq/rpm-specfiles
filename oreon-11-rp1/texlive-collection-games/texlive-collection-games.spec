%global source0_hash 76079fa4ba5089f72df8facaec979b3c943efa5f23405ca2596d79027c6764fb819b825c0a226cd009fb82c4b935adb78d4dea25dc5895d77064ba21f8c04c29

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-games
Epoch:          12
Version:        svn76381
Release:        4%{?dist}
Summary:        Games typesetting

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 9c647b07f787ddedb958a3bc866328df77ececc346031ce491b68e617af85cab5eaef58499a9c7d0b83920aabe89d99d733193984a3b05a07b70ea7b3ef7a421
%global source3_hash c0db0c11a0b0bda530f97332d3aadf7e4762bffb3b71f008c6b3c01a2c1763867c4fad4c1cfaf9ed4cfaf37a568335e8b5d272cecc0280674a9a6deaa4471bd3
%global source4_hash 1c40793df5515a0dcc71c9c9ef795c69c88075ad662b19fa84dc58d907d39081f351179b6f6dc4551d789ffe8b85ad00c3fa623c1fd90d36820a6d2b4663756f
%global source5_hash c464e581aa378d7ee32c25144ca2c39ea5a20ed1cdd66ae2c686e230bb1aff44a1c59c56c0ae130389ed19e237da38f0cd0c3b110cd631229d0aa986c833fa31
%global source6_hash c4352855431ebb09c6627428a7e655a1a55ef9e98c3d2fb3f3bea2f48f1a40504fe7c5cf1a89bcacd4df604868175878c311d0b1702882f15aca467acd3a92a6
%global source7_hash a51381589e038325fca57a587f3f3a2a7488c6e51bf1a279c1eaf488a9e13e6a7b89d711a0a5ab65cd32f047c08ed70395b904b7eade7df162f0dafe41c6e057
%global source8_hash 42f5880574be508188f20be2627bdee6e9d4ad55370508e82306fda63969b6f08d0c92ea92ac4ead7a9462c716e0b5bd66af863fad861549034ee08949219697
%global source9_hash 8ba6906864bb6c84e6875555ae0a59976614a7175613af573b86119249b863d46ca262c2d02c1a727d4c1a8536858a74156664d7d1593944ddeb85ff77e2e821
%global source10_hash c0b140fec796b9b0460e5ee1d4aaeea424c16ff8e0bdc3689b3ae3ab56509966bc3d245dc8da748d3762924cb2525684a24077e74ac36f5a235722ce3641795c
%global source11_hash f26b331546fbf2bad64991a171796758afdaedbe21c7411e05c5e4e5850f432dcbe50c9361cadf8d15ca67762537250c443c05a501bf151256103ee3186169eb
%global source12_hash eadb43d60592c8137babad2900c9966927870529c91b1447756c931a8501fc631106ac3d5aa5a29e254b0e791e4d1da0f41a10a4b657b8a8543837f6a35156fd
%global source13_hash 060c852170cf998367c043416c134e69107f8f2cfd533c1eaf270d3acf8183d5e6550f651e3f28603dc3a905d4015f600b2b1cb7dd236737f5c4331eb06f4d95
%global source14_hash b4eac6208ba400fb3371f9ebb4a7cce8e27fc4fa85b6113d5ad6e1f94455253a9a020de5989fa44dd25fad60691be7ffd7b27133bf81e9ed24943a2be2422235
%global source15_hash b4b147d231a1ee53127794880ca54923c646b063796e7c272525dde72e9234048faa09ad0d42520f400083daa11000affca741766a02ec73a5a735336acc18b6
%global source16_hash 946699c5766223ad51fa6e637a014d551903b5ae818dba64c0e8f61e5a770547e1c33587b7d78786a6048f73ff554e3c148ffa09c65d27eea32f082045dec73e
%global source17_hash fccfd1e52dcd10e79c068042b4ab3ec56ce58c23398583605446894bfd0102951547f5486a31ef8ffa64e31f7531406483591c92e144669d72d5b35672a9adea
%global source18_hash d537d8357fa1d718f685d3bd05afe849eaffcd63050b8ef5f85dfea39260b9268e7ed12e727ac3a14a7194f21e4de158bc0a8143408c45e5f3718ea143a27aff
%global source19_hash 7512a7fa81198895666d135bd50d75345e8d7152289f51126fa3fb68a028f05666d4807e63c82db5068a9aeaca11fcb06d7b0edd4d77804bee195409bf042144
%global source20_hash b8d1c056783c4a71484a00f0d80de4eb9de3beaa54cc4dc71e5a7c171871b5dacba753ad03ab196661b1bd73cf9d2eaf202a813b73bea405f807319a143644cb
%global source21_hash 0216a85d539ab19aef8c2c4f313f5095aa39e4955ae9610c14d0243081b7af98f50a74a2f7720b376493e660a5486f83e69b41f8cb8017ff66a8e706eb9ca71b
%global source22_hash e1672a5fc0087de00e61cc85498562973622d1e3f7fedb86813951b9ffa3ac943b5296967c41d7e0ad67a628c9781eaa8e543df00bb4baaaca875ecfb26bc9c5
%global source23_hash dcdb1fab95295751b72bb7eb3cacc4b20d7d0e408b97d7196528cc265e1784094a5049a2ad9f9eaccd81e35e7ee8372a8b5baef469cb5092e9ea0408b9621288
%global source24_hash 4af22bc285bac3f368778dae5c91cf6a1999748a6dfa5fba96e166ed320e124c33f2b6d6bee16ad8d00d0f8067b24bb3567a1aba849b74a6b02fed3bb85dbc0a
%global source25_hash 58493c9b39343846913263f53b3bfe0fd89e4adb4154580d1bb0ff5d32b5b91ddc75511a0241fa3b98faef8b2d9d7c1846aca486e0c7262f8b3ea7a6bfddc619
%global source26_hash b100e95290634e0697bc420259b287650c8bc436a950749c8f60955b4bb1f622f692730640c8b882400d7f1ac7a9cd847cfeacbd5310a5bd57f3925f21766159
%global source27_hash f34592d3d47f5cff749fc0bc44b4de233a13bb962674cb22e06dbabadfedfc303049c73b18cc0807e0f1827ab583732a0019345991b3bedd6daa1f3e84c40108
%global source28_hash 3c860331312e18a6b3c4c9560e1d5dff1eb05863789dda907b641670f59abbbcc1442f665f627d3d8e39f1a38faa15501b6dec71e57887e835a2a604fc9e2fd3
%global source29_hash 6dd4627b4f460bcdd91a3d40cda2e622f25c5df963e25e6f0ebb6f5dbd2f3a203a1f5ba3aebe23a8c667c23597b461a1e0a8604f6049b2f6e0933ea4603c7441
%global source30_hash efc8c4892ea4cc8ae395907fc428fe74d535d689a68b3b21422c5c944d4defd57747e519dbca9bd2df2dd010b99e3132afceadee36d547fc11b04480147626c4
%global source31_hash f19498f0f9a7ce349fab4291fef80ff2f2f9eb88c60edeb76174918955fab51f22a0d06b533112e594c0f4cfba23feab58c41fe75e1c4fa2fc4db7cd9f473d0e
%global source32_hash ee1a90d491debac3f22f470e5df79e11152d153cef97e8d2e38c5d8a60a1931384d65bb91a6d459e6aeba39741763fa67d589bf9004efc5059699ec621b99e43
%global source33_hash e82683253d7790448bddbcefc617d0f0e91b5373de477f1c78a5db9256d632983b1d5f700a0c6fcb4490b746e932de3fe40a22875a6c0d37f6d0ae728867b73e
%global source34_hash 97c92b9c8644cf060da8b3306c8a3f26d1c59f36b1731ca4b6af06ec77211ab676963d5ed8fb70c6a63096a7224cfaac22cf77d5dc39f937902815bea778f323
%global source35_hash 4590bbd431470ff57ca5f62f1cb313e95353b35e03862a1e9b88eaafd81bbbf256577557ddf50901c51036fdfb0773b51bc5b0ff78927a580c492b05393bc91c
%global source36_hash 250e53374752a67747bc55299b85fbe8449f0338a5cf514d6e9ab316ebc63a2ff0423011b3513e15690c1cd3a64ad96302a6cd48fa10e68ac3c49fddae004dd1
%global source37_hash 34b2e61744e3f8cf180a61ca13788834466dad7bdf831e576829e0f6613c5e8a6330075e89516915728a5936a68c14288c79e0f050e5956964d69bab3784d9c6
%global source38_hash 36c1a35cb4efb4dc340a439a921252cbaf48d3f0b7fab0010a7fa22d8b03e7b5b644244410efa9fdc63b5fbf69eb9396cc048908d00210e650941a0647d3f4d3
%global source39_hash d00c8ecbc9c76c2864a52a8bc9f802477e402a59c86789252bce1b8296735035b7b9cbb1c3a18baa76cd1d308d4af53d7d2f64ee9aa37a70e33bf27e1465207a
%global source40_hash 9bdd655263da0847bed65c71e423e301a35e69d7cceacd650c0e9d4be91800c0de5fa0d7aa917a6d5f5abcc585ed031e6ec84ef003bb813be41e3daa3ab95f82
%global source41_hash c40ee6abf6513cfc4289ddb97e325fcb46411a1ed514a78198466afdf08cc8edae329bfead5029a4d8635720f2b38fee60f5bb31cd63c98c96782e297758cabb
%global source42_hash 24f9e5fd7f3864aca81b1199e3125ded83944de9bb3b35d1a6ca2f211b8ba5c2ef9420465aea34ec7a92977242d045257becdcf993c2839de393c26e6339745e
%global source43_hash ba43a27b5e62496ccab1baba3aa9bf4b195661e77c1f79f7dccd7981fe95db26f6aaf09f21356aff761d0d749d6813fa402255e0ba37917f1ec5cc3006a8d371
%global source44_hash d4f274bfb04dabe6610bde4fb9e61ddc07a336ea7252d7f60bac950b202f89973a29c85a551d70bfe9270b54526d661122dc3d5ecd6203830b3e5eeba26ac0d1
%global source45_hash 06c61f5a0a2b39d644d5b741877f445dea48fefaaddfb7f60251ecb328f16ba2ec6f09731608ac5ca7b288fe77fc193984dad25b8f0ad0da5f35bdd43fb2f8ee
%global source46_hash 980a3bef8b8eb51cd454c835ba09205f8dedab92f747db9704c72d5433db75f68df298ee4ca06c6d68e0cb4c4b733c882d14bbbb9d877406163b0f95730a10ce
%global source47_hash 89dcaa05945e2ec3e435c96932c4f4320d79f49545b790aab10acdd626ecf73f98c0f499fbda1b0a2cdfddf7068b5fa2d4e5d9989a19eca52ce1204cc1ba0a74
%global source48_hash 0ea60067f88205070da91ada957ba68b85584273ccfa407ea625d324d2f7f838893636ce9de0be69cd82d52e72438c0300375cf45cd56c8eb6c89d04e127eeb0
%global source49_hash c258f3533b48b32805584c2aeda34ec269a7d413203209186a9983f2e80297e59d72ae9a7d3ec3466da93201631d53a2b8252faece3570a9ff1800cde143d2d5
%global source50_hash 01083dce26c97d5bba3a38beef51307dcdf23e097ce2f15f7fc41427c0b4ec731c8c483b76c9c797952e0741e2035fd122e5b1a9c110b38bbbddac332840cc31
%global source51_hash b995003ff03bef5d3da4267ec3104270c1a97d31a1b5380dbdbc418dd64d03383051328e4431f1bb6ff97055ef51bdeeeb74e071c5d57e8a81c8ed245aa7f251
%global source52_hash 0246c262b091ae410d53c3c8a2cc190bbfa453e6d7d196e0777c9790fec68640046b3a4e9068cfc3f2594dda23294a65c30d35a0463486723aa924a1428a36d6
%global source53_hash 8b2be660f0b0546b0f96dcbfd3f239624b70b40348ee57120d3a908f3fc95e86cbc29bb96eb4023732a7db65bce5751d7b34f3940a4f0da7f055c7c30be45121
%global source54_hash 5233ec0decd9426b3890364040fb271b779dc04bb6ab47bde9f3d1a74e00f41aa7a212b123bf61ab75ad5f6c7316ede71bc29a5dcffaca866e841d33be44a990
%global source55_hash cb39be06af98a16057c130450ccb9b9f878c07246c67bc0c51fe36504cf48993b520cac239051a9312c26b0e8a6a5e04190532f298712cc5dac60c37686d8c43
%global source56_hash d19f70404513d5378a2e56dfdd4513b23e555e8152f886be17d85a4398d0bd166110d29a79ab47e16a41ebc6811d6756132741758941e68a773a899b4da92d47
%global source57_hash 602132bc51f1ed20f045bf0c822f201f7bbf3386f9181599894e66cb3c59f4ed15364013a5e30bfc59b22ab3fe4931872b779d1e7f34b8dbcd1eabe058b1f5e3
%global source58_hash 29cc8526543698f218e8c9c20b424fb2b05d3ee0a67c70a2afadd33dc49f0030ceb440b349898b8bd66a53a5682aa8289d081e4502fa5ccdfe481b4e2430de03
%global source59_hash 0b2485f7833cc8f4912a035284fcc4d0e710d942330a16a36788f7d80ebc5d9eb9ceb98f6a15b11e6391429d4684c985a83753696c1202bff5f0c5f4e528ce59
%global source60_hash 6848acf10eb3c4b2e0dbb9e33868ac4a1c639771c1508a19e4d41512750cb0978dbb61a570830f2f555e09ade976d9cd5c91d23da73013a7310b9cae02b6ee1a
%global source61_hash bc62aac04466286d07ffaf65b31c4d7ecdc6f4194f99192700774a213ca52861b0296c3f9864c187a83926696ad3a3a139ae7c00be2167b970159a7605fb4570
%global source62_hash 4fedacde595f96c2bd8babf38d4aae73b3bd9f73572547ed5b93e98c16dec50e89651c42aa4d90046464c765aa2f4d5f32d8aeb6ec5de2bb30f6599e53314e81
%global source63_hash cddd446d5b63ed22ebc4e561e43fa8b4b1ab2cdb1ecc45ab98e60d6799646845a9d432aa45248e7cf70bfc4aea10cd42960a8846479df46a7cd701f792b4ca74
%global source64_hash 8ba85bf32ff739e4588512c2b33bf242b00e3f38a7ddb1b3f5582cd19b925e1adf52b4243857f1ef4b9d8198e8dc80a9aff8a63a7b3ff926978dc7e5c81262de
%global source65_hash c975c73b8737f008b7f31af86e6c8a89de3f907c6fe782f075b04819bd936da3853a8ecf15935c04970777a4873b5baa38f9c675cc8943190df84ddc511dedba
%global source66_hash af025805142a845bde22a5fe095fb96cd533d69c50bfcea8716dd7d61fc95c41727c16127c2f2b60c5bf2b55870d698db54d307c2b025aff3e251419ed58a3ce
%global source67_hash cc93ed7340380b2072ac7df4c0d343e43e1a3ae4252c42d9914edcb33232597a5c86d22cce3dc02218e6e725191f056ef9fb342e88d1a60dcadd8d011723b649
%global source68_hash 65baac7fa63a01c70293baa26d99d21dc999f959074a3d2668cf6661d3db059b47d2f577f8c9f5d7ac6014e601f50e547283c55541c492b3c2df4e5f01b65be5
%global source69_hash e576104ce9cecaf545b969309797f06fec96f0b660a5532f927c78bbec6d4520c7f45547098a067a670ae72878c5e1301ed67ad44439480cf9d1575d301fa16d
%global source70_hash 25a4d2bd7fd27fa844bd17f5eaff118e661fb2783bed639aae58975ee757621e8f01affbf5537ef6e3c84bfdda246734e2d86d47c3955d9ed1d1302553036801
%global source71_hash 80758f034a3c3a76f15ae6a239772636df2897a680c313a5a6d6e7ddcfc29cba0d7db069deacd70187354ab8469aef115585bafeafb68e010e5fc308e6fec6b7
%global source72_hash 43758d4e13f8cb5973fc4a4be9700bc2fb9743c513ecca890e4a46a19bda618895c98f904607b0fa92678f8df018bc0956fcfab30d11fca745c4df9aefac087e
%global source73_hash 381b58d46bab7b2c382462aa21ad1dff25b543b1097b2b0db39b338e13bc64c121135a156c3b4e2877beae867d76ba4ef91cdeeed4ee4b1364b3fb77e45a6588
%global source74_hash 7bb3ff5f788e8970abfb2777000d5fe0dd606730095a09d17141630c642178b5def83fb35cb460003edd5e040106be0acfd1a30b23c7ee67669f5fbe51a42775
%global source75_hash 7a2c61f9ff7894e472cb07ccaf2e60be3ac1fcd9c2053935d27c8e197dbf7746f663a3c35be4663710fc8b08a8ed932422b3e37e89203548903d12a4415a29b2
%global source76_hash 05e8d7001a6c9c2ec32c762b65e3285ff6c1c082efc26fb3c0be633f906a0b20762e5e0ee3eeca5be6c7ed9581b6f3501be24173c4f6aa19002a33d7e448028d
%global source77_hash 6b1c2473b60a3fa6551743ef0d290f2e51f4152e446db384f3fbdea6433ffc3db136cae2ecb4d8026eca8b726440aad78a66b81a726cf6d14d7f181bfaa9ed49
%global source78_hash ec3ebbab6bb6eb622e214e80e2494af24219c5aeacf9bb09c0e09a06f9de316c1664acae60ecfaf58c5bce5c63e4e80c5971dec49bef3764c8b4875d6d78ec13
%global source79_hash 28117df00d778cfcc2ac035545c561ba1f078f024a8676e32d339f4c47b2206e2711474edde9c15987c397dc192528c8a584dc6bd4121e6da6588dc1a2bed71c
%global source80_hash 4d47dde91731affbaaf168e1a3ed79160312d9533636a95c6f9736e6f8c01f2514ec4e4c015bc9d68d0abf637b39fc063820c856693e8876ff7aaa1935f009f9
%global source81_hash 7eaa938339d1e59241b85cbbec4238be4fe2aaf4dbb3544c6d1511723c62b96dc5fe38c4fae062dd2d61760739caf0df3652b710546a6725d072969df8e68b0b
%global source82_hash 16ea492fabb90e0a649d5ff8e13b358a4ff7a612df34cd60a7023a1572337d237b87bdd5deadd206513562cfc1a3b27e834c49fbd5204277d38dfcf3a1e4e586
%global source83_hash 0d60562aa05a1672035826378326352bc079860ec507375f4b4693be02df770b6ab3a2274c15dca019e4da833665ee43bfd9566c2566a0efc6a79779d951fc65
%global source84_hash 0ae0932ca377bfbe77af65e5cba54135d5fa7d5e50fccc387f147b11014402b1fb1d267c5786dce476e8a26b61c85d413ad9b2bde2c6ddd1502f72c478bb635f
%global source85_hash 39e5da38b2e5804859493d90a1bf5560bdeeca88c6aaf0a9db676f85af9581fb0ff538746d8ce12eb4fa4e9acff5c1b452efba1d8a10d8dcc5508ca263fd13e6
%global source86_hash 6d7c32ee5af671954871c3a9586e97add85622a3f256c5b1386c574f920bbc026a413065037ec9ee04495548a0f95697c66d78888457b25d41dddca783a64b6b
%global source87_hash 35c80fe9378d2b2c005c83558a136ffdd04581889bb97b97da4504ecd78319d547090f9daed29dccb1cbbc31f826196e9c7fe256d37fac25e7fbedaaff5d5929
%global source88_hash 412f2a8683fa77519aec633baf0a6f838f4aa9424f5ca8accab7329f121a8b5174025565d11156f199455b283ae064dc5a262e128550f56db1a380c434a9a424
%global source89_hash 60e1c4d7f68bd6d39e081d49bfa1ecfa7dc56b940172719b4d6d0f2e87456c4b511ac29bb1884f7c290e7b226eb6ecae8f2ce4de3f7f5fbbd21934c440395ab7
%global source90_hash 29f4ee374c7b9d07274fb6f622c0769ff6977ce522ae25fa24571c0b7e60f1e120e4e26d37c6c340372fc0a2dde71a25121fa9538a35aa100e21637d5c79c874
%global source91_hash 5e4cea3869e09763a1f378ecac332b25d88b0c1380bde6a29ee4e06c597c9404d004eaab92f4a9a89c0722df53a2e7abbaf2c548bc9d72288babcb50f15ec3ee
%global source92_hash 82c4afd28c595d0590a4ed2d16e3607ab675c608769fbf89763c999c4882da9cf5a484c191b5c68f92c37d9fecf7375911f6566ac688d657cda39ce79faf4979
%global source93_hash 721fb78c82d9f61efd9cb3111141a2b4e786af4d09a58d92f2030428ce8331fba8bad54208b1baa6e6ee78d9a1175edc92c5d0dd96f4ce26a758a0ddc4896f2b
%global source94_hash 7adef296257aebec026a5d365a496e6ac77f4f3e20e1b7fae16f2413a04b2b37d57affadd3632fdab82fa0fd0475482b2379f772e184022ce5eafe50556fbb78
%global source95_hash 478c8cba8623b184db1c9237b7a805219bf1ffb7ef45280fecf7cd75a1720ca0ea2e1e1ad73465ee20dbc2bbaf14667d4707524edbc073dd4fbd0537dbeca8c2
%global source96_hash 318cb98167123bf8d9a5f80db8e31a31f6f61536e938da3b68efc0dfec6722bc898d8295d32896c24d2842b262f22f70e08014c07755b6728dbb2040f64aef5e
%global source97_hash 216a7f2ff6f49208c9b8b25097e6e5a2bc7c4f2f700433fe95824460f7edb1f19f27d85af04eb2269229e1093eb737f753c6e374975233f9eaaa8154c5207359
%global source98_hash 13968c3d86a7c9749a4278ecce8e896fb7eb25f8806bd760ba6c32e52df252a0295d05ce21872763aa85ad8c93e6aa9c7dafb6de81a76cbae86b7ea1c0ee7183
%global source99_hash ac1df50c4c3582182cc4f80e98cdc9b6f92000916943ed58c71c0b8dc5354b67f855365e5d9556ddeadba3228cc63332af3064c26fc1f0cda9151ec7eabe5644
%global source100_hash 91553b59c175ddad4aa1ff3c7d78c697f1cbfea7e7c728d5879bc0edec1caa59bd93b215ab75889f4f331fcd82c2abc59ec50d98871783f1211b5096b88848c6
%global source101_hash 13e15f06f1813acbca2864b8cab80d11ba671757f35d94e10b1375b609d56f9fe5259324b77b71624e99dc8979b84b03025af7fc3110144931164f3c510c7e68
%global source102_hash 1dcd4fed3ac1fe8f382d04287ad0b20afce75bb34df790601b9d37812844e11df9c008966d43f85c550675d5943aaa4f71cf2b7ac8202b5b88ea7838a99465ef
%global source103_hash 221b2d24b947998f24c9fe543fd4fb697554ffd3b48173122552432ae45a79eb0e41fd1918ca5004421a63e624c2e17ecb2d6ab5e8fdeed182bab19773047052
%global source104_hash 20800e79fadda9dbe03571cd926e2d5ab16233e5e3b8d2472ef132acbe499b9e785b66fa1983de5ec96e48bde290ec195eaa1c47dea6917f54da0aec6abf64e1
%global source105_hash a968fe943229ef7616e9299be5eb920cead121c8b533bf8df8cc419c1d4029644f55160667c7099f5edd310d2ac8ab6ffdbafb1a6711bfab125269dc93a3018b
%global source106_hash f08c0b2e87ebcd8e62157d02c5a952089e35f2529c40807269eda376113786862bbd70d4fdbeb7f9725dc47ea34a0f5e96c43a1e0e95d4b3afbde7b7def57248
%global source107_hash dd1c774d64459e3026f7cc12573c25bba1b9494123016962f630ebac39bb29b58e55ac85b5e88c6203d47c70ed1f1c50dda57a871fb85f2002276244ad30d978
%global source108_hash ab5563a7ab31ce8d2b20b618575a2c4aada2234e65bee1dcaeef25e4fdcf95708a08b8192dff3bc87bf0a073bb0b7a96a0530c231ec429c454f3d4230eba92ee
%global source109_hash 0e17e7bba93272ec96a366fff14ccc6318d70ecc295518740f3849e8c84f582ebda39ef5bb0b46f8e2c4ba5f05651a6b47932e1ece00670ffca3de3812f64c0d
%global source110_hash edcddd897ae45e39e0e25ac63a5f7236cc6ff774f6cfaefdba1e45eba1b29ed9a9be23eef941c1d45cc81459e3caae84bbb8b5376a640fdc8ee9c6e1868119cc
%global source111_hash 5f9689362939aa574782b8a8633eb819992d18215148bb3dccfb76b5b701906f549913b2f12f73a1412f969acbff62542cf9edb654a1a13aedb9e5f3dbfb9a83
%global source112_hash a4b0f616e47fdb1137b7bec363059c206bc9dde9aaead3096186c4ef004dad20f7ce391f5f5576887fa33283b0de0070ac55964da2443da7d224c38bdf09a00d
%global source113_hash c874be4b481f83a50eb8cb2eead7d5293cd4b351098a98e62f67ed8710025aac16e38636907c4961240e6b46a4f815b5eccf2db7d79adcbe5c72237f56ebd657
%global source114_hash 31996118470475a2052de529268060a08928dcac6af41cab8e5e08fe93ac87e005d9399ce431b86d0a866cfddeb786eddfc6286b87ade9867056a192eb1c18b6
%global source115_hash aad931dd85d0b6a210c7e88da397e8041033faeb9ca7916a440f89db8941d1aecd091f238e123431dcee96aec4bfe72a4ac3fc54797a4be8fbe93b4ae9e243f2
%global source116_hash 0e3c9fe279366828244f84ca51f0d443d4091d549ed6ad58f5c11f75484e827bb78c236d27969686acea8443e88629059ebc27882d7fb82e492112bc5735a73f
%global source117_hash 4da982162c99a210d91a957697fffaf0c43a21839cbfb0b818f7dd706fab55bc76cf0816f9d71866d74c25a949c71c7900c6c391403f8d22901ce1bd7fc7df66
%global source118_hash 06022a513c8a78d2ef09640a48e633a174267280ce6070048d423843a050616560e5b836a2c7dd5bd27469b179588fc6783b04fb29a300d5f5f3eeb9a27795f0
%global source119_hash a3d51d5751d91a7d9923e8cd5fa187b072e384aeebb94bb269ce3bb9135860efe6d21c2fdc363d0c28627b6048fa9faf2fe6ee6ac89309dedf9e87d75583fb3d
%global source120_hash b6ab1e47d092e9278fad8dbe78593ad49b591b3efe8b0f659e1c08bf57bcc1103f9b3d76dedfdb033e922ca980099dd03cb6b19453fea65f4482d43b4ed55ce4
%global source121_hash 77b915a47ec13626aad3b21c3bcf2b7514abcbdb94bde8db409f3d2ff186d9ed0d70a57b93875d8ed06075a0cc58777af90d9d263baa31fd54df04d9ccd83ac9
%global source122_hash 8ed875eb3fb2106157e4b21fc0615a742ac66ae8d2a42a48b051a68ef3de1ec02206ddfeea954bd6626b1c53019ca68b898b596855de5476e7931d52cf135547

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-games.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bartel-chess-fonts.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bartel-chess-fonts.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chess.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chess.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chess-problem-diagrams.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chess-problem-diagrams.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chessboard.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chessboard.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chessfss.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chessfss.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chinesechess.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chinesechess.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crossword.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crossword.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crosswrd.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crosswrd.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/customdice.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/customdice.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/egameps.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/egameps.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eigo.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eigo.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gamebook.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gamebook.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gamebooklib.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gamebooklib.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/go.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/go.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hanoi.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/havannah.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/havannah.doc.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hexboard.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hexboard.doc.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hexgame.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hexgame.doc.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hmtrump.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hmtrump.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/horoscop.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/horoscop.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jeuxcartes.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jeuxcartes.doc.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jigsaw.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jigsaw.doc.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/labyrinth.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/labyrinth.doc.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logicpuzzle.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logicpuzzle.doc.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mahjong.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mahjong.doc.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathador.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathador.doc.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maze.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maze.doc.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multi-sudoku.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multi-sudoku.doc.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musikui.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musikui.doc.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nimsticks.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nimsticks.doc.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/onedown.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/onedown.doc.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/othello.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/othello.doc.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/othelloboard.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/othelloboard.doc.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pas-crosswords.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pas-crosswords.doc.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-go.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-go.doc.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/playcards.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/playcards.doc.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psgo.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psgo.doc.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quizztex.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quizztex.doc.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realtranspose.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realtranspose.doc.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reverxii.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reverxii.doc.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rouequestions.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rouequestions.doc.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rpgicons.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rpgicons.doc.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schwalbe-chess.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schwalbe-chess.doc.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scrabble.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scrabble.doc.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sgame.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sgame.doc.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skak.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skak.doc.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skaknew.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skaknew.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/soup.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/soup.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sudoku.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sudoku.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sudokubundle.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sudokubundle.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tangramtikz.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tangramtikz.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thematicpuzzle.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thematicpuzzle.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tictactoe.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tictactoe.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-triminos.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-triminos.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/trivialpursuit.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/trivialpursuit.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/twoxtwogame.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/twoxtwogame.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wargame.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wargame.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/weiqi.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/weiqi.doc.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wordle.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wordle.doc.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xq.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xq.doc.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xskak.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xskak.doc.tar.xz

# AppStream metadata for font components
Source123:        skaknew.metainfo.xml
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-bartel-chess-fonts
Requires:       texlive-chess
Requires:       texlive-chess-problem-diagrams
Requires:       texlive-chessboard
Requires:       texlive-chessfss
Requires:       texlive-chinesechess
Requires:       texlive-collection-latex
Requires:       texlive-crossword
Requires:       texlive-crosswrd
Requires:       texlive-customdice
Requires:       texlive-egameps
Requires:       texlive-eigo
Requires:       texlive-gamebook
Requires:       texlive-gamebooklib
Requires:       texlive-go
Requires:       texlive-hanoi
Requires:       texlive-havannah
Requires:       texlive-hexboard
Requires:       texlive-hexgame
Requires:       texlive-hmtrump
Requires:       texlive-horoscop
Requires:       texlive-jeuxcartes
Requires:       texlive-jigsaw
Requires:       texlive-labyrinth
Requires:       texlive-logicpuzzle
Requires:       texlive-mahjong
Requires:       texlive-mathador
Requires:       texlive-maze
Requires:       texlive-multi-sudoku
Requires:       texlive-musikui
Requires:       texlive-nimsticks
Requires:       texlive-onedown
Requires:       texlive-othello
Requires:       texlive-othelloboard
Requires:       texlive-pas-crosswords
Requires:       texlive-pgf-go
Requires:       texlive-playcards
Requires:       texlive-psgo
Requires:       texlive-quizztex
Requires:       texlive-realtranspose
Requires:       texlive-reverxii
Requires:       texlive-rouequestions
Requires:       texlive-rpgicons
Requires:       texlive-rubik
Requires:       texlive-schwalbe-chess
Requires:       texlive-scrabble
Requires:       texlive-sgame
Requires:       texlive-skak
Requires:       texlive-skaknew
Requires:       texlive-soup
Requires:       texlive-sudoku
Requires:       texlive-sudokubundle
Requires:       texlive-tangramtikz
Requires:       texlive-thematicpuzzle
Requires:       texlive-tictactoe
Requires:       texlive-tikz-triminos
Requires:       texlive-trivialpursuit
Requires:       texlive-twoxtwogame
Requires:       texlive-wargame
Requires:       texlive-weiqi
Requires:       texlive-wordle
Requires:       texlive-xq
Requires:       texlive-xskak

%description
Setups for typesetting various games, including chess.

%package -n texlive-bartel-chess-fonts
Summary:        A set of fonts supporting chess diagrams
Version:        svn20619
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bartel-chess-fonts
The fonts are provided as Metafont source.

%package -n texlive-chess
Summary:        Fonts for typesetting chess boards
Version:        svn20582
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chess.sty) = %{tl_version}

%description -n texlive-chess
The original (and now somewhat dated) TeX chess font package. Potential users
should consider skak (for alternative fonts, and notation support), texmate
(for alternative notation support), or chessfss (for flexible font choices).

%package -n texlive-chess-problem-diagrams
Summary:        A package for typesetting chess problem diagrams
Version:        svn74591
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(cpdparse.sty) = %{tl_version}
Provides:       tex(diagram.sty) = %{tl_version}

%description -n texlive-chess-problem-diagrams
This package provides macros to typeset chess problem diagrams including fairy
chess problems (mostly using rotated images of pieces) and other boards.

%package -n texlive-chessboard
Summary:        Print chess boards
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(animate.sty)
Requires:       tex(array.sty)
Requires:       tex(attachfile.sty)
Requires:       tex(babel.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(chessfss.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(doc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fourier.sty)
Requires:       tex(helvet.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
# LuxiMono Requires filtered - non-free font
Requires:       tex(makeidx.sty)
Requires:       tex(microtype.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(showexpl.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xspace.sty)
Provides:       tex(UF-chessboard-documentation.sty) = %{tl_version}
Provides:       tex(chessboard-keys-main.sty) = %{tl_version}
Provides:       tex(chessboard-keys-pgf.sty) = %{tl_version}
Provides:       tex(chessboard-pgf.sty) = %{tl_version}
Provides:       tex(chessboard.sty) = %{tl_version}

%description -n texlive-chessboard
This package offers commands to print chessboards. It can print partial boards,
hide pieces and fields, color the boards and put various marks on the board. It
has a lot of options to place pieces on the board. Using exotic pieces (e.g.,
for fairy chess) is possible. The documentation includes an example of an
animated chessboard, for those whose PDF viewer can display animations.

%package -n texlive-chessfss
Summary:        A package to handle chess fonts
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(chessfss.sty) = %{tl_version}
Provides:       tex(lsb1enc.def) = %{tl_version}
Provides:       tex(lsb2enc.def) = %{tl_version}
Provides:       tex(lsb3enc.def) = %{tl_version}
Provides:       tex(lsbc1enc.def) = %{tl_version}
Provides:       tex(lsbc2enc.def) = %{tl_version}
Provides:       tex(lsbc3enc.def) = %{tl_version}
Provides:       tex(lsbc4enc.def) = %{tl_version}
Provides:       tex(lsbc5enc.def) = %{tl_version}
Provides:       tex(lsbenc.def) = %{tl_version}
Provides:       tex(lsfenc.def) = %{tl_version}
Provides:       tex(lsienc.def) = %{tl_version}

%description -n texlive-chessfss
This package offers commands to use and switch between chess fonts. It uses the
LaTeX font selection scheme (nfss). The package doesn't parse, format and print
PGN input like e.g. the packages skak or texmate; the aim of the package is to
offer writers of chess packages a bundle of commands for fonts, so that they
don't have to implement all these commands for themselves. A normal user can
use the package to print e.g. single chess symbols and simple diagrams. The
documentation contains also a section about installation of chess fonts.

%package -n texlive-chinesechess
Summary:        Typeset Chinese chess with l3draw
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chinesechess.sty) = %{tl_version}

%description -n texlive-chinesechess
This LaTeX3 package based on l3draw provides macros and an environment for
Chinese chess manual writing.

%package -n texlive-crossword
Summary:        Typeset crossword puzzles
Version:        svn73579
License:        Crossword
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Provides:       tex(cwpuzzle.sty) = %{tl_version}

%description -n texlive-crossword
An extended grid-based puzzle package, designed to take all input (both grid
and clues) from the same file. The package can typeset grids with holes in them
(for advertisements, or other sorts of stuff), and can deal with several sorts
of puzzle: The classical puzzle contains numbers for the words and clues for
the words to be filled in. The numbered puzzle contains numbers in each cell
where identical numbers represent identical letters. The goal is to find out
which number corresponds to which letter. The fill-in type of puzzle consists
of a grid and a list of words. The goal is to place all words in the grid.
Sudoku and Kakuro puzzles involve filling in grids of numbers according to
their own rules. Format may be block-separated, or separated by thick lines.
Input to the package is somewhat redundant: specification of the grid is
separate from specification of the clues (if they're necessary). The author
considers this style both 'natural' and robust.

%package -n texlive-crosswrd
Summary:        Macros for typesetting crossword puzzles
Version:        svn16896
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(crosswrd.sty) = %{tl_version}

%description -n texlive-crosswrd
The package provides a LaTeX method of typesetting crosswords, and assists the
composer ensure that the grid all goes together properly. Brian Hamilton
Kelly's original was written for LaTeX 2.09, and needed to be updated to run
with current LaTeX.

%package -n texlive-customdice
Summary:        Simple commands for drawing customisable dice
Version:        svn64089
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Provides:       tex(customdice.sty) = %{tl_version}

%description -n texlive-customdice
The customdice package for LaTeX, LuaLaTeX and XeTeX that provides
functionality for drawing dice. The aim is to provide highly-customisable but
simple-to-use commands, allowing: adding custom text to dice faces; control
over colouring; control over sizing.

%package -n texlive-egameps
Summary:        LaTeX package for typesetting extensive games
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(egameps.sty) = %{tl_version}

%description -n texlive-egameps
The style is intended to have enough features to draw any extensive game with
relative ease. The facilities of PSTricks are used for graphics. (An older
version of the package, which uses the LaTeX picture environment rather than
PSTricks and consequently has many fewer features is available on the package
home page.)

%package -n texlive-eigo
Summary:        Comprehensive tools for creating Go (Weiqi/Baduk) game diagrams in LaTeX
Version:        svn76251
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(eigo.sty) = %{tl_version}

%description -n texlive-eigo
The eigo package provides comprehensive tools for creating Go (Weiqi/Baduk)
game diagrams in LaTeX documents. Developed with AI assistance, it offers
multiple stone colors with full RGB customization, automatic numbering systems
with alternating colors, geometric transformations (rotations, mirrors),
flexible board display options with enhanced 2pt borders for publication
quality, symbol placement, and full LuaLaTeX compatibility. The package
supports seven stone colors, border display, extended size presets with
validation, and advanced features for game analysis and problem presentation.

%package -n texlive-gamebook
Summary:        Typeset gamebooks and other interactive novels
Version:        svn24714
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(draftwatermark.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(extramarks.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(scrtime.sty)
Requires:       tex(titlesec.sty)
Provides:       tex(gamebook.sty) = %{tl_version}

%description -n texlive-gamebook
This package provides the means in order to lay-out gamebooks with LaTeX. A
simple gamebook example is included with the package, and acts as a tutorial.

%package -n texlive-gamebooklib
Summary:        Macros for setting numbered entries in shuffled order
Version:        svn67772
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lcg.sty)
Requires:       tex(macroswap.sty)
Requires:       tex(silence.sty)
Provides:       tex(gamebooklib.sty) = %{tl_version}

%description -n texlive-gamebooklib
This package provides macros and environments to allow the user to typeset a
series of cross-referenced, numbered "entries", shuffled into random order, to
produce an interactive novel or "gamebook". This allows entries to be written
in natural order and shuffled automatically into a repeatable non-linear order.
Limited support is provided for footnotes to appear at the natural position:
the end of each entry, or the end of each page, whichever is closest to the
footnote mark. This is unrelated to the gamebook package which is more
concerned with the formatting of entries rather than their order. The two
packages can be used together or separately.

%package -n texlive-go
Summary:        Fonts and macros for typesetting go games
Version:        svn28628
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(go.sty) = %{tl_version}

%description -n texlive-go
The macros provide for nothing more complicated than the standard 19x19 board;
the fonts are written in Metafont.

%package -n texlive-hanoi
Summary:        Tower of Hanoi in TeX
Version:        svn25019
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hanoi.tex) = %{tl_version}

%description -n texlive-hanoi
The Plain TeX program (typed in the shape of the towers of Hanoi) serves both
as a game and as a TeX programming exercise. As a game it will solve the towers
with (up to) 15 discs (with 15 discs, 32767 moves are needed).

%package -n texlive-havannah
Summary:        Diagrams of board positions in the games of Havannah and Hex
Version:        svn36348
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(havannah.sty) = %{tl_version}

%description -n texlive-havannah
This package defines macros for typesetting diagrams of board positions in the
games of Havannah and Hex.

%package -n texlive-hexboard
Summary:        For drawing Hex boards and games
Version:        svn62102
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(hexboard.sty) = %{tl_version}

%description -n texlive-hexboard
hexboard is a package for LaTeX that should also work with LuaTeX and XeTeX,
that provides functionality for drawing Hex boards and games. The aim is a
clean, clear design with flexibility for drawing different sorts of Hex
diagrams.

%package -n texlive-hexgame
Summary:        Provide an environment to draw a hexgame-board
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-poly.sty)
Requires:       tex(pstcol.sty)
Provides:       tex(hexgame.sty) = %{tl_version}

%description -n texlive-hexgame
Hex is a mathematical game invented by the Danish mathematician Piet Hein and
independently by the mathematician John Nash. This package defines an
environment that enables the user to draw such a game in a trivial way.

%package -n texlive-hmtrump
Summary:        Describe card games
Version:        svn54512
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(hmtrump.sty) = %{tl_version}

%description -n texlive-hmtrump
This package provides a font with LuaLaTeX support for describing card games.

%package -n texlive-horoscop
Summary:        Generate astrological charts in LaTeX
Version:        svn56021
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(starfont.sty)
Requires:       tex(trig.sty)
Requires:       tex(wasysym.sty)
Provides:       tex(horoscop.sty) = %{tl_version}

%description -n texlive-horoscop
The horoscop package provides a unified interface for astrological font
packages; typesetting with pict2e of standard wheel charts and some variations,
in PostScript- and PDF-generating TeX engines; and access to external
calculation software (Astrolog and Swiss Ephemeris) for computing object
positions.

%package -n texlive-jeuxcartes
Summary:        Macros to insert playing cards
Version:        svn76966
License:        LPPL-1.3c AND LGPL-2.1-only AND LicenseRef-Fedora-Public-Domain AND CC-BY-SA-4.0 AND MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(pifont.sty)
Requires:       tex(randomlist.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xstring.sty)
Provides:       tex(JeuxCartes.sty) = %{tl_version}

%description -n texlive-jeuxcartes
This package provides macros to insert playing cards, single, or hand, or
random-hand, Poker or French Tarot or Uno, from png files.

%package -n texlive-jigsaw
Summary:        Draw jigsaw pieces with TikZ
Version:        svn71923
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-epstopdf-pkg
Requires:       texlive-iftex
Requires:       texlive-pgf
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(tikz.sty)
Provides:       tex(jigsaw.sty) = %{tl_version}

%description -n texlive-jigsaw
This is a small LaTeX package to draw jigsaw pieces with TikZ. It is possible
to draw individual pieces and adjust their shape, create tile patterns or
automatically generate complete jigsaws.

%package -n texlive-labyrinth
Summary:        Draw labyrinths and solution paths
Version:        svn33454
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(picture.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(labyrinth.sty) = %{tl_version}

%description -n texlive-labyrinth
The labyrinth package provides code and an environment for typesetting simple
labyrinths with LaTeX, and generating an automatic or manual solution path.

%package -n texlive-logicpuzzle
Summary:        Typeset (grid-based) logic puzzles
Version:        svn34491
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(logicpuzzle.sty) = %{tl_version}
Provides:       tex(lpenv.sty) = %{tl_version}

%description -n texlive-logicpuzzle
The package allows the user to typeset various logic puzzles. At the moment the
following puzzles are supported: 2D-Sudoku (aka Magiequadrat, Diagon, ...),
Battleship (aka Bimaru, Marinespiel, Batalla Naval, ...), Bokkusu (aka
Kakurasu, Feldersummenratsel, ...), Bridges (akak Bruckenbau, Hashi, ...),
Chaos Sudoku, Four Winds (aka Eminent Domain, Lichtstrahl, ...), Hakyuu (aka
Seismic, Ripple Effect, ...), Hitori, Kakuro, Kendoku (aka Mathdoku, Calcudoku,
Basic, MiniPlu, Ken Ken, Square Wisdom, Sukendo, Caldoku, ..., Killer Sudoku
(aka Samunapure, Sum Number Place, Sumdoku, Gebietssummen, ...), Laser Beam
(aka Laserstrahl, ...), Magic Labyrinth (aka Magic Spiral, Magisches Labyrinth,
...), Magnets (aka Magnetplatte, Magnetfeld, ...), Masyu (aka Mashi,
{White|Black} Pearls, ...), Minesweeper (aka Minensuche, ...), Nonogram (aka
Griddlers, Hanjie, Tsunami, Logic Art, Logimage, ...), Number Link (aka
Alphabet Link, Arukone, Buchstabenbund, ...), Resuko, Schatzsuche, Skyline (aka
Skycrapers, Wolkenkratzer, Hochhauser, ...), including Skyline Sudoku and
Skyline Sudoku (N*N) variants, Slitherlink (aka Fences, Number Line, Dotty
Dilemma, Sli-Lin, Takegaki, Great Wall of China, Loop the Loop, Rundweg,
Gartenzaun, ...), Star Battle (aka Sternenschlacht, ...), Stars and Arrows (aka
Sternenhimmel, ...), Sudoku, Sun and Moon (aka Sternenhaufen, Munraito, ...),
Tents and Trees (aka Zeltlager, Zeltplatz, Camping, ...), and Tunnel.

%package -n texlive-mahjong
Summary:        Typeset Mahjong Tiles using MPSZ Notation
Version:        svn76924
License:        MIT AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(xparse.sty)
Provides:       tex(mahjong.sty) = %{tl_version}

%description -n texlive-mahjong
The mahjong package provides a LaTeX2e and LaTeX3 interface for typesetting
mahjong tiles using an extended version of MPSZ algebraic notation. Features
include spaces, rotated, blank, and concealed tiles, as well as red fives. The
size of the mahjong tiles can be controlled using a package option and an
optional argument of \mahjong. It is primarily aimed at Riichi (aka. Japanese)
Mahjong but can be used to typeset any style of mahjong.

%package -n texlive-mathador
Summary:        LaTeX commands for the French game "Mathador"
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bm.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(mathador.sty) = %{tl_version}

%description -n texlive-mathador
This is a LaTeX package with graphic commands for the French game MATHADOR (by
author Eric Trouillot and Reseau CANOPE). The principle of the game is like
this: Roll the dice! They give you one target number (between 0 and 99) and
five numbers to use to reach it. You can use the four arithmetic operations to
get there.

%package -n texlive-maze
Summary:        Generate random mazes
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(maze.sty) = %{tl_version}

%description -n texlive-maze
This package can generate random square mazes of a specified size. The mazes
generated by this package are natural and their solution is not too obvious.
The output it based on the picture environment.

%package -n texlive-multi-sudoku
Summary:        Create and customise Sudoku grids of various sizes
Version:        svn75941
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(xparse.sty)
Provides:       tex(multi-sudoku.sty) = %{tl_version}

%description -n texlive-multi-sudoku
This package provides tools for typesetting Sudoku grids of various sizes in
LaTeX. Unlike other Sudoku packages which are typically limited to the standard
9x9 layout, this package supports a broad range of grid sizes - from trivial
1x1 puzzles to extended 49x49 Sudokus - that's the limit for now! Grids are
drawn with our sudoku environment, which is based on using LaTeX's native
tabular environment. We include intuitive options to control dimensions, font
size, and grid thickness. Entries in the grid are inserted as in a regular
table, thus making it simple to create, customise, and fill Sudoku puzzles
manually.

%package -n texlive-musikui
Summary:        Easy creation of "arithmetical restoration" puzzles
Version:        svn47472
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(musikui.sty) = %{tl_version}

%description -n texlive-musikui
This package permits to easily typeset arithmetical restorations using LaTeX.
This package requires the graphicx package.

%package -n texlive-nimsticks
Summary:        Draws sticks for games of multi-pile Nim
Version:        svn64118
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(lcg.sty)
Requires:       tex(tikz.sty)
Provides:       tex(nimsticks.sty) = %{tl_version}

%description -n texlive-nimsticks
This LaTeX package provides commands \drawnimstick to draw a single nim stick
and \nimgame which represents games of multi-pile Nim. Nim sticks are drawn
with a little random wobble so they look 'thrown together' and not too regular.
The package also provides options to customise the size and colour of the
sticks, and flexibility to draw heaps of different objects.

%package -n texlive-onedown
Summary:        Typeset Bridge Diagrams
Version:        svn69067
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(collcell.sty)
Requires:       tex(environ.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(makecmds.sty)
Requires:       tex(moresize.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(relsize.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tracklang.sty)
Requires:       tex(translator.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(onedown.sty) = %{tl_version}

%description -n texlive-onedown
This is a comprehensive package to draw all sorts of bridge diagrams, including
hands (stand alone or arround a compass), bidding tables (stand alone or in
connection with hands/compass), trick tables, and expert quizzes. Features:
Works for all fontsizes from \ssmall to \HUGE. Different fonts for hands,
bidding diagrams, compass, etc. are possible. Annotations to card and bidding
diagrams. Automated check on consistency of suit and hands. Multilingual output
of bridge terms. Extensive documentation: User manual, Reference manual, and
Examples.

%package -n texlive-othello
Summary:        Modification of a Go package to create othello boards
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(othello.sty) = %{tl_version}

%description -n texlive-othello
A package (based on Kolodziejska's go), and fonts (as Metafont source) are
provided.

%package -n texlive-othelloboard
Summary:        Typeset Othello (Reversi) diagrams of any size, with annotations
Version:        svn23714
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(xstring.sty)
Provides:       tex(othelloboard.sty) = %{tl_version}

%description -n texlive-othelloboard
The package enables the user to generate high-quality Othello (also known as
Reversi) board diagrams of any size. The diagrams support annotations,
including full game transcripts. Automated board or transcript creation, from
plain text formats standard to WZebra (and other programs) is also supported.

%package -n texlive-pas-crosswords
Summary:        Creating crossword grids, using TikZ
Version:        svn32313
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(multido.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(pas-crosswords.sty) = %{tl_version}

%description -n texlive-pas-crosswords
The package produces crossword grids, using a wide variety of colours and
decorations of the grids and the text in them. The package uses TikZ for its
graphical output.

%package -n texlive-pgf-go
Summary:        Diagramming and commenting on Go games
Version:        svn74578
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(pgf-go-coordinate-parser.sty) = %{tl_version}
Provides:       tex(pgf-go-goban.sty) = %{tl_version}
Provides:       tex(pgf-go-marks.sty) = %{tl_version}
Provides:       tex(pgf-go-players.sty) = %{tl_version}
Provides:       tex(pgf-go-profiles.sty) = %{tl_version}
Provides:       tex(pgf-go-remember.sty) = %{tl_version}
Provides:       tex(pgf-go-stones.sty) = %{tl_version}
Provides:       tex(pgf-go.sty) = %{tl_version}

%description -n texlive-pgf-go
A LaTeX package for creating Go (Baduk) diagrams with ease. It features an
efficient coordinate-loading syntax to streamline workflows and offers flexible
profile manipulation, allowing users to customize board layouts, stones, and
annotations effortlessly.

%package -n texlive-playcards
Summary:        A simple template for drawing playcards
Version:        svn67342
License:        LGPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(contour.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(playcards.sty) = %{tl_version}

%description -n texlive-playcards
This small package provides commands for drawing customized playcards with
width 59mm and height 89mm, which are typical card dimensions.

%package -n texlive-psgo
Summary:        Typeset go diagrams with PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(psgo.sty) = %{tl_version}

%description -n texlive-psgo
Typeset go diagrams with PSTricks

%package -n texlive-quizztex
Summary:        Create quizzes like in TV shows
Version:        svn75977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quizztex.sty) = %{tl_version}

%description -n texlive-quizztex
This LaTeX package permits to create quizzes in the style of the TV shows <<
Qui veut gagner des millions ? >> ("Who Wants to Be a Millionaire?") or << Tout
le monde veut prendre sa place ! >>.

%package -n texlive-realtranspose
Summary:        The "real" way to transpose a Matrix
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(realtranspose.sty) = %{tl_version}

%description -n texlive-realtranspose
With realtranspose you can notate the transposition of a matrix by rotating the
symbols 90 degrees. This is an homage to the realhats package.

%package -n texlive-reverxii
Summary:        Playing Reversi in TeX
Version:        svn63753
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(reverxii.tex) = %{tl_version}

%description -n texlive-reverxii
Following the lead of xii.tex, this little (938 characters) program that plays
Reversi. (The program incorporates some primitive AI.)

%package -n texlive-rouequestions
Summary:        Draw a "question wheel" (roue de questions)
Version:        svn67670
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-euclide.sty)
Provides:       tex(RoueQuestions.sty) = %{tl_version}

%description -n texlive-rouequestions
This package helps to produce a game for students: It is a wheel displaying
questions, with hidden answers inside.

%package -n texlive-rpgicons
Summary:        Icons for tabletop role-playing games
Version:        svn77702
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(rpgicons-l3.sty) = %{tl_version}
Provides:       tex(rpgicons-pgf.sty) = %{tl_version}
Provides:       tex(rpgicons.sty) = %{tl_version}

%description -n texlive-rpgicons
This package provides a set of high-quality icons for use in notes for tabletop
role-playing games. The icons are meant to be used in the body text, but they
can also be used in other contexts such as graphics or diagrams. The package
comes in two variants, one based on the l3draw package, and the other on
PGF/TikZ.

%package -n texlive-schwalbe-chess
Summary:        Typeset the German chess magazine "Die Schwalbe"
Version:        svn73582
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(diagram.sty)
Provides:       tex(schwalbe.cls) = %{tl_version}
Provides:       tex(schwalbe.sty) = %{tl_version}
Provides:       tex(swruler.sty) = %{tl_version}

%description -n texlive-schwalbe-chess
The package is based on chess-problem-diagrams, which in its turn has a
dependency on the bartel-chess-fonts.

%package -n texlive-scrabble
Summary:        Commands for Scrabble boards
Version:        svn77114
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(randintlist.sty)
Requires:       tex(tikz.sty)
Provides:       tex(Scrabble.sty) = %{tl_version}

%description -n texlive-scrabble
This package provides some commands (in English and in French) to work with a
Scrabble Board : \ScrabbleBoard and \begin{EnvScrabble} and \ScrabblePutWord
for the English version, \PlateauScrabble and \begin{EnvScrabble} and
\ScrabblePlaceMot for the French version.

%package -n texlive-sgame
Summary:        LaTeX style for typesetting strategic games
Version:        svn30959
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Provides:       tex(sgame.sty) = %{tl_version}
Provides:       tex(sgamevar.sty) = %{tl_version}

%description -n texlive-sgame
Formats strategic games. For a 2x2 game, for example, the input:
\begin{game}{2}{2} &$L$ &$M$\\ $T$ &$2,2$ &$2,0$\\ $B$ &$3,0$ &$0,9$ \end{game}
produces output with (a) boxes around the payoffs, (b) payoff columns of equal
width, and (c) payoffs vertically centered within the boxes. Note that the game
environment will not work in the argument of another command.

%package -n texlive-skak
Summary:        Fonts and macros for typesetting chess games
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(chessfss.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lambda.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(skak.sty) = %{tl_version}

%description -n texlive-skak
This package provides macros and fonts in Metafont format which can be used to
typeset chess games using PGN, and to show diagrams of the current board in a
document. The package builds on work by Piet Tutelaers -- the main novelty is
the use of PGN for input instead of the more cumbersome coordinate notation
(g1f3 becomes the more readable Nf3 in PGN). An Adobe Type 1 implementation of
skak's fonts is available as package skaknew; an alternative chess notational
scheme is available in package texmate, and a general mechanism for selecting
chess fonts is provided in chessfss.

%package -n texlive-skaknew
Summary:        The skak chess fonts redone in Adobe Type 1
Version:        svn20031
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-skaknew
This package offers Adobe Type 1 versions of the fonts provided as Metafont
source by the skak bundle.

%package -n texlive-soup
Summary:        Generate alphabet soup puzzles
Version:        svn50815
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(soup.sty) = %{tl_version}

%description -n texlive-soup
Generate alphabet soup puzzles (aka word search puzzles), and variations using
numbers or other symbols. Provides macros to generate an alphabet soup style
puzzle (also known as word search puzzles or "find-the-word" puzzles). Allow
creating numbersoup and soups with custom symbol sets.

%package -n texlive-sudoku
Summary:        Create sudoku grids
Version:        svn67189
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sudoku.sty) = %{tl_version}

%description -n texlive-sudoku
The sudoku package provides an environment for typesetting sudoku grids. A
sudoku puzzle is a 9x9 grid where some of the squares in the grid contain
numbers. The rules are simple: every column can only contain the digits 1 to 9,
every row can only contain the digits 1 to 9 and every 3x3 box can only contain
the digits 1 to 9. More information, including help and example puzzles, can be
found at sudoku.org.uk. This site also has blank sudoku grids (or worksheets),
but you will not need to print them from there if you have this package
installed.

%package -n texlive-sudokubundle
Summary:        A set of sudoku-related packages
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(createsudoku.sty) = %{tl_version}
Provides:       tex(printsudoku.sty) = %{tl_version}
Provides:       tex(solvesudoku.sty) = %{tl_version}

%description -n texlive-sudokubundle
The bundle provides three packages: printsudoku, which provides a command
\sudoku whose argument is the name of a file containing a puzzle specification;
solvesudoku, which attempts to find a solution to the puzzle in the file named
in the argument; and createsudoku, which uses the random package to generate a
puzzle according to a bunch of parameters that the user sets via macros. The
bundle comes with a set of ready-prepared puzzle files.

%package -n texlive-tangramtikz
Summary:        Tangram puzzles, with TikZ
Version:        svn75123
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(TangramTikz.sty) = %{tl_version}

%description -n texlive-tangramtikz
This package provides some commands (with English and French keys) to work with
tangram puzzles: \begin{EnvTangramTikz} and \PieceTangram to position a piece,
\TangramTikz to display a predefined Tangram.

%package -n texlive-thematicpuzzle
Summary:        Horizontal banners in a puzzle style
Version:        svn75984
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
Provides:       tex(thematicpuzzle.sty) = %{tl_version}

%description -n texlive-thematicpuzzle
With this package it is possible to create a horizontal banner in the form of a
puzzle. There are some predefined themes.

%package -n texlive-tictactoe
Summary:        Drawing tic-tac-toe or Noughts and Crosses games
Version:        svn75712
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xspace.sty)
Provides:       tex(tictactoe.sty) = %{tl_version}

%description -n texlive-tictactoe
This package which provides commands for drawing grids for the game known
variously as tic-tac-toe (and variants), Noughts and Crosses, Naughts and
Crosses, Xs and Os, and so on.

%package -n texlive-tikz-triminos
Summary:        Create triminos, made with TikZ
Version:        svn73533
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tikz-triminos.sty) = %{tl_version}

%description -n texlive-tikz-triminos
Create (1 or 9 or 12) TriMinos with some customizations: size, font, logo,
colors; automatic texts adjustment; full version, or joker usage. Inspiration
from Paul Matthies

%package -n texlive-trivialpursuit
Summary:        Insert Trivial Pursuit board game
Version:        svn76152
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Provides:       tex(TrivialPursuit.sty) = %{tl_version}

%description -n texlive-trivialpursuit
This is a package to display a Trivial Pursuit board game, with customization.

%package -n texlive-twoxtwogame
Summary:        Visualize 2x2 normal-form games
Version:        svn70423
License:        Apache-2.0 AND CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pgfmath-xfp.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tikzscale.sty)
Provides:       tex(twoxtwogame.sty) = %{tl_version}

%description -n texlive-twoxtwogame
This is a package for the visualization of 2x2 normal form games. The package
is based on PGF/TikZ and produces beautiful vector graphics that are intended
for use in scientific publications. The commands include the creation of
graphical representations of 2x2 games, the visualization of equilibria in 2x2
games and game embeddings for 2x2 games.

%package -n texlive-wargame
Summary:        A LaTeX package to prepare hex'n'counter wargames
Version:        svn72903
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(tikzlibrarywargame.chit.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarywargame.hex.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarywargame.natoapp6c.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarywargame.util.code.tex) = %{tl_version}
Provides:       tex(wargame.sty) = %{tl_version}
Provides:       tex(wgexport.cls) = %{tl_version}

%description -n texlive-wargame
This package can help make classic Hex'n'Counter wargames using LaTeX. The
package provides tools for generating Hex maps and boards Counters for units,
markers, and so on Counter sheets Order of Battle charts Illustrations in the
rules using the defined maps and counters The result will often be a PDF (or
set of PDFs) that contains everything one will need for a game (rules, charts,
boards, counter sheets). The package uses NATO App6 symbology for units. The
package uses NATO App6 symbology for units. The package uses TikZ for most
things. The package supports exporting the game to a VASSAL module See also the
README.md file for more, and of course the documentation (including the
tutorial in tutorial/game.pdf).

%package -n texlive-weiqi
Summary:        Use LaTeX3 to typeset Weiqi (Go)
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(weiqi.sty) = %{tl_version}

%description -n texlive-weiqi
This package uses LaTeX3 to typeset Weiqi (Go). Shi Yong LaTeX3 Chuang Jian Yi
Ge Pai Ban Wei Qi Qi Pu De Hong Bao .

%package -n texlive-wordle
Summary:        Create wordle grids
Version:        svn72059
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(wordle.sty) = %{tl_version}

%description -n texlive-wordle
This package provides environments (in French or English) to display wordle
grids: \begin{WordleGrid} for the English version, \begin{GrilleSutom} for the
French version.

%package -n texlive-xq
Summary:        Support for writing about xiangqi
Version:        svn35211
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xq.sty) = %{tl_version}

%description -n texlive-xq
The package is for writing about xiangqi or chinese chess. You can write games
or parts of games and show diagrams with special positions.

%package -n texlive-xskak
Summary:        An extension to the skak package for chess typesetting
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(chessboard.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(xifthen.sty)
Provides:       tex(xskak-keys.sty) = %{tl_version}
Provides:       tex(xskak-nagdef.sty) = %{tl_version}
Provides:       tex(xskak.sty) = %{tl_version}

%description -n texlive-xskak
Xskak, as its prime function, saves information about a chess game for later
use (e.g., to loop through a game to make an animated board). The package also
extends the input that the parsing commands can handle and offers an interface
to define and switch between indefinite levels of styles.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

mkdir -p %{buildroot}%{_datadir}/fonts
mkdir -p %{buildroot}%{_datadir}/appdata

tar -xf %{SOURCE2} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE3} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE4} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE5} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE6} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE7} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE8} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE9} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE10} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE11} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE12} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE13} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE14} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE15} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE16} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE17} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE18} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE19} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE20} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE21} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE22} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE23} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE24} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE25} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE26} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE27} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE28} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE29} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE30} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE31} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE32} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE33} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE34} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE35} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE36} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE37} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE38} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE39} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE40} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE41} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE42} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE43} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE44} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE45} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE46} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE47} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE48} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE49} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE50} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE51} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE52} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE53} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE54} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE55} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE56} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE57} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE58} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE59} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE60} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE61} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE62} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE63} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE64} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE65} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE66} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE67} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE68} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE69} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE70} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE71} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE72} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE73} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE74} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE75} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE76} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE77} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE78} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE79} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE80} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE81} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE82} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE83} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE84} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE85} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE86} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE87} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE88} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE89} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE90} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE91} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE92} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE93} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE94} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE95} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE96} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE97} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE98} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE99} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE100} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE101} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE102} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE103} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE104} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE105} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE106} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE107} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE108} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE109} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE110} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE111} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE112} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE113} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE114} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE115} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE116} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE117} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE118} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE119} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE120} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE121} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE122} -C %{buildroot}%{_texmf_main}

# Install AppStream metadata for font components
cp %{SOURCE123} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/skaknew %{buildroot}%{_datadir}/fonts/skaknew

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-bartel-chess-fonts
%license gpl2.txt
%{_texmf_main}/fonts/source/public/bartel-chess-fonts/
%{_texmf_main}/fonts/tfm/public/bartel-chess-fonts/
%doc %{_texmf_main}/doc/fonts/bartel-chess-fonts/

%files -n texlive-chess
%license pd.txt
%{_texmf_main}/fonts/source/public/chess/
%{_texmf_main}/fonts/tfm/public/chess/
%{_texmf_main}/tex/latex/chess/
%doc %{_texmf_main}/doc/fonts/chess/

%files -n texlive-chess-problem-diagrams
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chess-problem-diagrams/
%doc %{_texmf_main}/doc/latex/chess-problem-diagrams/

%files -n texlive-chessboard
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chessboard/
%doc %{_texmf_main}/doc/latex/chessboard/

%files -n texlive-chessfss
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/chessfss/
%{_texmf_main}/tex/latex/chessfss/
%doc %{_texmf_main}/doc/latex/chessfss/

%files -n texlive-chinesechess
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chinesechess/
%doc %{_texmf_main}/doc/latex/chinesechess/

%files -n texlive-crossword
%license other-free.txt
%{_texmf_main}/tex/latex/crossword/
%doc %{_texmf_main}/doc/latex/crossword/

%files -n texlive-crosswrd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/crosswrd/
%doc %{_texmf_main}/doc/latex/crosswrd/

%files -n texlive-customdice
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/customdice/
%doc %{_texmf_main}/doc/latex/customdice/

%files -n texlive-egameps
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/egameps/
%doc %{_texmf_main}/doc/latex/egameps/

%files -n texlive-eigo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eigo/
%doc %{_texmf_main}/doc/latex/eigo/

%files -n texlive-gamebook
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gamebook/
%doc %{_texmf_main}/doc/latex/gamebook/

%files -n texlive-gamebooklib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gamebooklib/
%doc %{_texmf_main}/doc/latex/gamebooklib/

%files -n texlive-go
%license pd.txt
%{_texmf_main}/fonts/source/public/go/
%{_texmf_main}/fonts/tfm/public/go/
%{_texmf_main}/tex/latex/go/
%doc %{_texmf_main}/doc/fonts/go/

%files -n texlive-hanoi
%license pd.txt
%{_texmf_main}/tex/plain/hanoi/

%files -n texlive-havannah
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/havannah/
%doc %{_texmf_main}/doc/latex/havannah/

%files -n texlive-hexboard
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/hexboard/
%doc %{_texmf_main}/doc/latex/hexboard/

%files -n texlive-hexgame
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hexgame/
%doc %{_texmf_main}/doc/latex/hexgame/

%files -n texlive-hmtrump
%license cc-by-sa-4.txt
%{_texmf_main}/fonts/truetype/public/hmtrump/
%{_texmf_main}/tex/lualatex/hmtrump/
%doc %{_texmf_main}/doc/lualatex/hmtrump/

%files -n texlive-horoscop
%license pd.txt
%{_texmf_main}/tex/latex/horoscop/
%doc %{_texmf_main}/doc/latex/horoscop/

%files -n texlive-jeuxcartes
%license lppl1.3c.txt
%license lgpl2.1.txt
%license pd.txt
%license cc-by-sa-4.txt
%license mit.txt
%{_texmf_main}/tex/latex/jeuxcartes/
%doc %{_texmf_main}/doc/latex/jeuxcartes/

%files -n texlive-jigsaw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jigsaw/
%doc %{_texmf_main}/doc/latex/jigsaw/

%files -n texlive-labyrinth
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/labyrinth/
%doc %{_texmf_main}/doc/latex/labyrinth/

%files -n texlive-logicpuzzle
%license lppl1.3c.txt
%{_texmf_main}/scripts/logicpuzzle/
%{_texmf_main}/tex/latex/logicpuzzle/
%doc %{_texmf_main}/doc/latex/logicpuzzle/

%files -n texlive-mahjong
%license mit.txt
%license pd.txt
%{_texmf_main}/tex/latex/mahjong/
%doc %{_texmf_main}/doc/latex/mahjong/

%files -n texlive-mathador
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mathador/
%doc %{_texmf_main}/doc/latex/mathador/

%files -n texlive-maze
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/maze/
%doc %{_texmf_main}/doc/latex/maze/

%files -n texlive-multi-sudoku
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/multi-sudoku/
%doc %{_texmf_main}/doc/latex/multi-sudoku/

%files -n texlive-musikui
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musikui/
%doc %{_texmf_main}/doc/latex/musikui/

%files -n texlive-nimsticks
%license mit.txt
%{_texmf_main}/tex/latex/nimsticks/
%doc %{_texmf_main}/doc/latex/nimsticks/

%files -n texlive-onedown
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/onedown/
%doc %{_texmf_main}/doc/latex/onedown/

%files -n texlive-othello
%license gpl2.txt
%{_texmf_main}/fonts/source/public/othello/
%{_texmf_main}/fonts/tfm/public/othello/
%{_texmf_main}/tex/latex/othello/
%doc %{_texmf_main}/doc/latex/othello/

%files -n texlive-othelloboard
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/othelloboard/
%doc %{_texmf_main}/doc/latex/othelloboard/

%files -n texlive-pas-crosswords
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pas-crosswords/
%doc %{_texmf_main}/doc/latex/pas-crosswords/

%files -n texlive-pgf-go
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgf-go/
%doc %{_texmf_main}/doc/latex/pgf-go/

%files -n texlive-playcards
%license lgpl.txt
%{_texmf_main}/tex/latex/playcards/
%doc %{_texmf_main}/doc/latex/playcards/

%files -n texlive-psgo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/psgo/
%doc %{_texmf_main}/doc/latex/psgo/

%files -n texlive-quizztex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quizztex/
%doc %{_texmf_main}/doc/latex/quizztex/

%files -n texlive-realtranspose
%license mit.txt
%{_texmf_main}/tex/latex/realtranspose/
%doc %{_texmf_main}/doc/latex/realtranspose/

%files -n texlive-reverxii
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/reverxii/
%doc %{_texmf_main}/doc/generic/reverxii/

%files -n texlive-rouequestions
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rouequestions/
%doc %{_texmf_main}/doc/latex/rouequestions/

%files -n texlive-rpgicons
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rpgicons/
%doc %{_texmf_main}/doc/latex/rpgicons/

%files -n texlive-schwalbe-chess
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/schwalbe-chess/
%doc %{_texmf_main}/doc/latex/schwalbe-chess/

%files -n texlive-scrabble
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/scrabble/
%doc %{_texmf_main}/doc/latex/scrabble/

%files -n texlive-sgame
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sgame/
%doc %{_texmf_main}/doc/latex/sgame/

%files -n texlive-skak
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/skak/
%{_texmf_main}/fonts/tfm/public/skak/
%{_texmf_main}/tex/latex/skak/
%doc %{_texmf_main}/doc/latex/skak/

%files -n texlive-skaknew
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/skaknew/
%{_texmf_main}/fonts/map/dvips/skaknew/
%{_texmf_main}/fonts/opentype/public/skaknew/
%{_texmf_main}/fonts/tfm/public/skaknew/
%{_texmf_main}/fonts/type1/public/skaknew/
%doc %{_texmf_main}/doc/fonts/skaknew/
%{_datadir}/fonts/skaknew
%{_datadir}/appdata/skaknew.metainfo.xml

%files -n texlive-soup
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/soup/
%doc %{_texmf_main}/doc/latex/soup/

%files -n texlive-sudoku
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sudoku/
%doc %{_texmf_main}/doc/latex/sudoku/

%files -n texlive-sudokubundle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sudokubundle/
%doc %{_texmf_main}/doc/latex/sudokubundle/

%files -n texlive-tangramtikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tangramtikz/
%doc %{_texmf_main}/doc/latex/tangramtikz/

%files -n texlive-thematicpuzzle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thematicpuzzle/
%doc %{_texmf_main}/doc/latex/thematicpuzzle/

%files -n texlive-tictactoe
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/tictactoe/
%doc %{_texmf_main}/doc/latex/tictactoe/

%files -n texlive-tikz-triminos
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-triminos/
%doc %{_texmf_main}/doc/latex/tikz-triminos/

%files -n texlive-trivialpursuit
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/trivialpursuit/
%doc %{_texmf_main}/doc/latex/trivialpursuit/

%files -n texlive-twoxtwogame
%license apache2.txt
%license cc-by-4.txt
%{_texmf_main}/tex/latex/twoxtwogame/
%doc %{_texmf_main}/doc/latex/twoxtwogame/

%files -n texlive-wargame
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/wargame/
%doc %{_texmf_main}/doc/latex/wargame/

%files -n texlive-weiqi
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/weiqi/
%doc %{_texmf_main}/doc/latex/weiqi/

%files -n texlive-wordle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/wordle/
%doc %{_texmf_main}/doc/latex/wordle/

%files -n texlive-xq
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/xq/
%{_texmf_main}/fonts/tfm/public/xq/
%{_texmf_main}/tex/latex/xq/
%doc %{_texmf_main}/doc/fonts/xq/

%files -n texlive-xskak
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xskak/
%doc %{_texmf_main}/doc/latex/xskak/

%changelog
%autochangelog
