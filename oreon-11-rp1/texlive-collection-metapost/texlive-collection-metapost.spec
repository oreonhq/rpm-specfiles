%global source0_hash 039445d3317551f8cc0f1bf1ec9b8aa9e8510465020a400e931ccbeffaaaaa88e28a755c437266f6836293cbca02b443a5bbd646a7f558cf43e5384705645ddf

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-metapost
Epoch:          12
Version:        svn73627
Release:        3%{?dist}
Summary:        MetaPost and Metafont packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 09026f967084d5f1804a32166e854ac410a768f6b4654d9ea9bb69dd29acb8a3199919daa1fd6dd48963ea5d6454b9b9d8263939e5af81a8f07f66f08b5f4835
%global source3_hash 49c6515e979a87ce270d32b367c5800acffa4b638a8bed3e20f3e74387c2e7ee4ae0c2ea8b232e2ae57d0d0a730424d18911835581c0c274732f3d36f650693b
%global source4_hash ac7fff708b3e25312460a740241ed003ee471f84dd4d30388d9cde8380ec9a6b6fa6fd6aba69b170c464a25bec44f1669fabc4ac2d7d3e216885b7e683f88af6
%global source5_hash 9e4561e97ea77c84e3c1cc8f75ca61318937c45b7b50dab66d6745f61725b6397458a05e50a267937bf6db4b28558ff0e9f2225078b9516fe574620982ab2cb4
%global source6_hash 86bd39051095fde2a99b232b1139c4c196467d0e1825b3c1c73bd25551a55edb6417a0810b20c4ac3d53ff82519364f2ac72fde3845a750396a4f6a8966c73ef
%global source7_hash 01fc4226a952c76b52726d1217649d9d98ec708163e4a9b997e36f505b385ed145182bca747a2b5334cfe8b4663d010a699664728c5be05cc4daba63ff1f3c00
%global source8_hash e57e7a249f36cc47eab12eb5c85ce6bd31b7790c4030f9412b6f749c0dbe06a8c654811d880c895cd1b6f0c5011e617d70fcaaa75e1d9a59861fc61274682630
%global source9_hash ec5d16885bdc824cfaf0e5185698c906a709991e7ba611c41191763c7a54f67fdb17adc7f27985c76d77f7644ac485eec20df0767c9a4b5845aef9632c1fa95b
%global source10_hash 5f56f9ab77b2f250aff664b0007aa17eccad96d6f674ae7417f610b62d84123fc85bc80cf83948e0df2a7bfb721300e149fc764b03638e5005cc4832f2fa5544
%global source11_hash 0bc738eb48fc34b7cb35240622925d43e5ff5fce21b1c560158b2ceee2790a284b33816fd192a5b0161544ee5add98f4e3ebe7dd0165273d53e5ea2de7d994ac
%global source12_hash b7f2b56f305d552bd857a5950fad2dadbf800857d4c8ee411fd2f5786697385404fce3956e59b5928ed5f0a688117dd740c0f56806674d08cd8cb1d52b79a9d8
%global source13_hash a79d9883615568bd6c0d5aac44cc2ce28e0bd08e96f802d500515428ffb5400beadea94347abab7752904ae01342049b8d6687f6047aa9d8b27f5fe3a647bd02
%global source14_hash dc09380d453b2c83359fa1862f6d289162ed4ec12e7f1b2842789db26e780713981261369dee0d03561a6864bb8bb25e071ca73c3d85e6218667587fa78f55bd
%global source15_hash 3418aa91ac8daf98f2ccbe67c2ca13bcf8fc5adb380f7c56e133f4487bc3ab701be1925d7a5878fc02ab7b8607e70991887a3d875d25b777b5489b7ae904aa7b
%global source16_hash 5028360a2b412232b06b0bc53352c7a0a379943c14781b49b45cb75aef044df5bda24449dbf13601d1a574e5349bd0f2d2f7b7969f10bf72b3aeebe9e81b6ecb
%global source17_hash 480edb224fcb42457c6252d4b6fd8cf42796e9b2ac72aa8d4bb22b3840cb10a55a509a47b8c504efbdba3e28192acee367e99638dfdbf9cab4fc5628496cd5db
%global source18_hash f9251142a990038acde2f1e7b61b94eba39b2c4f5c43a1151af29a17d5f0efb0cddc0af1ac8d056d8617b5ab4eef29bba14a4731ef933480a9bdb95fcc15d023
%global source19_hash 2cac5738a39157563707879656b473e7ac7edac2f304c209c8164c7878b10f0d5dcba1d38232ed6ba8e20fe21b3a0cf78dfd51733b993ccd5fcb2c0a05ea31c6
%global source20_hash 04a5314e51590eb43f92ca75aaadd1519152a38d246c588e0fef896935b00c2019679284c093d781a18de66423779c099142e636a5f0f451579534efe63e8ee7
%global source21_hash 8f014452d5c1dadfc9e1b67d4c99b4b446bbc7a220e3f73519a3d9ed7d976470df1ec91e5e2094671e7ff28cafe69566e8749d7e7ce6267af440cef5c6e2506f
%global source22_hash 1991bc0b471276ca3db68a8ba7611becc4557de4335a321b5c3e92c1fefbe34dc0488ab44850835b5ceb1684ce429e7756fb86d885e2da2177e0d9081797aa0c
%global source23_hash aac2e20a993818576f9e1efb153e9285b17b48827a1547a0c1033f22fa1a52f84ede214b4322ce4c6ddff69b8736f214f27370b3f1c006ea6e5fe2ab9fd64304
%global source24_hash 9d7c35499df5c8c8efe8ea51d88c4cd9ddc6bd5238ec527d842aaa9ce42c30bb1d73c667f5aca22f385d3725c7443f043a2b63cd337a7f6d5b5d5810ea34bf64
%global source25_hash e4eefb43d63c6522c3080a76b4df3a369932bc9e2f868ed0143d62fd2365bb74e6891705b287d19b4ca4b2560b0573d6ff9a0e5cf2a3da2e4b21482cd6cdd0b9
%global source26_hash a40edaf5480da6a48a3e31b8134ab7643c8b8a383d42634cbf1a2b7554365a8ccab7dfc01478d2b6768383cb30dd3662b8f004b57e2c1ee945c62354f07c4a1a
%global source27_hash 29977e23e6f86c906dcd6b198bd762de2335898b916fed220ec49d55e0c1647ef97914e809a1fb20f82bee17cd19c4879931f5c0f5d6662f65e673dea8103682
%global source28_hash 5581d61860060b10a8d434f70216c33b6dad932cdf8c365f1c2894f10fcf4cdb267b362c94f494d6457f7b5871319ca64abe883ff9a24a68ee6e95e7939fd2f2
%global source29_hash cc820f53ada3f60820c6b0f3f3714acfe03b920eaad75b7f7c19a62165b93193c4f21e7e23fd430b5c4121636296227248a9925df3caabf64097adb6a0e46c62
%global source30_hash 7141dcd00d60dfe807812f2be33808865792d73479d7518fd099321e8235b1a130cdb19dccefb1f5a2f959d5d7304d41cb387cd2d9d496abdffa97141df12652
%global source31_hash e65849212e57a4967a32162a1dd0fced0a9a352c8b968ce73aac35a9223f68d49ecbbdcd9b4fadb252e863a1d5a19fb3df94872b3cbe7f0b8f9624dca5604b7b
%global source32_hash e1440fcf8eb0ccd3b140649c590c902882a8a5a02d4cc14589ed44193f3a70bf13839e9de9663c500bb6874d6fce34f5a21c07e38a7456738548b6ebf449b258
%global source33_hash 0c91f7e1c8fe4910fa7052440edd9afd81c8932e99368219c8a5037bddfa4c8c11037576e9c94721062df9cf7fd5d467389ddcf3aed3e1853be38846c049100f
%global source34_hash e1d0df154733e752fd300ca28eb15d299de213f6510dfb56e62396cd7a2332f370d3a3744dc157f0be8f5d8a212606c685e5e6eff5cd884765d1f5b214f63bda
%global source35_hash 421fdca46017b5a25dcde5b87cd7cc1ffbdecb3daec8791d56a75b50f726c325e59572c1f2e7d4caf0da60fc46ba29965b9c8e2a26bcc3feb8a0bf9af68c26db
%global source36_hash 71983591270b533a6824a836948fdd15d19c3f966c8277d8948b13c5f38b29c29c0b7fe577661f1ecc570dd71d89fa964afd254d50556b6893667cda95e21aa7
%global source37_hash 02c2eb4991aa9775feec0846eaad9ddb74123a64eba8a3731c8e40c689844e542793e0f6884df8666f3cec2ed43af26b2d25254cd0536920c6ff0b107f35bf5b
%global source38_hash a660377614522f159698d0577ec2fbb210e639787ed2267530d40e45c12f72f188f1e5000c7bd7865a7d1cb74627b5dcdcb8a44c3b17a1c7ff62b0c9ce0e430f
%global source39_hash 89b0baa7ffa7fb3c3b0b7ef000cbb4e2656dff839c846dda575e262f5ce7c4e62b9f737c9dc8c2e7b1c788e439c4b524f2ab7fb4e3685157a4aa8f3044b21413
%global source40_hash 8284f61e74ac52067f40ba176557345aa641c3882dadc1f850afc5e27c6c322277407ec7f45019435832b266e7bf3954b360442537bb60c9ea9bd729bbe0bc02
%global source41_hash d5d695a8715871d3c7b9674f95a31f6ff3e4ecb0f14e8e12bde65ab429c4e85e20958653510cd77fb50ba1a09d915a7408d1ac4d8a306a53033caea36da487d3
%global source42_hash e32eddbc519ed33687c1fbe36b2cf45f9ee886a78c0a088f6648da42dbebb0a72064ec4b9d5333656cc3bed7b251ef3a758926db88e6bb79ffd4536489717db5
%global source43_hash 02cda290799bde7288220d0b634b970a6ac543fd63318bcf90c4ad06eab074f5851e7bc42c9359af709eccc0c8847a0d3d1a9e27cdfd3f60c7143de7ac4d3901
%global source44_hash b6754a4f881ee11941a7cbe3f97376bf43e8ab8123ddb95c95bac90937f9b86669ef83cf052f93011a88199d129373b993cbf7b24755de95e1fcba9c03b508b5
%global source45_hash a445baf6db8508e23505a2afc70c0cc4efdd245c9ef45d77c3dad6da33128e99753b7072d74d5e4e3e37d0a1ba8be0b358ab00a4703d8fb18c9223c2ac6de1db
%global source46_hash ae15180c2edbb90ccfd1c449438b25a2ea641dc3b353f12dc451e253197873e79e2f60cfe3b678be708bfeb13140bcb7139f8332d2471b7c4904d552682ebb63
%global source47_hash fa62240255931591e8f8b10af4780fdc0c51b4dea6e95b820e2b526af0cafbc39e9a5f9ddaa4190d5c030ec5dbd1a43626c3edadee692b23c023c2409b701169
%global source48_hash cf587c174e44da9496ece876bfcb8330bc52173cc3bd6d1b1351efc75a7c333ed8c7cbd41c079d492947a1ee43d8043fabebc80b4c7a5d348eb054e82c704e3b
%global source49_hash 0bfe1fa6a4b3a8923cfbe9bdc4fa1b27567df66365db447346fdcc739675d1d815515e09fbe96f44369643c38e6a8007a0f8d089ed8504020fe0a0e2a795ea9a
%global source50_hash f4857ee20c14735140d79738ac1d2ddc57421f89aca3e57dd8f5bdddc4f51189185b4d9e0bc55a4a8c226381ab4babeab4740dc1978bd1dc82de347b87c0f9d2
%global source51_hash caa7ff99b9bdd29c81d82225a653ed49ca48d99a9bd9c3c5a5fc1d3486131c8bee9844a8640d3a96d796d565443d632ccc1966c374573193bbe6b61c1dedcbf3
%global source52_hash e59dd121f9a176e628697e31b720507723867a0b7b68b73531aa825bb02b07d04ff705bdfbeb369fe3a2d304f4c6c5aad3f823aaa4c82257540f1459cf099cb1
%global source53_hash 59f17d78ef78a142bde5783996f149b3a7c740c2b3ec6f90133115ebddcf6c460dada543482f5379872054a74eb772bab8afd96fa48b2484f7932a478b8bde2d
%global source54_hash 96773f0d0e2788d13738930fa1aa727c7ca2edee020f3848326d7be3533c177ac977564aed533c59695b1e6c4c65e191784cbc3e7e70becdd651cd702b462ef5
%global source55_hash 6c649c32111a6350d36c69405fc272a917144be429bd84c0f118a74e1232c06744e66fb6647c5a742f58c6c78b46830a1484bbed3a9a962380ece6b16c555169
%global source56_hash 361983a020165d094bcd0fc9616be74bd2b5c72542b1e1b257b5ec42ac6be1175caf59c79e156da2bf6fecfe3746b4e33a4a8fc978eb124939ce0ffd2c383081
%global source57_hash 97ec26cc1ed8e181c7d69af264204772c9075e3650044b58cad938fd6918f9cbf5c849699e31846f437e41410492b67668a7ec33e848cf6b5fb9c2d52d7a7947
%global source58_hash c175c40a328444d6de99c713af6a48fcd3301acb2276035789b3c9b1e7b9ca9cb401c71026eea85c0549fc264273206b2234627618c565ba6d1a1a6aba10b20d
%global source59_hash f57b16cfe2da00edfa30e98ba5a95fe9d4793beea585c4f890448bf1242a3333625de7158e5754e1831d7c037de9035d57da7907e94640aa44df28749ac47ea9
%global source60_hash b487908c102e43777884e2414bf5ebd60bdebb5431481a312d26b6ed37d0e714fa16ffdbd6663fabddb366affab8070695182cd5ea74bb08c685669bbb24cb42
%global source61_hash bf3c5449c2fedf3c7737a07ac55b4655d2e8ffc20e1ea7d9c8e1c83d49d0d292db9a8e8bd11a171d61e0bd351fcfbb59aaee20d1ac1df1ba80f8cd955bb9e2d5
%global source62_hash ec4b54162452503472089ec2ccfeb75df4ecd9cc40b93146deeebe49fbdfe39af878d606f90fa792cf7912cd30a2a772fa67db1c7a9f8c59027c6c147ff0a648
%global source63_hash ed7ad7706d3cd6b4b393c9dc6c46e78ae90cd88fd558bf3582f8297d650c325900e199f889573cb4700fbcd1df623337975f71d75e9f036b12aba1ba5e3ff875
%global source64_hash a05c274e3b23d8b4a4302b9676363aa190f921d0e6f64503f09c8b3183381381ba7fd8e0883442cb2418155aa71f19210a72f99e01187f1d7c8e69d77417d655
%global source65_hash d4429f035993678dc00f3b350c95446cb89b85d10c5a16d5018af9bf60b2d958001432c06ab125252f0ea859ebe56dfe54d7a3442709060c9810d6569fa525d8
%global source66_hash e5899aace25cef3a690150cf09e76bddc008f426800588ef7d21361229b0040dff74af7b43d563b05d8c3d16166e34b5a21e8e25ae3e97ca80e5ffe5c4925392
%global source67_hash 2b64199f50ae5b0e6528bf041ac2422574f9adf467183f3ee3d58ebd91317ce25937699be29d0a5954565a4fd326719f11bc04a35cb4938489696ae479d5d7f5
%global source68_hash 58e4a909374486cd2d4313d62a49e4e30a5e85f8ef2cc0d9a7e734b546ad8b36e3bbfb96f3eecaa9c10b8d7b3b1557aa9e0b5dae5b4547d42cabc64d2f2949d3
%global source69_hash d1ca204228c1bc76d4f15257687a865c650fa83742dd126b3d7cd5e93e725b2da31eedfbca9a86e93eaa08df487b0432cc41f0d4fd2f99951f874691acf47016
%global source70_hash 1efc3f1f1c93456a3038ae5037ad5dcc4b177c57852f7db475a7ce6d2002559b370ba22dcc6d312c68ba75c03523cdf0df8546fff8dab032832d3ff3148b5d65
%global source71_hash 4ec7cadd89449ca049fdd723de9e29f20199a630fc28585a4802e3ce3666783822e4f0769907cafbfb0fe097b1da4a08d3e5e5f4038ecebbe9fe3543dd3413d6
%global source72_hash 559cfb4903e6a01b4b0b27b4430c04fd27791dde0872a3cc477094bbcbcb859acc73933fba09b1d0f7db3082d5c67fa939bf5849908604c0b98dba9b7a32034a
%global source73_hash 8faf458987ab9f48368704bccbcb3848e464c42dd6d086ea12314fda25775080e463a7a984193d01cce43c25259c1556577aa7c06483add7747202f25f6b910f
%global source74_hash 5f63ead399de02af4655168c5c3411611f177d792792d8ded9e5340c62e452f2d6a29c089a95eb897a5047234c7877cd67436089c0a320074385b16dce8d8033
%global source75_hash 3362a8b1514c8247be585af9459e6e7c750e471e65bd22879e5f0ae06f1211fafe0ea9411e386437d6650c33eae5e2b8f038850fe11b066f004a1c50ab343d8d
%global source76_hash 5d711f7a981f701e11874916fe8d22fa237404dc119fc2d5c8f8e9b3eaf8feb59a63023ec30f0c67d304839e4971288a669d70a697260af35e401edf00673adb
%global source77_hash 954c8e3a8a0deafea163c9bea9da6bd1c27fcc9b5270408fdd29f0051ece1f4138a0af99808cf85279823cb48475b8e21b3a450f021d678fc5b2fbdf28e55320
%global source78_hash b7c3fbfebab7e013028f54a1333bfb244fb03859dde92a41f8c6bdc5b6e66bdf82d3f54261a733ea962d17156f6a4bcf42b2ff6279f1bba4ed095388bdbcd49b
%global source79_hash c5182c439a22299425a842c013a9b2baca3b4e9b25d7941cb9c56a8a9659e027a06eadcaf688089f77ca744157564a6aadef1b714365af01e6b76385f66f9957
%global source80_hash 4677a293c69c68eff3018f963adc1cd0c4da41b072ab993dfc74fc1c0114461dc4cba26c49acc9466d5d0601fabcb4c16d8f0a4e81ce6f9484b8466901b2533d
%global source81_hash 974afd6e49a86421f82ac673715247d9558ed93abdb9ae54d6726f0b09a607e4ce2863b97a87370a2efb14dcf14af76b4910e230106b8f3d9631c9273cfbbec4
%global source82_hash e4ef7bdc43280c4311a6e8abf2719815196fb0ed0a8450501061e0b3b0bb44cd60947d6d623ff753c5ad1384d98219df695865e6459eef02b2b96f00906d023a
%global source83_hash f74c3c34d37eabc3b5e857a90e8da2c6ffaa3b4a6974c6b1127f898fb727ff18f0f399e9c4ccde8d4d198bece0ea83fbbac37a1ba1d381576166b5a2742113c5
%global source84_hash 3b0e4c0395cc461196ecb722ed70674d2ef470474c948455d10b35b32c8b86f0da667f2ee2c15ca5c3748f00e408efaee9e959a0c880d17fa75d34817e9ae48a
%global source85_hash 4d0338ec9b1820eafd0bf23b2e32597ceee2f3740ccf2974ca14132c85363847d8c44560135f3eaa3b6cf7a8f9ab1a8c3b2177cc10929537c0d34698f3d27a9c
%global source86_hash 7df2224f9970b72cfa1474898c057799fe42d717876eed864f35aab113d01dfb483edb71f7f4a0a98b6762bbc309ce6fb51e41dc222a6f19be2025f6448fb1cd
%global source87_hash 01cdc4c8443c50a91dd408c52122e8ae65257344176227a508cb082f92d61bc02756d47e27f75d7862d3c87c26add2003604956ad00b448f63b4f6417c520ba6
%global source88_hash 35289692327bdc68acbd442588fbd37185f9e00e3e4ca78fe500474c53ef96542042cebd18cba7720bdca0b72f19384fd3b8afcf45447644bb3c560a1385595f
%global source89_hash 4e082b6b61ae9f2d02c6bdf7fe5beeb6b6384b2718c1644b945b175bc17c951ec7890fe7e81eb59faea4ae86da93eaf51467450cd61d223e734408e624bd8abb
%global source90_hash 2c295a28748f8df117a5abf16a758b079d7481f579e1bb571fc758bae505860e1a1b82f9615259b14359eb4ea8f43be82de6ae6d761225ea76bc0da167b6786c
%global source91_hash f7bd44c9720512297f15ff6cee1c49ca52c29fc206f739e6aa447e778fed00a64e282aeab9d42b215cac69a64ab39f3919433bd0640d30d55ac540e2dde07967
%global source92_hash d271c1f9e7b9c45694463982da8c9542fea326d7e191a705e92f5b423e054c3f926768d2209844ddabbe75eb610d4a5cb05ffd53098cdca9e35328c865027eff
%global source93_hash f040046978cf51bbaf3347406e224fe60a85f449c1fac1703e7a2d936140b099c14ffd488ebe4c3d932b35a8380f943250734a054ea5165ed26b2be712ad577c
%global source94_hash 08532f43fb7aac979e78d30f27f36047d7b70733ef6bdd65d26a40e6818f2b73852d4a6ac5eeae8cd29fc86e1630d2ba068b9707666f66a13e2090a6da81ac25
%global source95_hash a9fd27694ea7491321580ee325f8b151bbcfcf6da14ecce85b6d4e68b09cdf125c810a5170aacc966835fad8f2aaefd78916920cc3e896cad7738d026450ed83
%global source96_hash 667d3c5590468170acfded106a2a468d9abe7b4b34a9b56d153d401a60e8f24bce99a4f6c5f2761572a42b85c7faae5741ee5b6f22c3f1004e6d6685463b9350
%global source97_hash 7780972480a1355a05cbcca3c46f3e5284b120a93ed2265f0fcceb6965f55ed793756cf96df63aa8da589dd12fe1b8127bd470077b9f9dda758238ced566b3e6
%global source98_hash 5507082be0235ec2253ddc0b03e239607b9d140952799684e5193e4d3d584846d33a59aa9b1630d058f17cacf7cedd2fe0a180b40207ea8f10947b534784fc02
%global source99_hash 66e6a27aa277b45b44c156d408c764da5bee6dc540f2058a783f02bbe806c95052267a5ed79ea49b5dc356d0f03747e9b186542640b34753a693ecffa158a6a4
%global source100_hash c750497229b8bd41eca05b221ed2ca2ca49db8cbbff03bfce2712869d352ae0385e4c10e9730e0b2f8286db9af1e1b87f10d599788a3dfe8d41c28efb8b0e4a6

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-metapost.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/automata.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/automata.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbcard.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbcard.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blockdraw_mp.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blockdraw_mp.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bpolynomial.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bpolynomial.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmarrows.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmarrows.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drv.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drv.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviincl.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviincl.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emp.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emp.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsincl.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsincl.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expressg.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expressg.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exteps.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exteps.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/featpost.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/featpost.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feynmf.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feynmf.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feynmp-auto.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feynmp-auto.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fiziko.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fiziko.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garrigues.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garrigues.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gmp.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gmp.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hatching.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hatching.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hershey-mp.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hershey-mp.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/huffman.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/huffman.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexmp.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexmp.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mcf2graph.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mcf2graph.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metago.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metago.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metaobj.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metaobj.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metaplot.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metaplot.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metapost-colorbrewer.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metapost-colorbrewer.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metauml.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metauml.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfpic.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfpic.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfpic4ode.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfpic4ode.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-hatching.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-hatching.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp-geom2d.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp-geom2d.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp-neuralnetwork.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp-neuralnetwork.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp3d.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp3d.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mparrows.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mparrows.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpattern.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpattern.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpchess.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpchess.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpcolornames.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpcolornames.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpgraphics.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpgraphics.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpkiviat.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpkiviat.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mptrees.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mptrees.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piechartmp.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piechartmp.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/repere.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/repere.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/roex.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/roundrect.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/roundrect.doc.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shapes.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shapes.doc.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/slideshow.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/slideshow.doc.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splines.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splines.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suanpan.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suanpan.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textpath.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textpath.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/threeddice.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/threeddice.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-automata
Requires:       texlive-bbcard
Requires:       texlive-blockdraw_mp
Requires:       texlive-bpolynomial
Requires:       texlive-cmarrows
Requires:       texlive-collection-basic
Requires:       texlive-drv
Requires:       texlive-dviincl
Requires:       texlive-emp
Requires:       texlive-epsincl
Requires:       texlive-expressg
Requires:       texlive-exteps
Requires:       texlive-featpost
Requires:       texlive-feynmf
Requires:       texlive-feynmp-auto
Requires:       texlive-fiziko
Requires:       texlive-garrigues
Requires:       texlive-gmp
Requires:       texlive-hatching
Requires:       texlive-hershey-mp
Requires:       texlive-huffman
Requires:       texlive-latexmp
Requires:       texlive-mcf2graph
Requires:       texlive-metago
Requires:       texlive-metaobj
Requires:       texlive-metaplot
Requires:       texlive-metapost
Requires:       texlive-metapost-colorbrewer
Requires:       texlive-metauml
Requires:       texlive-mfpic
Requires:       texlive-mfpic4ode
Requires:       texlive-minim-hatching
Requires:       texlive-mp-geom2d
Requires:       texlive-mp-neuralnetwork
Requires:       texlive-mp3d
Requires:       texlive-mparrows
Requires:       texlive-mpattern
Requires:       texlive-mpchess
Requires:       texlive-mpcolornames
Requires:       texlive-mpgraphics
Requires:       texlive-mpkiviat
Requires:       texlive-mptrees
Requires:       texlive-piechartmp
Requires:       texlive-repere
Requires:       texlive-roex
Requires:       texlive-roundrect
Requires:       texlive-shapes
Requires:       texlive-slideshow
Requires:       texlive-splines
Requires:       texlive-suanpan
Requires:       texlive-textpath
Requires:       texlive-threeddice

%description
MetaPost and Metafont packages

%package -n texlive-automata
Summary:        Finite state machines, graphs and trees in MetaPost
Version:        svn19717
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-automata
The package offers a collection of macros for MetaPost to make easier to draw
finite-state machines, automata, labelled graphs, etc. The user defines nodes,
which may be isolated or arranged into matrices or trees; edges connect pairs
of nodes through arbitrary paths. Parameters, that specify the shapes of nodes
and the styles of edges, may be adjusted.

%package -n texlive-bbcard
Summary:        BS bingo, calendar and baseball-score cards
Version:        svn19440
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bbcard
Three jiffy packages for creating cards of various sorts with MetaPost.

%package -n texlive-blockdraw_mp
Summary:        Block diagrams and bond graphs, with MetaPost
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-blockdraw_mp
A set of simple MetaPost macros for the task. While the task is not itself
difficult to program, it is felt that many users will be happy to have a
library for the job..

%package -n texlive-bpolynomial
Summary:        Drawing polynomial functions of up to order 3
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bpolynomial
This MetaPost package helps plotting polynomial and root functions up to order
three. The package provides macros to calculate Bezier curves exactly matching
a given constant, linear, quadratic or cubic polynomial, or square or cubic
root function. In addition, tangents on all functions and derivatives of
polynomials can be calculated.

%package -n texlive-cmarrows
Summary:        MetaPost arrows and braces in the Computer Modern style
Version:        svn24378
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cmarrows
This MetaPost package contains macros to draw arrows and braces in the Computer
Modern style.

%package -n texlive-drv
Summary:        Derivation trees with MetaPost
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-drv
A set of MetaPost macros for typesetting derivation trees (such as used in
sequent calculus, type inference, programming language semantics...). No
MetaPost knowledge is needed to use these macros.

%package -n texlive-dviincl
Summary:        Include a DVI page into MetaPost output
Version:        svn29349
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dviincl
DVItoMP is one of the auxiliary programs available to any MetaPost package; it
converts a DVI file into a MetaPost file. Using it, one can envisage including
a DVI page into an EPS files generated by MetaPost. Such files allow pages to
include other pages.

%package -n texlive-emp
Summary:        "Encapsulate" MetaPost figures in a document
Version:        svn23483
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(emp.sty) = %{tl_version}

%description -n texlive-emp
Emp is a package for encapsulating MetaPost figures in LaTeX: the package
provides environments where you can place MetaPost commands, and means of using
that code as fragments for building up figures to include in your document. So,
with emp, the procedure is to run your document with LaTeX, run MetaPost, and
then complete running your document in the normal way. Emp is therefore useful
for keeping illustrations in synchrony with the text. It also frees you from
inventing descriptive names for PostScript files that fit into the confines of
file system conventions.

%package -n texlive-epsincl
Summary:        Include EPS in MetaPost figures
Version:        svn29349
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-epsincl
The package facilitates including EPS files in MetaPost figures; it makes use
of (G)AWK.

%package -n texlive-expressg
Summary:        Diagrams consisting of boxes, lines, and annotations
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-expressg
A MetaPost package providing facilities to assist in drawing diagrams that
consist of boxes, lines, and annotations. Particular support is provided for
creating EXPRESS-G diagrams, for example IDEF1X, OMT, Shlaer-Mellor, and NIAM
diagrams. The package may also be used to create UML and most other
Box-Line-Annotation charts, but not Gantt charts directly.

%package -n texlive-exteps
Summary:        Include EPS figures in MetaPost
Version:        svn19859
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-exteps
Exteps is a module for including external EPS figures into MetaPost figures. It
is written entirely in MetaPost, and does not therefore require any post
processing of the MetaPost output.

%package -n texlive-featpost
Summary:        MetaPost macros for 3D
Version:        svn35346
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-featpost
These macros allow the production of three-dimensional schemes containing:
angles, circles, cylinders, cones and spheres, among other things.

%package -n texlive-feynmf
Summary:        Macros and fonts for creating Feynman (and other) diagrams
Version:        svn17259
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Provides:       tex(feynmf.sty) = %{tl_version}
Provides:       tex(feynmp.sty) = %{tl_version}

%description -n texlive-feynmf
The feynmf package provides an interface to Metafont (inspired by the
facilities of mfpic) to use simple structure specifications to produce
relatively complex diagrams. (The feynmp package, also part of this bundle,
uses MetaPost in the same way.) While the package was designed for Feynman
diagrams, it could in principle be used for diagrams in graph and similar
theories, where the structure is semi-algorithmically determined.

%package -n texlive-feynmp-auto
Summary:        Automatic processing of feynmp graphics
Version:        svn30223
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(feynmp.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(pdftexcmds.sty)
Provides:       tex(feynmp-auto.sty) = %{tl_version}

%description -n texlive-feynmp-auto
The package takes care of running Metapost on the output files produced by the
feynmp package, so that the compiled pictures will be available in the next run
of LaTeX. The package honours options that apply to feynmp.

%package -n texlive-fiziko
Summary:        A MetaPost library for physics textbook illustrations
Version:        svn61944
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fiziko
This MetaPost library was initially written to automate some elements of black
and white illustrations for a physics textbook. It provides functions to draw
things like lines of variable width, shaded spheres, and tubes of different
kinds, which can be used to produce images of a variety of objects. The library
also contains functions to draw some objects constructed from these primitives.

%package -n texlive-garrigues
Summary:        MetaPost macros for the reproduction of Garrigues' Easter nomogram
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-garrigues
MetaPost macros for the reproduction of Garrigues' Easter nomogram. These
macros are described in Denis Roegel: An introduction to nomography: Garrigues'
nomogram for the computation of Easter, TUGboat (volume 30, number 1, 2009,
pages 88-104)

%package -n texlive-gmp
Summary:        Enable integration between MetaPost pictures and LaTeX
Version:        svn21691
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(gmp.sty) = %{tl_version}

%description -n texlive-gmp
The package allows integration between MetaPost pictures and LaTeX. The main
feature is that passing parameters to the MetaPost pictures is possible and the
picture code can be put inside arguments to commands, including \newcommand.

%package -n texlive-hatching
Summary:        MetaPost macros for hatching interior of closed paths
Version:        svn23818
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hatching
The file hatching.mp contains a set of MetaPost macros for hatching interior of
closed paths. Examples of usage are included.

%package -n texlive-hershey-mp
Summary:        MetaPost support for the Hershey font file format
Version:        svn70885
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hershey-mp
This package provides MetaPost support for reading jhf vector font files, used
by (mostly? only?) the so-called Hershey Fonts of the late 1960s. The package
does not include the actual font files, which you can probably find in the
software repository of your operating system.

%package -n texlive-huffman
Summary:        Drawing binary Huffman trees with MetaPost and METAOBJ
Version:        svn67071
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-huffman
This MetaPost package allows to draw binary Huffman trees from two arrays : an
array of strings, and an array of weights (numeric). It is based on the METAOBJ
package which provides many tools for building trees in general.

%package -n texlive-latexmp
Summary:        Interface for LaTeX-based typesetting in MetaPost
Version:        svn55643
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-latexmp
The MetaPost package latexMP implements a user-friendly interface to access
LaTeX-based typesetting capabilities in MetaPost. The text to be typeset is
given as string. This allows even dynamic text elements, for example counters,
to be used in labels. Compared to other implementations it is much more
flexible, since it can be used as direct replacement for btex.etex, and much
faster, compared for example to the solution provided by tex.mp.

%package -n texlive-mcf2graph
Summary:        Draw chemical structure diagrams with MetaPost
Version:        svn76506
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mcf2graph
The Molecular Coding Format (MCF) is a linear notation for describing chemical
structure diagrams. This package converts MCF to graphic files using MetaPost.

%package -n texlive-metago
Summary:        MetaPost output of Go positions
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metago
The package allows you to draw Go game positions with MetaPost. Two methods of
usage are provided, either using the package programmatically, or using the
package via a script (which may produce several images).

%package -n texlive-metaobj
Summary:        MetaPost package providing high-level objects
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metaobj
METAOBJ is a large MetaPost package providing high-level objects. It implements
many of PSTricks' features for node connections, but also trees, matrices, and
many other things. It more or less contains boxes.mp and rboxes.mp. There is a
large (albeit not complete) documentation distributed with the package. It is
easily extensible with new objects.

%package -n texlive-metaplot
Summary:        Plot-manipulation macros for use in MetaPost
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metaplot
MetaPlot is a set of MetaPost macros for manipulating pre-generated plots (and
similar objects), and formatting them for inclusion in a MetaPost figure. The
intent is that the plots can be generated by some outside program, in an
abstract manner that does not require making decisions about on-page sizing and
layout, and then they can be imported into MetaPlot and arranged using the full
capabilities of MetaPost. Metaplot also includes a very flexible set of macros
for generating plot axes, which may be useful in other contexts as well.
Presently, MetaPlot is in something of a pre-release beta state; it is quite
functional, but the syntax of the commands is still potentially in flux.

%package -n texlive-metapost-colorbrewer
Summary:        An implementation of the colorbrewer2.org colours for MetaPost
Version:        svn48753
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metapost-colorbrewer
This package provides two MetaPost include files that define all the
colorbrewer2.org colours: colorbrewer-cmyk.mp colorbrewer-rgb.mp The first
defines all the colours as CMYK, the second as RGB. Use whichever one you
prefer. For an example of what you can do, and a list of all the names, have a
look at colorbrewer-sampler.mp. You can also see the names on
http://colorbrewer2.org. The package also includes the Python script used to
generate the MP source from the colorbrewer project.

%package -n texlive-metauml
Summary:        MetaPost library for typesetting UML diagrams
Version:        svn49923
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metauml
MetaUML is a MetaPost library for typesetting UML diagrams, which provides a
usable, human-friendly textual notation for UML, offering now support for
class, package, activity, state, and use case diagrams.

%package -n texlive-mfpic
Summary:        Draw Metafont/post pictures from (La)TeX commands
Version:        svn28444
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Provides:       tex(mfpic.sty) = %{tl_version}
Provides:       tex(mfpic.tex) = %{tl_version}
Provides:       tex(mfpicdef.tex) = %{tl_version}

%description -n texlive-mfpic
Mfpic is a scheme for producing pictures from (La)TeX commands. Commands \mfpic
and \endmfpic (in LaTeX, the mfpic environment) enclose a group in which
drawing commands may be placed. The commands generate a Meta-language file,
which may be processed by MetaPost (or even Metafont). The resulting image file
will be read back in to the document to place the picture at the point where
the original (La)TeX commands appeared. Note that the ability to use MetaPost
here means that the package works equally well in LaTeX and pdfLaTeX.

%package -n texlive-mfpic4ode
Summary:        Macros to draw direction fields and solutions of ODEs
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mfpic4ode.sty) = %{tl_version}
Provides:       tex(mfpic4ode.tex) = %{tl_version}

%description -n texlive-mfpic4ode
The package is a small set of macros for drawing direction fields, phase
portraits and trajectories of differential equations and two dimensional
autonomous systems. The Euler, Runge-Kutta and 4th order Runge-Kutta algorithms
are available to solve the ODEs. The picture is translated into mfpic macros
and MetaPost is used to create the final drawing. The package is was designed
for use with LaTeX, but it can be used in plain TeX as well.

%package -n texlive-minim-hatching
Summary:        Create tiling patterns with the minim-mp MetaPost processor
Version:        svn70885
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-minim-hatching
This is a small proof-of-concept library of tiling patterns for use with the
minim-mp MetaPost processor.

%package -n texlive-mp-geom2d
Summary:        Flat geometry with MetaPost
Version:        svn77019
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mp-geom2d
This package was written with the aim of providing MetaPost macros for creating
a geometry figure that closely matches an imperative description: Let A be the
point with coordinates (2,3). Let B be the point with coordinates (4,5). Draw
the line (A, B). ...

%package -n texlive-mp-neuralnetwork
Summary:        Drawing artificial neural networks with MetaPost and METAOBJ
Version:        svn73627
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mp-neuralnetwork
This MetaPost package allows to draw artificial neural networks. It is based on
the METAOBJ package which provides many tools to draw and arrange nodes. This
package is in beta version -- do not hesitate to report bugs, as well as
requests for improvement.

%package -n texlive-mp3d
Summary:        3D animations
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mp3d
Create animations of 3-dimensional objects (such as polyhedra) in MetaPost.

%package -n texlive-mparrows
Summary:        MetaPost module with different types of arrow heads
Version:        svn39729
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mparrows
A package to provide different types of arrow heads to be used with MetaPost
commands drawarrow and drawdblarrow commands.

%package -n texlive-mpattern
Summary:        Patterns in MetaPost
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpattern
A package for defining and using patterns in MetaPost, using the Pattern Color
Space available in PostScript Level 2.

%package -n texlive-mpchess
Summary:        Drawing chess boards and positions with MetaPost
Version:        svn73149
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpchess
This package allows you to draw chess boards and positions. The appearance of
the drawings is modern and largely inspired by what is offered by the excellent
web site Lichess.org. Relying on MetaPost probably allows more graphic
flexibility than the excellent LaTeX packages. This package is in beta version,
do not hesitate to report bugs, as well as requests for improvement

%package -n texlive-mpcolornames
Summary:        Extend list of predefined colour names for MetaPost
Version:        svn23252
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpcolornames
The MetaPost format plain.mp provides only five built-in colour names
(variables), all of which are defined in the RGB model: red, green and blue for
the primary colours and black and white. The package makes more than 500 colour
names from different colour sets in different colour models available to
MetaPost. Colour sets include X11, SVG, DVIPS and xcolor specifications.

%package -n texlive-mpgraphics
Summary:        Process and display MetaPost figures inline
Version:        svn29776
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(iftex.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(mpgraphics.sty) = %{tl_version}

%description -n texlive-mpgraphics
The package allows LaTeX users to typeset MetaPost code inline and display
figures in their documents with only and only one run of LaTeX, pdfLaTeX or
XeLaTeX (no separate runs of mpost). Mpgraphics achieves this by using the
shell escape (\write 18) feature of current TeX distributions, so that the
whole process is automatic and the end user is saved the tiresome processing.

%package -n texlive-mpkiviat
Summary:        MetaPost package to draw Kiviat diagrams
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpkiviat
This MetaPost package allows to draw Kiviat diagrams (or radar chart, web
chart, spider chart, etc.).

%package -n texlive-mptrees
Summary:        Probability trees with MetaPost
Version:        svn70887
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mptrees
This package provides MetaPost tools for drawing simple probability trees and
graphs (in discrete geometry).

%package -n texlive-piechartmp
Summary:        Draw pie-charts using MetaPost
Version:        svn19440
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-piechartmp
The piechartmp package is an easy way to draw pie-charts with MetaPost. The
package implements an interface that enables users with little MetaPost
experience to draw charts. A highlight of the package is the possibility of
suppressing some segments of the chart, thus creating the possibility of
several charts from the same data.

%package -n texlive-repere
Summary:        MetaPost macros for secondary school mathematics teachers
Version:        svn66998
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-repere
This package provides MetaPost macros for drawing secondary school mathematics
figures in a coordinate system: axis, grids points, vectors functions (curves,
tangents, integrals, sequences) statistic diagrams plane geometry (polygons,
circles) arrays and game boards

%package -n texlive-roex
Summary:        Metafont-PostScript conversions
Version:        svn45818
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-roex
A Metafont support package including: epstomf, a tiny AWK script for converting
EPS files into Metafont; mftoeps for generating (encapsulated) PostScript files
readable, e.g., by CorelDRAW, Adobe Illustrator and Fontographer; a collection
of routines (in folder progs) for converting Metafont-coded graphics into
encapsulated PostScript; and roex.mf, which provides Metafont macros for
removing overlaps and expanding strokes. In mftoeps, Metafont writes PostScript
code to a log-file, from which it may be extracted by either TeX or AWK.

%package -n texlive-roundrect
Summary:        MetaPost macros for highly configurable rounded rectangles (optionally with text)
Version:        svn39796
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-roundrect
The roundrect macros for MetaPost provide ways to produce rounded rectangles,
which may or may not contain a title bar or text (the title bar may itself
contain text). They are extremely configurable.

%package -n texlive-shapes
Summary:        Draw polygons, reentrant stars, and fractions in circles with MetaPost
Version:        svn42428
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-shapes
The shapes set of macros allows drawing regular polygons; their corresponding
reentrant stars in all their variations; and fractionally filled circles
(useful for visually demonstrating the nature of fractions) in MetaPost.

%package -n texlive-slideshow
Summary:        Generate slideshow with MetaPost
Version:        svn15878
License:        McPhee-slideshow
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-slideshow
The package provides a means of creating presentations in MetaPost, without
intervention from other utilities (except a distiller). Such an arrangement has
its advantages (though there are disadvantages too).

%package -n texlive-splines
Summary:        MetaPost macros for drawing cubic spline interpolants
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-splines
This is a small package of macros for creating cubic spline interpolants in
MetaPost or Metafont. Given a list of points the macros can produce a closed or
a relaxed spline joining them. Given a list of function values y_j at x_j, the
result would define the graph of a cubic spline interpolating function y=f(x),
which is either periodic or relaxed.

%package -n texlive-suanpan
Summary:        MetaPost macros for drawing Chinese and Japanese abaci
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-suanpan
These macros are described in Denis Roegel: MetaPost macros for drawing Chinese
and Japanese abaci, TUGboat (volume 30, number 1, 2009, pages 74-79)

%package -n texlive-textpath
Summary:        Setting text along a path with MetaPost
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(soul.sty)
Provides:       tex(textpathmp.sty) = %{tl_version}

%description -n texlive-textpath
This MetaPost package provides macros to typeset text along a free path with
the help of LaTeX, thereby preserving kerning and allowing for 8-bit input
(accented characters).

%package -n texlive-threeddice
Summary:        Create images of dice with one, two, or three faces showing, using MetaPost
Version:        svn20675
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-threeddice
The package provides MetaPost code to create all possible symmetrical views (up
to rotation) of a right-handed die. Configuration is possible by editing the
source code, following the guidance in the documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-automata
%license lppl1.3c.txt
%{_texmf_main}/metapost/automata/
%doc %{_texmf_main}/doc/metapost/automata/

%files -n texlive-bbcard
%license pd.txt
%{_texmf_main}/metapost/bbcard/
%doc %{_texmf_main}/doc/metapost/bbcard/

%files -n texlive-blockdraw_mp
%license lppl1.3c.txt
%{_texmf_main}/metapost/blockdraw_mp/
%doc %{_texmf_main}/doc/metapost/blockdraw_mp/

%files -n texlive-bpolynomial
%license lppl1.3c.txt
%{_texmf_main}/metapost/bpolynomial/
%doc %{_texmf_main}/doc/metapost/bpolynomial/

%files -n texlive-cmarrows
%license lppl1.3c.txt
%{_texmf_main}/metapost/cmarrows/
%doc %{_texmf_main}/doc/metapost/cmarrows/

%files -n texlive-drv
%license lppl1.3c.txt
%{_texmf_main}/metapost/drv/
%doc %{_texmf_main}/doc/metapost/drv/

%files -n texlive-dviincl
%license pd.txt
%{_texmf_main}/metapost/dviincl/
%doc %{_texmf_main}/doc/metapost/dviincl/

%files -n texlive-emp
%license gpl2.txt
%{_texmf_main}/tex/latex/emp/
%doc %{_texmf_main}/doc/latex/emp/

%files -n texlive-epsincl
%license pd.txt
%{_texmf_main}/metapost/epsincl/
%doc %{_texmf_main}/doc/metapost/epsincl/

%files -n texlive-expressg
%license lppl1.3c.txt
%{_texmf_main}/metapost/expressg/
%doc %{_texmf_main}/doc/metapost/expressg/

%files -n texlive-exteps
%license gpl2.txt
%{_texmf_main}/metapost/exteps/
%doc %{_texmf_main}/doc/metapost/exteps/

%files -n texlive-featpost
%license gpl2.txt
%{_texmf_main}/metapost/featpost/
%doc %{_texmf_main}/doc/metapost/featpost/

%files -n texlive-feynmf
%license gpl2.txt
%{_texmf_main}/metafont/feynmf/
%{_texmf_main}/metapost/feynmf/
%{_texmf_main}/tex/latex/feynmf/
%doc %{_texmf_main}/doc/latex/feynmf/

%files -n texlive-feynmp-auto
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/feynmp-auto/
%doc %{_texmf_main}/doc/latex/feynmp-auto/

%files -n texlive-fiziko
%license gpl3.txt
%license cc-by-sa-4.txt
%{_texmf_main}/metapost/fiziko/
%doc %{_texmf_main}/doc/metapost/fiziko/

%files -n texlive-garrigues
%license lppl1.3c.txt
%{_texmf_main}/metapost/garrigues/
%doc %{_texmf_main}/doc/metapost/garrigues/

%files -n texlive-gmp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gmp/
%doc %{_texmf_main}/doc/latex/gmp/

%files -n texlive-hatching
%license pd.txt
%{_texmf_main}/metapost/hatching/
%doc %{_texmf_main}/doc/metapost/hatching/

%files -n texlive-hershey-mp
%license other-free.txt
%{_texmf_main}/metapost/hershey-mp/
%doc %{_texmf_main}/doc/metapost/hershey-mp/

%files -n texlive-huffman
%license lppl1.3c.txt
%{_texmf_main}/metapost/huffman/
%doc %{_texmf_main}/doc/metapost/huffman/

%files -n texlive-latexmp
%license pd.txt
%{_texmf_main}/metapost/latexmp/
%doc %{_texmf_main}/doc/metapost/latexmp/

%files -n texlive-mcf2graph
%license mit.txt
%{_texmf_main}/metapost/mcf2graph/
%doc %{_texmf_main}/doc/metapost/mcf2graph/

%files -n texlive-metago
%license lppl1.3c.txt
%{_texmf_main}/metapost/metago/
%doc %{_texmf_main}/doc/metapost/metago/

%files -n texlive-metaobj
%license lppl1.3c.txt
%{_texmf_main}/metapost/metaobj/
%doc %{_texmf_main}/doc/metapost/metaobj/

%files -n texlive-metaplot
%license lppl1.3c.txt
%{_texmf_main}/metapost/metaplot/
%doc %{_texmf_main}/doc/latex/metaplot/

%files -n texlive-metapost-colorbrewer
%license gpl3.txt
%{_texmf_main}/metapost/metapost-colorbrewer/
%doc %{_texmf_main}/doc/metapost/metapost-colorbrewer/

%files -n texlive-metauml
%license gpl2.txt
%{_texmf_main}/metapost/metauml/
%doc %{_texmf_main}/doc/metapost/metauml/

%files -n texlive-mfpic
%license lppl1.3c.txt
%{_texmf_main}/metafont/mfpic/
%{_texmf_main}/metapost/mfpic/
%{_texmf_main}/tex/generic/mfpic/
%doc %{_texmf_main}/doc/generic/mfpic/

%files -n texlive-mfpic4ode
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mfpic4ode/
%doc %{_texmf_main}/doc/latex/mfpic4ode/

%files -n texlive-minim-hatching
%license other-free.txt
%{_texmf_main}/metapost/minim-hatching/
%doc %{_texmf_main}/doc/latex/minim-hatching/

%files -n texlive-mp-geom2d
%license lppl1.3c.txt
%{_texmf_main}/metapost/mp-geom2d/
%doc %{_texmf_main}/doc/metapost/mp-geom2d/

%files -n texlive-mp-neuralnetwork
%license lppl1.3c.txt
%{_texmf_main}/metapost/mp-neuralnetwork/
%doc %{_texmf_main}/doc/metapost/mp-neuralnetwork/

%files -n texlive-mp3d
%license lppl1.3c.txt
%{_texmf_main}/metapost/mp3d/
%doc %{_texmf_main}/doc/metapost/mp3d/

%files -n texlive-mparrows
%license pd.txt
%{_texmf_main}/metapost/mparrows/
%doc %{_texmf_main}/doc/metapost/mparrows/

%files -n texlive-mpattern
%license pd.txt
%{_texmf_main}/metapost/mpattern/
%doc %{_texmf_main}/doc/metapost/mpattern/

%files -n texlive-mpchess
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/fonts/truetype/public/mpchess/
%{_texmf_main}/metapost/mpchess/
%doc %{_texmf_main}/doc/metapost/mpchess/

%files -n texlive-mpcolornames
%license lppl1.3c.txt
%{_texmf_main}/metapost/mpcolornames/
%doc %{_texmf_main}/doc/metapost/mpcolornames/

%files -n texlive-mpgraphics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mpgraphics/
%doc %{_texmf_main}/doc/latex/mpgraphics/

%files -n texlive-mpkiviat
%license lppl1.3c.txt
%{_texmf_main}/metapost/mpkiviat/
%doc %{_texmf_main}/doc/metapost/mpkiviat/

%files -n texlive-mptrees
%license lppl1.3c.txt
%{_texmf_main}/metapost/mptrees/
%doc %{_texmf_main}/doc/metapost/mptrees/

%files -n texlive-piechartmp
%license lppl1.3c.txt
%{_texmf_main}/metapost/piechartmp/
%doc %{_texmf_main}/doc/metapost/piechartmp/

%files -n texlive-repere
%license lppl1.3c.txt
%{_texmf_main}/metapost/repere/
%doc %{_texmf_main}/doc/metapost/repere/

%files -n texlive-roex
%license pd.txt
%{_texmf_main}/metafont/roex/

%files -n texlive-roundrect
%license lppl1.3c.txt
%{_texmf_main}/metapost/roundrect/
%doc %{_texmf_main}/doc/metapost/roundrect/

%files -n texlive-shapes
%license lppl1.3c.txt
%{_texmf_main}/metapost/shapes/
%doc %{_texmf_main}/doc/metapost/shapes/

%files -n texlive-slideshow
%license other-free.txt
%{_texmf_main}/metapost/slideshow/
%doc %{_texmf_main}/doc/metapost/slideshow/

%files -n texlive-splines
%license lppl1.3c.txt
%{_texmf_main}/metapost/splines/
%doc %{_texmf_main}/doc/metapost/splines/

%files -n texlive-suanpan
%license lppl1.3c.txt
%{_texmf_main}/metapost/suanpan/
%doc %{_texmf_main}/doc/metapost/suanpan/

%files -n texlive-textpath
%license lppl1.3c.txt
%{_texmf_main}/metapost/textpath/
%{_texmf_main}/tex/latex/textpath/
%doc %{_texmf_main}/doc/metapost/textpath/

%files -n texlive-threeddice
%license lppl1.3c.txt
%{_texmf_main}/metapost/threeddice/
%doc %{_texmf_main}/doc/metapost/threeddice/

%changelog
%autochangelog
