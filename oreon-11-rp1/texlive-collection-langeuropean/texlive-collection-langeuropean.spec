%global source0_hash 6e9efc0cf10951f2cff65a0db2ac534da80e7d4ffa424bf82a657f06d9fe88be5ca811a1808c2f301150ccdad464c5a2b5e8c8393a96a7b9c7db5e7bf8e0c2f7

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langeuropean
Epoch:          12
Version:        svn73414
Release:        5%{?dist}
Summary:        Other European languages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 7acac8416e424db754f1e02844e175dc76c694d46efa30e1e29d855cbe3ffff1a50b95c38e2de2e88944bb11920cdf2295254b3855b5d6e13bfb930665cda8c2
%global source3_hash 83b050d9bcfd2d4b7ff54458a559401ecf5abfb020c39b7b7c29f3fe9cc656980a63354df549ff4b93ec4ffb382e60578d5657c268ffb7282dfa5e45fc66539f
%global source4_hash fc96fc03fe38dedddf4f284372dc5b98d25f021de74ef0edc28a35d158fafce7ba2ce203fa24518b77a08d2aa50ef5efa5e04162f6f9c6eb5b5ba69608f3eaff
%global source5_hash 76fb2e29058298c1dd17a0398ee689f381f1cdb5c626323f2cc4712eb7207e2ff0610a4099d69c1fe41fdbcddbca4e80ac414bdce0a131f67de1307ff8da7aeb
%global source6_hash 5f4a1f1f8b48e5083c1aa84db9e5aec69446e141671b114b905d48a09bc018e78b74c1a14730781133f98c7eec1746ed382f0b1ba765b4af1e3de24c71a00a47
%global source7_hash 425609718f28a29b4be04027e65fd07b38d1e01da433de703bb86458f6b1928edb2e3992a6ff18610246b640c00391ed56908490ca9dcae26d91e7021fa09f32
%global source8_hash 5fa80d92372b641f310fb9ec9c881000a5cb86b189b95db25a391f8d5a345c7a5b1a5ae044dd9dd5e7a2e8ea3821da439378021a946c9ef62b60a198ccdb796c
%global source9_hash d2d0e24754163c2c0001b421e9bcf9635963758f5bea3e1732d36ab82ba996dab117686fdf68c5d9ddf6f5cc5ee409e0bbe84a8552d8ab6b44d289bc3dad3edf
%global source10_hash 6f03d6984d248451ce8d9781a6949a6d811e15878b72bff2415e5c84a104bec75a5176d5aaceca982a33f51074334cfe80aeaf0c54e0218a45d055a3b8b7f6ba
%global source11_hash 2ca1ba6a4ace7ced845c18c7d6670c7b9bef48554615f60023bcedf84ec837dbceab64252fee2a0c619c306641ae977bc295ba6cd2a58ff0b5e4cfd22a4fb610
%global source12_hash 85c6d1360db9c7825b9891da93f70b6e78d06edc23be8aef2dd7f8479b9afb266a9decabd89f804449399387793d01d328ce4a27fc5649319f52967bf8fe286f
%global source13_hash cac9cb3e06fc6f6facf24ab9f69d6b5c5d7bf83fee097378b5457dfa1839d3106d70149d04bc438bd7a1b8dc2a165e1f630f541b23577b0183a8198c6f739ac5
%global source14_hash f5d21052e4c2da9ca3263b12d42a97a6f901657e6b90bd925a771354559245b0433ec46f4370b9864a6388d1e40aa9eb7dab251dea89a7eba864e3fb887df316
%global source15_hash afa3aea5b500530e4b6d91477340eb54b8c0f841affb869d3235571203c474bc64cb0ef7032b7f6a7838e7a0a3b56f4977aff78ad2fb914b7f17402e903020b8
%global source16_hash 03357f8b0c101e5e186fa4211a971e625f6970a3129a2594a611c74b77b36a27a288d2da518d21e6e2e5d98bb82802b2115d47e31e6258f01c003be854090baf
%global source17_hash ca732f4b6ccb9ae27f99aaabc99037d9f3d04bc170b9a8bb189a81b6bc9f55fd757c5755bf51ff423850f6b45c88a5645f75a462fc9d9e9b989fa04c1a2cc7c1
%global source18_hash 8bbefe78d6a9aad3d8d7fda63144d245cbe52381f30e58de9425d9e147fd1213ae47203a22b4e9d552ecc713485f1d174f7bf46ae7b43f8c9247921a7d2e8ed3
%global source19_hash 0d0d0a0dafcfef50aa495c28da2ba3b51aa3e57a4f5aa0679b90f37c4f993ccc2c8facb9301249b9b89065009c60f15fd630db7824eeef5af416bf73c54059a1
%global source20_hash b823e6236f586bd4f18ca7f40bd5665e020444ba785ea106b396fb5dba80afb4bba465a1ac9054efc409496c82a8041a275602144205641b457bfb4fbe1d1019
%global source21_hash 4bfa5e267d16913c9ae7602bbe906f855f77cccd49815d8b7f4e504abfb76d5cea58051bc407464d0a85ba0a26f2c19b1e1c1b8a9873f7e54ae157090b781155
%global source22_hash 92949af26b8c5bd9db39743c66f645be90cd24ca1a99fd0f836cb986da908b0575fbacd1e70552b5fb41722c502b6e9917557fe650d510a61112247b45b806e8
%global source23_hash c0d261c15fc7004de08859888545e9ad5fbf35bd79995117e2c9095e9573d83772e5aa1dbc0ca0eb7b982394e71f31d205dfadd99a7c1f3e422955db4845f766
%global source24_hash 46aca093e061948272d2a54ff9f95b94b101582f0ec9d795668983c37b518be3c3d76d2c8e6901126d3dd7342db003589bacce9a40cfd573263a953bbedbfc48
%global source25_hash bc859f01f52ad51da7df9d458e507b62eb69e40e1dc39362ff32ea8ee8890acce8ce49120fce967f321c9d674f4334c62c9bf2b3f8017288b724ecfe3943d667
%global source26_hash ff9ff05bb88820fd52a0650b5d824831c2f58e39d745b35f68422f4d904504934aecfcdcdbb1e846517ec35a7b22e134eef71b46f3819ce5ec4119de36fd09c4
%global source27_hash 9febb4056f41de0011d75009e0bfedf4227d869591ba661380d6a7bcd2ecb6a8ded2e1e933ef4c2a9ac31bb1b604bf975a9181ebd2fd3f188f4a2a01a8f445c2
%global source28_hash bbdd05e7106494f23892f3455ad224d3deb1881f5a73720e2c73e7401514fed324484416def64e2e8fd7c2416b521fb2d4527585d2302a220330925c296afecb
%global source29_hash c31f7efd7415f3439635b293c9aad2cfc2632352534e579c0f8d3e74443fb7aa88a95e19735a7b65137d81899ad9d2ad8bbdb28c5da2ff05a2be9dbad552b0f8
%global source30_hash a64ff7b7aab3a3f440a8f3491a8809931d6f9d4c3b65b35a5ab10d46cedeac1746c9b6701c31abb50ab7ff8477b65222cec73342c33d008d1132c83e9fb89cdf
%global source31_hash 791544c5062ea0744d3e353ad380551cb674267fc268a0f21b649b896db2a23101969244b8f862c6c6785fb806a9d8a576eedbe1cce19117e05e210c0560feec
%global source32_hash b277fcc4c1cc58650722016eb9489fca635f7faed3788a93cceddb48ea25e6168b575b2554f616916f3f201100d69233b34c66871f085fa470473f47fe0c553a
%global source33_hash bbb2654b2ccef7a91d536a9a66f309f457459fc5c9d72ead212d10bbb2f8d8410128886fa388b5572e0ba4227ff54b421d0ef40a954c4be7c4dc902da3178166
%global source34_hash 83e8aa3c7e8e018f79c848ebd884f0d0a07c87953611342b5a9f25df1241ddd931ede31a03b1670922049948a6f9ebc88676de0a4be9e144a3f99e22fb857fd7
%global source35_hash 76dac9c2b95699a42018ad370afc1236668a37a71707a6c1a8fff1921df9edf30730f71337c1128f64b7448a0bd3f99e432ddbc1219534884e8476a8c7fdf338
%global source36_hash c061ca1ec358e4d8df05e0adadd5d87695cf3b9f86cab52eaa0e08b1f5b1fedb66febe32107e74c1926fa4d697b056d7d3f119db525b90ff7e7bde30fd015508
%global source37_hash 7284141fbecedad06cfef78f50b4c13ebb3af76ced474c456a364c97943b51b9a233ecf6797e561ab0936ef7d082adc80daea0de4e961baab60e494bd72f7061
%global source38_hash 14d720627c4733b17439371ff76253ac49a5749f57039521a6570bdf7ba2ff2c7a6bb967d8755787f672a9c21ceeb1c1f1cd435c0808b7c643a6c37c1d9e31d3
%global source39_hash fdc1380eab3f7850d651b81a50579b409bfc3cd7dd7f4c478a9bf013350921c216ab54c2e5bbae379f85570a6b03997207a2f3aeb521247cd864dd18f7cf794e
%global source40_hash f1f2f26b5466d10e995d76f7003c202650e3976b82b431d2bae768a582bc0c5662fc120739c49fcfd1226da3595c8a6b2e8c952a491718c45e69770c09d542a9
%global source41_hash 86433fa646eb6b2f7ee0ba54f1dafa73b81bd98012859c59408883cc76ec876720ef526cb2f526bd4a8385c0371f9bb01ae6d604661deabb4ec920172986adf0
%global source42_hash 72fe6338ef6f172a23790402a632881906689117e7227b6f2f2fb6129fca9a7d44c42ddd48e8286252f3b5fce9dc34439594882c1f80f33557ef5ef70afe4993
%global source43_hash a2fa0cc72a205fcc25c2baeb7717a573bf8f2db5438e49c9de8a90e8da37d4f267ff30f08f8bb79f08756f5d227acddba8c069c8a5c257adf95c3afac271927f
%global source44_hash c2ed9093ab202be8ade1abfdf257c21347ddaaabb6fa933f69464a8074082be5ff552dfc76ddbc06b5f1904fca5e053bf5cf90093307f6b427f7fa721d7df8a6
%global source45_hash 1d999a967433f30950f04659265ced6462bcec778ea2878ca7fc7f05e823d9008b49f9a3e136265eefa192ad0aced05d3161691fede729e9e28ad038fd1ca7ad
%global source46_hash c0a4570e8a53c6add9e35d8fd44e30b6d252c31695a49f62a4564832f94af9bc89db9c1062c14d1184fce5bea4d6916242fd13b9d36510b9fffbb4f9ca3fe536
%global source47_hash 81927ea97549ea2d227b135bc33fc181437e467ba304b428ac0d8fe220dd49c46d483cc13f23d58e6cb93d1457125d1e0a4df2451b39e17d844f24e387116647
%global source48_hash ae90b12a3c59dd52a8a87d2bc68b64ed9e957888e3498bbaef08faca749ca23b7c103639b16571edb848cfb88bab2c531b058fb0908290f026797ca4d97e74f5
%global source49_hash b21f5f23a84f0c779f7ab062aeda7c3fa6b586d96e276741500ee6f5d06ff2a282f8a94e349a1fd4336a364c164f6eb17b254df4258f0b3a303767950707ecb2
%global source50_hash 469f520355f3098c2ee4a62d2839df8c0ed3215a45ed2b9030897212a20fae816df6e4ad5a02fbe8fadc034bd4158393b46e823f31c58c982744520d3003f90e
%global source51_hash ef17be5de84042c7f723d647d48481edbfdc01d4faef9842c71b651c1702e6ba148031a627599b7c0f27f5e3ba1605c6bb4f8da89ca383e3065781f52b731b9c
%global source52_hash 3dc4c5e4a21b59dddf26bab24a3244c0d2ee3d5aff826f4aa6d2db7fd8b4237c10fed7a6925c81aecce380912662f3bf581afe9fa2eb29354c5c53f5fc930bf0
%global source53_hash c91a2c61580678f8639f8b0631a67901eb61c7f2b84f1d94c71e5d280de588511bd6aabcf40878efc5e819d81419ba6e943de172eb4405ce52cb0f862ad50976
%global source54_hash 41e5d322cd44d8e6d107ea028c3043c6c178d6de492b0537fd44357922598b3014de6a7ad18b37822aeea4bd51bbe17b155bf01abcb4538ed0cf4268db5654d5
%global source55_hash 289feb736ccae0f92d42979ec864464a478035869a4ca20c4e1426eaeaaf073f26f3196016055ab7d38fe033536ea8f09f23c5d559885006b367bf623745c626
%global source56_hash 02916936992e00e7aa884b46b6f786dd0fe5a0aaa6e2c6c4e28fe72de7fe5260fca7cdd37efc4a775a8d172e3993c98df7cec3d1ad08f01487f7cb0c8f2d179a
%global source57_hash 06931a6b9987a7affd4632ea5cc79028a2a88c584523c03ce79c2a15268947fb1103137da158886c7957e0a7c938ca69c1c5c7d88104c892cae611c914f6fb93
%global source58_hash 921e7843a2628b97b3a2051435620000122c4fddead77367fabd011517a184b852b87964638d52630818faa905a1acc84f401ce2af8928143c768caac400406d
%global source59_hash 468ee5cc95573f48415fc22babefd9c83548315e40761f4bbbdfd86adbcba26d55c5f1c0b0c0eefdd31877648d262bd9a8302a4252a0b85809751a577790a318
%global source60_hash e2f696c4ade89a1ad4f859797901c9592ecd031684bc79bcc032b491585925328d1bc40f99e3cfa5d6b2d6f31df51ba07dd17298f7bfdb4fe7be9337bc6ccf73
%global source61_hash ee68a2f0c41dac79d00a4103804ad735b5bdc78bad660d5933e61e88290a2dea17a695ea45129a672cdb301e1c89e4fc319173df1fbfd87f944abbe46f7f1dd0
%global source62_hash 1325b4c8c0ff8c1e53d27b5696da419f99852bd6c272176bab4e03f91bb6a715de51d24317b9cec1af50ee0ae2b34c03c51afe9cedb8903a1e8f74bbee3cc06f
%global source63_hash c4280453d1f133fa8bb9d60c25755497787a76d1e87056e4e4932632fd48db48a1fd76856efaa26e5888d456333284e85ab9a9037ec218fc6b4127782bf9959c
%global source64_hash b99e3bb1e577ee5bef01e195eb6f5577941853608b1ff9f4874b818802ab5e165721df0a8663a4a2993eaf21bc541bf4365234d0b5f47c085b0b9e5a2a57a9a4
%global source65_hash 88d6372772fc53762fa727fe53db7367433acca5a60af0b1997a161221937f08d216afcadad4fd965e7b775a07b68ea55aab6fa583f072c9fd64180b6b5927b7
%global source66_hash ac3d7d67fc68a3aa63c90b4bc625eb2dacb47d804d59c54a52f0fb973f25c5e9f16f343ae052bad34a7fdcc7eef8ffcc62dbe538c09a4d852845489684a20aa3
%global source67_hash 3fc12f2c4e1e44eed7b946ab109d4a3005317990b2c4e402fd06c4f08afb209819291aff3146958d5389c284b1bf17b45536e3f2a26adf79437b6006cc724fdd
%global source68_hash 9008c19bae250136f5f61364560d3d1077d81365936634e0ed22843d13c516e92fd67ded637f373aa1f3f2e2d9f1a72d1b6732ad7ce2da6d8328cb1651fd5198
%global source69_hash c6c32e9038d177a99b0cdf3aa86344771ae086337eecf3632f91a9585d6d7714a26ba977065945b38630a0fca05eb1fce574b4bb09d93679ebfe47bece7e742c
%global source70_hash e0a77801b4f104bf3ffa03db61b8cdd51824c8ee1e6dd40c120f604c62390777110f90b0eaf39c7a392296159bac68e182d1aef32375ed9733ca9d63d9a57867
%global source71_hash bb37e815c555a58107c83ce2d12775852122c208d04f2c721a0e5ffc223e3149c01dffb241df1058b66edb05b80f85397c20469ac8346b1cccfa6b9682c5d546
%global source72_hash 4cd1c07016710d79b3ef6e0ba480394aef9a1dbb534c139adceb8405c9870de995d5e9af8803d2e2eb01ffac8a524e62e224dbdbc4d847efe0b6d7632cbe58f7
%global source73_hash 27acd3ef5b5a24654b26f04cf0415478dd56b4dea90c491c39f3a2589e47ab35350641dd51b3049bc6e609f882dbdd04dd927e6653434817fdca705ff4fac2b1
%global source74_hash 0707b2f9bba508427a9ac564a9d8406c8696249c49cd5d8094c0a0ecc65db443322ae49e8b147159d3813396758b2cb03afcb9ddd1687b86597fbdb90190cf92
%global source75_hash e9f2e7f188abd5355a7f6a1873f33dea5f3d9f0fe26c10c5f77acfb8780e06cd789e1ebdaaa2445e9cd88fe7c946b260490b97b04f06adb1413798d79612b3d1
%global source76_hash 68578a19e863a679a45d14a43c1b65f48ec4c83cc3d13cbb3c4d92f8daafba20d853c708028abf00d5ff2ac9844345a1836c3d4b15cbbfe1ab9fe5232abea5b6
%global source77_hash c963ff535e0dd7f389c6acb81e04c0159a425b4f6855a21b0c6a203b46cec7086d28a77cde61573485f64b1557535702a2582b6031472e2934f12b5188b8d9ce
%global source78_hash c8057f70ad5f929cf14be69c20ce7aad8c00ba55309c8a4e17e786db5ce769dc41de175ab53116d92c6ae267585f18ec0bac9e6e4c4bdcce1e65e67450e59a5e
%global source79_hash a81b22eab8aa4e8a8fe8ca3715e33d71e271440e4032abdf412ec6d4d453252c8d7601d2a49ff0c371221db355264e5f12e62ffb78423d2d7a63dc26d9ca61f9
%global source80_hash 19878db2775d3dad30321d175eba2f6f35858c02994ce8e7e00d3cd41e22f798f4ce6a2e86eb7b70f5bbe8cda759ff92bd65a2950f3d07f4a996daf4d78da74b
%global source81_hash db2aad0b8f68892ccfcab929e5e248016031f2723d1cc3b3d10c9e16b3af694e3fb482c2b52d12de381585c6eb807cc9281956e058a6a4569d5c5d84bc87141b
%global source82_hash ed4a1dbb549795509b843ae7b14fc4ad6fea1b6519aafc775d9facee523f9e1acde2e8d5ccc3761ac7cad58136949026051d0d53ae022d5909066d6622d81679
%global source83_hash 993d1f4346a5ba77c23b615c52f4043f8e73ba3fadffce00d9653bd3c75b1ca6d5ec6874aeb2ae8222bc5bab2010109a2b4dc0c7d874c8577a3596c936f83b15
%global source84_hash e0fbfdff4a606d1702a505581885a9db4928f2ec5c35077492478cbb568fe6c8fa23eae0fe792279cd9ec6a6516e3a0d9c41ec18b67b434d5dc4d669d3a1662b
%global source85_hash ce4ae8c8912de4b80f71f22097d806ce26a8779ef87a6887e84a1c1b838800e3885049c70bcf1e01088c3765131c30a5e66493c1d352ced169c8c1b175644a1b
%global source86_hash 9080822fda2e31f8f53f65dcd269af52ded32f284492ee1e20c539c2756cac868ea07031482e8f5aa2fb4282d92e3fdc7c38d4c1b2ae19a5fc3c73298f57f798
%global source87_hash a3c2edcb1df6087bed0ed1b84603b9efc4d4b9f159410c1a600ce247d7aab95e3d8e8fc400d8f77e4b7048b923e3a42e96a9bca73c0ebddf0a9a4e1482db95c8
%global source88_hash 24f4dcf3a955e6556d687560391b65f6417e2ee88e0ed3eccf8bdb629fa405d177a85dd947ff76b4d614ca417d765d8abd33e6a7df463c0088ba2380f89df852
%global source89_hash 859bdc09a249117ebdf23798284044ed2ef073d00643ce3370626e3e93f7bcf1b3f9d9d724b3dd5a71d0f1e85abb253bd550bafb237a1ec146ad88311ef1ca5c
%global source90_hash 6edeccb96458ed2f31ad0b909b1a68de28e2e2be5c5b23999e466e48ec891e695d4d9c16b91d7a10e8bbf0c4c85a882212d2cc70c9638820838b81c1cded6ba4
%global source91_hash 669c8602f7a33a6f78ec91d17fbc7576a820d249e08a9a914e2620bf021ac8291b68c26feedd3d8b5797c7ff84e496784cb36e509d5828b3426ff29542b41b58
%global source92_hash c28157280dad4ac8ce003a8a68c546dda74dc51fd137280b883e3249306f1dca58611986a275ec43af71e1038c0b10f473577321cd8bbe325a29aff2c7237fcc
%global source93_hash 81c4e9c64b6b74e01e92cdde42b4a2cf52372ae9beee2d4e02875c23a58981adca758ac36a3b30d3cfbc926810da3b23c732f5e8c7783a2cf87381c5cf63cdfb
%global source94_hash 5b3a5431a816e53c7eae7229ad99a523ca2d397bd2135eba5bf87bdacd9d3e51910c5e54d6dc79338c91c6e4aab645a9968d06e1d40f0039559b5f5244a673f6
%global source95_hash 2d50e0f15f5787eee430acd76697e98b90799ddffff601790e39dabeb8f5ed52e63c6d39076f8e34b40e596d4af1b96a2a2badc76635db4946636e214b572f5f
%global source96_hash 7835080a255432e1bc022c480185737c817e0cb1782fb52f9475e6cd86efdcd60c9f58d38bd24830d560303fbe8456a81dd7c774288818bc25393658c70ecb11
%global source97_hash c2cd1b54daf74e78e6087159fa827ece77f2dc835eda81e03fce861581e812536292f3f0b70b8bb77107c0a4032d12006e870303156a3f3c7cb653020ed9b97c
%global source98_hash ae7a5e3bea2bd62a0cdbbfbde7e0d9e06554fa4b3bb825b45febed42556fa101fd2e6c611ad9fc1cc87ed5c92540977780fde47ae78a89dd37b70f89c94b5e8d
%global source99_hash c8635db5888817d392706b8b65aa5158a4973cf236dad7fe31a9545857daab15a6c1f2f82ab06e71e50a4af94824b17ac89c394a759721e192966a1f78433d47
%global source100_hash 29fc8b6a2645f241e8af437de3a295be8d56a088bd7c7666c35b14f104f242e68ecef2757d62a393400d9f337eb685e48ebac06769259c723d634312a7288ab9
%global source101_hash 0369a6bad93a533394453750846f7b7f503aebea3edcf47ee58fd7458d6289353b6c7da00f8480c7a86834c86465f8200e4c606e160f8b18d6240b00e004ae6d
%global source102_hash 9f867e2c2d9e0d50b718a90337856676f61960867db45802797bfceca56f7b992d6b01cad71694f0b7ec8cfe049fbe7019a23594fa9ff6ed64563fc050a52690
%global source103_hash 1252d1100e8b136c8cbfc9b3ef267b98255559e980f96e4966cbf77ad1a6dafb787e7e03fe14e609e7786e4338de93a37be293172bc8ae1d8aa548c4c9033893
%global source104_hash db4c10c6892446c01ba58606b8f099073d6375ce144b68156fd0c29977de0e886790e4839b85639cc05a1eb42a2a8380d57928af0a406c996e318a771cd8f2f3
%global source105_hash a0c6005c6e0f35802591bd75084658d3dc220e37ef47019b31a7bd233985980692033c50ad923627100df117c0f7e1bb3663f6bb0bc88ca67d180fe25d331bde
%global source106_hash 3d05b533c3618c8583fda08e7682baa41bba5c422f40fce20eeace0523ae6bc99f83ca0762544f38a86f980f99b3b5f58e2fe1817bcac1188196beb0808cd0a0
%global source107_hash 84d74207f2dceb9453217ad235af031a448b222207c156415acfcbfcd6e2ebb6a88669f3a2662f99f004c22a1bf0cf1d8bef9ae21fe70d7993334e052e44ecae
%global source108_hash d5b05705c81e0d04477cb56571710c8416251b8c3e2349fb4623794994dfb3ebe416a14828590bd5d0861b7edf633c497d70037dd982139fe5d4a1aa452acc2d
%global source109_hash 01d207fe9d77df0a225cd5fe718f118bc755c1e23c9dcb2bc4e0b4c2983205469baeeefcc195b150cc54f4540ea71d96cfc393fe61a32f7e85d5c9b5944c5938
%global source110_hash 653fea96310508e8a30c76821d1cd83dbf579052fecbb8c859d40cb39926d24ae0141b4788901b34b4839615b33d5995eed2b6a27f6abcae981b9d47b6ebeb34
%global source111_hash cd7065dc6a916941a0fd05ea342d29499b6f7496d1934e06c49e7ea1a99c5be5cd515bbcbc2b5935ff8132adcc7b94e653d55de967700410ace55697f6fc156e
%global source112_hash fb9c9f00433ba959ad8f7b5acc93b1e7b0db1cffec96b7c988eeaaae89ceecc815071a1e21f78d36279e529f4e9095602b1887d3c5d4164494be502cf4a19873
%global source113_hash 61ceb0b55cdf94ebadff3b81d6a1327adc877737016ac611d6e0bc3e0e4f76ab34122ab97f83239b0e0982ce17a4220392cb42f73486c1abee0d7febea9287e1
%global source114_hash 3e231cf63ff0971d116a22ac1a491c6cd085b17550c6397168e71a5a4eace9cc8ea89d63adafc343602bbb9738822b4fc0cd48f8ba48c5c07bae2e465a35879e
%global source115_hash c1c2c8320b53b4048b2ee4141c33b8532e9ca07d87c1aebcf3745edac74d4ca6e4bf545483c62bfe9de81fdc60356ec56c695c1c4f08c64e276ea182d0012e78
%global source116_hash b1e0ec4717d0b837d44672edaa4fa27139dafb5723a242563404107040a452fe70a8970e640225f06ba12d40528f6236d2ccf4dbaf763e2b54d4ae399a35b0d5

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langeuropean.tar.xz#/collection-langeuropean.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/armtex.tar.xz#/armtex.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/armtex.doc.tar.xz#/armtex.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-albanian.tar.xz#/babel-albanian.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-albanian.doc.tar.xz#/babel-albanian.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-bosnian.tar.xz#/babel-bosnian.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-bosnian.doc.tar.xz#/babel-bosnian.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-breton.tar.xz#/babel-breton.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-breton.doc.tar.xz#/babel-breton.doc.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-croatian.tar.xz#/babel-croatian.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-croatian.doc.tar.xz#/babel-croatian.doc.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-danish.tar.xz#/babel-danish.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-danish.doc.tar.xz#/babel-danish.doc.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-dutch.tar.xz#/babel-dutch.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-dutch.doc.tar.xz#/babel-dutch.doc.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-estonian.tar.xz#/babel-estonian.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-estonian.doc.tar.xz#/babel-estonian.doc.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-finnish.tar.xz#/babel-finnish.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-finnish.doc.tar.xz#/babel-finnish.doc.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-friulan.tar.xz#/babel-friulan.or11.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-friulan.doc.tar.xz#/babel-friulan.doc.or11.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-hungarian.tar.xz#/babel-hungarian.or11.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-hungarian.doc.tar.xz#/babel-hungarian.doc.or11.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-icelandic.tar.xz#/babel-icelandic.or11.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-icelandic.doc.tar.xz#/babel-icelandic.doc.or11.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-irish.tar.xz#/babel-irish.or11.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-irish.doc.tar.xz#/babel-irish.doc.or11.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-kurmanji.tar.xz#/babel-kurmanji.or11.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-kurmanji.doc.tar.xz#/babel-kurmanji.doc.or11.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-latin.tar.xz#/babel-latin.or11.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-latin.doc.tar.xz#/babel-latin.doc.or11.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-latvian.tar.xz#/babel-latvian.or11.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-latvian.doc.tar.xz#/babel-latvian.doc.or11.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-lithuanian.tar.xz#/babel-lithuanian.or11.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-lithuanian.doc.tar.xz#/babel-lithuanian.doc.or11.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-macedonian.tar.xz#/babel-macedonian.or11.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-macedonian.doc.tar.xz#/babel-macedonian.doc.or11.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-norsk.tar.xz#/babel-norsk.or11.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-norsk.doc.tar.xz#/babel-norsk.doc.or11.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-occitan.tar.xz#/babel-occitan.or11.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-occitan.doc.tar.xz#/babel-occitan.doc.or11.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-piedmontese.tar.xz#/babel-piedmontese.or11.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-piedmontese.doc.tar.xz#/babel-piedmontese.doc.or11.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-romanian.tar.xz#/babel-romanian.or11.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-romanian.doc.tar.xz#/babel-romanian.doc.or11.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-romansh.tar.xz#/babel-romansh.or11.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-romansh.doc.tar.xz#/babel-romansh.doc.or11.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-samin.tar.xz#/babel-samin.or11.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-samin.doc.tar.xz#/babel-samin.doc.or11.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-scottish.tar.xz#/babel-scottish.or11.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-scottish.doc.tar.xz#/babel-scottish.doc.or11.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-slovenian.tar.xz#/babel-slovenian.or11.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-slovenian.doc.tar.xz#/babel-slovenian.doc.or11.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-swedish.tar.xz#/babel-swedish.or11.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-swedish.doc.tar.xz#/babel-swedish.doc.or11.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-turkish.tar.xz#/babel-turkish.or11.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-turkish.doc.tar.xz#/babel-turkish.doc.or11.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-welsh.tar.xz#/babel-welsh.or11.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-welsh.doc.tar.xz#/babel-welsh.doc.or11.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/finbib.tar.xz#/finbib.or11.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gloss-occitan.tar.xz#/gloss-occitan.or11.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gloss-occitan.doc.tar.xz#/gloss-occitan.doc.or11.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hrlatex.tar.xz#/hrlatex.or11.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hrlatex.doc.tar.xz#/hrlatex.doc.or11.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/huaz.tar.xz#/huaz.or11.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/huaz.doc.tar.xz#/huaz.doc.or11.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hulipsum.tar.xz#/hulipsum.or11.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hulipsum.doc.tar.xz#/hulipsum.doc.or11.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-albanian.tar.xz#/hyphen-albanian.or11.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-croatian.tar.xz#/hyphen-croatian.or11.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-danish.tar.xz#/hyphen-danish.or11.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-dutch.tar.xz#/hyphen-dutch.or11.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-estonian.tar.xz#/hyphen-estonian.or11.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-finnish.tar.xz#/hyphen-finnish.or11.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-friulan.tar.xz#/hyphen-friulan.or11.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-hungarian.tar.xz#/hyphen-hungarian.or11.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-hungarian.doc.tar.xz#/hyphen-hungarian.doc.or11.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-icelandic.tar.xz#/hyphen-icelandic.or11.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-irish.tar.xz#/hyphen-irish.or11.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-kurmanji.tar.xz#/hyphen-kurmanji.or11.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-latin.tar.xz#/hyphen-latin.or11.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-latvian.tar.xz#/hyphen-latvian.or11.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-lithuanian.tar.xz#/hyphen-lithuanian.or11.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-macedonian.tar.xz#/hyphen-macedonian.or11.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-norwegian.tar.xz#/hyphen-norwegian.or11.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-occitan.tar.xz#/hyphen-occitan.or11.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-piedmontese.tar.xz#/hyphen-piedmontese.or11.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-romanian.tar.xz#/hyphen-romanian.or11.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-romansh.tar.xz#/hyphen-romansh.or11.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-slovenian.tar.xz#/hyphen-slovenian.or11.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-swedish.tar.xz#/hyphen-swedish.or11.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-turkish.tar.xz#/hyphen-turkish.or11.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-uppersorbian.tar.xz#/hyphen-uppersorbian.or11.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-welsh.tar.xz#/hyphen-welsh.or11.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kaytannollista-latexia.tar.xz#/kaytannollista-latexia.or11.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kaytannollista-latexia.doc.tar.xz#/kaytannollista-latexia.doc.or11.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lithuanian.tar.xz#/lithuanian.or11.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lithuanian.doc.tar.xz#/lithuanian.doc.or11.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-dutch.tar.xz#/lshort-dutch.or11.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-dutch.doc.tar.xz#/lshort-dutch.doc.or11.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-estonian.tar.xz#/lshort-estonian.or11.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-estonian.doc.tar.xz#/lshort-estonian.doc.or11.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-finnish.tar.xz#/lshort-finnish.or11.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-finnish.doc.tar.xz#/lshort-finnish.doc.or11.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-slovenian.tar.xz#/lshort-slovenian.or11.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-slovenian.doc.tar.xz#/lshort-slovenian.doc.or11.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-turkish.tar.xz#/lshort-turkish.or11.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-turkish.doc.tar.xz#/lshort-turkish.doc.or11.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nevelok.tar.xz#/nevelok.or11.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nevelok.doc.tar.xz#/nevelok.doc.or11.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rojud.tar.xz#/rojud.or11.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rojud.doc.tar.xz#/rojud.doc.or11.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/swebib.tar.xz#/swebib.or11.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/swebib.doc.tar.xz#/swebib.doc.or11.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turkmen.tar.xz#/turkmen.or11.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turkmen.doc.tar.xz#/turkmen.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-armtex
Requires:       texlive-babel-albanian
Requires:       texlive-babel-bosnian
Requires:       texlive-babel-breton
Requires:       texlive-babel-croatian
Requires:       texlive-babel-danish
Requires:       texlive-babel-dutch
Requires:       texlive-babel-estonian
Requires:       texlive-babel-finnish
Requires:       texlive-babel-friulan
Requires:       texlive-babel-hungarian
Requires:       texlive-babel-icelandic
Requires:       texlive-babel-irish
Requires:       texlive-babel-kurmanji
Requires:       texlive-babel-latin
Requires:       texlive-babel-latvian
Requires:       texlive-babel-lithuanian
Requires:       texlive-babel-macedonian
Requires:       texlive-babel-norsk
Requires:       texlive-babel-occitan
Requires:       texlive-babel-piedmontese
Requires:       texlive-babel-romanian
Requires:       texlive-babel-romansh
Requires:       texlive-babel-samin
Requires:       texlive-babel-scottish
Requires:       texlive-babel-slovenian
Requires:       texlive-babel-swedish
Requires:       texlive-babel-turkish
Requires:       texlive-babel-welsh
Requires:       texlive-collection-basic
Requires:       texlive-finbib
Requires:       texlive-gloss-occitan
Requires:       texlive-hrlatex
Requires:       texlive-huaz
Requires:       texlive-hulipsum
Requires:       texlive-hyphen-albanian
Requires:       texlive-hyphen-croatian
Requires:       texlive-hyphen-danish
Requires:       texlive-hyphen-dutch
Requires:       texlive-hyphen-estonian
Requires:       texlive-hyphen-finnish
Requires:       texlive-hyphen-friulan
Requires:       texlive-hyphen-hungarian
Requires:       texlive-hyphen-icelandic
Requires:       texlive-hyphen-irish
Requires:       texlive-hyphen-kurmanji
Requires:       texlive-hyphen-latin
Requires:       texlive-hyphen-latvian
Requires:       texlive-hyphen-lithuanian
Requires:       texlive-hyphen-macedonian
Requires:       texlive-hyphen-norwegian
Requires:       texlive-hyphen-occitan
Requires:       texlive-hyphen-piedmontese
Requires:       texlive-hyphen-romanian
Requires:       texlive-hyphen-romansh
Requires:       texlive-hyphen-slovenian
Requires:       texlive-hyphen-swedish
Requires:       texlive-hyphen-turkish
Requires:       texlive-hyphen-uppersorbian
Requires:       texlive-hyphen-welsh
Requires:       texlive-kaytannollista-latexia
Requires:       texlive-lithuanian
Requires:       texlive-lshort-dutch
Requires:       texlive-lshort-estonian
Requires:       texlive-lshort-finnish
Requires:       texlive-lshort-slovenian
Requires:       texlive-lshort-turkish
Requires:       texlive-nevelok
Requires:       texlive-rojud
Requires:       texlive-swebib
Requires:       texlive-turkmen

%description
Support for a number of European languages; others (Greek, German, French, ...)
have their own collections, depending simply on the size of the support.

%package -n texlive-armtex
Summary:        A system for writing in Armenian with TeX and LaTeX
Version:        svn69418
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(arm.tex) = %{tl_version}
Provides:       tex(armkb-a8.tex) = %{tl_version}
Provides:       tex(armkb-u8.tex) = %{tl_version}
Provides:       tex(armscii8.def) = %{tl_version}
Provides:       tex(armtex.sty) = %{tl_version}
Provides:       tex(ot6enc.def) = %{tl_version}

%description -n texlive-armtex
ArmTeX is a system for typesetting Armenian text with Plain TeX or LaTeX(2e).
It may be used with input: from a standard Latin keyboard without any special
encoding and/or support for Armenian letters, from any keyboard which uses an
encoding that has Armenian letters in the second half (characters 128-255) of
the extended ASCII table (for example ArmSCII8 Armenian standard), from an
Armenian keyboard using UTF-8 encoding. Users should note that the manuals
still mostly describe the previous version of the package (ArmTeX 2.0).
However, a description of the new features of ArmTeX 3.0 is provided at the end
of the README file.

%package -n texlive-babel-albanian
Summary:        Support for Albanian within babel
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(albanian.ldf) = %{tl_version}

%description -n texlive-babel-albanian
The package provides support for typesetting Albanian (as part of the babel
system).

%package -n texlive-babel-bosnian
Summary:        Babel contrib support for Bosnian
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bosnian.ldf) = %{tl_version}

%description -n texlive-babel-bosnian
The package provides a language definition file that enables support of Bosnian
with babel.

%package -n texlive-babel-breton
Summary:        Babel contributed support for Breton
Version:        svn77470
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(breton.ldf) = %{tl_version}

%description -n texlive-babel-breton
Breton (being, principally, a spoken language) does not have typographic rules
of its own; this package provides an "appropriate" selection of French and
British typographic rules.

%package -n texlive-babel-croatian
Summary:        Babel contributed support for Croatian
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(croatian.ldf) = %{tl_version}

%description -n texlive-babel-croatian
The package establishes Croatian conventions in a document (or a subset of the
conventions, if Croatian is not the main language of the document).

%package -n texlive-babel-danish
Summary:        Babel contributed support for Danish
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(danish.ldf) = %{tl_version}

%description -n texlive-babel-danish
The package provides a language definition, file for use with babel, which
establishes Danish conventions in a document (or a subset of the conventions,
if Danish is not the main language of the document).

%package -n texlive-babel-dutch
Summary:        Babel contributed support for Dutch
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(afrikaans.ldf) = %{tl_version}
Provides:       tex(dutch.ldf) = %{tl_version}

%description -n texlive-babel-dutch
The package provides a language definition, file for use with babel, which
establishes Dutch conventions in a document (or a subset of the conventions, if
Dutch is not the main language of the document).

%package -n texlive-babel-estonian
Summary:        Babel support for Estonian
Version:        svn38064
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(estonian.ldf) = %{tl_version}

%description -n texlive-babel-estonian
The package provides the language definition file for support of Estonian in
babel. Some shortcuts are defined, as well as translations to Estonian of
standard "LaTeX names".

%package -n texlive-babel-finnish
Summary:        Babel support for Finnish
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(finnish.ldf) = %{tl_version}

%description -n texlive-babel-finnish
The package provides a language description file that enables support of
Finnish with babel.

%package -n texlive-babel-friulan
Summary:        Babel/Polyglossia support for Friulan(Furlan)
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(friulan.ldf) = %{tl_version}

%description -n texlive-babel-friulan
The package provides a language description file that enables support of
Friulan either with babel or with polyglossia.

%package -n texlive-babel-hungarian
Summary:        Babel support for Hungarian
Version:        svn77586
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(magyar.ldf) = %{tl_version}

%description -n texlive-babel-hungarian
The package provides a language definition file that enables support of
Hungarian with babel.

%package -n texlive-babel-icelandic
Summary:        Babel support for Icelandic
Version:        svn51551
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(icelandic.ldf) = %{tl_version}

%description -n texlive-babel-icelandic
The package provides the language definition file for support of Icelandic in
babel. Some shortcuts are defined, as well as translations to Icelandic of
standard "LaTeX names".

%package -n texlive-babel-irish
Summary:        Babel support for Irish
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(irish.ldf) = %{tl_version}

%description -n texlive-babel-irish
The package provides the language definition file for support of Irish Gaelic
in babel. The principal content is translations to Irish of standard "LaTeX
names". (No shortcuts are defined.)

%package -n texlive-babel-kurmanji
Summary:        Babel support for Kurmanji
Version:        svn30279
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(kurmanji.ldf) = %{tl_version}

%description -n texlive-babel-kurmanji
The package provides the language definition file for support of Kurmanji in
babel. Kurmanji belongs to the family of Kurdish languages. Some shortcuts are
defined, as well as translations to Kurmanji of standard "LaTeX names". Note
that the package is dealing with 'Northern' Kurdish, written using a
Latin-based alphabet. The arabxetex package offers support for Kurdish written
in Arabic script.

%package -n texlive-babel-latin
Summary:        Babel support for Latin
Version:        svn76176
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(classicallatin.ldf) = %{tl_version}
Provides:       tex(classiclatin.ldf) = %{tl_version}
Provides:       tex(ecclesiasticallatin.ldf) = %{tl_version}
Provides:       tex(ecclesiasticlatin.ldf) = %{tl_version}
Provides:       tex(latin.ldf) = %{tl_version}
Provides:       tex(medievallatin.ldf) = %{tl_version}

%description -n texlive-babel-latin
The babel-latin package provides the babel languages latin, classicallatin,
medievallatin, and ecclesiasticallatin. It also defines several useful
shorthands as well as some modifiers for typographical fine-tuning.

%package -n texlive-babel-latvian
Summary:        Babel support for Latvian
Version:        svn71108
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(latvian.ldf) = %{tl_version}

%description -n texlive-babel-latvian
The package provides the language definition file for support of Latvian in
babel.

%package -n texlive-babel-lithuanian
Summary:        Babel support for documents written in Lithuanian
Version:        svn66513
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lithuanian.ldf) = %{tl_version}

%description -n texlive-babel-lithuanian
Babel support material for documents written in Lithuanian moved from the
lithuanian package into a new package babel-lithuanian to match babel support
for other languages.

%package -n texlive-babel-macedonian
Summary:        Babel module to support Macedonian Cyrillic
Version:        svn39587
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(macedonian.ldf) = %{tl_version}

%description -n texlive-babel-macedonian
The package provides support for Macedonian documents written in Cyrillic, in
babel.

%package -n texlive-babel-norsk
Summary:        Babel support for Norwegian
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(norsk.ldf) = %{tl_version}
Provides:       tex(norwegian.ldf) = %{tl_version}
Provides:       tex(nynorsk.ldf) = %{tl_version}

%description -n texlive-babel-norsk
The package provides the language definition file for support of Norwegian in
babel. Some shortcuts are defined, as well as translations to Norsk of standard
"LaTeX names".

%package -n texlive-babel-occitan
Summary:        Babel support for Occitan
Version:        svn39608
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(occitan.ldf) = %{tl_version}

%description -n texlive-babel-occitan
Occitan language description file with usage instructions.

%package -n texlive-babel-piedmontese
Summary:        Babel support for Piedmontese
Version:        svn30282
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(piedmontese.ldf) = %{tl_version}

%description -n texlive-babel-piedmontese
The package provides the language definition file for support of Piedmontese in
babel. Some shortcuts are defined, as well as translations to Piedmontese of
standard "LaTeX names".

%package -n texlive-babel-romanian
Summary:        Babel support for Romanian
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(romanian.ldf) = %{tl_version}

%description -n texlive-babel-romanian
The package provides the language definition file for support of Romanian in
babel. Translations to Romanian of standard "LaTeX names" are provided.

%package -n texlive-babel-romansh
Summary:        Babel/Polyglossia support for the Romansh language
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(romansh.ldf) = %{tl_version}

%description -n texlive-babel-romansh
The package provides a language description file that enables support of
Romansh either with babel or with polyglossia.

%package -n texlive-babel-samin
Summary:        Babel support for Samin
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(northernsami.ldf) = %{tl_version}
Provides:       tex(samin.ldf) = %{tl_version}

%description -n texlive-babel-samin
The package provides the language definition file for support of North Sami in
babel. (Several Sami dialects/languages are spoken in Finland, Norway, Sweden
and on the Kola Peninsula of Russia). Not all use the same alphabet, and no
attempt is made to support any other than North Sami here. Some shortcuts are
defined, as well as translations to Norsk of standard "LaTeX names".

%package -n texlive-babel-scottish
Summary:        Babel support for Scottish Gaelic
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(scottish.ldf) = %{tl_version}
Provides:       tex(scottishgaelic.ldf) = %{tl_version}

%description -n texlive-babel-scottish
The package provides the language definition file for support of Gaidhlig
(Scottish Gaelic) in babel. Some shortcuts are defined, as well as translations
of standard "LaTeX names".

%package -n texlive-babel-slovenian
Summary:        Babel support for typesetting Slovenian
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(slovene.ldf) = %{tl_version}
Provides:       tex(slovenian.ldf) = %{tl_version}

%description -n texlive-babel-slovenian
The package provides the language definition file for support of Slovenian in
babel. Several shortcuts are defined, as well as translations to Slovenian of
standard "LaTeX names".

%package -n texlive-babel-swedish
Summary:        Babel support for typesetting Swedish
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(swedish.ldf) = %{tl_version}

%description -n texlive-babel-swedish
The package provides the language definition file for Swedish.

%package -n texlive-babel-turkish
Summary:        Babel support for Turkish documents
Version:        svn51560
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(turkish.ldf) = %{tl_version}

%description -n texlive-babel-turkish
The package provides support, within babel, of the Turkish language.

%package -n texlive-babel-welsh
Summary:        Babel support for Welsh
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(welsh.ldf) = %{tl_version}

%description -n texlive-babel-welsh
The package provides the language definition file for Welsh. (Mostly
Welsh-language versions of the standard names in a LaTeX file.)

%package -n texlive-finbib
Summary:        A Finnish version of plain.bst
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-finbib
A Finnish version of plain.bst

%package -n texlive-gloss-occitan
Summary:        Polyglossia support for Occitan
Version:        svn52593
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-gloss-occitan-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-gloss-occitan-doc <= 11:%{version}

%description -n texlive-gloss-occitan
Occitan language description file for polyglossia

%package -n texlive-hrlatex
Summary:        LaTeX support for Croatian documents
Version:        svn18020
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amsopn.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(calc.sty)
Requires:       tex(cancel.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(framed.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(multicol.sty)
Requires:       tex(optional.sty)
Requires:       tex(paralist.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(fsbispit.cls) = %{tl_version}
Provides:       tex(fsbmath.sty) = %{tl_version}
Provides:       tex(hrlatex.sty) = %{tl_version}

%description -n texlive-hrlatex
This package simplifies creation of new documents for the (average) Croatian
user. As an example, a class file hrdipl.cls (designed for the graduation
thesis at the University of Zagreb) and sample thesis documents are included.

%package -n texlive-huaz
Summary:        Automatic Hungarian definite articles and suffixes
Version:        svn77576
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(refcount.sty)
Requires:       tex(xstring.sty)
Provides:       tex(huaz.sty) = %{tl_version}

%description -n texlive-huaz
In Hungarian there are two definite articles, "a" and "az", which are
determined by the pronunciation of the subsequent word. The definite article is
"az", if the first phoneme of the pronounced word is a vowel, otherwise it is
"a". The huaz package helps the user to insert automatically the correct
definite article for cross-references and other commands containing text.
Another service offered by the package is the automatic suffixing of numbers
and cross-references, also based on their pronunciation.

%package -n texlive-hulipsum
Summary:        Hungarian dummy text (Lorum ipse)
Version:        svn77317
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hulipsum.sty) = %{tl_version}

%description -n texlive-hulipsum
Lorem ipsum is an improper Latin filler dummy text, cf. the lipsum package. It
is commonly used for demonstrating the textual elements of a document template.
Lorum ipse is a Hungarian variation of Lorem ipsum. (Lorum is a Hungarian card
game, and ipse is a Hungarian slang word meaning bloke.) With this package you
can typeset 150 paragraphs of Lorum ipse. All paragraphs are taken with
permission from http://www.lorumipse.hu. Thanks to Lorum Ipse Lab (Viktor Nagy
and David Takacs) for their work.

%package -n texlive-hyphen-albanian
Summary:        Albanian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-quote-sq.tex) = %{tl_version}
Provides:       tex(hyph-sq.ec.tex) = %{tl_version}
Provides:       tex(hyph-sq.tex) = %{tl_version}
Provides:       tex(loadhyph-sq.tex) = %{tl_version}

%description -n texlive-hyphen-albanian
Hyphenation patterns for Albanian in UTF-8 and T1 encoding.

%package -n texlive-hyphen-croatian
Summary:        Croatian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-hr.ec.tex) = %{tl_version}
Provides:       tex(hyph-hr.tex) = %{tl_version}
Provides:       tex(loadhyph-hr.tex) = %{tl_version}

%description -n texlive-hyphen-croatian
Hyphenation patterns for Croatian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-danish
Summary:        Danish hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-da.ec.tex) = %{tl_version}
Provides:       tex(hyph-da.tex) = %{tl_version}
Provides:       tex(loadhyph-da.tex) = %{tl_version}

%description -n texlive-hyphen-danish
Hyphenation patterns for Danish in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-dutch
Summary:        Dutch hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-nl.ec.tex) = %{tl_version}
Provides:       tex(hyph-nl.tex) = %{tl_version}
Provides:       tex(loadhyph-nl.tex) = %{tl_version}

%description -n texlive-hyphen-dutch
Hyphenation patterns for Dutch in T1/EC and UTF-8 encodings. These patterns
don't handle cases like 'menuutje' > 'menu-tje', and don't hyphenate words that
have different hyphenations according to their meaning.

%package -n texlive-hyphen-estonian
Summary:        Estonian hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-et.ec.tex) = %{tl_version}
Provides:       tex(hyph-et.tex) = %{tl_version}
Provides:       tex(loadhyph-et.tex) = %{tl_version}

%description -n texlive-hyphen-estonian
Hyphenation patterns for Estonian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-finnish
Summary:        Finnish hyphenation patterns.
Version:        svn73410
License:        LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-fi-x-school.ec.tex) = %{tl_version}
Provides:       tex(hyph-fi-x-school.tex) = %{tl_version}
Provides:       tex(hyph-fi.ec.tex) = %{tl_version}
Provides:       tex(hyph-fi.tex) = %{tl_version}
Provides:       tex(loadhyph-fi-x-school.tex) = %{tl_version}
Provides:       tex(loadhyph-fi.tex) = %{tl_version}

%description -n texlive-hyphen-finnish
Hyphenation patterns for Finnish in T1 and UTF-8 encodings. The older set,
labelled just 'fi', tries to implement etymological rules, while the newer ones
(fi-x-school) implements the simpler rules taught at Finnish school.

%package -n texlive-hyphen-friulan
Summary:        Friulan hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-fur.ec.tex) = %{tl_version}
Provides:       tex(hyph-fur.tex) = %{tl_version}
Provides:       tex(hyph-quote-fur.tex) = %{tl_version}
Provides:       tex(loadhyph-fur.tex) = %{tl_version}

%description -n texlive-hyphen-friulan
Hyphenation patterns for Friulan in ASCII encoding. They are supposed to comply
with the common spelling of the Friulan (Furlan) language as fixed by the
Regional Law N.15/96 dated November 6, 1996 and its following amendments.

%package -n texlive-hyphen-hungarian
Summary:        Hungarian hyphenation patterns.
Version:        svn73410
License:        MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-hu.ec.tex) = %{tl_version}
Provides:       tex(hyph-hu.tex) = %{tl_version}
Provides:       tex(loadhyph-hu.tex) = %{tl_version}

%description -n texlive-hyphen-hungarian
Hyphenation patterns for Hungarian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-icelandic
Summary:        Icelandic hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-is.ec.tex) = %{tl_version}
Provides:       tex(hyph-is.tex) = %{tl_version}
Provides:       tex(loadhyph-is.tex) = %{tl_version}

%description -n texlive-hyphen-icelandic
Hyphenation patterns for Icelandic in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-irish
Summary:        Irish hyphenation patterns.
Version:        svn73410
License:        GPL-2.0-or-later OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ga.ec.tex) = %{tl_version}
Provides:       tex(hyph-ga.tex) = %{tl_version}
Provides:       tex(loadhyph-ga.tex) = %{tl_version}

%description -n texlive-hyphen-irish
Hyphenation patterns for Irish (Gaeilge) in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-kurmanji
Summary:        Kurmanji hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-kmr.ec.tex) = %{tl_version}
Provides:       tex(hyph-kmr.tex) = %{tl_version}
Provides:       tex(loadhyph-kmr.tex) = %{tl_version}

%description -n texlive-hyphen-kurmanji
Hyphenation patterns for Kurmanji (Northern Kurdish) as spoken in Turkey and by
the Kurdish diaspora in Europe, in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-latin
Summary:        Latin hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-la-x-classic.ec.tex) = %{tl_version}
Provides:       tex(hyph-la-x-classic.tex) = %{tl_version}
Provides:       tex(hyph-la-x-liturgic.ec.tex) = %{tl_version}
Provides:       tex(hyph-la-x-liturgic.tex) = %{tl_version}
Provides:       tex(hyph-la.ec.tex) = %{tl_version}
Provides:       tex(hyph-la.tex) = %{tl_version}
Provides:       tex(loadhyph-la-x-classic.tex) = %{tl_version}
Provides:       tex(loadhyph-la-x-liturgic.tex) = %{tl_version}
Provides:       tex(loadhyph-la.tex) = %{tl_version}

%description -n texlive-hyphen-latin
Hyphenation patterns for Latin in T1/EC and UTF-8 encodings, mainly in modern
spelling (u when u is needed and v when v is needed), medieval spelling with
the ligatures \ae and \oe and the (uncial) lowercase 'v' written as a 'u' is
also supported. Apparently there is no conflict between the patterns of modern
Latin and those of medieval Latin. Hyphenation patterns for the Classical Latin
in T1/EC and UTF-8 encodings. Classical Latin hyphenation patterns are
different from those of 'plain' Latin, the latter being more adapted to modern
Latin. Hyphenation patterns for the Liturgical Latin in T1/EC and UTF-8
encodings.

%package -n texlive-hyphen-latvian
Summary:        Latvian hyphenation patterns.
Version:        svn73410
License:        LGPL-2.1-only OR GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-lv.l7x.tex) = %{tl_version}
Provides:       tex(hyph-lv.tex) = %{tl_version}
Provides:       tex(loadhyph-lv.tex) = %{tl_version}

%description -n texlive-hyphen-latvian
Hyphenation patterns for Latvian in L7X and UTF-8 encodings.

%package -n texlive-hyphen-lithuanian
Summary:        Lithuanian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-lt.l7x.tex) = %{tl_version}
Provides:       tex(hyph-lt.tex) = %{tl_version}
Provides:       tex(loadhyph-lt.tex) = %{tl_version}

%description -n texlive-hyphen-lithuanian
Hyphenation patterns for Lithuanian in L7X and UTF-8 encodings. \lefthyphenmin
and \righthyphenmin have to be at least 2.

%package -n texlive-hyphen-macedonian
Summary:        Macedonian hyphenation patterns.
Version:        svn73410
License:        GPL-1.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-mk.macedonian.tex) = %{tl_version}
Provides:       tex(hyph-mk.tex) = %{tl_version}
Provides:       tex(loadhyph-mk.tex) = %{tl_version}

%description -n texlive-hyphen-macedonian
Hyphenation patterns for Macedonian

%package -n texlive-hyphen-norwegian
Summary:        Norwegian Bokmal and Nynorsk hyphenation patterns.
Version:        svn73410
License:        FSFAP
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-nb.ec.tex) = %{tl_version}
Provides:       tex(hyph-nb.tex) = %{tl_version}
Provides:       tex(hyph-nn.ec.tex) = %{tl_version}
Provides:       tex(hyph-nn.tex) = %{tl_version}
Provides:       tex(hyph-no.tex) = %{tl_version}
Provides:       tex(loadhyph-nb.tex) = %{tl_version}
Provides:       tex(loadhyph-nn.tex) = %{tl_version}

%description -n texlive-hyphen-norwegian
Hyphenation patterns for Norwegian Bokmal and Nynorsk in T1/EC and UTF-8
encodings.

%package -n texlive-hyphen-occitan
Summary:        Occitan hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-oc.ec.tex) = %{tl_version}
Provides:       tex(hyph-oc.tex) = %{tl_version}
Provides:       tex(hyph-quote-oc.tex) = %{tl_version}
Provides:       tex(loadhyph-oc.tex) = %{tl_version}

%description -n texlive-hyphen-occitan
Hyphenation patterns for Occitan in T1/EC and UTF-8 encodings. They are
supposed to be valid for all the Occitan variants spoken and written in the
wide area called 'Occitanie' by the French. It ranges from the Val d'Aran
within Catalunya, to the South Western Italian Alps encompassing the southern
half of the French pentagon.

%package -n texlive-hyphen-piedmontese
Summary:        Piedmontese hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-pms.tex) = %{tl_version}
Provides:       tex(hyph-quote-pms.tex) = %{tl_version}
Provides:       tex(loadhyph-pms.tex) = %{tl_version}

%description -n texlive-hyphen-piedmontese
Hyphenation patterns for Piedmontese in ASCII encoding. Compliant with
'Gramatica dla lengua piemonteisa' by Camillo Brero.

%package -n texlive-hyphen-romanian
Summary:        Romanian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ro.ec.tex) = %{tl_version}
Provides:       tex(hyph-ro.tex) = %{tl_version}
Provides:       tex(loadhyph-ro.tex) = %{tl_version}

%description -n texlive-hyphen-romanian
Hyphenation patterns for Romanian in T1/EC and UTF-8 encodings. The UTF-8
patterns use U+0219 for the character 's with comma accent' and U+021B for 't
with comma accent', but we may consider using U+015F and U+0163 as well in the
future. Generated by PatGen2-output hyphen-level 9.

%package -n texlive-hyphen-romansh
Summary:        Romansh hyphenation patterns.
Version:        svn74115
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-rm.ec.tex) = %{tl_version}
Provides:       tex(hyph-rm.tex) = %{tl_version}
Provides:       tex(loadhyph-rm.tex) = %{tl_version}

%description -n texlive-hyphen-romansh
Hyphenation patterns for Romansh. All Romansh idioms and Rumantsch Grischun
taken into account, developed in collaboration with Fundaziun Medias
Rumantschas (Romansh news agency) and Lia Rumantscha (Romansh umbrella
organisation).

%package -n texlive-hyphen-slovenian
Summary:        Slovenian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sl.ec.tex) = %{tl_version}
Provides:       tex(hyph-sl.tex) = %{tl_version}
Provides:       tex(loadhyph-sl.tex) = %{tl_version}

%description -n texlive-hyphen-slovenian
Hyphenation patterns for Slovenian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-swedish
Summary:        Swedish hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sv.ec.tex) = %{tl_version}
Provides:       tex(hyph-sv.tex) = %{tl_version}
Provides:       tex(loadhyph-sv.tex) = %{tl_version}

%description -n texlive-hyphen-swedish
Hyphenation patterns for Swedish in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-turkish
Summary:        Turkish hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-tr.ec.tex) = %{tl_version}
Provides:       tex(hyph-tr.tex) = %{tl_version}
Provides:       tex(loadhyph-tr.tex) = %{tl_version}

%description -n texlive-hyphen-turkish
Hyphenation patterns for Turkish in T1/EC and UTF-8 encodings. Auto-generated
from a script included in the distribution. The patterns for Turkish were first
produced for the Ottoman Texts Project in 1987 and were suitable for both
Modern Turkish and Ottoman Turkish in Latin script, however the required
character set didn't fit into EC encoding, so support for Ottoman Turkish had
to be dropped to keep compatibility with 8-bit engines.

%package -n texlive-hyphen-uppersorbian
Summary:        Upper Sorbian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-hsb.ec.tex) = %{tl_version}
Provides:       tex(hyph-hsb.tex) = %{tl_version}
Provides:       tex(loadhyph-hsb.tex) = %{tl_version}

%description -n texlive-hyphen-uppersorbian
Hyphenation patterns for Upper Sorbian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-welsh
Summary:        Welsh hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-cy.ec.tex) = %{tl_version}
Provides:       tex(hyph-cy.tex) = %{tl_version}
Provides:       tex(loadhyph-cy.tex) = %{tl_version}

%description -n texlive-hyphen-welsh
Hyphenation patterns for Welsh in T1/EC and UTF-8 encodings.

%package -n texlive-kaytannollista-latexia
Summary:        Practical manual for LaTeX (Finnish)
Version:        svn77555
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-kaytannollista-latexia-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-kaytannollista-latexia-doc <= 11:%{version}

%description -n texlive-kaytannollista-latexia
"Kaytannollista Latexia" is a practical manual for LaTeX written in the Finnish
language. The manual covers most of the topics that a typical document author
needs. So it can be a useful guide for beginners as well as a reference manual
for advanced users.

%package -n texlive-lithuanian
Summary:        Lithuanian language support
Version:        svn66461
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cp775.def) = %{tl_version}
Provides:       tex(l7xenc.def) = %{tl_version}
Provides:       tex(l7xenc.sty) = %{tl_version}
Provides:       tex(latin7.def) = %{tl_version}

%description -n texlive-lithuanian
This language support package provides: extra 8-bit encoding L7x used by
fontenc: l7xenc.def, l7xenc.dfu, l7xenc.sty Lithuanian TeX support for URW
family Type1 fonts: map, fd, tfm with L7x encoding extra code page definitions
used by inputenc: cp775.def, latin7.def

%package -n texlive-lshort-dutch
Summary:        Introduction to LaTeX in Dutch
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-dutch-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-dutch-doc <= 11:%{version}

%description -n texlive-lshort-dutch
This is the Dutch (Nederlands) translation of the Short Introduction to
LaTeX2e.

%package -n texlive-lshort-estonian
Summary:        Estonian introduction to LaTeX
Version:        svn39323
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-estonian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-estonian-doc <= 11:%{version}

%description -n texlive-lshort-estonian
This is the Estonian translation of Short Introduction to LaTeX2e.

%package -n texlive-lshort-finnish
Summary:        Finnish introduction to LaTeX
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-finnish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-finnish-doc <= 11:%{version}

%description -n texlive-lshort-finnish
This is the Finnish translation of Short Introduction to LaTeX2e, with added
coverage of Finnish typesetting rules.

%package -n texlive-lshort-slovenian
Summary:        Slovenian translation of lshort
Version:        svn77050
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-slovenian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-slovenian-doc <= 11:%{version}

%description -n texlive-lshort-slovenian
A Slovenian translation of the Not So Short Introduction to LaTeX2e.

%package -n texlive-lshort-turkish
Summary:        Turkish introduction to LaTeX
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-turkish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-turkish-doc <= 11:%{version}

%description -n texlive-lshort-turkish
A Turkish translation of Oetiker's (not so) short introduction.

%package -n texlive-nevelok
Summary:        LaTeX package for automatic definite articles for Hungarian
Version:        svn39029
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xstring.sty)
Provides:       tex(nevelok.sty) = %{tl_version}

%description -n texlive-nevelok
LaTeX package for automatic definite articles for Hungarian

%package -n texlive-rojud
Summary:        A font with the images of the counties of Romania
Version:        svn56895
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Provides:       tex(rojud.sty) = %{tl_version}

%description -n texlive-rojud
This package provides a Type 1 font with images of the 42 counties of Romania,
constructed using a general method which is described in detail in the
documentation. The package name is an abbreviation of "judetele Romaniei" (=
counties of Romania).

%package -n texlive-swebib
Summary:        Swedish bibliography styles
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-swebib
The bundle contains Swedish versions of the standard bibliography styles, and
of the style plainnat. The styles should be functionally equivalent to the
corresponding original styles, apart from the Swedish translations. The styles
do not implement Swedish collation.

%package -n texlive-turkmen
Summary:        Babel support for Turkmen
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(turkmen.ldf) = %{tl_version}

%description -n texlive-turkmen
The package provides support for Turkmen in babel, but integration with babel
is not available.

%post -n texlive-hyphen-albanian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/albanian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "albanian loadhyph-sq.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{albanian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{albanian}{loadhyph-sq.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-albanian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/albanian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{albanian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-croatian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/croatian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "croatian loadhyph-hr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{croatian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{croatian}{loadhyph-hr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-croatian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/croatian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{croatian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-danish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/danish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "danish loadhyph-da.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{danish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{danish}{loadhyph-da.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-danish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/danish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{danish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-dutch
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/dutch.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "dutch loadhyph-nl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{dutch}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{dutch}{loadhyph-nl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-dutch
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/dutch.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{dutch}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-estonian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/estonian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "estonian loadhyph-et.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{estonian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{estonian}{loadhyph-et.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-estonian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/estonian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{estonian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-finnish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/finnish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "finnish loadhyph-fi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{finnish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{finnish}{loadhyph-fi.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/schoolfinnish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "schoolfinnish loadhyph-fi-x-school.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{schoolfinnish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{schoolfinnish}{loadhyph-fi-x-school.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-finnish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/finnish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{finnish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/schoolfinnish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{schoolfinnish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-friulan
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/friulan.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "friulan loadhyph-fur.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{friulan}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{friulan}{loadhyph-fur.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-friulan
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/friulan.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{friulan}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-hungarian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/hungarian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "hungarian loadhyph-hu.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{hungarian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{hungarian}{loadhyph-hu.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-hungarian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/hungarian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{hungarian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-icelandic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/icelandic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "icelandic loadhyph-is.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{icelandic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{icelandic}{loadhyph-is.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-icelandic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/icelandic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{icelandic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-irish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/irish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "irish loadhyph-ga.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{irish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{irish}{loadhyph-ga.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-irish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/irish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{irish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-kurmanji
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/kurmanji.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "kurmanji loadhyph-kmr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{kurmanji}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{kurmanji}{loadhyph-kmr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-kurmanji
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/kurmanji.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{kurmanji}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-latin
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/classiclatin.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "classiclatin loadhyph-la-x-classic.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{classiclatin}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{classiclatin}{loadhyph-la-x-classic.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/latin.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "latin loadhyph-la.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{latin}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{latin}{loadhyph-la.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/liturgicallatin.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "liturgicallatin loadhyph-la-x-liturgic.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{liturgicallatin}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{liturgicallatin}{loadhyph-la-x-liturgic.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-latin
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/classiclatin.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{classiclatin}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/latin.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{latin}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/liturgicallatin.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{liturgicallatin}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-latvian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/latvian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "latvian loadhyph-lv.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{latvian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{latvian}{loadhyph-lv.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-latvian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/latvian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{latvian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-lithuanian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/lithuanian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "lithuanian loadhyph-lt.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{lithuanian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{lithuanian}{loadhyph-lt.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-lithuanian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/lithuanian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{lithuanian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-macedonian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/macedonian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "macedonian loadhyph-mk.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{macedonian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{macedonian}{loadhyph-mk.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-macedonian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/macedonian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{macedonian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-norwegian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/bokmal.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "bokmal loadhyph-nb.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=norwegian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=norwegian" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=norsk.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=norsk" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{bokmal}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{bokmal}{loadhyph-nb.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{norwegian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{norwegian}{loadhyph-nb.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{norsk}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{norsk}{loadhyph-nb.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/nynorsk.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "nynorsk loadhyph-nn.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{nynorsk}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{nynorsk}{loadhyph-nn.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-norwegian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/bokmal.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=norwegian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=norsk.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{bokmal}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{norwegian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{norsk}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/nynorsk.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{nynorsk}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-occitan
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/occitan.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "occitan loadhyph-oc.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{occitan}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{occitan}{loadhyph-oc.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-occitan
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/occitan.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{occitan}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-piedmontese
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/piedmontese.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "piedmontese loadhyph-pms.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{piedmontese}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{piedmontese}{loadhyph-pms.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-piedmontese
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/piedmontese.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{piedmontese}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-romanian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/romanian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "romanian loadhyph-ro.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{romanian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{romanian}{loadhyph-ro.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-romanian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/romanian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{romanian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-romansh
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/romansh.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "romansh loadhyph-rm.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{romansh}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{romansh}{loadhyph-rm.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-romansh
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/romansh.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{romansh}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-slovenian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/slovenian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "slovenian loadhyph-sl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=slovene.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=slovene" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{slovenian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{slovenian}{loadhyph-sl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{slovene}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{slovene}{loadhyph-sl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-slovenian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/slovenian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=slovene.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{slovenian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{slovene}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-swedish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/swedish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "swedish loadhyph-sv.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{swedish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{swedish}{loadhyph-sv.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-swedish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/swedish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{swedish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-turkish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/turkish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "turkish loadhyph-tr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{turkish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{turkish}{loadhyph-tr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-turkish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/turkish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{turkish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-uppersorbian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/uppersorbian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "uppersorbian loadhyph-hsb.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{uppersorbian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{uppersorbian}{loadhyph-hsb.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-uppersorbian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/uppersorbian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{uppersorbian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-welsh
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/welsh.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "welsh loadhyph-cy.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{welsh}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{welsh}{loadhyph-cy.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-welsh
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/welsh.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{welsh}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%prep
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h_expected="%{source2_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h_expected="%{source3_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h_expected="%{source4_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h_expected="%{source5_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h_expected="%{source6_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
test "%{source7_hash}" = "none" || { f="%{SOURCE7}"; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h_expected="%{source7_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source7_hash}" || { echo "oreon: Source7 hash mismatch" >&2; exit 1; }; }
test "%{source8_hash}" = "none" || { f="%{SOURCE8}"; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h_expected="%{source8_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source8_hash}" || { echo "oreon: Source8 hash mismatch" >&2; exit 1; }; }
test "%{source9_hash}" = "none" || { f="%{SOURCE9}"; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h_expected="%{source9_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source9_hash}" || { echo "oreon: Source9 hash mismatch" >&2; exit 1; }; }
test "%{source10_hash}" = "none" || { f="%{SOURCE10}"; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h_expected="%{source10_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source10_hash}" || { echo "oreon: Source10 hash mismatch" >&2; exit 1; }; }
test "%{source11_hash}" = "none" || { f="%{SOURCE11}"; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h_expected="%{source11_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source11_hash}" || { echo "oreon: Source11 hash mismatch" >&2; exit 1; }; }
test "%{source12_hash}" = "none" || { f="%{SOURCE12}"; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h_expected="%{source12_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source12_hash}" || { echo "oreon: Source12 hash mismatch" >&2; exit 1; }; }
test "%{source13_hash}" = "none" || { f="%{SOURCE13}"; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h_expected="%{source13_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source13_hash}" || { echo "oreon: Source13 hash mismatch" >&2; exit 1; }; }
test "%{source14_hash}" = "none" || { f="%{SOURCE14}"; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h_expected="%{source14_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source14_hash}" || { echo "oreon: Source14 hash mismatch" >&2; exit 1; }; }
test "%{source15_hash}" = "none" || { f="%{SOURCE15}"; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h_expected="%{source15_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source15_hash}" || { echo "oreon: Source15 hash mismatch" >&2; exit 1; }; }
test "%{source16_hash}" = "none" || { f="%{SOURCE16}"; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h_expected="%{source16_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source16_hash}" || { echo "oreon: Source16 hash mismatch" >&2; exit 1; }; }
test "%{source17_hash}" = "none" || { f="%{SOURCE17}"; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h_expected="%{source17_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source17_hash}" || { echo "oreon: Source17 hash mismatch" >&2; exit 1; }; }
test "%{source18_hash}" = "none" || { f="%{SOURCE18}"; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h_expected="%{source18_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source18_hash}" || { echo "oreon: Source18 hash mismatch" >&2; exit 1; }; }
test "%{source19_hash}" = "none" || { f="%{SOURCE19}"; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h_expected="%{source19_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source19_hash}" || { echo "oreon: Source19 hash mismatch" >&2; exit 1; }; }
test "%{source20_hash}" = "none" || { f="%{SOURCE20}"; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h_expected="%{source20_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source20_hash}" || { echo "oreon: Source20 hash mismatch" >&2; exit 1; }; }
test "%{source21_hash}" = "none" || { f="%{SOURCE21}"; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h_expected="%{source21_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source21_hash}" || { echo "oreon: Source21 hash mismatch" >&2; exit 1; }; }
test "%{source22_hash}" = "none" || { f="%{SOURCE22}"; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h_expected="%{source22_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source22_hash}" || { echo "oreon: Source22 hash mismatch" >&2; exit 1; }; }
test "%{source23_hash}" = "none" || { f="%{SOURCE23}"; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h_expected="%{source23_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source23_hash}" || { echo "oreon: Source23 hash mismatch" >&2; exit 1; }; }
test "%{source24_hash}" = "none" || { f="%{SOURCE24}"; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h_expected="%{source24_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source24_hash}" || { echo "oreon: Source24 hash mismatch" >&2; exit 1; }; }
test "%{source25_hash}" = "none" || { f="%{SOURCE25}"; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h_expected="%{source25_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source25_hash}" || { echo "oreon: Source25 hash mismatch" >&2; exit 1; }; }
test "%{source26_hash}" = "none" || { f="%{SOURCE26}"; test -f "$f" || { echo "oreon: missing Source26 $f" >&2; exit 1; }; h_expected="%{source26_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source26_hash}" || { echo "oreon: Source26 hash mismatch" >&2; exit 1; }; }
test "%{source27_hash}" = "none" || { f="%{SOURCE27}"; test -f "$f" || { echo "oreon: missing Source27 $f" >&2; exit 1; }; h_expected="%{source27_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source27_hash}" || { echo "oreon: Source27 hash mismatch" >&2; exit 1; }; }
test "%{source28_hash}" = "none" || { f="%{SOURCE28}"; test -f "$f" || { echo "oreon: missing Source28 $f" >&2; exit 1; }; h_expected="%{source28_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source28_hash}" || { echo "oreon: Source28 hash mismatch" >&2; exit 1; }; }
test "%{source29_hash}" = "none" || { f="%{SOURCE29}"; test -f "$f" || { echo "oreon: missing Source29 $f" >&2; exit 1; }; h_expected="%{source29_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source29_hash}" || { echo "oreon: Source29 hash mismatch" >&2; exit 1; }; }
test "%{source30_hash}" = "none" || { f="%{SOURCE30}"; test -f "$f" || { echo "oreon: missing Source30 $f" >&2; exit 1; }; h_expected="%{source30_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source30_hash}" || { echo "oreon: Source30 hash mismatch" >&2; exit 1; }; }
test "%{source31_hash}" = "none" || { f="%{SOURCE31}"; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h_expected="%{source31_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source31_hash}" || { echo "oreon: Source31 hash mismatch" >&2; exit 1; }; }
test "%{source32_hash}" = "none" || { f="%{SOURCE32}"; test -f "$f" || { echo "oreon: missing Source32 $f" >&2; exit 1; }; h_expected="%{source32_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source32_hash}" || { echo "oreon: Source32 hash mismatch" >&2; exit 1; }; }
test "%{source33_hash}" = "none" || { f="%{SOURCE33}"; test -f "$f" || { echo "oreon: missing Source33 $f" >&2; exit 1; }; h_expected="%{source33_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source33_hash}" || { echo "oreon: Source33 hash mismatch" >&2; exit 1; }; }
test "%{source34_hash}" = "none" || { f="%{SOURCE34}"; test -f "$f" || { echo "oreon: missing Source34 $f" >&2; exit 1; }; h_expected="%{source34_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source34_hash}" || { echo "oreon: Source34 hash mismatch" >&2; exit 1; }; }
test "%{source35_hash}" = "none" || { f="%{SOURCE35}"; test -f "$f" || { echo "oreon: missing Source35 $f" >&2; exit 1; }; h_expected="%{source35_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source35_hash}" || { echo "oreon: Source35 hash mismatch" >&2; exit 1; }; }
test "%{source36_hash}" = "none" || { f="%{SOURCE36}"; test -f "$f" || { echo "oreon: missing Source36 $f" >&2; exit 1; }; h_expected="%{source36_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source36_hash}" || { echo "oreon: Source36 hash mismatch" >&2; exit 1; }; }
test "%{source37_hash}" = "none" || { f="%{SOURCE37}"; test -f "$f" || { echo "oreon: missing Source37 $f" >&2; exit 1; }; h_expected="%{source37_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source37_hash}" || { echo "oreon: Source37 hash mismatch" >&2; exit 1; }; }
test "%{source38_hash}" = "none" || { f="%{SOURCE38}"; test -f "$f" || { echo "oreon: missing Source38 $f" >&2; exit 1; }; h_expected="%{source38_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source38_hash}" || { echo "oreon: Source38 hash mismatch" >&2; exit 1; }; }
test "%{source39_hash}" = "none" || { f="%{SOURCE39}"; test -f "$f" || { echo "oreon: missing Source39 $f" >&2; exit 1; }; h_expected="%{source39_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source39_hash}" || { echo "oreon: Source39 hash mismatch" >&2; exit 1; }; }
test "%{source40_hash}" = "none" || { f="%{SOURCE40}"; test -f "$f" || { echo "oreon: missing Source40 $f" >&2; exit 1; }; h_expected="%{source40_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source40_hash}" || { echo "oreon: Source40 hash mismatch" >&2; exit 1; }; }
test "%{source41_hash}" = "none" || { f="%{SOURCE41}"; test -f "$f" || { echo "oreon: missing Source41 $f" >&2; exit 1; }; h_expected="%{source41_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source41_hash}" || { echo "oreon: Source41 hash mismatch" >&2; exit 1; }; }
test "%{source42_hash}" = "none" || { f="%{SOURCE42}"; test -f "$f" || { echo "oreon: missing Source42 $f" >&2; exit 1; }; h_expected="%{source42_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source42_hash}" || { echo "oreon: Source42 hash mismatch" >&2; exit 1; }; }
test "%{source43_hash}" = "none" || { f="%{SOURCE43}"; test -f "$f" || { echo "oreon: missing Source43 $f" >&2; exit 1; }; h_expected="%{source43_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source43_hash}" || { echo "oreon: Source43 hash mismatch" >&2; exit 1; }; }
test "%{source44_hash}" = "none" || { f="%{SOURCE44}"; test -f "$f" || { echo "oreon: missing Source44 $f" >&2; exit 1; }; h_expected="%{source44_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source44_hash}" || { echo "oreon: Source44 hash mismatch" >&2; exit 1; }; }
test "%{source45_hash}" = "none" || { f="%{SOURCE45}"; test -f "$f" || { echo "oreon: missing Source45 $f" >&2; exit 1; }; h_expected="%{source45_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source45_hash}" || { echo "oreon: Source45 hash mismatch" >&2; exit 1; }; }
test "%{source46_hash}" = "none" || { f="%{SOURCE46}"; test -f "$f" || { echo "oreon: missing Source46 $f" >&2; exit 1; }; h_expected="%{source46_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source46_hash}" || { echo "oreon: Source46 hash mismatch" >&2; exit 1; }; }
test "%{source47_hash}" = "none" || { f="%{SOURCE47}"; test -f "$f" || { echo "oreon: missing Source47 $f" >&2; exit 1; }; h_expected="%{source47_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source47_hash}" || { echo "oreon: Source47 hash mismatch" >&2; exit 1; }; }
test "%{source48_hash}" = "none" || { f="%{SOURCE48}"; test -f "$f" || { echo "oreon: missing Source48 $f" >&2; exit 1; }; h_expected="%{source48_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source48_hash}" || { echo "oreon: Source48 hash mismatch" >&2; exit 1; }; }
test "%{source49_hash}" = "none" || { f="%{SOURCE49}"; test -f "$f" || { echo "oreon: missing Source49 $f" >&2; exit 1; }; h_expected="%{source49_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source49_hash}" || { echo "oreon: Source49 hash mismatch" >&2; exit 1; }; }
test "%{source50_hash}" = "none" || { f="%{SOURCE50}"; test -f "$f" || { echo "oreon: missing Source50 $f" >&2; exit 1; }; h_expected="%{source50_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source50_hash}" || { echo "oreon: Source50 hash mismatch" >&2; exit 1; }; }
test "%{source51_hash}" = "none" || { f="%{SOURCE51}"; test -f "$f" || { echo "oreon: missing Source51 $f" >&2; exit 1; }; h_expected="%{source51_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source51_hash}" || { echo "oreon: Source51 hash mismatch" >&2; exit 1; }; }
test "%{source52_hash}" = "none" || { f="%{SOURCE52}"; test -f "$f" || { echo "oreon: missing Source52 $f" >&2; exit 1; }; h_expected="%{source52_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source52_hash}" || { echo "oreon: Source52 hash mismatch" >&2; exit 1; }; }
test "%{source53_hash}" = "none" || { f="%{SOURCE53}"; test -f "$f" || { echo "oreon: missing Source53 $f" >&2; exit 1; }; h_expected="%{source53_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source53_hash}" || { echo "oreon: Source53 hash mismatch" >&2; exit 1; }; }
test "%{source54_hash}" = "none" || { f="%{SOURCE54}"; test -f "$f" || { echo "oreon: missing Source54 $f" >&2; exit 1; }; h_expected="%{source54_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source54_hash}" || { echo "oreon: Source54 hash mismatch" >&2; exit 1; }; }
test "%{source55_hash}" = "none" || { f="%{SOURCE55}"; test -f "$f" || { echo "oreon: missing Source55 $f" >&2; exit 1; }; h_expected="%{source55_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source55_hash}" || { echo "oreon: Source55 hash mismatch" >&2; exit 1; }; }
test "%{source56_hash}" = "none" || { f="%{SOURCE56}"; test -f "$f" || { echo "oreon: missing Source56 $f" >&2; exit 1; }; h_expected="%{source56_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source56_hash}" || { echo "oreon: Source56 hash mismatch" >&2; exit 1; }; }
test "%{source57_hash}" = "none" || { f="%{SOURCE57}"; test -f "$f" || { echo "oreon: missing Source57 $f" >&2; exit 1; }; h_expected="%{source57_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source57_hash}" || { echo "oreon: Source57 hash mismatch" >&2; exit 1; }; }
test "%{source58_hash}" = "none" || { f="%{SOURCE58}"; test -f "$f" || { echo "oreon: missing Source58 $f" >&2; exit 1; }; h_expected="%{source58_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source58_hash}" || { echo "oreon: Source58 hash mismatch" >&2; exit 1; }; }
test "%{source59_hash}" = "none" || { f="%{SOURCE59}"; test -f "$f" || { echo "oreon: missing Source59 $f" >&2; exit 1; }; h_expected="%{source59_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source59_hash}" || { echo "oreon: Source59 hash mismatch" >&2; exit 1; }; }
test "%{source60_hash}" = "none" || { f="%{SOURCE60}"; test -f "$f" || { echo "oreon: missing Source60 $f" >&2; exit 1; }; h_expected="%{source60_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source60_hash}" || { echo "oreon: Source60 hash mismatch" >&2; exit 1; }; }
test "%{source61_hash}" = "none" || { f="%{SOURCE61}"; test -f "$f" || { echo "oreon: missing Source61 $f" >&2; exit 1; }; h_expected="%{source61_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source61_hash}" || { echo "oreon: Source61 hash mismatch" >&2; exit 1; }; }
test "%{source62_hash}" = "none" || { f="%{SOURCE62}"; test -f "$f" || { echo "oreon: missing Source62 $f" >&2; exit 1; }; h_expected="%{source62_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source62_hash}" || { echo "oreon: Source62 hash mismatch" >&2; exit 1; }; }
test "%{source63_hash}" = "none" || { f="%{SOURCE63}"; test -f "$f" || { echo "oreon: missing Source63 $f" >&2; exit 1; }; h_expected="%{source63_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source63_hash}" || { echo "oreon: Source63 hash mismatch" >&2; exit 1; }; }
test "%{source64_hash}" = "none" || { f="%{SOURCE64}"; test -f "$f" || { echo "oreon: missing Source64 $f" >&2; exit 1; }; h_expected="%{source64_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source64_hash}" || { echo "oreon: Source64 hash mismatch" >&2; exit 1; }; }
test "%{source65_hash}" = "none" || { f="%{SOURCE65}"; test -f "$f" || { echo "oreon: missing Source65 $f" >&2; exit 1; }; h_expected="%{source65_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source65_hash}" || { echo "oreon: Source65 hash mismatch" >&2; exit 1; }; }
test "%{source66_hash}" = "none" || { f="%{SOURCE66}"; test -f "$f" || { echo "oreon: missing Source66 $f" >&2; exit 1; }; h_expected="%{source66_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source66_hash}" || { echo "oreon: Source66 hash mismatch" >&2; exit 1; }; }
test "%{source67_hash}" = "none" || { f="%{SOURCE67}"; test -f "$f" || { echo "oreon: missing Source67 $f" >&2; exit 1; }; h_expected="%{source67_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source67_hash}" || { echo "oreon: Source67 hash mismatch" >&2; exit 1; }; }
test "%{source68_hash}" = "none" || { f="%{SOURCE68}"; test -f "$f" || { echo "oreon: missing Source68 $f" >&2; exit 1; }; h_expected="%{source68_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source68_hash}" || { echo "oreon: Source68 hash mismatch" >&2; exit 1; }; }
test "%{source69_hash}" = "none" || { f="%{SOURCE69}"; test -f "$f" || { echo "oreon: missing Source69 $f" >&2; exit 1; }; h_expected="%{source69_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source69_hash}" || { echo "oreon: Source69 hash mismatch" >&2; exit 1; }; }
test "%{source70_hash}" = "none" || { f="%{SOURCE70}"; test -f "$f" || { echo "oreon: missing Source70 $f" >&2; exit 1; }; h_expected="%{source70_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source70_hash}" || { echo "oreon: Source70 hash mismatch" >&2; exit 1; }; }
test "%{source71_hash}" = "none" || { f="%{SOURCE71}"; test -f "$f" || { echo "oreon: missing Source71 $f" >&2; exit 1; }; h_expected="%{source71_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source71_hash}" || { echo "oreon: Source71 hash mismatch" >&2; exit 1; }; }
test "%{source72_hash}" = "none" || { f="%{SOURCE72}"; test -f "$f" || { echo "oreon: missing Source72 $f" >&2; exit 1; }; h_expected="%{source72_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source72_hash}" || { echo "oreon: Source72 hash mismatch" >&2; exit 1; }; }
test "%{source73_hash}" = "none" || { f="%{SOURCE73}"; test -f "$f" || { echo "oreon: missing Source73 $f" >&2; exit 1; }; h_expected="%{source73_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source73_hash}" || { echo "oreon: Source73 hash mismatch" >&2; exit 1; }; }
test "%{source74_hash}" = "none" || { f="%{SOURCE74}"; test -f "$f" || { echo "oreon: missing Source74 $f" >&2; exit 1; }; h_expected="%{source74_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source74_hash}" || { echo "oreon: Source74 hash mismatch" >&2; exit 1; }; }
test "%{source75_hash}" = "none" || { f="%{SOURCE75}"; test -f "$f" || { echo "oreon: missing Source75 $f" >&2; exit 1; }; h_expected="%{source75_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source75_hash}" || { echo "oreon: Source75 hash mismatch" >&2; exit 1; }; }
test "%{source76_hash}" = "none" || { f="%{SOURCE76}"; test -f "$f" || { echo "oreon: missing Source76 $f" >&2; exit 1; }; h_expected="%{source76_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source76_hash}" || { echo "oreon: Source76 hash mismatch" >&2; exit 1; }; }
test "%{source77_hash}" = "none" || { f="%{SOURCE77}"; test -f "$f" || { echo "oreon: missing Source77 $f" >&2; exit 1; }; h_expected="%{source77_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source77_hash}" || { echo "oreon: Source77 hash mismatch" >&2; exit 1; }; }
test "%{source78_hash}" = "none" || { f="%{SOURCE78}"; test -f "$f" || { echo "oreon: missing Source78 $f" >&2; exit 1; }; h_expected="%{source78_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source78_hash}" || { echo "oreon: Source78 hash mismatch" >&2; exit 1; }; }
test "%{source79_hash}" = "none" || { f="%{SOURCE79}"; test -f "$f" || { echo "oreon: missing Source79 $f" >&2; exit 1; }; h_expected="%{source79_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source79_hash}" || { echo "oreon: Source79 hash mismatch" >&2; exit 1; }; }
test "%{source80_hash}" = "none" || { f="%{SOURCE80}"; test -f "$f" || { echo "oreon: missing Source80 $f" >&2; exit 1; }; h_expected="%{source80_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source80_hash}" || { echo "oreon: Source80 hash mismatch" >&2; exit 1; }; }
test "%{source81_hash}" = "none" || { f="%{SOURCE81}"; test -f "$f" || { echo "oreon: missing Source81 $f" >&2; exit 1; }; h_expected="%{source81_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source81_hash}" || { echo "oreon: Source81 hash mismatch" >&2; exit 1; }; }
test "%{source82_hash}" = "none" || { f="%{SOURCE82}"; test -f "$f" || { echo "oreon: missing Source82 $f" >&2; exit 1; }; h_expected="%{source82_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source82_hash}" || { echo "oreon: Source82 hash mismatch" >&2; exit 1; }; }
test "%{source83_hash}" = "none" || { f="%{SOURCE83}"; test -f "$f" || { echo "oreon: missing Source83 $f" >&2; exit 1; }; h_expected="%{source83_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source83_hash}" || { echo "oreon: Source83 hash mismatch" >&2; exit 1; }; }
test "%{source84_hash}" = "none" || { f="%{SOURCE84}"; test -f "$f" || { echo "oreon: missing Source84 $f" >&2; exit 1; }; h_expected="%{source84_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source84_hash}" || { echo "oreon: Source84 hash mismatch" >&2; exit 1; }; }
test "%{source85_hash}" = "none" || { f="%{SOURCE85}"; test -f "$f" || { echo "oreon: missing Source85 $f" >&2; exit 1; }; h_expected="%{source85_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source85_hash}" || { echo "oreon: Source85 hash mismatch" >&2; exit 1; }; }
test "%{source86_hash}" = "none" || { f="%{SOURCE86}"; test -f "$f" || { echo "oreon: missing Source86 $f" >&2; exit 1; }; h_expected="%{source86_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source86_hash}" || { echo "oreon: Source86 hash mismatch" >&2; exit 1; }; }
test "%{source87_hash}" = "none" || { f="%{SOURCE87}"; test -f "$f" || { echo "oreon: missing Source87 $f" >&2; exit 1; }; h_expected="%{source87_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source87_hash}" || { echo "oreon: Source87 hash mismatch" >&2; exit 1; }; }
test "%{source88_hash}" = "none" || { f="%{SOURCE88}"; test -f "$f" || { echo "oreon: missing Source88 $f" >&2; exit 1; }; h_expected="%{source88_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source88_hash}" || { echo "oreon: Source88 hash mismatch" >&2; exit 1; }; }
test "%{source89_hash}" = "none" || { f="%{SOURCE89}"; test -f "$f" || { echo "oreon: missing Source89 $f" >&2; exit 1; }; h_expected="%{source89_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source89_hash}" || { echo "oreon: Source89 hash mismatch" >&2; exit 1; }; }
test "%{source90_hash}" = "none" || { f="%{SOURCE90}"; test -f "$f" || { echo "oreon: missing Source90 $f" >&2; exit 1; }; h_expected="%{source90_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source90_hash}" || { echo "oreon: Source90 hash mismatch" >&2; exit 1; }; }
test "%{source91_hash}" = "none" || { f="%{SOURCE91}"; test -f "$f" || { echo "oreon: missing Source91 $f" >&2; exit 1; }; h_expected="%{source91_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source91_hash}" || { echo "oreon: Source91 hash mismatch" >&2; exit 1; }; }
test "%{source92_hash}" = "none" || { f="%{SOURCE92}"; test -f "$f" || { echo "oreon: missing Source92 $f" >&2; exit 1; }; h_expected="%{source92_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source92_hash}" || { echo "oreon: Source92 hash mismatch" >&2; exit 1; }; }
test "%{source93_hash}" = "none" || { f="%{SOURCE93}"; test -f "$f" || { echo "oreon: missing Source93 $f" >&2; exit 1; }; h_expected="%{source93_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source93_hash}" || { echo "oreon: Source93 hash mismatch" >&2; exit 1; }; }
test "%{source94_hash}" = "none" || { f="%{SOURCE94}"; test -f "$f" || { echo "oreon: missing Source94 $f" >&2; exit 1; }; h_expected="%{source94_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source94_hash}" || { echo "oreon: Source94 hash mismatch" >&2; exit 1; }; }
test "%{source95_hash}" = "none" || { f="%{SOURCE95}"; test -f "$f" || { echo "oreon: missing Source95 $f" >&2; exit 1; }; h_expected="%{source95_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source95_hash}" || { echo "oreon: Source95 hash mismatch" >&2; exit 1; }; }
test "%{source96_hash}" = "none" || { f="%{SOURCE96}"; test -f "$f" || { echo "oreon: missing Source96 $f" >&2; exit 1; }; h_expected="%{source96_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source96_hash}" || { echo "oreon: Source96 hash mismatch" >&2; exit 1; }; }
test "%{source97_hash}" = "none" || { f="%{SOURCE97}"; test -f "$f" || { echo "oreon: missing Source97 $f" >&2; exit 1; }; h_expected="%{source97_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source97_hash}" || { echo "oreon: Source97 hash mismatch" >&2; exit 1; }; }
test "%{source98_hash}" = "none" || { f="%{SOURCE98}"; test -f "$f" || { echo "oreon: missing Source98 $f" >&2; exit 1; }; h_expected="%{source98_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source98_hash}" || { echo "oreon: Source98 hash mismatch" >&2; exit 1; }; }
test "%{source99_hash}" = "none" || { f="%{SOURCE99}"; test -f "$f" || { echo "oreon: missing Source99 $f" >&2; exit 1; }; h_expected="%{source99_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source99_hash}" || { echo "oreon: Source99 hash mismatch" >&2; exit 1; }; }
test "%{source100_hash}" = "none" || { f="%{SOURCE100}"; test -f "$f" || { echo "oreon: missing Source100 $f" >&2; exit 1; }; h_expected="%{source100_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source100_hash}" || { echo "oreon: Source100 hash mismatch" >&2; exit 1; }; }
test "%{source101_hash}" = "none" || { f="%{SOURCE101}"; test -f "$f" || { echo "oreon: missing Source101 $f" >&2; exit 1; }; h_expected="%{source101_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source101_hash}" || { echo "oreon: Source101 hash mismatch" >&2; exit 1; }; }
test "%{source102_hash}" = "none" || { f="%{SOURCE102}"; test -f "$f" || { echo "oreon: missing Source102 $f" >&2; exit 1; }; h_expected="%{source102_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source102_hash}" || { echo "oreon: Source102 hash mismatch" >&2; exit 1; }; }
test "%{source103_hash}" = "none" || { f="%{SOURCE103}"; test -f "$f" || { echo "oreon: missing Source103 $f" >&2; exit 1; }; h_expected="%{source103_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source103_hash}" || { echo "oreon: Source103 hash mismatch" >&2; exit 1; }; }
test "%{source104_hash}" = "none" || { f="%{SOURCE104}"; test -f "$f" || { echo "oreon: missing Source104 $f" >&2; exit 1; }; h_expected="%{source104_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source104_hash}" || { echo "oreon: Source104 hash mismatch" >&2; exit 1; }; }
test "%{source105_hash}" = "none" || { f="%{SOURCE105}"; test -f "$f" || { echo "oreon: missing Source105 $f" >&2; exit 1; }; h_expected="%{source105_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source105_hash}" || { echo "oreon: Source105 hash mismatch" >&2; exit 1; }; }
test "%{source106_hash}" = "none" || { f="%{SOURCE106}"; test -f "$f" || { echo "oreon: missing Source106 $f" >&2; exit 1; }; h_expected="%{source106_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source106_hash}" || { echo "oreon: Source106 hash mismatch" >&2; exit 1; }; }
test "%{source107_hash}" = "none" || { f="%{SOURCE107}"; test -f "$f" || { echo "oreon: missing Source107 $f" >&2; exit 1; }; h_expected="%{source107_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source107_hash}" || { echo "oreon: Source107 hash mismatch" >&2; exit 1; }; }
test "%{source108_hash}" = "none" || { f="%{SOURCE108}"; test -f "$f" || { echo "oreon: missing Source108 $f" >&2; exit 1; }; h_expected="%{source108_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source108_hash}" || { echo "oreon: Source108 hash mismatch" >&2; exit 1; }; }
test "%{source109_hash}" = "none" || { f="%{SOURCE109}"; test -f "$f" || { echo "oreon: missing Source109 $f" >&2; exit 1; }; h_expected="%{source109_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source109_hash}" || { echo "oreon: Source109 hash mismatch" >&2; exit 1; }; }
test "%{source110_hash}" = "none" || { f="%{SOURCE110}"; test -f "$f" || { echo "oreon: missing Source110 $f" >&2; exit 1; }; h_expected="%{source110_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source110_hash}" || { echo "oreon: Source110 hash mismatch" >&2; exit 1; }; }
test "%{source111_hash}" = "none" || { f="%{SOURCE111}"; test -f "$f" || { echo "oreon: missing Source111 $f" >&2; exit 1; }; h_expected="%{source111_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source111_hash}" || { echo "oreon: Source111 hash mismatch" >&2; exit 1; }; }
test "%{source112_hash}" = "none" || { f="%{SOURCE112}"; test -f "$f" || { echo "oreon: missing Source112 $f" >&2; exit 1; }; h_expected="%{source112_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source112_hash}" || { echo "oreon: Source112 hash mismatch" >&2; exit 1; }; }
test "%{source113_hash}" = "none" || { f="%{SOURCE113}"; test -f "$f" || { echo "oreon: missing Source113 $f" >&2; exit 1; }; h_expected="%{source113_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source113_hash}" || { echo "oreon: Source113 hash mismatch" >&2; exit 1; }; }
test "%{source114_hash}" = "none" || { f="%{SOURCE114}"; test -f "$f" || { echo "oreon: missing Source114 $f" >&2; exit 1; }; h_expected="%{source114_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source114_hash}" || { echo "oreon: Source114 hash mismatch" >&2; exit 1; }; }
test "%{source115_hash}" = "none" || { f="%{SOURCE115}"; test -f "$f" || { echo "oreon: missing Source115 $f" >&2; exit 1; }; h_expected="%{source115_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source115_hash}" || { echo "oreon: Source115 hash mismatch" >&2; exit 1; }; }
test "%{source116_hash}" = "none" || { f="%{SOURCE116}"; test -f "$f" || { echo "oreon: missing Source116 $f" >&2; exit 1; }; h_expected="%{source116_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source116_hash}" || { echo "oreon: Source116 hash mismatch" >&2; exit 1; }; }
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-armtex
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/armenian/
%{_texmf_main}/fonts/map/dvips/armenian/
%{_texmf_main}/fonts/source/public/armenian/
%{_texmf_main}/fonts/tfm/public/armenian/
%{_texmf_main}/fonts/type1/public/armenian/
%{_texmf_main}/tex/latex/armenian/
%{_texmf_main}/tex/plain/armenian/
%doc %{_texmf_main}/doc/generic/armenian/

%files -n texlive-babel-albanian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-albanian/
%doc %{_texmf_main}/doc/generic/babel-albanian/

%files -n texlive-babel-bosnian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-bosnian/
%doc %{_texmf_main}/doc/generic/babel-bosnian/

%files -n texlive-babel-breton
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-breton/
%doc %{_texmf_main}/doc/generic/babel-breton/

%files -n texlive-babel-croatian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-croatian/
%doc %{_texmf_main}/doc/generic/babel-croatian/

%files -n texlive-babel-danish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-danish/
%doc %{_texmf_main}/doc/generic/babel-danish/

%files -n texlive-babel-dutch
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-dutch/
%doc %{_texmf_main}/doc/generic/babel-dutch/

%files -n texlive-babel-estonian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-estonian/
%doc %{_texmf_main}/doc/generic/babel-estonian/

%files -n texlive-babel-finnish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-finnish/
%doc %{_texmf_main}/doc/generic/babel-finnish/

%files -n texlive-babel-friulan
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-friulan/
%doc %{_texmf_main}/doc/generic/babel-friulan/

%files -n texlive-babel-hungarian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-hungarian/
%doc %{_texmf_main}/doc/generic/babel-hungarian/

%files -n texlive-babel-icelandic
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-icelandic/
%doc %{_texmf_main}/doc/generic/babel-icelandic/

%files -n texlive-babel-irish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-irish/
%doc %{_texmf_main}/doc/generic/babel-irish/

%files -n texlive-babel-kurmanji
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-kurmanji/
%doc %{_texmf_main}/doc/generic/babel-kurmanji/

%files -n texlive-babel-latin
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-latin/
%doc %{_texmf_main}/doc/generic/babel-latin/

%files -n texlive-babel-latvian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-latvian/
%doc %{_texmf_main}/doc/generic/babel-latvian/

%files -n texlive-babel-lithuanian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-lithuanian/
%doc %{_texmf_main}/doc/generic/babel-lithuanian/

%files -n texlive-babel-macedonian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-macedonian/
%doc %{_texmf_main}/doc/generic/babel-macedonian/

%files -n texlive-babel-norsk
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-norsk/
%doc %{_texmf_main}/doc/generic/babel-norsk/

%files -n texlive-babel-occitan
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-occitan/
%doc %{_texmf_main}/doc/generic/babel-occitan/

%files -n texlive-babel-piedmontese
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-piedmontese/
%doc %{_texmf_main}/doc/generic/babel-piedmontese/

%files -n texlive-babel-romanian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-romanian/
%doc %{_texmf_main}/doc/generic/babel-romanian/

%files -n texlive-babel-romansh
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-romansh/
%doc %{_texmf_main}/doc/generic/babel-romansh/

%files -n texlive-babel-samin
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-samin/
%doc %{_texmf_main}/doc/generic/babel-samin/

%files -n texlive-babel-scottish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-scottish/
%doc %{_texmf_main}/doc/generic/babel-scottish/

%files -n texlive-babel-slovenian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-slovenian/
%doc %{_texmf_main}/doc/generic/babel-slovenian/

%files -n texlive-babel-swedish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-swedish/
%doc %{_texmf_main}/doc/generic/babel-swedish/

%files -n texlive-babel-turkish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-turkish/
%doc %{_texmf_main}/doc/generic/babel-turkish/

%files -n texlive-babel-welsh
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-welsh/
%doc %{_texmf_main}/doc/generic/babel-welsh/

%files -n texlive-finbib
%license other-free.txt
%{_texmf_main}/bibtex/bst/finbib/

%files -n texlive-gloss-occitan
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/gloss-occitan/

%files -n texlive-hrlatex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hrlatex/
%doc %{_texmf_main}/doc/latex/hrlatex/

%files -n texlive-huaz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/huaz/
%doc %{_texmf_main}/doc/latex/huaz/

%files -n texlive-hulipsum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hulipsum/
%doc %{_texmf_main}/doc/latex/hulipsum/

%files -n texlive-hyphen-albanian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-croatian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-danish
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-dutch
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-estonian
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-finnish
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-friulan
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-hungarian
%license other-free.txt
%license gpl2.txt
%license lgpl2.1.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%doc %{_texmf_main}/doc/generic/huhyphen/
%doc %{_texmf_main}/doc/generic/hyph-utf8/

%files -n texlive-hyphen-icelandic
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-irish
%license gpl2.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-kurmanji
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-latin
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-latvian
%license lgpl2.1.txt
%license gpl2.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-lithuanian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-macedonian
%license gpl.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-norwegian
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-occitan
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-piedmontese
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-romanian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-romansh
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-slovenian
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-swedish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-turkish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-uppersorbian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-welsh
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-kaytannollista-latexia
%license cc-by-sa-4.txt
%doc %{_texmf_main}/doc/latex/kaytannollista-latexia/

%files -n texlive-lithuanian
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/lithuanian/
%{_texmf_main}/fonts/map/dvips/lithuanian/
%{_texmf_main}/fonts/tfm/public/lithuanian/
%{_texmf_main}/tex/latex/lithuanian/
%doc %{_texmf_main}/doc/latex/lithuanian/

%files -n texlive-lshort-dutch
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-dutch/

%files -n texlive-lshort-estonian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-estonian/

%files -n texlive-lshort-finnish
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-finnish/

%files -n texlive-lshort-slovenian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-slovenian/

%files -n texlive-lshort-turkish
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-turkish/

%files -n texlive-nevelok
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nevelok/
%doc %{_texmf_main}/doc/latex/nevelok/

%files -n texlive-rojud
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/rojud/
%{_texmf_main}/fonts/tfm/public/rojud/
%{_texmf_main}/fonts/type1/public/rojud/
%{_texmf_main}/tex/latex/rojud/
%doc %{_texmf_main}/doc/fonts/rojud/

%files -n texlive-swebib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/swebib/
%doc %{_texmf_main}/doc/latex/swebib/

%files -n texlive-turkmen
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/turkmen/
%doc %{_texmf_main}/doc/latex/turkmen/

%changelog
%autochangelog
