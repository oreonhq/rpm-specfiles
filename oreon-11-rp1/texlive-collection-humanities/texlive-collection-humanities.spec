%global source0_hash 14355b512f069866c7c0a75147c7dd8be16cb5d9b7a286cb6dc88a539f662f2cc2826336433bb2a4f92258859cc118832a9d414094550705be78d8c9136f0946

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-humanities
Epoch:          12
Version:        svn75384
Release:        5%{?dist}
Summary:        Humanities packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 1e06f07576666fb7b54c78d930f66fef78571469bffc3ef448687c8bbb0d23d41761e17c8ec1293bb6527e31fc70413df1b7de5c9a06514e6aa8242ed90deb09
%global source3_hash ad8f2e42a4a31368000909c5841fddc189bc2331b47f2c64b16ec509bd662a1b82df3ea8b712f0bdf1c40f123ac28221179b4352e20631d9fb776c0b2939bc4c
%global source4_hash 9733edc421691d61eda442c8d7c7a6ab1e05811847b68b3736e44fb90a155810c298353d01ddfc0e2611d4a1644e2361626040dbebc1bb304dba07bf55d2685b
%global source5_hash b6202bb0f2df2351d0b27d167b2f5ab6ba7108b8f760d1b86e1bb89c520fe279f94b2e60add2b6efaaf73f14509572a684920ada2b6f59b75247542b6c3838a3
%global source6_hash ba3c4e41b566d0a26bd9f0d11d8e776fe04a18aac451435ff0283ff273971138407753bd6806f34708c5a2f0c1b2581c71de46bbc2e0c8063c9838b3d946f2ca
%global source7_hash 6fd81f90d0c94644231e911ab44827b77864842a3fa91127fb53114179488e5ffd66a404a1b5afee513e0cd3f4c83f38cae547e6dd6484403926c4c46b5cdec7
%global source8_hash 5ae9356781549cb5ecbdfa33085ede0fdbcb7f131d55484153484c777f88e23cf965507afde803e7bc5b775aeb416b9ee767815b5dbec444a3d21be18c7445f4
%global source9_hash a904b4c9c0c8f3ff1feaaad8d1650b383ff0110bcf463f004938c51bce84ffc860082bf3e598922eedf0aeaa664ef0379ea3304f6dc5b681679d9545026c6bf4
%global source10_hash 3af7da247ff7f9708ef076a3fe110979e7ff07be0afb08597feeda9ae31e60a66eb2bbbb5da015e10566e83a116cc9f2efa56fe91a57717230fb35bd004c209d
%global source11_hash 08393d76bca59dcbd715cc443ffbf7a1e15894ac6a2963d0ce770c96974c14d42283fd9237c215fe454ec4403a21387ba9dee52ea1bd93b83ab4a13fbc65157c
%global source12_hash 148a4c17ce567327825b8a846b7e5972493c7b661f51f71ba55bbb4979c90ffefddeccfa2a324b88386ba66527757f2deb62381a0e1291a7eb1df381e19d11d3
%global source13_hash eb1e327c7cd6f3ad5e06cd48787a5394e488669888fe5a1603168a719b6eacc6ee88095af3b0f2456eca96f7a6fb0d6299ab667f4df0636900c0f4b0bd48be94
%global source14_hash d61da72538a7d83ee902081aefc23f3addf2fd6e5fa7ebb207fdac16546d13602c50419682e842df8f36a899c2c0aba0aaf615bf64202135dd9f470f5391838d
%global source15_hash fc28e1dc8614d836637350a20478a0e8a03121909cb42bfd1cf4caf8e7adc01a4ac3eba08e82c389c41a567cd00f191ecd8938ac40a0a226e2fbdac047ecb733
%global source16_hash b3906f5edd65487c0c973d72543baee38cfab1d9f53cf260e90d60f82b29a85eeca3931aac40f32276769f86aab21a8cbcd68979d00fc570298806f5153e1056
%global source17_hash dd0bf879c497f840d266f5c625e77b64d88757300a9c6e855676116e51626c24317b5a122f719d788411c997882c1a282fecdcd5c6207b2feb06f3558dc37871
%global source18_hash 582f86d63318543ab785575ebc59be6ed2ce38fcb6c32d26f5eaf2a7e601ca76f8c4c66285187996d9840b1dde0dd8dd3b9de5801e6776b02d0e903de1d38d60
%global source19_hash aee4c29230fd7c6f1e063ef5011f23bc1432dd772b930a4b0c8b033a4cbbbfcb4fd5df7b46e841db8b851052d8adb9de5dec571c743f7f5b8f13214fb81cb2c6
%global source20_hash 75095bca5c801cd8a4931c778d133148dab6874d4c05d1e1d69cbac6427ddc1b5cff7343445dc9a0932d7d3269aa41b11777baaf32f3dd973785aedefaeb643a
%global source21_hash 4fb033b386109509fff21b4c5f8bce1c069546d4aece30aed5e37fdbb38b4201f77dfbd617027c0c117d8bc5caf7c81fd53cbed661885963d10f43c57752883a
%global source22_hash c15ba71a0c37a05df2d334bba94797d70c345af0d443dee2ca02be4e52bcd2e130b9a5d5c1904c1c72a8cf423d5d67b84c6ea7b8517380d3cc57700b81535cb8
%global source23_hash a1af1af4e137425e0359c96fd9001fec6da403ad9478d5a9024648a200082d98cf9e93ccf310dd0257d8179d996b422b58d513ad42380316304aeadac6a0fc7b
%global source24_hash 4103aa370bc8314433b5cc9242390340467591bc38e2f5b820f9d35a1951bb9fe9e384b1d3c64a0434b3c3dc87c42463a0af5d9ff872180bc2b7a08d4b40c080
%global source25_hash c59cfa6957a21c5e74d9a15b7621536170137447111f9a88295e79aa7a29dcbb3d1f1f1367afd7243d2506b864a53df41b0e10419592a5e4e12af8e1e90216d4
%global source26_hash 963ca793d2d6b0fd0c32d32a9db848b96fd5201868c6bc8d3b88ba62838e398a588e187c41434d328a8651a0f31640c9ce5f14ec4218b6025b6bc50cbc33f67f
%global source27_hash 21d7faef59a965bacef6c00e9c656da6d9117716609073764c1f191db4f36efccace8506de9fde1777c8410689077ef2682bb149fcb78faac1b17b50548834fc
%global source28_hash d617c13bc755330b3b4d62d2345ac135210c5c598cf88489b59b350864dc894da6d66f4c0911d051dc14cb3027b2d14653d50e8010946c40d4150c0cfcb511c0
%global source29_hash 3bfadf293561df4efe0739acd28258a94a164019d6cdc30b36273aedb3840161d57c615b7eb2f83c9cee1f5e10be98841f883b8dbf610e011353404240f55eb6
%global source30_hash 2014fc075fab46dc109a290838b9aa5e52bd0a33c370bf822ad6fb74a8d492b58b5ec1adcdf1d0532cf8a53ed3de3eec80a87e550508675e2bebc048f3e89bde
%global source31_hash 13b1ea6059e50c1b13ce83b7723f88a78b349d442494898002bb0069efdb209055b3bdc04de73ba70fed1adc63ba87a4185526724624fd3cce15a23ddd2c4927
%global source32_hash f5e09cb98551cf83dc00e188948ec63eadb6975b1ee22f1d3854825d65c9d382b40a0cb2128ee9e66d9d02a936686d1a6b0ad4773196a236b9bf089bfbc8296b
%global source33_hash 63e4ee4ffc0576252d18e10e3c9241cc3454f9a48627045f48d24d2fb9401ad0de37487314776567017ac085782b5dcb311ba3990ecb8b74da08cb8d84d0222d
%global source34_hash f82d96ea63af1f77da2a557a7fa0e5b400c2a6ce2ccdf02756e05c4f0a059ac384581723217f56970a68ad61929b537a5d4a9290af5679c91545333621db6883
%global source35_hash bb48ca0f3adfdac7b0c7f31e7e7ebb53c0b61e5f8236957dd13433e0d1f9038a9d344a6b7e8fef238e23bca74ab946a466736e0620c6e187c2291e7739ff2316
%global source36_hash 98692f781fead4dc292648153ca18a05d03f2c44174bce8b2f72e85fd1e98cb5ef0fb67c12f33dc982f1d04958873ea4e78f486fadb0c94544ecb66180ee52bf
%global source37_hash 7e37c0c2e8443aedd6462251f603e2eef9cbacc45d980d79bf42cdc64b7ab0a5d81f50ae65251c17115265c45e641a5930de640099f04dc8112155f68ce9adf0
%global source38_hash b7bee17f7a69ef44a06d2915b26ceea2e63d386be25029fdaf19b3626fba28d4005afe3ec7275d75e6007efa76eb486daff54dd36ae1d44e77ca8e7bfe448c59
%global source39_hash 82a7ac9c378e2c034f3c7bf142d9978fa9f276dad8300f009b0ae9d1c45b519dd02e7729c9aa72d39f36f2cdc070684fa5e44784a281c38d26c29f77704365e6
%global source40_hash 08426bab6c0627e945d620a338c6081a8a21d80567d4a4b686617d0d57c99b1e148f5e5c3406a0337ee4ad61bd795dca353c28b0f33d397c5b47515969fa5951
%global source41_hash 4d19c663f73791712d9c24361d8e2a0c2faf25bdac15dcce48825f02468f6a798eff7e147f531368bcc8d7e2a1938202b5614e2434cd46866f359f8349564adc
%global source42_hash 4d6fd00247c6c915956679674dd029048cb96ac3bc97606c0a299bbaff24a4cbb9440d557eb2945151720265ecb27bf15c638c003e1039dafee56471dfa03945
%global source43_hash ede48ff67dacf107baf50be345b042a7b64c815442875281241b7de4c3be56ec40c969e40ec69669f31058bbbe9b27c51cae25938d93bec99a8c57dfb8e9cb75
%global source44_hash 3b78fab41ed9af5a657987448a60b2005edb40f8ae7bb3b5efe7c5250230acc8a1b930a61efba2808ab78c3b07d0c76d49a7734b33a8e2a5c302caf752dbf5ce
%global source45_hash f67ec5e21d7fbd843fb1d87893d835c1f98583ea5bdbcaf2455c6f7fbaddd7010daf02da7b2444273983432cd5c5f6efe4bded6116130f5301b0de3e26cf55f3
%global source46_hash 511130814ed94c7f0829802a0c3e8e613b0c4aae50854f6e06779448f430e78c8712142fe04d3662b799a488d90944072847dd223b01b642de78c1f98649e79a
%global source47_hash 1c439e351102ae3f768ae38404cc5d98403028fb6fa6088cd53eea40593ee03c10d20955f3fadef41f41af6d23f139ba356a9b06ed735644b67d3f42a076e0af
%global source48_hash 16d4b14025e142be2c0d21509041d99ee2eb9b4b765abfa3102cf79759c79e79f43191f8ba1fcea3d8c7269bdeb6feb0a9efafb1f1ea195b58ed97a307386bdf
%global source49_hash 0cc3548f9a640e3c6756298ff609bc5458f30fe096fb8557881356624dcfc6f81068af21731df3c5635381ef98c9b30c1f297213b8489e2bab8840c78f723ed8
%global source50_hash b465117d5634dc4eeaefbc2c12a4d0fb892f4a27ed66057938701fe51e4dedfb5b7f28d796145d89a59b2667cf61c7175803f72e5970cf81244329130d173136
%global source51_hash 7e7fa49106457f13aed11bcf80a1e38f000f5161e9a67bdbb174371db63a3953109f26da3cef8781d2c13abb4b86d5cb0c2b1b41e6f2cd3584512bed1a67cf6a
%global source52_hash b8068fd9cac47601ba4c6ce1282d29f66e19bf059ebb4b2ee41d0c7137916b62410f75443989f77fe8394a7bfb5444f84f8080c0c7d97c32e87b891f58e5cf25
%global source53_hash 92276a48a53e1994e46a6f4d26519178abe78e32d1ff2d0fa421b510e46603f13c22a011e7ff52be59ffcf3d2452482124fc9debd4b8fdabda2e196e6559fc64
%global source54_hash f9bf7792ac09a6b5a69ae642e0becbcb1ed0c2eea3254b31da62bb9b7e3e161c24109e0bcacc8b89e3d03426710378f04e13a05be467115eaea2be028f8e5812
%global source55_hash 6a348acfd0e0701954195210bc717666308743f5f282b9efb7a253ab860a0372ed383cc2c8811527eeb2ed72c46be95cfb9e133d156fe8b906b67ed5140437af
%global source56_hash 686dbb33df2670af909a80863943a8870ecef128679ab679f3d90d1747042b752c9aea15660c962b0f02418233d4d152e64357d5b57884a2fc2371acb3d90a52
%global source57_hash fe424a7db4be743168c4b1016fc25c95d33cf9d66767b39db0e79a5ba1bb667c76b9b5f10b23a08449362a3fef281d60f0b53e2b0f196846efe9f4765f3f08c6
%global source58_hash 449cffd6dd9cb9e6b91434788c051b21b0bfc74d8203de777f08307c7cb883472c436a146fbc16b1c10e42389ce9a961a3c3b9d20fac9563bc7edad7dd6d5b4b
%global source59_hash c6941d669a2dd43a90adea97b657d3df0c261976ca1916ee09b16c288462dec644bd84581a9cfafffaa8a9426a5ad7cd4c91f52a291652fae1d612b537a9f94c
%global source60_hash a1ae1dd7e25701c8d2e703d3eec317d0e318226bb2500e2791ddc65cd9407f3a323b765b1681fa1ec662ae0aacda787c9dcffd178e8937103c638980db19e1b0
%global source61_hash 9049df1119fe10f90e4ae230279ec2828d06aee13987977c77745e7752462d54c35cd1426c9745108bf10ec170cf4e9fedddadcb1740735b31555609c5480546
%global source62_hash 5b5f0814c7d2e9e59ad3858e8a643043b9de85a4d199fba95f4b59605594bfd8cd735de587eafbe5d25c1c130bf761d174a78572e53e151066ed4ed5ef4eb22b
%global source63_hash 6d0de896d9e743a32ad9b50210597554add05fb7353962f26be18c19ff303d15259af123282fc6894987558662f429b8e9e0fa355f201b3137f4f3963188c34d
%global source64_hash f2454ca4af4802969873f387928f22e034febf0f135587e888d3ca1b0d1492df8ea1ec4138903192fc6a3000665dc90cfd95d38e8ca90e6b181485445c104ce4
%global source65_hash 089d4453e755ba67abeb226d57e63fa688bb79e8862a5b4f280301137fab4df4cb897ffbff13597865fdd31f413d3dfb05158c7c9996fc2f502605bac99178ca
%global source66_hash 6e592585309e31930c0a7a119b5a8a3f0c6f5f0f9b6f11731fd2daa14fc750de2159d4d20076a4b6941d37c5dfccdae1a9b641e733b4f3db1ac5501339e6f163
%global source67_hash 0f279f63f59126dddbe6c9bcc99c1acbb38b0c2dcae1cf6922c0044ce763b2593988f23214bd054dc758bfd1e20caf2d6234501f9fc9c782ffdf935b79ea3b3b
%global source68_hash 406e846ebe7ed721218368cd00a021edc41af41f1ccb5989925abad92d4cbf4d604abac8144945599530c85917d9404141052ba9891b778d1006b7d339499041
%global source69_hash 6efbea453691fe2af7f436e79e1a486abf5dda14e2457ca3c1c2bda9c8461016d4436eee82a18b079a2491e1c4eb2f7dcbaeaf8fe8b8c7846e744f02da8e3b6f
%global source70_hash 725c80a8133637d9caaf1fe28d99d6d1994a0c01693310ef971e373009fce34c3575cde714f9b8d1c15acbb1620000c59b01cf7c5a2322e8f029461b2d0dc5a7
%global source71_hash 5819f47565f3c258c7c1b0c4a565ada7b7d0b29c47ef18fd005085f6da8ff0d53d75a7a6a8ae187d3eceec8c66ad879853e76d1424828f2ab96c2319ca4baf0d
%global source72_hash c375a62dd5d220adfcb99ec42ecf8aeb75161d5c1ef542578a1911d3b3e343144716c26f518df448583ed4443242c1e66479f7c34cf074bd4d257d1a4e8c7358
%global source73_hash 870712c7c61ba66e7a45e04e6e5ae4be8f6adf70d00dc26f7d18c2b12165bdf9f0a724987e4ae6995047ad79ca5081ac3091eb063e11edc45bf9af288385515b
%global source74_hash 1a09e6dbde9c24d88e21fffe24ead7ee7567a2c7bccd2ef33e49eb1bc8eff2befb3828a87616872f63d1d8eeba21814cefc8bbe756b17f887558449aaccb1668
%global source75_hash cf284387780c9b2f4a79ebdd781388525aeb2a03ad9d85048061a6c43728bb6f2f4fc840ebb499a44a3fdf612ff4a20f36c17a377f959be813b4ee4d12288fb7
%global source76_hash 0465e183077f7daa57d2bbc5f1a76afa72770718d2dc969ebc3078b213738f5ae3919f3ebbee04ae54ff7b8ad6e35630fb22293b5cdac31ee5bf31680433ad15
%global source77_hash 80ea19243537e769c49a3411e036c5811b19586fda3878894126a151af4ddff46a554db7bc07f488f692fe9efd0934149c8c94cde75b92c880bfcc28218ae5a1
%global source78_hash 86e91b884be131df6b4da6441a9fbeb872e0f345eed49005ef74d58eb3ef8a2724da98cc810a51b58d45047d77545ac6b9512612b5946ba29d443dd14bbdb263
%global source79_hash befa46f8ef7c4c89e18339ececbd53341aa50d6bfc8927001d17395cba42db0f0ca3414619c746c78e4f5f4f9cb1f6db813defc7b89299f5b29e9c0866852c82
%global source80_hash 062e3017f077a7717ac74884ec17f1e776280dca3508cc62abfddbcd73c30150089e9fb3f2ffbac1624b1e709640dbbb229722bb41f2bb9c66aa41c4c9d889e1
%global source81_hash e8bb2d40bb5817e68943e683f1440276cd68b976ac2d0c6c19b0168cac81a3b2e431aeca1922ecd613c9157d506453f6de43ac352ebc546683e1e8e2bfbcfafc
%global source82_hash e9bba80cd6fcd7b1e7b0e46fe594b3e25986dac5fe39d329ed4b8e15bc6b542e033a392abcad4e0c67d5401066703a1a89658ebc612d2adcf846de81b34fb78f
%global source83_hash e8e3ffc366be12ec5273c85a352a6c44ee22af072fdc9e63db390c0d3435e390c28ca83279a1a54f95af991890b7e47ba896612407ed605e229ec184cb1e5096
%global source84_hash eb9fb0ce2891008b639530bdc906b37ba7090f9a4b73d911a308e353882f992da6ff27af124d191283d75d5371adbf749d7813703f4962ae4141b7830f998fb4
%global source85_hash b89abcb1d2fadb4ee2eb14c7b0ec469a610bbcd8868c1162b964456d00d7aaab3118f91a3bd5da4c6c8ffda707e0edf24d158d075b42c929109b4a2f15f19f05
%global source86_hash 034795568410f28105e50f9d0097ed3bba502bc495a88129a7fa61e57da111462ac519702012a4ab9b6c7fc01920b3d21e5c4747098b3f5941048aabc541801c
%global source87_hash da9168bd66986e901cf61c9311c792d26496494ae00a83c429fcf489a59e7e657b967f3d666cfb1ecc60be2a9257e194e870954431045fb5e4a8539e9aaf26fd
%global source88_hash 9138482d740e9ed83c1a18eb497d6b06cbd75ae11ff0f2663fe973311ca7dbace1758d89c23cfb3f7d44b728f2c113d19f3d82ff1274b44c175d38e7ccfe7bcb
%global source89_hash 1961e563535b3f22124605bf9fbea028243aeb88a396b6bd3741ec4e1c43fa06bdfbd7c58564f5400e0541d1ee53193669646f2fea937123248d7129be393082
%global source90_hash 9f381007c2526f51483d7c190cd7cf86cb399e95475841900ffa8f522d3da71f4f451b42562783d756e252e513ca1f9e9e8586517057a8f6b881cbbecb5c3987
%global source91_hash c16142acf0c3f9e4f347c9ceff7a6c29557c0c2c4d2232ce9df146279b3cd4e1019e703479f426709a3feeb6ac46fb91f7dcee8cad35b19c83c9893661322f96
%global source92_hash 5d5761fc11721b029cb12cf40e7e1f12ae791ebce9382cb6d120cefc11ae54c46e68d5724de25f294cdbda0221f99ce7d5940b54d4e7eca1a50e131b0c29647d
%global source93_hash 5dc05f3b10714a44179340c7bda1af04b80b146b75a90fd91dc4a6ecd7f8b1dfcbbc59d34be1178252b923fa18f52f0fe80ef15fbc6c4e71a8073e648befc755
%global source94_hash 366aa5059888426c74dc7686a8bb2c6d730331bf959d20ddc608f6934add247e3066c07fbf099d8849f9104a6c07e72fcea059ec00960b0e1074c30bac9e75a3
%global source95_hash 54613a88ac48e09c608ce999adc88430e02b65580f443450eb1dbeb179064c49e1ddca990e5616b79ef4f6e6bd069362899e663bea37cf7bc443534756676b03
%global source96_hash 6e39e34a7c293f503949da66f1d5ebc65ae0388dc56e87992e9fc4daff1a250196afe68150be14ee2ec3242393ce9e5ea7b681cba31b7ed1c2d58526f6506554
%global source97_hash 550c21bcd8af04041f1fac11f2be3ae2a1f01265ad6bf31243569820c7b8d83f32ccd0cdbcc4d5a7a5905ae9aa0512a449a1b2d6923affceb344152e6c12d72d
%global source98_hash d14dd76c4b1abd9ff7adbef7e4c3bc1f732156dc2d989787bed7382e0288c44dcde18ce05143e6af03ebe83c753bd2b6682cb4f56c73934ca4209a114eb9e3ef
%global source99_hash ed723ffc17a98c8d4a8c960f56a3550ea74db84fdd06d26b08b5c46b12310fdb9b7b7719ffa25e8ddd21f17642f5f64f1c96327066a131c468cee8ff185cb199
%global source100_hash 974795ca0b4a286077e38f4b3b120cf9fe243d450b87b8397adec2c5425b865cdfbe70b86b815d513edb6ae7051d9ad3003fcd6a15b5b02b624dcd4ee0534164
%global source101_hash 9aa4407d1b317442dd76f762af5b673460bbbcec89e47835521688085183e00ba9dbb70dc9e86a95235bd9a32da701c846ceb2985dc70894ca8abe334428a532
%global source102_hash d73410293db8858f8b76b2bbce50c6ecd4d08da328d5c9edbd6deb2f2e79c78d6cc0868147db2d0b8c1942bc3e178b8195712366f749b6eda216b25317cc7d66
%global source103_hash 93eeebe83ed4315a637a3bc971ad90b9bea287f92e70bf0038c3363b9cf8590dd1cff3dbaea1a5debaf53771313957a8d531ce84a8926b2e02c41c346b3f6410
%global source104_hash 8472bc96265ea7fd3be748f147238b6852079ba002f9c7548f5a5e8cb0f34a8155a799635ee5e31b22bb30554795a6fd08e62312b25ce83e727e10f6ccd13f37
%global source105_hash 82df4a8fa154a09cd8231c21f3a450a089796306e8275b17291bfc903ef00b316a1ae0a4175637294ecbed0dd6eeffa7baf134d60352284aa07e0a1a0224c205
%global source106_hash 1652260a3e946a8847ceb7f937893bad27a24737d9b3573466f7369ce9cdbf900af0ef6c7f0bf3033200664da736e8232c3fbf6db61bb7d51acec1010d13a3e0
%global source107_hash 922ce1569fce889bc4608e9a5da4a45b7c3d2e80303ac36167efe6767c266844664de00384447e288da70383fe91261e5914394a6fdf8644349f785600271e5e
%global source108_hash 695d16e6630efa10363d6c94f410cdf11947dd0c0e59987cdf01e0c699c53c994a702b3802b8830e38b6f5b0ce654af5710ef93b094fbc08954eb8d9bc5d2915
%global source109_hash f2fce885e0aa65d42413ad7ba26a38ff787fed8c1ac5d6434e949e229d4f728a055a6a2ed80f36fe94f6fdf11cac3bafbd2a945cb9bf2ec0b436eacbe1ba58aa
%global source110_hash 2f8f254fb1b41efbb210dd3e88bc6e26b1d554c6ba1b87227a5b956105229aa5bd7074bcad6e02bd914c122d4496cc4185b34f998fd3d8334c2b2a7ee1a7e953
%global source111_hash 27ffcc0c826ddd1f434a47ea4302c4456835adcc3c66ca5329da9191e28ebe4eb5ae375fa7048fc539e57b9bd02c0903bd135a3c38ba87d52d8547d5960d4fb2
%global source112_hash 6153417c5d2677a56adf031c5f2f27e4c2bf204c0acef1cc5cd49355370aa336814bad7d2be00e95d22bcf73b9b69105a255d15f29ed650511c0eccc3c9bda07
%global source113_hash 8c507ec7719b92f2cf82527c7799b073ff2679cf820528b489eb7d8c83d28d098033760cf092bceb9ee7e28fec15eb580122c080b982dbb12e0e65176121e84c
%global source114_hash d15e3a433549b27d590a7630f80a92872dd3e1693b45516dba488c19e7285a5c5f520fe052767e4665767f613c08e05d20e2696c0e57c2751ec3f29fa6ed85a0
%global source115_hash 77d537cd007e44c7663906ab474bf52a259e1e6da4e539fb92c5779b83844ded4af4ffb9a052475ee6b932df6bd886d89de944dea468dcef105f6a58c32fb772
%global source116_hash 5f78d2d61050d9ed84d56136fe59b4674f4e03a536015e3ebc3b9500dd8a08878164ce9fb1aa9ca9a1262a000149061f3fe22f10cfd68941316aa186b81fe923
%global source117_hash 7b4ca312ea917329260eb0a19bd504ac2f3ddfb5f066806296b164fc541bfe26e6ed1c03ffac5b52af6b19fb4ba1e77b5228ac4b4db0c2ee8f2394fc0f888d09

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-humanities.tar.xz#/collection-humanities.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adtrees.tar.xz#/adtrees.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adtrees.doc.tar.xz#/adtrees.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref.tar.xz#/bibleref.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref.doc.tar.xz#/bibleref.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-lds.tar.xz#/bibleref-lds.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-lds.doc.tar.xz#/bibleref-lds.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-mouth.tar.xz#/bibleref-mouth.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-mouth.doc.tar.xz#/bibleref-mouth.doc.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-parse.tar.xz#/bibleref-parse.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-parse.doc.tar.xz#/bibleref-parse.doc.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/covington.tar.xz#/covington.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/covington.doc.tar.xz#/covington.doc.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dramatist.tar.xz#/dramatist.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dramatist.doc.tar.xz#/dramatist.doc.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvgloss.tar.xz#/dvgloss.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvgloss.doc.tar.xz#/dvgloss.doc.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecltree.tar.xz#/ecltree.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecltree.doc.tar.xz#/ecltree.doc.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edfnotes.tar.xz#/edfnotes.or11.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edfnotes.doc.tar.xz#/edfnotes.doc.or11.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edmac.tar.xz#/edmac.or11.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edmac.doc.tar.xz#/edmac.doc.or11.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eledform.tar.xz#/eledform.or11.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eledform.doc.tar.xz#/eledform.doc.or11.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eledmac.tar.xz#/eledmac.or11.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eledmac.doc.tar.xz#/eledmac.doc.or11.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex.tar.xz#/expex.or11.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex.doc.tar.xz#/expex.doc.or11.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex-glossonly.tar.xz#/expex-glossonly.or11.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex-glossonly.doc.tar.xz#/expex-glossonly.doc.or11.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gb4e.tar.xz#/gb4e.or11.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gb4e.doc.tar.xz#/gb4e.doc.or11.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gb4e-next.tar.xz#/gb4e-next.or11.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gb4e-next.doc.tar.xz#/gb4e-next.doc.or11.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gmverse.tar.xz#/gmverse.or11.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gmverse.doc.tar.xz#/gmverse.doc.or11.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interlinear.tar.xz#/interlinear.or11.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interlinear.doc.tar.xz#/interlinear.doc.or11.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jura.tar.xz#/jura.or11.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jura.doc.tar.xz#/jura.doc.or11.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juraabbrev.tar.xz#/juraabbrev.or11.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juraabbrev.doc.tar.xz#/juraabbrev.doc.or11.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juramisc.tar.xz#/juramisc.or11.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juramisc.doc.tar.xz#/juramisc.doc.or11.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jurarsp.tar.xz#/jurarsp.or11.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jurarsp.doc.tar.xz#/jurarsp.doc.or11.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langnames.tar.xz#/langnames.or11.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langnames.doc.tar.xz#/langnames.doc.or11.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ledmac.tar.xz#/ledmac.or11.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ledmac.doc.tar.xz#/ledmac.doc.or11.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexikon.tar.xz#/lexikon.or11.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexikon.doc.tar.xz#/lexikon.doc.or11.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexref.tar.xz#/lexref.or11.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexref.doc.tar.xz#/lexref.doc.or11.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ling-macros.tar.xz#/ling-macros.or11.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ling-macros.doc.tar.xz#/ling-macros.doc.or11.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguex.tar.xz#/linguex.or11.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguex.doc.tar.xz#/linguex.doc.or11.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguistix.tar.xz#/linguistix.or11.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguistix.doc.tar.xz#/linguistix.doc.or11.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liturg.tar.xz#/liturg.or11.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liturg.doc.tar.xz#/liturg.doc.or11.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liturgy-cw.tar.xz#/liturgy-cw.or11.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liturgy-cw.doc.tar.xz#/liturgy-cw.doc.or11.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metrix.tar.xz#/metrix.or11.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metrix.doc.tar.xz#/metrix.doc.or11.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nnext.tar.xz#/nnext.or11.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nnext.doc.tar.xz#/nnext.doc.or11.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/opbible.tar.xz#/opbible.or11.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/opbible.doc.tar.xz#/opbible.doc.or11.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parallel.tar.xz#/parallel.or11.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parallel.doc.tar.xz#/parallel.doc.or11.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parrun.tar.xz#/parrun.or11.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parrun.doc.tar.xz#/parrun.doc.or11.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phonrule.tar.xz#/phonrule.or11.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phonrule.doc.tar.xz#/phonrule.doc.or11.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plari.tar.xz#/plari.or11.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plari.doc.tar.xz#/plari.doc.or11.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/play.tar.xz#/play.or11.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/play.doc.tar.xz#/play.doc.or11.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poemscol.tar.xz#/poemscol.or11.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poemscol.doc.tar.xz#/poemscol.doc.or11.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poetry.tar.xz#/poetry.or11.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poetry.doc.tar.xz#/poetry.doc.or11.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poetrytex.tar.xz#/poetrytex.or11.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poetrytex.doc.tar.xz#/poetrytex.doc.or11.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qobitree.tar.xz#/qobitree.or11.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qobitree.doc.tar.xz#/qobitree.doc.or11.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qtree.tar.xz#/qtree.or11.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qtree.doc.tar.xz#/qtree.doc.or11.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reledmac.tar.xz#/reledmac.or11.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reledmac.doc.tar.xz#/reledmac.doc.or11.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rrgtrees.tar.xz#/rrgtrees.or11.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rrgtrees.doc.tar.xz#/rrgtrees.doc.or11.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rtklage.tar.xz#/rtklage.or11.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rtklage.doc.tar.xz#/rtklage.doc.or11.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/screenplay.tar.xz#/screenplay.or11.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/screenplay.doc.tar.xz#/screenplay.doc.or11.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/screenplay-pkg.tar.xz#/screenplay-pkg.or11.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/screenplay-pkg.doc.tar.xz#/screenplay-pkg.doc.or11.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sides.tar.xz#/sides.or11.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sides.doc.tar.xz#/sides.doc.or11.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stage.tar.xz#/stage.or11.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stage.doc.tar.xz#/stage.doc.or11.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textglos.tar.xz#/textglos.or11.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textglos.doc.tar.xz#/textglos.doc.or11.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thalie.tar.xz#/thalie.or11.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thalie.doc.tar.xz#/thalie.doc.or11.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theatre.tar.xz#/theatre.or11.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theatre.doc.tar.xz#/theatre.doc.or11.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tree-dvips.tar.xz#/tree-dvips.or11.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tree-dvips.doc.tar.xz#/tree-dvips.doc.or11.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/verse.tar.xz#/verse.or11.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/verse.doc.tar.xz#/verse.doc.or11.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xyling.tar.xz#/xyling.or11.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xyling.doc.tar.xz#/xyling.doc.or11.tar.xz

# Patches
Patch0:         texlive-rtklage-scrpage2-obsolete-fixes.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-adtrees
Requires:       texlive-bibleref
Requires:       texlive-bibleref-lds
Requires:       texlive-bibleref-mouth
Requires:       texlive-bibleref-parse
Requires:       texlive-collection-latex
Requires:       texlive-covington
Requires:       texlive-diadia
Requires:       texlive-dramatist
Requires:       texlive-dvgloss
Requires:       texlive-ecltree
Requires:       texlive-edfnotes
Requires:       texlive-edmac
Requires:       texlive-eledform
Requires:       texlive-eledmac
Requires:       texlive-expex
Requires:       texlive-expex-glossonly
Requires:       texlive-gb4e
Requires:       texlive-gb4e-next
Requires:       texlive-gmverse
Requires:       texlive-interlinear
Requires:       texlive-jura
Requires:       texlive-juraabbrev
Requires:       texlive-juramisc
Requires:       texlive-jurarsp
Requires:       texlive-langnames
Requires:       texlive-ledmac
Requires:       texlive-lexikon
Requires:       texlive-lexref
Requires:       texlive-ling-macros
Requires:       texlive-linguex
Requires:       texlive-linguistix
Requires:       texlive-liturg
Requires:       texlive-liturgy-cw
Requires:       texlive-metrix
Requires:       texlive-nnext
Requires:       texlive-opbible
Requires:       texlive-parallel
Requires:       texlive-parrun
Requires:       texlive-phonrule
Requires:       texlive-plari
Requires:       texlive-play
Requires:       texlive-poemscol
Requires:       texlive-poetry
Requires:       texlive-poetrytex
Requires:       texlive-qobitree
Requires:       texlive-qtree
Requires:       texlive-reledmac
Requires:       texlive-rrgtrees
Requires:       texlive-rtklage
Requires:       texlive-screenplay
Requires:       texlive-screenplay-pkg
Requires:       texlive-sides
Requires:       texlive-stage
Requires:       texlive-textglos
Requires:       texlive-thalie
Requires:       texlive-theatre
Requires:       texlive-tree-dvips
Requires:       texlive-verse
Requires:       texlive-xyling

%description
Packages for law, linguistics, social sciences, humanities, etc.

%package -n texlive-adtrees
Summary:        Macros for drawing adpositional trees
Version:        svn51618
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cancel.sty)
Requires:       tex(epic.sty)
Provides:       tex(adtrees.sty) = %{tl_version}

%description -n texlive-adtrees
This package provides a means to write adpositional trees, a formalism devoted
to representing natural language expressions. The package relies on epic and
cancel.

%package -n texlive-bibleref
Summary:        Format bible citations
Version:        svn75257
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsgen.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xstring.sty)
Provides:       tex(bibleref-xidx.sty) = %{tl_version}
Provides:       tex(bibleref.sty) = %{tl_version}

%description -n texlive-bibleref
The bibleref package offers consistent formatting of references to parts of the
Christian bible, in a number of well-defined formats. It depends on ifthen,
fmtcount, and amsgen.

%package -n texlive-bibleref-lds
Summary:        Bible references, including those to the scriptures of the Church of Jesus Christ of Latter Day Saints
Version:        svn25526
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bibleref-mouth.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(bibleref-lds.sty) = %{tl_version}

%description -n texlive-bibleref-lds
The package extends the bibleref-mouth package to support references to the
scriptures of The Church of Jesus Christ of Latter-day Saints (LDS). The
package requires bibleref-mouth to run, and its reference syntax is the same as
that of the parent package.

%package -n texlive-bibleref-mouth
Summary:        Consistent formatting of Bible references
Version:        svn25527
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fmtcount.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(bibleref-mouth.sty) = %{tl_version}

%description -n texlive-bibleref-mouth
The package allows Bible references to be formatted in a consistent way. It is
similar to the bibleref package, except that the formatting macros are all
purely expandable -- that is, they are all implemented in TeX's mouth. This
means that they can be used in any expandable context, such as an argument to a
\url command.

%package -n texlive-bibleref-parse
Summary:        Specify Bible passages in human-readable format
Version:        svn22054
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bibleref.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(scrlfile.sty)
Provides:       tex(bibleref-parse.sty) = %{tl_version}

%description -n texlive-bibleref-parse
The package parses Bible passages that are given in human readable format. It
accepts a wide variety of formats. This allows for a simpler and more
convenient interface to the functionality of the bibleref package.

%package -n texlive-covington
Summary:        LaTeX macros for Linguistics
Version:        svn77216
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(varwidth.sty)
Provides:       tex(covington.sty) = %{tl_version}

%description -n texlive-covington
Numerous minor LaTeX enhancements for linguistics, including multiple accents
on the same letter, interline glosses (word-by-word translations), Discourse
Representation Structures, and example numbering.

%package -n texlive-dramatist
Summary:        Typeset dramas, both in verse and in prose
Version:        svn35866
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(dramatist.sty) = %{tl_version}

%description -n texlive-dramatist
This package is intended for typesetting drama of any length. It provides two
environments for typesetting dialogues in prose or in verse; new document
divisions corresponding to acts and scenes; macros that control the appearance
of characters and stage directions; and automatic generation of a `dramatis
personae' list.

%package -n texlive-dvgloss
Summary:        Facilities for setting interlinear glossed text
Version:        svn29103
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dvgloss.sty) = %{tl_version}

%description -n texlive-dvgloss
The package provides extensible macros for setting interlinear glossed text --
useful, for instance, for typing linguistics papers. The operative word here is
"extensible": few features are built in, but some flexible and powerful
facilities are included for adding your own.

%package -n texlive-ecltree
Summary:        Trees using epic and eepic macros
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ecltree.sty) = %{tl_version}

%description -n texlive-ecltree
The package recursively draws trees: each subtree is defined in a 'bundle'
environment, with a set of leaves described by \chunk macros. A chunk may have
a bundle environment inside it.

%package -n texlive-edfnotes
Summary:        Critical annotations to footnotes with ednotes
Version:        svn21540
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fnlineno.sty)
Provides:       tex(edfnotes.sty) = %{tl_version}

%description -n texlive-edfnotes
The package modifies the annotation commands and label-test mechanism of the
ednotes package so that critical notes appear on the pages and in the order
that one would expect.

%package -n texlive-edmac
Summary:        Typeset critical editions
Version:        svn72250
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(edmac.tex) = %{tl_version}
Provides:       tex(edmacfss.sty) = %{tl_version}
Provides:       tex(edstanza.tex) = %{tl_version}
Provides:       tex(tabmac.tex) = %{tl_version}

%description -n texlive-edmac
This is the type example package for typesetting scholarly critical editions.

%package -n texlive-eledform
Summary:        Define textual variants
Version:        svn38114
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(eledmac.sty)
Provides:       tex(eledform.sty) = %{tl_version}

%description -n texlive-eledform
The package provides commands to formalize textual variants in critical
editions typeset using eledmac.

%package -n texlive-eledmac
Summary:        Typeset scholarly editions
Version:        svn45418
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(eledmac.sty) = %{tl_version}
Provides:       tex(eledpar.sty) = %{tl_version}

%description -n texlive-eledmac
A package for typesetting scholarly critical editions, replacing the
established ledmac package. Ledmac itself was a LaTeX port of the plain TeX
EDMAC macros. The package supports indexing by page and by line numbers, and
simple tabular- and array-style environments. The package is distributed with
the related eledpar package. The package is now superseded by reledmac.

%package -n texlive-expex
Summary:        Linguistic examples and glosses, with reference capabilities
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(epltxchapno.sty) = %{tl_version}
Provides:       tex(epltxfn.sty) = %{tl_version}
Provides:       tex(eptexfn.tex) = %{tl_version}
Provides:       tex(expex-demo.tex) = %{tl_version}
Provides:       tex(expex.sty) = %{tl_version}
Provides:       tex(expex.tex) = %{tl_version}

%description -n texlive-expex
The package provides macros for typesetting linguistic examples and glosses,
with a refined mechanism for referencing examples and parts of examples. The
package can be used with LaTeX using the .sty wrapper or with PlainTex.

%package -n texlive-expex-glossonly
Summary:        Help gb4e, linguex, and covington users use the ExPex glossing macros
Version:        svn69914
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(covington.sty)
Requires:       tex(expex.sty)
# Ignoring dependency on gb4e-emulate.sty - not part of TeX Live
Requires:       tex(linguex.sty)
Provides:       tex(expex-glossonly.sty) = %{tl_version}

%description -n texlive-expex-glossonly
The ExPex package by John Frampton provides very fine-grained control over
glossing and example formatting, including unlimited gloss lines and various
ways of formatting multiline glosses. By contrast the cgloss4e glossing macros
provided with gb4e, linguex, and covington, although very capable at basic
glossing, lack the degree of customization that is sometimes needed for more
complex glossing. On the other hand, for those users who have heavily invested
in using either gb4e or linguex, or covington, shifting to ExPex can be quite
daunting and burdensome, especially since the basic syntax of the examples is
quite different. This package is an attempt to have the best of both worlds: it
allows gb4e, linguex and covington users to keep using those packages for basic
example numbering and formatting, but also allows them to use the glossing
macros that ExPex provides.

%package -n texlive-gb4e
Summary:        Linguistic tools
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cgloss4e.sty) = %{tl_version}
Provides:       tex(gb4e.sty) = %{tl_version}

%description -n texlive-gb4e
Provides an environment for linguistic examples, tools for glosses, and various
other goodies. The code was developed from the midnight and covington packages.

%package -n texlive-gb4e-next
Summary:        Linguistic tools
Version:        svn72692
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gb4e-next.sty) = %{tl_version}

%description -n texlive-gb4e-next
The package provides gb4e users two relative example reference commands. \Next
refers to the next example in the document and \Prev refers to the previous
example. No explicit label command is required.

%package -n texlive-gmverse
Summary:        A package for typesetting (short) poems
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gmverse.sty) = %{tl_version}

%description -n texlive-gmverse
A redefinition of the verse environment to make the \\ command optional for
line ends and to give it a possibility of optical centering and `right-hanging'
alignment of lines broken because of length.

%package -n texlive-interlinear
Summary:        A package for creating interlinear glossed texts with customizable formatting
Version:        svn72106
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-enumitem
Requires:       texlive-etoolbox
Requires:       texlive-l3packages
Requires:       texlive-marginnote
Requires:       texlive-xifthen
Requires:       texlive-xkeyval
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(interlinear.sty) = %{tl_version}

%description -n texlive-interlinear
The interlinear package facilitates the creation of interlinear glossed texts,
commonly used in linguistic examples. It is based on the gb4e package and
builds upon its functionality to provide enhanced features. It offers extensive
customization options, allowing users to control font styles, formatting, and
layout. With predefined styles and margin note customization, interlinear
provides a flexible solution for presenting linguistic data.

%package -n texlive-jura
Summary:        A document class for German legal texts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(alphanum.sty) = %{tl_version}
Provides:       tex(jura.cls) = %{tl_version}

%description -n texlive-jura
Implements the standard layout for German term papers in law (one-and-half
linespacing, 7 cm margins, etc.). Includes alphanum that permits alphanumeric
section numbering (e.g., A. Introduction; III. International Law).

%package -n texlive-juraabbrev
Summary:        Abbreviations for typesetting (German) juridical documents
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(juraabbrev.sty) = %{tl_version}

%description -n texlive-juraabbrev
This package should be helpful for people working on (German) law. It helps you
to handle abbreviations and creates a list of those (pre-defined) abbreviations
that have actually been used in the document

%package -n texlive-juramisc
Summary:        Typesetting German juridical documents
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xspace.sty)
Provides:       tex(jurabase.sty) = %{tl_version}
Provides:       tex(jurabook.cls) = %{tl_version}
Provides:       tex(juraovw.cls) = %{tl_version}
Provides:       tex(juraurtl.cls) = %{tl_version}

%description -n texlive-juramisc
A collection of classes for typesetting court sentences, legal opinions, books
and dissertations for German lawyers. A jurabook class is also provided, which
may not yet be complete.

%package -n texlive-jurarsp
Summary:        Citations of judgements and official documents in (German) juridical documents
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xspace.sty)
Provides:       tex(jurarsp.sty) = %{tl_version}

%description -n texlive-jurarsp
This package should be helpful for people working on (German) law. It (ab)uses
BibTeX for citations of judgements and official documents. For this purpose, a
special BibTeX-style is provided.

%package -n texlive-langnames
Summary:        Name languages and their genetic affiliations consistently
Version:        svn69101
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(langnames.sty) = %{tl_version}
Provides:       tex(ln_fams_glot.tex) = %{tl_version}
Provides:       tex(ln_fams_wals.tex) = %{tl_version}
Provides:       tex(ln_langs_glot.tex) = %{tl_version}
Provides:       tex(ln_langs_glot_native.tex) = %{tl_version}
Provides:       tex(ln_langs_wals.tex) = %{tl_version}
Provides:       tex(ln_langs_wals_native.tex) = %{tl_version}

%description -n texlive-langnames
This package attempts to make the typing of language names, codes, and families
slightly easier by providing macros to access pre-defined
language--code--family combinations from two important databases, as well as
the possibility to create new combinations. It may be particularly useful for
large, collaborative projects as well as typologically minded ones with a
variety of language examples.

%package -n texlive-ledmac
Summary:        Typeset scholarly editions
Version:        svn41811
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(afoot.sty) = %{tl_version}
Provides:       tex(ledarab.sty) = %{tl_version}
Provides:       tex(ledmac.sty) = %{tl_version}
Provides:       tex(ledpar.sty) = %{tl_version}

%description -n texlive-ledmac
A macro package for typesetting scholarly critical editions. The ledmac package
is a LaTeX port of the plain TeX EDMAC macros. It supports indexing by page and
line number and simple tabular- and array-style environments. The package is
distributed with the related ledpar and ledarab packages. The package is now
superseded by reledmac.

%package -n texlive-lexikon
Summary:        Macros for a two language dictionary
Version:        svn17364
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ipa.sty)
Provides:       tex(lexikon.sty) = %{tl_version}

%description -n texlive-lexikon
Macros for a two language dictionary

%package -n texlive-lexref
Summary:        Convenient and uniform references to legal provisions
Version:        svn36026
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(nomencl.sty)
Requires:       tex(splitidx.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xstring.sty)
Provides:       tex(lexref.sty) = %{tl_version}

%description -n texlive-lexref
The package is aimed at continental lawyers (especially those in Switzerland
and Germany), allowing the user to make references to legal provisions
conveniently and uniformly. The package also allows the user to add cited Acts
to a nomenclature list (automatically), and to build specific indexes for each
cited Act. The package is still under development, and should be treated as an
'alpha'-release.

%package -n texlive-ling-macros
Summary:        Macros for typesetting formal linguistics
Version:        svn42268
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(pbox.sty)
Requires:       tex(relsize.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(ulem.sty)
Requires:       tex(upgreek.sty)
Provides:       tex(ling-macros.sty) = %{tl_version}

%description -n texlive-ling-macros
This package contains macros for typesetting glosses and formal expressions. It
covers a range of subfields in formal linguistics.

%package -n texlive-linguex
Summary:        Format linguists' examples
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tree-dvips.sty)
Requires:       tex(xspace.sty)
Provides:       tex(linguex.sty) = %{tl_version}
Provides:       tex(linguho.sty) = %{tl_version}
Provides:       tex(ps-trees.sty) = %{tl_version}

%description -n texlive-linguex
This bundle comprises two packages: The linguex package facilitates the
formatting of linguist examples, automatically taking care of example
numbering, indentations, indexed brackets, and the '*' in grammaticality
judgments. The ps-trees package provides linguistic trees, building on the
macros of tree-dvips, but overcoming some of the older package's shortcomings.

%package -n texlive-linguistix
Summary:        Enhanced support for linguistics
Version:        svn77571
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(linguistix-american.sty) = %{tl_version}
Provides:       tex(linguistix-base.sty) = %{tl_version}
Provides:       tex(linguistix-british.sty) = %{tl_version}
Provides:       tex(linguistix-english.sty) = %{tl_version}
Provides:       tex(linguistix-fixpex.sty) = %{tl_version}
Provides:       tex(linguistix-fonts.sty) = %{tl_version}
Provides:       tex(linguistix-glossing.sty) = %{tl_version}
Provides:       tex(linguistix-greek.sty) = %{tl_version}
Provides:       tex(linguistix-ipa.sty) = %{tl_version}
Provides:       tex(linguistix-languages.sty) = %{tl_version}
Provides:       tex(linguistix-leipzig.sty) = %{tl_version}
Provides:       tex(linguistix-logos.sty) = %{tl_version}
Provides:       tex(linguistix-marathi.sty) = %{tl_version}
Provides:       tex(linguistix-nfss.sty) = %{tl_version}
Provides:       tex(linguistix.sty) = %{tl_version}

%description -n texlive-linguistix
This is an experimental bundle of packages that provide enhanced support for
typesetting in linguistics. It can be used as a single package, or the packages
can be loaded independently for separate features. Currently, it provides the
following packages: LinguisTiX-base: A base package used by other LinguisTiX
siblings LinguisTiX-fixpex: Solves the compatibility bug between expex and
unicode-math LinguisTiX-fonts: General text in the New Computer Modern font
family LinguisTiX-ipa: IPA text in the New Computer Modern font family
LinguisTiX-glossing: Accessible interlinear glossing LinguisTiX-leipzig:
Leipzig-style glossing with tagging LinguisTiX-languages: Support for modern
multilingual typesetting LinguisTiX-logos: For printing the logos of the
LinguisTiX bundle LinguisTiX-nfss: Extra control over NFSS

%package -n texlive-liturg
Summary:        Support for typesetting Catholic liturgical texts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(color.sty)
Requires:       tex(ecclesiastic.sty)
Requires:       tex(lettrine.sty)
Provides:       tex(liturg.sty) = %{tl_version}

%description -n texlive-liturg
The packages offers simple macros for typesetting Catholic liturgical texts,
particularly Missal and Breviary texts. The package assumes availability of
Latin typesetting packages.

%package -n texlive-liturgy-cw
Summary:        Create Common Worship style documents
Version:        svn76053
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(bibleref.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(framed.sty)
Requires:       tex(geometry.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(liturgy-cw.sty) = %{tl_version}

%description -n texlive-liturgy-cw
This package greatly simplifies the typesetting of service sheets and booklets
in the style of the Common Worship liturgical resources of the Church of
England. The package provides commands for a number of liturgical elements,
including rubrics, responsories and 'required part' indicators.

%package -n texlive-metrix
Summary:        Typeset metric marks for Latin text
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(metrix.sty) = %{tl_version}

%description -n texlive-metrix
The package may be used to type the prosodics/metrics of (latin) verse; it
provides macros to typeset the symbols standing alone, and in combination with
symbols, giving automatic alignment. The package requires TikZ (including the
calc library), xpatch, and xparse (thus also requiring the experimental LaTeX3
environment).

%package -n texlive-nnext
Summary:        Extension for the gb4e package
Version:        svn56575
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(xspace.sty)
Provides:       tex(nnext.sty) = %{tl_version}

%description -n texlive-nnext
This is an add-on for the gb4e package used in linguistics. It implements the
\Next, \NNext, \Last, and \LLast commands from the linguex package or the
\nextx, \anextx, \lastx, \blastx, and \bblastx commands from the expex package.

%package -n texlive-opbible
Summary:        Creating a study Bible with OpTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(opbible-hebrew.tex) = %{tl_version}

%description -n texlive-opbible
This package includes OpTeX macros which allow to create a study Bible in many
language variants. The main Bible text is in separate files while the
commentary apparatus can be written in other files. TeX is able to join all
these data into a single print of a study Bible. Moreover, multiple language
variants and translation subvariants are provided.

%package -n texlive-parallel
Summary:        Typeset parallel texts
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(parallel.sty) = %{tl_version}

%description -n texlive-parallel
Provides a parallel environment which allows two potentially different texts to
be typeset in two columns, while maintaining alignment. The two columns may be
on the same page, or on facing pages. This arrangement of text is commonly used
when typesetting translations, but it can have value when comparing any two
texts.

%package -n texlive-parrun
Summary:        Typesets (two) streams of text running parallel
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(parrun.sty) = %{tl_version}

%description -n texlive-parrun
For typesetting translated text and the original source, parallel on the same
page, one above the other.

%package -n texlive-phonrule
Summary:        Typeset linear phonological rules
Version:        svn43963
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(phonrule.sty) = %{tl_version}

%description -n texlive-phonrule
The package provides macros for typesetting phonological rules like those in
'Sound Pattern of English' (Chomsky and Halle 1968).

%package -n texlive-plari
Summary:        Typesetting stageplay scripts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(plari.cls) = %{tl_version}

%description -n texlive-plari
Plari (the name comes from the Finnish usage for the working copy of a play) is
a report-alike class, without section headings, and with paragraphs vertically
separated rather than indented.

%package -n texlive-play
Summary:        Typeset drama using LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(play.cls) = %{tl_version}
Provides:       tex(play.sty) = %{tl_version}

%description -n texlive-play
A class and style file that supports the typesetting of plays, including
options for line numbering.

%package -n texlive-poemscol
Summary:        Typesetting Critical Editions of Poetry
Version:        svn56082
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(poemscol.sty) = %{tl_version}

%description -n texlive-poemscol
The package offers LaTeX macros for typesetting critical editions of poetry.
Its features include automatic linenumbering, generation of separate endnotes
sections for emendations, textual collations, and explanatory notes, special
marking for cases in which page breaks occur during stanza breaks, running
headers of the form 'Notes to pp. xx-yy' for the notes sections, index of
titles and first lines, and automatic generation of a table of contents.

%package -n texlive-poetry
Summary:        Facilities for typesetting poetry and poetical structure
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(imakeidx.sty)
Requires:       tex(modulus.sty)
Provides:       tex(poetry.sty) = %{tl_version}

%description -n texlive-poetry
This package provides some macros and general doodads for typesetting poetry.
There is, of course, already the excellent verse package, and the poetrytex
package provides some extra functionality on top of it. But poetry provides
much of the same functionality in a bit of a different way, and with a few
additional abilities, such as facilities for a list of poems, an index of first
lines, and some structural commands.

%package -n texlive-poetrytex
Summary:        Typeset anthologies of poetry
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tocloft.sty)
Provides:       tex(poetrytex.sty) = %{tl_version}

%description -n texlive-poetrytex
The package is designed to aid in the management and formatting of anthologies
of poetry and other writings; it does not concern itself with actually
typesetting the verse itself.

%package -n texlive-qobitree
Summary:        LaTeX macros for typesetting trees
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(qobitree.tex) = %{tl_version}

%description -n texlive-qobitree
Provides commands \branch and \leaf for specifying the elements of the tree;
you build up your tree with those commands, and then issue the \tree command to
typeset the whole.

%package -n texlive-qtree
Summary:        Draw tree structures
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(qtree.sty) = %{tl_version}

%description -n texlive-qtree
The package offers support for drawing tree diagrams, and is especially
suitable for linguistics use. It allows trees to be specified in a simple
bracket notation, automatically calculates branch sizes, and supports both
DVI/PostScript and PDF output by use of pict2e facilities. The package is a
development of the existing qobitree package, offering a new front end.

%package -n texlive-reledmac
Summary:        Typeset scholarly editions
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(reledmac.sty) = %{tl_version}
Provides:       tex(reledpar.sty) = %{tl_version}

%description -n texlive-reledmac
A package for typesetting scholarly critical editions, replacing the
established ledmac and eledmac packages. Ledmac itself was a LaTeX port of the
plain TeX EDMAC macros. The package supports indexing by page and by line
numbers, and simple tabular- and array-style environments. The package is
distributed with the related reledpar package.

%package -n texlive-rrgtrees
Summary:        Linguistic tree diagrams for Role and Reference Grammar (RRG) with LaTeX
Version:        svn27322
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-node.sty)
Requires:       tex(pst-tree.sty)
Provides:       tex(rrgtrees.sty) = %{tl_version}

%description -n texlive-rrgtrees
A set of LaTeX macros that makes it easy to produce linguistic tree diagrams
suitable for Role and Reference Grammar (RRG). This package allows the
construction of trees with crossing lines, as is required by this theory for
many languages. There is no known limit on number of tree nodes or levels.
Requires the pst-node and pst-tree LaTeX packages.

%package -n texlive-rtklage
Summary:        A package for German lawyers
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(rtklage.cls) = %{tl_version}

%description -n texlive-rtklage
RATeX is a newly developed bundle of packages and classes provided for German
lawyers. Now in the early beginning it only contains rtklage, a class to make
lawsuits.

%package -n texlive-screenplay
Summary:        A class file to typeset screenplays
Version:        svn27223
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hardmarg.sty) = %{tl_version}
Provides:       tex(screenplay.cls) = %{tl_version}

%description -n texlive-screenplay
The class implements the format recommended by the Academy of Motion Picture
Arts and Sciences.

%package -n texlive-screenplay-pkg
Summary:        Package version of the screenplay document class
Version:        svn44965
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(setspace.sty)
Provides:       tex(screenplay-pkg.sty) = %{tl_version}

%description -n texlive-screenplay-pkg
This package implements the tools of the screenplay document class in the form
of a package so that screenplay fragments can be included within another
document class. For full documentation of the available commands, please
consult the screenplay class documentation in addition to the included package
documentation.

%package -n texlive-sides
Summary:        A LaTeX class for typesetting stage plays
Version:        svn76924
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sides.cls) = %{tl_version}

%description -n texlive-sides
This is a LaTeX class for typesetting stage plays, based on the plari class
written by Antti-Juhani Kaijanaho in 1998. It has been updated and several
formatting changes have been made to it--most noticeably there are no longer
orphans.

%package -n texlive-stage
Summary:        A LaTeX class for stage plays
Version:        svn62929
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(stage.cls) = %{tl_version}

%description -n texlive-stage
Stage.cls is a LaTeX class for creating plays of any length in a standard
manuscript format for production and submission.

%package -n texlive-textglos
Summary:        Typeset and index linguistic gloss abbreviations
Version:        svn30788
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(textglos.sty) = %{tl_version}

%description -n texlive-textglos
The package provides a set of macros for in-line linguistic examples (as
opposed to interlinear glossing, set apart from the main text). It prevents
hyphenated examples from breaking across lines and consistently formats
phonemic examples, orthographic examples, and more.

%package -n texlive-thalie
Summary:        Typeset drama plays
Version:        svn65249
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(translations.sty)
Requires:       tex(xspace.sty)
Provides:       tex(thalie.sty) = %{tl_version}

%description -n texlive-thalie
The package provides tools to typeset drama plays. It defines commands to
introduce characters' lines, to render stage directions, to divide a play into
acts and scenes and to build the dramatis personae automatically.

%package -n texlive-theatre
Summary:        A sophisticated package for typesetting stage plays
Version:        svn45363
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-theatre-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-theatre-doc <= 11:%{version}

%description -n texlive-theatre
This package enables the user to typeset stage plays in a way that permits to
create highly customized printouts for each actor.

%package -n texlive-tree-dvips
Summary:        Trees and other linguists' macros
Version:        svn21751
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lingmacros.sty) = %{tl_version}
Provides:       tex(tree-dvips.sty) = %{tl_version}

%description -n texlive-tree-dvips
The package defines a mechanism for specifying connected trees that uses a
tabular environment to generate node positions. The package uses PostScript
code, loaded by dvips, so output can only be generated by use of dvips. The
package lingmacros.sty defines a few macros for linguists: \enumsentence for
enumerating sentence examples, simple tabular-based non-connected tree macros,
and gloss macros.

%package -n texlive-verse
Summary:        Aids for typesetting simple verse
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(verse.sty) = %{tl_version}

%description -n texlive-verse
The package documentation discusses approaches to the problem; the package is
strong on layout, from simple alternate-line indentation to the Mouse's tale
from Alice in Wonderland.

%package -n texlive-xyling
Summary:        Draw syntactic trees, etc., for linguistics literature, using xy-pic
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xy.sty)
Provides:       tex(xyling.sty) = %{tl_version}

%description -n texlive-xyling
The macros in this package model the construction of linguistic tree structures
as a genuinely graphical problem: they contain two types of objects, BRANCHES
and NODE LABELS, and these are positioned relative to a GRID. It is essential
that each of these three elements is constructed independent of the other two,
and hence they can be modified without unwanted side effects. The macros are
based on the xy-pic package.

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
test "%{source117_hash}" = "none" || { f="%{SOURCE117}"; test -f "$f" || { echo "oreon: missing Source117 $f" >&2; exit 1; }; h_expected="%{source117_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source117_hash}" || { echo "oreon: Source117 hash mismatch" >&2; exit 1; }; }
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
tar -xf %{SOURCE117} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Removing pre-built binary from opbible.doc
rm -rf %{buildroot}%{_texmf_main}/doc/optex/opbible/txs-gen/mod2tex

# Apply scrpage2 obsolete fix patches
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-rtklage-scrpage2-obsolete-fixes.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-adtrees
%license gpl2.txt
%{_texmf_main}/tex/latex/adtrees/
%doc %{_texmf_main}/doc/latex/adtrees/

%files -n texlive-bibleref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref/
%doc %{_texmf_main}/doc/latex/bibleref/

%files -n texlive-bibleref-lds
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-lds/
%doc %{_texmf_main}/doc/latex/bibleref-lds/

%files -n texlive-bibleref-mouth
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-mouth/
%doc %{_texmf_main}/doc/latex/bibleref-mouth/

%files -n texlive-bibleref-parse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-parse/
%doc %{_texmf_main}/doc/latex/bibleref-parse/

%files -n texlive-covington
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/covington/
%doc %{_texmf_main}/doc/latex/covington/

%files -n texlive-dramatist
%license gpl2.txt
%{_texmf_main}/tex/latex/dramatist/
%doc %{_texmf_main}/doc/latex/dramatist/

%files -n texlive-dvgloss
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dvgloss/
%doc %{_texmf_main}/doc/latex/dvgloss/

%files -n texlive-ecltree
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ecltree/
%doc %{_texmf_main}/doc/latex/ecltree/

%files -n texlive-edfnotes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/edfnotes/
%doc %{_texmf_main}/doc/latex/edfnotes/

%files -n texlive-edmac
%license gpl2.txt
%{_texmf_main}/tex/generic/edmac/
%doc %{_texmf_main}/doc/generic/edmac/

%files -n texlive-eledform
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eledform/
%doc %{_texmf_main}/doc/latex/eledform/

%files -n texlive-eledmac
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eledmac/
%doc %{_texmf_main}/doc/latex/eledmac/

%files -n texlive-expex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/expex/
%doc %{_texmf_main}/doc/generic/expex/

%files -n texlive-expex-glossonly
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/expex-glossonly/
%doc %{_texmf_main}/doc/latex/expex-glossonly/

%files -n texlive-gb4e
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gb4e/
%doc %{_texmf_main}/doc/latex/gb4e/

%files -n texlive-gb4e-next
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gb4e-next/
%doc %{_texmf_main}/doc/latex/gb4e-next/

%files -n texlive-gmverse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gmverse/
%doc %{_texmf_main}/doc/latex/gmverse/

%files -n texlive-interlinear
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/interlinear/
%doc %{_texmf_main}/doc/latex/interlinear/

%files -n texlive-jura
%license gpl2.txt
%{_texmf_main}/tex/latex/jura/
%doc %{_texmf_main}/doc/latex/jura/

%files -n texlive-juraabbrev
%license gpl2.txt
%{_texmf_main}/makeindex/juraabbrev/
%{_texmf_main}/tex/latex/juraabbrev/
%doc %{_texmf_main}/doc/latex/juraabbrev/

%files -n texlive-juramisc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/juramisc/
%doc %{_texmf_main}/doc/latex/juramisc/

%files -n texlive-jurarsp
%license gpl2.txt
%{_texmf_main}/bibtex/bst/jurarsp/
%{_texmf_main}/tex/latex/jurarsp/
%doc %{_texmf_main}/doc/latex/jurarsp/

%files -n texlive-langnames
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/langnames/
%doc %{_texmf_main}/doc/latex/langnames/

%files -n texlive-ledmac
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ledmac/
%doc %{_texmf_main}/doc/latex/ledmac/

%files -n texlive-lexikon
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lexikon/
%doc %{_texmf_main}/doc/latex/lexikon/

%files -n texlive-lexref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lexref/
%doc %{_texmf_main}/doc/latex/lexref/

%files -n texlive-ling-macros
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ling-macros/
%doc %{_texmf_main}/doc/latex/ling-macros/

%files -n texlive-linguex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/linguex/
%doc %{_texmf_main}/doc/latex/linguex/

%files -n texlive-linguistix
%license gpl3.txt
%{_texmf_main}/tex/latex/linguistix/
%doc %{_texmf_main}/doc/latex/linguistix/

%files -n texlive-liturg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/liturg/
%doc %{_texmf_main}/doc/latex/liturg/

%files -n texlive-liturgy-cw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/liturgy-cw/
%doc %{_texmf_main}/doc/latex/liturgy-cw/

%files -n texlive-metrix
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/metrix/
%doc %{_texmf_main}/doc/latex/metrix/

%files -n texlive-nnext
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nnext/
%doc %{_texmf_main}/doc/latex/nnext/

%files -n texlive-opbible
%license gpl2.txt
%{_texmf_main}/tex/optex/opbible/
%doc %{_texmf_main}/doc/optex/opbible/

%files -n texlive-parallel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/parallel/
%doc %{_texmf_main}/doc/latex/parallel/

%files -n texlive-parrun
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/parrun/
%doc %{_texmf_main}/doc/latex/parrun/

%files -n texlive-phonrule
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/phonrule/
%doc %{_texmf_main}/doc/latex/phonrule/

%files -n texlive-plari
%license gpl2.txt
%{_texmf_main}/tex/latex/plari/
%doc %{_texmf_main}/doc/latex/plari/

%files -n texlive-play
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/play/
%doc %{_texmf_main}/doc/latex/play/

%files -n texlive-poemscol
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/poemscol/
%doc %{_texmf_main}/doc/latex/poemscol/

%files -n texlive-poetry
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/poetry/
%doc %{_texmf_main}/doc/latex/poetry/

%files -n texlive-poetrytex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/poetrytex/
%doc %{_texmf_main}/doc/latex/poetrytex/

%files -n texlive-qobitree
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/qobitree/
%doc %{_texmf_main}/doc/latex/qobitree/

%files -n texlive-qtree
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/qtree/
%doc %{_texmf_main}/doc/latex/qtree/

%files -n texlive-reledmac
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/reledmac/
%doc %{_texmf_main}/doc/latex/reledmac/

%files -n texlive-rrgtrees
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rrgtrees/
%doc %{_texmf_main}/doc/latex/rrgtrees/

%files -n texlive-rtklage
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rtklage/
%doc %{_texmf_main}/doc/latex/rtklage/

%files -n texlive-screenplay
%license gpl2.txt
%{_texmf_main}/tex/latex/screenplay/
%doc %{_texmf_main}/doc/latex/screenplay/

%files -n texlive-screenplay-pkg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/screenplay-pkg/
%doc %{_texmf_main}/doc/latex/screenplay-pkg/

%files -n texlive-sides
%license gpl2.txt
%{_texmf_main}/tex/latex/sides/
%doc %{_texmf_main}/doc/latex/sides/

%files -n texlive-stage
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/stage/
%doc %{_texmf_main}/doc/latex/stage/

%files -n texlive-textglos
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/textglos/
%doc %{_texmf_main}/doc/latex/textglos/

%files -n texlive-thalie
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thalie/
%doc %{_texmf_main}/doc/latex/thalie/

%files -n texlive-theatre
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/theatre/

%files -n texlive-tree-dvips
%license lppl1.3c.txt
%{_texmf_main}/dvips/tree-dvips/
%{_texmf_main}/tex/latex/tree-dvips/
%doc %{_texmf_main}/doc/latex/tree-dvips/

%files -n texlive-verse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/verse/
%doc %{_texmf_main}/doc/latex/verse/

%files -n texlive-xyling
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xyling/
%doc %{_texmf_main}/doc/latex/xyling/

%changelog
%autochangelog
