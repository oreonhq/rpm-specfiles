%global source0_hash 5d755fc9f82f7e966cfc7c0abb0236cf148f4f052c9e9831f2a00103c7665696e607377dd6767b90e2ee3d70fb7191aa2c533d0b0f3b0e22ad1e064440e027c3

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langother
Epoch:          12
Version:        svn74620
Release:        3%{?dist}
Summary:        Other languages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash a7f841e874dc4d28ee25c11352ee616b0c410953bbdecacab68d3965c47c6348728f2b9120a36e8ae06b6d9800ee599e0073258ded95d66b0005e970b2ea7297
%global source3_hash de02f19d0f626b3a00a6369862558d287ce2cb7a15389d176f8f98b815c1bfa21e42d403c5fe285fbde26234a2f690d20a0e8ce435fbc37bccf72255d0121214
%global source4_hash 5b0c2cc1afcc4060249be20271af92c71c866db47d2551a176b5685c58182a6ca17da9540dd9a7c7abd33de75b0335a625aa921fdbd77329bc91d16718fb346a
%global source5_hash 827c294eb1cedd51a3924796b461ec3d6c858e7875254e0fdb6cb496fecbb6d2ec541e930327c54cc446b15dd69ed795470ae6cbf1cf1e51c0f3ae90f3f6c12f
%global source6_hash a01ff01e32ed89553fc59e8a1d34da25c94e766b498d41ebe974a7683718bff38e12dc70489167c1b9fe14ff14c14bda0b000dd47c11d65c00b654822cf29d10
%global source7_hash 2656063aae4df2daae2036477081f00f141f50d5205dbb6d1c173dcaaa3f9ca1cd5a77c49c7e9e9c2ecb82874a77d84a739724ce36811f460a98b18508910722
%global source8_hash 8e6297b5563400085dab80ed86355a62d1983a148c239980f41700345b92881b4c047be26484aa7cf6329d60c18032fd975d0625d69b29d2f33bfe112ee61dec
%global source9_hash 12e9e9944888d44a02e56a6ecd5b0c796b2d62c667cbfb6dea9ede4e11c68456851d08419943a0f17d3acfbee9e56866c6a64fd411b787435f99b0fc8351b262
%global source10_hash a94349c8b73220dd87e8d52693e9070085b2502368a9bad15bfd3c3f1fcf637b4c46fdea0d5237c2640abfb80639b3e7f5462a46b1329965ad6954f9ef779af0
%global source11_hash 9f0774eeefbc469d408d66c3908c19f5efc49b22b45317740c4dfb5e696ac2cc0b0c5cde78726a01a96c9f638ab998498103b36ea2ef1ed2e2e2a555e21be7cc
%global source12_hash 5d0e5c6e471a36836406be3b2212b0ced5df43be13d3864b8301bff639986a2e3b5aef08a6546d6ba03bc2ddc86e6dc86eaf35d59fdfb5f81403f22ceca18d8c
%global source13_hash afd2545cbc5a6282dc53be44e70b2dcc09c29464afb106f5d170c5bd0652f4d8ec1b0a92e29b1ba62a2249236320b4c2025318c8331e7f19707b105da279f0f2
%global source14_hash acedab649ecf14a4ff1daf79dc7b35378fd0be4f1c6cf89d38ce8a7eb9adfbe7778c02a00f62e0a67d7ffc6cce4a25508a3e7d0a8fa57ec26b555185b233b879
%global source15_hash 44e7c24f0d179aa547f32fe4b4b8d1eab72f3f0e698632fc4f0f4dd1b8c4010656bc85a998f9fbc744b5690a06ae8bd6b4d5dc69ab754b335dd4c19a13478762
%global source16_hash 99e72fc367dc5cef35be2b7308bd7bcf53c211ae3f3d203d15e8ee716e31c50703bb8c71731f3d07b249cb3edc72f0d01f23d663697be7a99bf5959c492b25cf
%global source17_hash de963df363a6b8969eb05200fda92396d3102cf270123a30ddf045f98437ccf31f6fec8d23cd22913bac76b9fdeef8144b5eb362580dc7a991abfca6aaf8c8fc
%global source18_hash 5fb27adaad0923bc0f8ac8a6ff39dc0fd24172ad4f48789361048a268f2b667c99aa08bc50f0cb21a50b5e49945856672efd2ac79e0dc2a6292b619f1d3adf5b
%global source19_hash c2ac5e710fb7fb584723bee3770b33b175c52dbf29574e73cde57cc291302d1658f7423256bff15a71b0d92ea52de3591122950f7ae33384ea2c4cb9e732eb71
%global source20_hash e6e68749352b8705140d18cabc8121cefd418c03700f3c71c65508bb314e2ab36e8de1f1a8ad3202722e7592035b8bbac405ffe9f1cc675db98f03e6ce44ffcd
%global source21_hash 2566faf90f744a4622d1cc125f61e869b85cb1c5e720143fffa1f69356a4f5ca44b367f8f85eece1e749d8bfec105ac484e519ec248995faa73fcdedaa6a214e
%global source22_hash a9cb52818040ec7de78bb1623ca31475c961e65ec4464aa0030dbde8e72f317f8afe69b21f0346ba69c825fff0e81e316f7a2a160d557d183bcaefac78c036aa
%global source23_hash 5d8d8ce83968c13663920f5705c3155911cb20f7637467c8a30436973fe2b9bd060f9183deec7df44c0a5c3958e8b0722e0d0fb375c6f985f34eaaf27414a4da
%global source24_hash 4e3e5c6d8944040177a21f04e63bd40e85c24e9327eeddfe98072da38590c58523f676fd7532e4e00d0e3cc88121a2885788d606d2dc9ca02fd91c7f04a6ef57
%global source25_hash 791539a57534c4870a81ec2318298b29e9e9ad925161b0a4cf52c49086a865d5b58b60da10829a5fb37e66f0d161b396beb127e586457c556875f1205fac9360
%global source26_hash ddb75c37017c1b0b6af2cfbdf574526cdfdce2099d599a23cc8ac819f6ebe5ea7a2eda4bd743af93d78835ca5dccb3d7fa55db22b3154862aa4affe83c28185f
%global source27_hash b078464ce848b24d692d4dded7c9827f37fdb4141b719c71e28b5ef0a827f9ea5c2137745f9689fcb89a486d4a88a94a043a62348e86b5736a68ea48c7f33e16
%global source28_hash 206832f90fc33e68d199b209debf434198822e808ed237a0f5533f6b13c4a46314cdc5740f6cea0b05d0f0e688039e7f89928b449fc21483093b0ec26c9c04c7
%global source29_hash b523943da9d0a11af7b97cc34dac928b832123f2804a1271a66a8fd177c241fd3dfff590d96c959bea414a368de6539142d4c9ef87f22e0fb75ed107d11c7d63
%global source30_hash 84d2b5b85f423e171bb90821f9e4518d06a640c02b03638295322e0ea6aedfdb831b6a4e62d3c25259b7b70aa0fe68ffe3081f6de0b0c71fe03c10616c74347e
%global source31_hash 05ca923b97240a766d3ff448c6b16a33613a16e3307509ed7c369da6ec889e7e19d57e5f542b829c788ac4e87bd7025a62af9f7127e2eebe7fdd3eba4aeeb7ce
%global source32_hash a131c43c6a5a86d011381cd904ff0866241e03cf077f26a9dd348c065e818fdcf94e2b59fad9fb357246d8bfcc049dc1871c8c6ba94b0c8c9fb86d7168d509a0
%global source33_hash b88131292ca89c72e04e21271e1375cfff36be8029be8543891905f4ca84ac445a0f29562445c9e590e601752dc8822b8bb47aa3bb40b3907e6a43fd47765130
%global source34_hash 7bce3a31febfc6a959ba4779d975cf93276a0bd1115e06a50a3c8d705e49e8d6747ecebc7eac2147f021a538dda1bb241d8f320ef1486229c930141e06d6ae26
%global source35_hash 4a7f3628efd913a362786564dd260dc1a63e51a397af3d92222db6f758b7a7792b13e58422d2604ae98f615fb5fc42e77f265e505236db9bc981d7951e0ee1ed
%global source36_hash 65a73380bcfd8892ab2eb93d088076e2d5371019244bc8a65a4695e69a45f743248fce59557533add032a02a0b7ea4f02d6ea4634265d2d9718a5b100f5a18c6
%global source37_hash 591d932ae099aa168d55f9479842d25c5212dd7aed27eac1a5d05a111a8a396baae7c73ddafe1087a7b8008528c50b1a85825851643d8107133d41470ce1e397
%global source38_hash 8999ea42b82e56cbb06e2485060b829a0781550834ea421607b4621199692976488f4031266eee1a6b1443b12828e2fb5148ff43eff137c01ee9db8770bb1565
%global source39_hash 65d8f613ddb651cef4c345791a4a849e3f672930fb94d1ba789e827b466c459bc321762c71675cb4c5fdec8fc456520bb7013d5b737b4ff2bd049bb5917a98ef
%global source40_hash 72b0d55477aad038dfbeb83f759d81e63fbd62bd78bbdc062009ae1c8a17ec27daf6877a362beac07390d56adc66792d6a0c3afa85b9a12c4f4007116c0a2dbb
%global source41_hash d8180be1dd9e5902e28be8b99da435336ba8ecef9dbf046a675453ea68a507f392baca9c7704807aa9678eacb3665e8e2ef4b0b1b49a72f202468ac6792f0331
%global source42_hash ed589b111ae0fdc366d483328133ff0cf5206637121cb6fd3fb915c88c968bcc573747d73b976488477a7c3d8668e365a6b124b9a88db40d3d71c60282a0d3f6
%global source43_hash 4f1a3aabe1ec6e8f288af9da308e19ccf6c2bfd904c95b35d7ffedaba47410608a7776a3d50f00664c8d318a063b020ae2047be0114dad681396ed29b38a6a2c
%global source44_hash 84f97fb5320ada95562aade797fdb62577e533feee9d7ece5cc51e17303012b198c0b1e6b4f720dc1539c4cb917ac71e3da6f48776d6fcfe84d4527ffd7b78dd
%global source45_hash 81f2ed72d5cef9119c94c4b0025e31be6739153e36b7b31a2c59b0cbe5a683a67746da8346345d561472fdbb760c07831d1936222ce1388ee12d70c9053ca8ac
%global source46_hash 12bb408f7ba4774d943aa954bd3d2558a329d383a65cd4780f6c5bdc39f51b943f01d87ad203aea3b02768dc0b9ab42f681175c18a1e1dd901255aae05156558
%global source47_hash a7495a0d6bd394811ff22438a42afe3c5109633da7c606a732f4c5746cc4162fa1c86ac3774aa7754e9b07c499f3519423d4b6fb212ecae156b0b8e8f848d914
%global source48_hash c8586fad30d340f19e013b542fb924e5346ed608bac655e2313e1172a10547455b17ec43982fcd20adc7e1b01cd1895ec80801c5a4e278cfc30fe2e6b21745fb
%global source49_hash 083d3db57520397171dea5cc855ecd3858cb96fac10407d7fca3453d8bef25214c95a01cf87fd9cae4900eae26910741fcca3162b602259a064c4a2f4f97f34d
%global source50_hash 5c27626c22275c42c25737d35af3c39a98a921037f6b9165a3222e168dd2c679e75e6854f88713681bdaa8eb8961bf58cff3b34c207bd1775ffea474b3524ffd
%global source51_hash bc7f81a0f09b544bee91bd387504f5a764e7a6df207f3255f5ba25b1fe654532b14e2c7ea9d1d2804db875b05e210b11058eecf7c15fd1fa7a7b516e2bb20207
%global source52_hash 1f6651a4aa033a7cff44caff62d01f3dc5dc280bd19d8a0541c78cd35116e9f765517a078f6f6f7a25f9ee42fc4e4e743b86a746e80583b491ac399d46e94ff1
%global source53_hash 459a131616a15431dd489aaa87a23533ae5eb58575f38757a81af8eba425bd4e5c0c0f3a11a3c030d04ecd7d29e9ab08b3f4e270961c4c8e8791c15a497ba7fe
%global source54_hash 2c00d0723c06809728695deeb8d78e4f4aecf951aaf46ccf00aede446fadbe92b37445eebd7dd94ded423a1c18dabc4f68921cd2a65a73e35a3961f58c033175
%global source55_hash da11b8894bcca538acdd879bb5a34d78f0b80e542d363cc6ee59af321c6a6562627ec1c7eba1a950d44084555996323ac9a0e117fe6f145d7693da81d5823cf8
%global source56_hash 4dccedba21b986bf65b5a5e3ab121e482a526b3372cbb2c3720b383ebbfbe1cbb231c2af4c0a6af9157df9eb8aafaa5462c088ad7f77e76cc4445c69782a8035
%global source57_hash d43949e34e612601dd0c1a173426de32011cee025fe27b0d48b3359f2088787254b8989ddbdc94bc64038facbe0386a2da512edd0f854ee02b62ffc06a6a2d1c
%global source58_hash a3fc85e7d1d84ecfc6bbdf16e06ae3f3475f975d59ece3f64d10cc1b24f05402018686eee1b7fccf7899633be67b1c0cbcbe7de78b0ecd93d45aa8d76872c690
%global source59_hash 7b56c77c6c9c9b8d68b58622358524915f0e96e8fedcf7646fa29d64e4966c94086f2321a5f61fc062fe42fdff3a7fd6b86e868cd5ea07af049286e956ad003b
%global source60_hash a43130d2b65c06f6f936c2f3fd2a684439da830fded0f7495c87f9e8948789c3d25831f080f49acb3cd69466ee043087ea485a47ec86773cf856ec311973a171
%global source61_hash d495f579d785bfa9a834adc956e806d585c7db6867e4da849acb7c57a1222bf102d37640c30a26d5843b8575eda9e39cc9c5516e9b8bbcfa058818e78d54242b
%global source62_hash 27b588e0de7c2653e5331cc3625f110d23204d589416ec3ef61bd6b3c3c99ee63d7db57473d81f159dcbefe47ff582737a127039651afa2d81ac1c95082447a5
%global source63_hash ad81c2d807e54a31bec0e8ed7fb71eb95e988c182652a32bf8133bb4774ec8d79ef983fd7ca2b53b32a4e6a5776b76d478ddb3d9ece4614e627e596aad1ad8e9
%global source64_hash 322a1b50d4964953e7aebea49dd03b6b1cbc97b4d07d08783bb607a3f20e900be2358e870fe706f321d1312dceaa8777856e01ffc104028cb2f99904b9316884
%global source65_hash 4b5abd027bfe41b6270dc903c80d233027351f21693c35664eb4b4f2526161a6307801e472f4d415c5475741336bca0b1be8aa378651de380cdc7f075b521ddd
%global source66_hash ea304982c6aa01db8394d35cb3bb14287b8771266514999e030f88f08e0d155562a304c48c50ff8b6c1729c9ce9f3775f8cb4f66d9475e28c04e08ddcecb7c04
%global source67_hash 99c09f751a1807ce1ee5842627cc9b7f77c6e6cb53e2505eba9c5dfba7fe156e5ccd1d8a4d664cdb5b24e7ce449c8a352c961b6c83804ee6ae003def10dad2ef
%global source68_hash 4eb2324899b72bf67676852c5f18359cd6a387c7a49b84f13bf1b8073395ef33b2d368f894d85cca0f73c32d0c9357ecf501b5447190cc218fb2d06846478390
%global source69_hash eb9b8b12f15a8662eea0e3df907264093074cac1d8f8e1f027186b35f3f3318c4b8c120d261be21350fa660b51a5f33e196d957864b0676395ded0f70940464a
%global source70_hash 51dcfff4a8df46a8715d07d2528d3a1960479ce4bffba9b8eb5170d5d6307f0c776e197bdbe788d316067070c1d5f5d1382c32430e94ea83664868931a844e52
%global source71_hash 8b61b8aee0e95339b356fa85b9bb7ad3833ccf410267eb31a84a811c25c4e34ac350952fa26ed6461468bfeca37121e809ba560fbed7a0d8e747613708ff7795
%global source72_hash 8d8c686edbf3e70e70fa577c7d09f2e3d3f1ab938253ed01892ba030be0ba948bba48d67503a6f215628e03160bb32878f868d8a72b5a0d65ce3400fb9011ac9
%global source73_hash e498d5ec469420db789dac92e314f9ac0355b4afa2c43d4dce2de3eb23481db2687283f9ccce2ffd6edfd7b8f2d7ca3bf7425f0ff43ed46d7ca2dc9e3bc16797
%global source74_hash ead89b61f23f527d4b545775c821792aaa5a4c3a6290767139dd8872ff6419de248d2f1d657589f469b49bc7b8a68a3368d5c26aa61a39ef6a0e6835cea97389
%global source75_hash e81deefb7fa47e336a6b9fc363fa75c35576fa40de1771fff207dff22106b33d185c267d76a3897f2188d2dbdf9d2b93a1caddcdae38eb770cd7c5d6f1ccdbb2
%global source76_hash fc805e2749305cff0164ccd8d0b043d26731fd6f39e19c0023c87e4812f8509b923d4c1a97594563394dd7bbbe4a99d3b25aa37366f6e5bfb3cc1c2aa21c0606
%global source77_hash 4acdbf8ae23c3e3b503f38312459f962a3fcb391c34c8dc34fec6557b834ab8ddec0b34b3963e90eb1a177f9380359911999d88f6e304106bdb05b3ce2b34186
%global source78_hash cd518884e6f6076e338c39b1a61e6db5e8e37eea800cd0834bc8f1f2fe970d521eeca7ac60e717123f552c6d720ad393c921ac3a6efc8cb1843636b762a55986
%global source79_hash c8b5fd05a28924e6520732ebce4ef4feecddab54ac6c0ecda20636939efba953bf2ac4643452126c0b1c0b17baa4dc82b34eaecc6364dbdf973b66d09fd10ea8
%global source80_hash 4ab0ec2051a882ae5ca1040f76d18d2de9c72ab8e63217e3998d8e07154e917c6aaff57ebc00b9d9e5fac032d608485e965c635c5edc608f4e932bfae41aaf11
%global source81_hash 09efe0c19bc1eb154d144b7c2fb41cfb9a1108380de94ff4c7087e0ba18804c514542c4990268a255deaf0a56a3baa73b0d0ff1c21c54f86181c6490b43188b1
%global source82_hash d50e2be5baeaa2544b4967f9f3b34fed3238188ad3fac63d8bdf9ecddf9721244435540f662f68429214fcb4dc7254610b9aa512434e59f9d09d304ca83e096b
%global source83_hash 4117b8162fa06919e11ea6719965dc3a99df82744f44d6166517fd18e00d25b32b6400325f4912c535ea51b7757d690853b24558c9ea15b0d529ea0f07a84650
%global source84_hash 8fdf6ee4ae69a1249afa8dcc00a17d01adf29582f8cb1a1eb49568c980ca9e0ff99783e290cc6de658966da5b4663718da99156fd32f172b04562713da18a0aa
%global source85_hash 960ee181474ecd09ae94a27755bc19cd5a9ee49366bb3115cdae018cdca54bf1860b21979647a2fc33b74a27027c2b8958380fc8d407d62cdf82b33566327b7c
%global source86_hash a2760f9ee06eaa0123d6eaedb9478961c9a6c46565860e495794c4d09701af661225598b0a54eda78d63afd2f92cac6e52dcf579895c8efbf845237b90b231c8
%global source87_hash 30ceb34f8cef47cbf2e363845e08a448d498d497b5ad5e6f8d89d9590017d33ff24b42d1d0785777c5b8e4d039a67589c0fc85f81a66c852636d22a37ab5d906
%global source88_hash 0e22d101efb924c873e50dba18cdd41b73d488736f8f584a60d5db287b109db90df0eaaa094df86b971e259cdb97fa11d5ff2a5eacdde5e3cccd7a3dbd5bc5e5
%global source89_hash 8c6d58f219f4fc1cce84e451c56e75c171dbb730784959c3d2ca5378868ff11f7d54c603d02db1fab7f48efd5b8ce226b51e36ee496e65d18f160a3873c33be0
%global source90_hash 89b1e0d05087b3dd547f76af1d2aad2acd24d684f0951de015c831dbe845e2b9c890beb6d15c8a9f563be9da75c3ffeff25a805ac19c383fded0dd2626e85ed5
%global source91_hash 25f6bd1e6e9586b261721b66b6b193c07f60dc074f7b7b1911b0a8ba4f33815c86945bcb3946ffe153f70f0dbaeec4dca8e5574f8369c754a6151fc271029f3b
%global source92_hash 246dbb624a2e2e30bd5468c2596e7b3f7183c7dd9d03eda42fbed88fe51f16b53801ed39f85590d2739a93d48bc413fce5c52685d5425615f650b19f56013261
%global source93_hash 970ea49b1f31b3fcbcd33f0312af27fd019e5ca714140e143b38271c542b99bfc8e65d39e8313d8b159619f4b757ae94dbbad432420aae2eb61de8afee40c0b6
%global source94_hash 9cab25f43f5587f120ba0390952efd798acd68b27ce010b1f3c624fcfc9f5e077d5de8eeafccb0ef48ab309c09cf6fb520de7ec15c1a31db8d48dd37c0ef0cd2
%global source95_hash df3386dfde77adcc99f3a168e35b4ec4c5c38b19dc2454ec10c01c0913abbbd4c4b975eff772e16cb0b0266e478ef94cd32a75284dedc04d18d15f9217da8008
%global source96_hash d0b17b3bf7d0ec7c430965e61ba2b22c9177ccd7c0de63848d5918ef6de732729a17b6415ecc51ea6e0b0aceed81c988462487a72ea5d2088115c15328efaa6c
%global source97_hash 5a4b043778811bfec1ecc847ee191dc64b3f99ae0adb8fda2b16fdfddabf195133d53acf295fb18dd70460e1c1d200d3e6889815edabcdd0bca9d007d7a309f1
%global source98_hash ded2197bb621622c7f9947ce736814a6acb63ce86bd866792a8fe8e1f22a8131ee12c785a81c764ab707e5bf1b2c99df73c1214ff71159e3c9fdd34ee7aef7cb
%global source99_hash b0679c76c3d3a2b7c64ace32329164d70e2d7657673a6f81a0441247be19d669151cbbdc2ac589d442b69cf97441c51dbb1535450729f1f680fe58092a994adb
%global source100_hash a707ab88cc8e0fb52516e712cf6dfacab5fff4b44bc4c5b0c9e8f4cdb67b1a86974b1599209fb96f83b27fe8aad8ff56d50acd1ac598f44a2952eaa02917b44c
%global source101_hash 6ad06e6a867b323c382b85fa1effe16280566b1b61dd37be0bd7e9384d145fff2b1b4ff8117aa49749db1f15495e835e3367b0b7191cf9444e36fed662ffd0ed
%global source102_hash c3d6ff664edd89fa711e9573b138b29b113b588ddef9ad4a258e1f28c4ca2aad1f05741a402c1c1972bbc317e0cb989ce7a51e52d59b42629343d9a5780b64d0
%global source103_hash 1dcecf9ac38a9099625ed6be3955af8b063ee5b5b8d0d3e3ab8c94a8215b72b86a0b5dbe930eb69680917bd3d6652b3f4f08bb377197ab6f3d2fccf2b96aa59e
%global source104_hash 924266d547910d25ed5355ec2ef697d271dd992aeb6767d5bcb703d4d07cd34b6844e9a821ed93f5a04237aba1c185fb68926967e78043f390785b619c2389d2
%global source105_hash 96eeb5289b4b0ce252eba1daf15fbccaf2cbb2d251a85818b6dd761048532f36355619e37f1f857caf4592cbf85d112d6d48d5944c455ef36da9913529a783fc
%global source106_hash 0f360c3f43c6562520b8843269068fc46ecc405cd3a4d8faecddc4f606d69cedcab28950fc1d2e11699e297fe4d70c4c3d50765a2ec30541c237914accbc7129

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langother.tar.xz#/collection-langother.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/akshar.tar.xz#/akshar.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/akshar.doc.tar.xz#/akshar.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsldoc-vn.tar.xz#/amsldoc-vn.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsldoc-vn.doc.tar.xz#/amsldoc-vn.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aramaic-serto.tar.xz#/aramaic-serto.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aramaic-serto.doc.tar.xz#/aramaic-serto.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-azerbaijani.tar.xz#/babel-azerbaijani.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-azerbaijani.doc.tar.xz#/babel-azerbaijani.doc.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-esperanto.tar.xz#/babel-esperanto.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-esperanto.doc.tar.xz#/babel-esperanto.doc.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-georgian.tar.xz#/babel-georgian.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-georgian.doc.tar.xz#/babel-georgian.doc.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-hebrew.tar.xz#/babel-hebrew.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-hebrew.doc.tar.xz#/babel-hebrew.doc.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-indonesian.tar.xz#/babel-indonesian.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-indonesian.doc.tar.xz#/babel-indonesian.doc.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-interlingua.tar.xz#/babel-interlingua.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-interlingua.doc.tar.xz#/babel-interlingua.doc.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-malay.tar.xz#/babel-malay.or11.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-malay.doc.tar.xz#/babel-malay.doc.or11.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-sorbian.tar.xz#/babel-sorbian.or11.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-sorbian.doc.tar.xz#/babel-sorbian.doc.or11.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-thai.tar.xz#/babel-thai.or11.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-thai.doc.tar.xz#/babel-thai.doc.or11.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-vietnamese.tar.xz#/babel-vietnamese.or11.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-vietnamese.doc.tar.xz#/babel-vietnamese.doc.or11.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangla.tar.xz#/bangla.or11.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangla.doc.tar.xz#/bangla.doc.or11.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangtex.tar.xz#/bangtex.or11.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangtex.doc.tar.xz#/bangtex.doc.or11.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bengali.tar.xz#/bengali.or11.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bengali.doc.tar.xz#/bengali.doc.or11.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/burmese.tar.xz#/burmese.or11.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/burmese.doc.tar.xz#/burmese.doc.or11.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjhebrew.tar.xz#/cjhebrew.or11.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjhebrew.doc.tar.xz#/cjhebrew.doc.or11.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctib.tar.xz#/ctib.or11.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctib.doc.tar.xz#/ctib.doc.or11.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/culmus.tar.xz#/culmus.or11.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/culmus.doc.tar.xz#/culmus.doc.or11.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ethiop.tar.xz#/ethiop.or11.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ethiop.doc.tar.xz#/ethiop.doc.or11.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ethiop-t1.tar.xz#/ethiop-t1.or11.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ethiop-t1.doc.tar.xz#/ethiop-t1.doc.or11.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fc.tar.xz#/fc.or11.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fc.doc.tar.xz#/fc.doc.or11.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fonts-tlwg.tar.xz#/fonts-tlwg.or11.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fonts-tlwg.doc.tar.xz#/fonts-tlwg.doc.or11.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hebrew-fonts.tar.xz#/hebrew-fonts.or11.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hebrew-fonts.doc.tar.xz#/hebrew-fonts.doc.or11.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hindawi-latex-template.tar.xz#/hindawi-latex-template.or11.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hindawi-latex-template.doc.tar.xz#/hindawi-latex-template.doc.or11.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-afrikaans.tar.xz#/hyphen-afrikaans.or11.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-armenian.tar.xz#/hyphen-armenian.or11.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-coptic.tar.xz#/hyphen-coptic.or11.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-esperanto.tar.xz#/hyphen-esperanto.or11.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-ethiopic.tar.xz#/hyphen-ethiopic.or11.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-georgian.tar.xz#/hyphen-georgian.or11.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-hebrew.tar.xz#/hyphen-hebrew.or11.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-indic.tar.xz#/hyphen-indic.or11.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-indonesian.tar.xz#/hyphen-indonesian.or11.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-interlingua.tar.xz#/hyphen-interlingua.or11.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-sanskrit.tar.xz#/hyphen-sanskrit.or11.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-sanskrit.doc.tar.xz#/hyphen-sanskrit.doc.or11.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-thai.tar.xz#/hyphen-thai.or11.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-turkmen.tar.xz#/hyphen-turkmen.or11.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-vietnamese.tar.xz#/hyphen-vietnamese.or11.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-mr.tar.xz#/latex-mr.or11.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-mr.doc.tar.xz#/latex-mr.doc.or11.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexbangla.tar.xz#/latexbangla.or11.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexbangla.doc.tar.xz#/latexbangla.doc.or11.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latino-sine-flexione.tar.xz#/latino-sine-flexione.or11.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latino-sine-flexione.doc.tar.xz#/latino-sine-flexione.doc.or11.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-thai.tar.xz#/lshort-thai.or11.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-thai.doc.tar.xz#/lshort-thai.doc.or11.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-vietnamese.tar.xz#/lshort-vietnamese.or11.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-vietnamese.doc.tar.xz#/lshort-vietnamese.doc.or11.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntheorem-vn.tar.xz#/ntheorem-vn.or11.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntheorem-vn.doc.tar.xz#/ntheorem-vn.doc.or11.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-bn.tar.xz#/quran-bn.or11.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-bn.doc.tar.xz#/quran-bn.doc.or11.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-id.tar.xz#/quran-id.or11.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-id.doc.tar.xz#/quran-id.doc.or11.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-ur.tar.xz#/quran-ur.or11.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-ur.doc.tar.xz#/quran-ur.doc.or11.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sanskrit.tar.xz#/sanskrit.or11.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sanskrit.doc.tar.xz#/sanskrit.doc.or11.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sanskrit-t1.tar.xz#/sanskrit-t1.or11.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sanskrit-t1.doc.tar.xz#/sanskrit-t1.doc.or11.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thaienum.tar.xz#/thaienum.or11.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thaienum.doc.tar.xz#/thaienum.doc.or11.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thaispec.tar.xz#/thaispec.or11.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thaispec.doc.tar.xz#/thaispec.doc.or11.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tuzuk.tar.xz#/tuzuk.or11.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tuzuk.doc.tar.xz#/tuzuk.doc.or11.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-alphabets.tar.xz#/unicode-alphabets.or11.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-alphabets.doc.tar.xz#/unicode-alphabets.doc.or11.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vntex.tar.xz#/vntex.or11.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vntex.doc.tar.xz#/vntex.doc.or11.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wnri.tar.xz#/wnri.or11.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wnri.doc.tar.xz#/wnri.doc.or11.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wnri-latex.tar.xz#/wnri-latex.or11.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wnri-latex.doc.tar.xz#/wnri-latex.doc.or11.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-devanagari.tar.xz#/xetex-devanagari.or11.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-devanagari.doc.tar.xz#/xetex-devanagari.doc.or11.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-akshar
Requires:       texlive-amsldoc-vn
Requires:       texlive-aramaic-serto
Requires:       texlive-babel-azerbaijani
Requires:       texlive-babel-esperanto
Requires:       texlive-babel-georgian
Requires:       texlive-babel-hebrew
Requires:       texlive-babel-indonesian
Requires:       texlive-babel-interlingua
Requires:       texlive-babel-malay
Requires:       texlive-babel-sorbian
Requires:       texlive-babel-thai
Requires:       texlive-babel-vietnamese
Requires:       texlive-bangla
Requires:       texlive-bangtex
Requires:       texlive-bengali
Requires:       texlive-burmese
Requires:       texlive-cjhebrew
Requires:       texlive-collection-basic
Requires:       texlive-ctib
Requires:       texlive-culmus
Requires:       texlive-ebong
Requires:       texlive-ethiop
Requires:       texlive-ethiop-t1
Requires:       texlive-fc
Requires:       texlive-fonts-tlwg
Requires:       texlive-hebrew-fonts
Requires:       texlive-hindawi-latex-template
Requires:       texlive-hyphen-afrikaans
Requires:       texlive-hyphen-armenian
Requires:       texlive-hyphen-coptic
Requires:       texlive-hyphen-esperanto
Requires:       texlive-hyphen-ethiopic
Requires:       texlive-hyphen-georgian
Requires:       texlive-hyphen-hebrew
Requires:       texlive-hyphen-indic
Requires:       texlive-hyphen-indonesian
Requires:       texlive-hyphen-interlingua
Requires:       texlive-hyphen-sanskrit
Requires:       texlive-hyphen-thai
Requires:       texlive-hyphen-turkmen
Requires:       texlive-hyphen-vietnamese
Requires:       texlive-latex-mr
Requires:       texlive-latexbangla
Requires:       texlive-latino-sine-flexione
Requires:       texlive-lshort-thai
Requires:       texlive-lshort-vietnamese
Requires:       texlive-ntheorem-vn
Requires:       texlive-quran-bn
Requires:       texlive-quran-id
Requires:       texlive-quran-ur
Requires:       texlive-sanskrit
Requires:       texlive-sanskrit-t1
Requires:       texlive-thaienum
Requires:       texlive-thaispec
Requires:       texlive-tuzuk
Requires:       texlive-unicode-alphabets
Requires:       texlive-velthuis
Requires:       texlive-vntex
Requires:       texlive-wnri
Requires:       texlive-wnri-latex
Requires:       texlive-xetex-devanagari

%description
Support for languages not otherwise listed, including Indic, Thai, Vietnamese,
Hebrew, Indonesian, African languages, and plenty more. The split is made
simply on the basis of the size of the support, to keep both collection sizes
and the number of collections reasonable.

%package -n texlive-akshar
Summary:        Support for syllables in the Devanagari script
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(akshar.sty) = %{tl_version}

%description -n texlive-akshar
This LaTeX3 package provides macros and interfaces to work with Devanagari
characters and syllables in a more correct way.

%package -n texlive-amsldoc-vn
Summary:        Vietnamese translation of AMSLaTeX documentation
Version:        svn21855
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsldoc-vn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsldoc-vn-doc <= 11:%{version}

%description -n texlive-amsldoc-vn
This is a Vietnamese translation of amsldoc, the users' guide to amsmath.

%package -n texlive-aramaic-serto
Summary:        Fonts and LaTeX for Syriac written in Serto
Version:        svn74548
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(assyr.sty) = %{tl_version}
Provides:       tex(serto.sty) = %{tl_version}
Provides:       tex(syriac.sty) = %{tl_version}

%description -n texlive-aramaic-serto
This package enables (La)TeX users to typeset words or phrases (e-TeX
extensions are needed) in Syriac (Aramaic) using the Serto-alphabet. The
package includes a preprocessor written in Python (>= 1.5.2) in order to deal
with right-to-left typesetting for those who do not want to use elatex and to
choose the correct letter depending on word context (initial/medial/final
form). Detailed documentation and examples are included.

%package -n texlive-babel-azerbaijani
Summary:        Support for Azerbaijani within babel
Version:        svn44197
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(azerbaijani.ldf) = %{tl_version}

%description -n texlive-babel-azerbaijani
This is the babel style for Azerbaijani. This language poses special challenges
because no "traditional" font encoding contains the full character set, and
therefore a mixture must be used (e.g., T2A and T1). This package is compatible
with Unicode engines (LuaTeX, XeTeX), which are very likely the most convenient
way to write Azerbaijani documents.

%package -n texlive-babel-esperanto
Summary:        Babel support for Esperanto
Version:        svn75781
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(esperanto.ldf) = %{tl_version}

%description -n texlive-babel-esperanto
The package provides the language definition file for support of Esperanto in
babel. Some shortcuts are defined, as well as translations to Esperanto of
standard "LaTeX names".

%package -n texlive-babel-georgian
Summary:        Babel support for Georgian
Version:        svn45864
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(georgian.ldf) = %{tl_version}
Provides:       tex(georgian.sty) = %{tl_version}
Provides:       tex(georgiancaps.tex) = %{tl_version}

%description -n texlive-babel-georgian
The package provides support for use of Babel in documents written in Georgian.
The package is adapted for use both under 'traditional' TeX engines, and under
XeTeX and LuaTeX.

%package -n texlive-babel-hebrew
Summary:        Babel support for Hebrew
Version:        svn68016
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(inputenc.sty)
Provides:       tex(hebcal.sty) = %{tl_version}
Provides:       tex(hebrew.ldf) = %{tl_version}
Provides:       tex(hebrew_newcode.sty) = %{tl_version}
Provides:       tex(hebrew_oldcode.sty) = %{tl_version}
Provides:       tex(hebrew_p.sty) = %{tl_version}
Provides:       tex(rlbabel.def) = %{tl_version}

%description -n texlive-babel-hebrew
The package provides the language definition file for support of Hebrew in
babel. Macros to control the use of text direction control of TeX--XeT and
e-TeX are provided (and may be used elsewhere). Some shortcuts are defined, as
well as translations to Hebrew of standard "LaTeX names".

%package -n texlive-babel-indonesian
Summary:        Support for Indonesian within babel
Version:        svn75372
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bahasa.ldf) = %{tl_version}
Provides:       tex(bahasai.ldf) = %{tl_version}
Provides:       tex(indon.ldf) = %{tl_version}
Provides:       tex(indonesian.ldf) = %{tl_version}

%description -n texlive-babel-indonesian
This is the babel style for Indonesian.

%package -n texlive-babel-interlingua
Summary:        Babel support for Interlingua
Version:        svn30276
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(interlingua.ldf) = %{tl_version}

%description -n texlive-babel-interlingua
The package provides the language definition file for support of Interlingua in
babel. Translations to Interlingua of standard "LaTeX names" (no shortcuts are
provided). Interlingua itself is an auxiliary language, built from the common
vocabulary of Spanish/Portuguese, English, Italian and French, with some
normalisation of spelling.

%package -n texlive-babel-malay
Summary:        Support for Malay within babel
Version:        svn43234
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bahasam.ldf) = %{tl_version}
Provides:       tex(malay.ldf) = %{tl_version}
Provides:       tex(melayu.ldf) = %{tl_version}
Provides:       tex(meyalu.ldf) = %{tl_version}

%description -n texlive-babel-malay
This is the babel style for Malay.

%package -n texlive-babel-sorbian
Summary:        Babel support for Upper and Lower Sorbian
Version:        svn60975
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lsorbian.ldf) = %{tl_version}
Provides:       tex(usorbian.ldf) = %{tl_version}

%description -n texlive-babel-sorbian
The package provides language definitions file for support of both Upper and
Lower Sorbian, in babel. Some shortcuts are defined, as well as translations to
the relevant language of standard "LaTeX names".

%package -n texlive-babel-thai
Summary:        Support for Thai within babel
Version:        svn30564
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lthenc.def) = %{tl_version}
Provides:       tex(thai.ldf) = %{tl_version}
Provides:       tex(tis620.def) = %{tl_version}

%description -n texlive-babel-thai
The package provides support for typesetting Thai text. within the babel
system.

%package -n texlive-babel-vietnamese
Summary:        Babel support for typesetting Vietnamese
Version:        svn39246
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(vietnamese.ldf) = %{tl_version}

%description -n texlive-babel-vietnamese
The package provides the language definition file for support of Vietnamese in
babel.

%package -n texlive-bangla
Summary:        A comprehensive Bangla LaTeX package
Version:        svn76924
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-charissil
Requires:       texlive-doulossil
Requires:       tex(CharisSIL.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(polyglossia.sty)
Provides:       tex(bangla.sty) = %{tl_version}
Provides:       tex(banglamap.tex) = %{tl_version}

%description -n texlive-bangla
This package provides all the necessary LaTeX frontends for the Bangla language
and comes with some fonts of its own.

%package -n texlive-bangtex
Summary:        Writing Bangla and Assamese with LaTeX
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bangfont.tex) = %{tl_version}

%description -n texlive-bangtex
The bundle provides class files for writing Bangla and Assamese with LaTeX, and
Metafont sources for fonts.

%package -n texlive-bengali
Summary:        Support for the Bengali language
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(beng.sty) = %{tl_version}

%description -n texlive-bengali
The package is based on Velthuis' transliteration scheme, with extensions to
deal with the Bengali letters that are not in Devanagari. The package also
supports Assamese.

%package -n texlive-burmese
Summary:        Basic Support for Writing Burmese
Version:        svn25185
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(relsize.sty)
Provides:       tex(birm.sty) = %{tl_version}

%description -n texlive-burmese
This package provides basic support for writing Burmese. The package provides a
preprocessor (written in Perl), an Adobe Type 1 font, and LaTeX macros.

%package -n texlive-cjhebrew
Summary:        Typeset Hebrew with LaTeX
Version:        svn43444
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luabidi.sty)
Provides:       tex(cjhebrew.sty) = %{tl_version}

%description -n texlive-cjhebrew
The cjhebrew package provides Adobe Type 1 fonts for Hebrew, and LaTeX macros
to support their use. Hebrew text can be vocalised, and a few accents are also
available. The package makes it easy to include Hebrew text in other-language
documents. The package makes use of the e-TeX extensions to TeX, so should be
run using an "e-LaTeX".

%package -n texlive-ctib
Summary:        Tibetan for TeX and LaTeX2e
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(ctib.sty) = %{tl_version}
Provides:       tex(ctib.tex) = %{tl_version}
Provides:       tex(lctenc.def) = %{tl_version}

%description -n texlive-ctib
A package using a modified version of Sirlin's Tibetan font. An advantage of
this Tibetan implementation is that all consonant clusters are formed by TeX
and Metafont. No external preprocessor is needed.

%package -n texlive-culmus
Summary:        Hebrew fonts from the Culmus project
Version:        svn76924
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(culmus.sty) = %{tl_version}

%description -n texlive-culmus
Hebrew fonts from the Culmus Project. Both Type1 and Open/TrueType versions of
the fonts are provided, as well as font definition files. It is recommended to
use these fonts with the NHE8 font encoding, from the hebrew-fonts package.

%package -n texlive-ethiop
Summary:        LaTeX macros and fonts for typesetting Amharic
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(etharab.sty) = %{tl_version}
Provides:       tex(ethiop.ldf) = %{tl_version}
Provides:       tex(ethiop.sty) = %{tl_version}

%description -n texlive-ethiop
Ethiopian language support for the babel package, including a collection of
fonts and TeX macros for typesetting the characters of the languages of
Ethiopia, with Metafont fonts based on EthTeX's. The macros use the Babel
framework.

%package -n texlive-ethiop-t1
Summary:        Type 1 versions of Amharic fonts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ethiop-t1
These fonts are drop-in Adobe type 1 replacements for the fonts of the ethiop
package.

%package -n texlive-fc
Summary:        Fonts for African languages
Version:        svn32796
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(newlfont.sty)
Provides:       tex(fclfont.sty) = %{tl_version}
Provides:       tex(fcuse.sty) = %{tl_version}
Provides:       tex(t4enc.def) = %{tl_version}
Provides:       tex(t4phonet.sty) = %{tl_version}

%description -n texlive-fc
The fonts are provided as Metafont source, in the familiar arrangement of lots
of (autogenerated) preamble files and a modest set of glyph specifications. (A
similar arrangement appears in the ec and lh font bundles.)

%package -n texlive-fonts-tlwg
Summary:        Thai fonts for LaTeX from TLWG
Version:        svn60817
License:        GPL-2.0-or-later AND LPPL-1.3c AND Bitstream-Vera
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(fonts-tlwg.sty) = %{tl_version}

%description -n texlive-fonts-tlwg
A collection of free Thai fonts, supplied as FontForge sources, and with LaTeX
.fd files.

%package -n texlive-hebrew-fonts
Summary:        Input encodings, font encodings and font definition files for Hebrew
Version:        svn68038
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(8859-8.def) = %{tl_version}
Provides:       tex(cp1255.def) = %{tl_version}
Provides:       tex(cp862.def) = %{tl_version}
Provides:       tex(he8enc.def) = %{tl_version}
Provides:       tex(hebfont.sty) = %{tl_version}
Provides:       tex(lheenc.def) = %{tl_version}
Provides:       tex(nhe8enc.def) = %{tl_version}
Provides:       tex(si960.def) = %{tl_version}

%description -n texlive-hebrew-fonts
A collection of input encodings, font encodings and font definition files for
the Hebrew language.

%package -n texlive-hindawi-latex-template
Summary:        A LaTeX template for authors of the Hindawi journals
Version:        svn57757
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-hindawi-latex-template-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hindawi-latex-template-doc <= 11:%{version}

%description -n texlive-hindawi-latex-template
This package contains a LaTeX template for authors of the Hindawi journals.
Authors can use this template for formatting their research articles for
submissions. The package has been created and is maintained by the Typeset
team.

%package -n texlive-hyphen-afrikaans
Summary:        Afrikaans hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-af.ec.tex) = %{tl_version}
Provides:       tex(hyph-af.tex) = %{tl_version}
Provides:       tex(hyph-quote-af.tex) = %{tl_version}
Provides:       tex(loadhyph-af.tex) = %{tl_version}

%description -n texlive-hyphen-afrikaans
Hyphenation patterns for Afrikaans in T1/EC and UTF-8 encodings. OpenOffice
includes older patterns created by a different author, but the patterns
packaged with TeX are considered superior in quality.

%package -n texlive-hyphen-armenian
Summary:        Armenian hyphenation patterns.
Version:        svn73410
License:        LGPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-hy.tex) = %{tl_version}
Provides:       tex(loadhyph-hy.tex) = %{tl_version}

%description -n texlive-hyphen-armenian
Hyphenation patterns for Armenian for Unicode engines. Auto-generated from a
script included in hyph-utf8.

%package -n texlive-hyphen-coptic
Summary:        Coptic hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(copthyph.tex) = %{tl_version}
Provides:       tex(hyph-cop.tex) = %{tl_version}
Provides:       tex(loadhyph-cop.tex) = %{tl_version}

%description -n texlive-hyphen-coptic
Hyphenation patterns for Coptic in UTF-8 encoding as well as in ASCII-based
encoding for 8-bit engines. The latter can only be used with special Coptic
fonts (like CBcoptic). The patterns are considered experimental.

%package -n texlive-hyphen-esperanto
Summary:        Esperanto hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-eo.il3.tex) = %{tl_version}
Provides:       tex(hyph-eo.tex) = %{tl_version}
Provides:       tex(loadhyph-eo.tex) = %{tl_version}

%description -n texlive-hyphen-esperanto
Hyphenation patterns for Esperanto ISO Latin 3 and UTF-8 encodings. Note that
TeX distributions don't ship any suitable fonts in Latin 3 encoding, so unless
you create your own font support or want to use MlTeX, using native Unicode
engines is highly recommended.

%package -n texlive-hyphen-ethiopic
Summary:        Hyphenation patterns for Ethiopic scripts.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-mul-ethi.tex) = %{tl_version}
Provides:       tex(loadhyph-mul-ethi.tex) = %{tl_version}

%description -n texlive-hyphen-ethiopic
Hyphenation patterns for languages written using the Ethiopic script for
Unicode engines. They are not supposed to be linguistically relevant in all
cases and should, for proper typography, be replaced by files tailored to
individual languages.

%package -n texlive-hyphen-georgian
Summary:        Georgian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ka.t8m.tex) = %{tl_version}
Provides:       tex(hyph-ka.tex) = %{tl_version}
Provides:       tex(loadhyph-ka.tex) = %{tl_version}

%description -n texlive-hyphen-georgian
Hyphenation patterns for Georgian in T8M, T8K and UTF-8 encodings.

%package -n texlive-hyphen-hebrew
Summary:        Hebrew hyphenation patterns.
Version:        svn74032
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-he.tex) = %{tl_version}

%description -n texlive-hyphen-hebrew
Prevents hyphenation in Arabic.

%package -n texlive-hyphen-indic
Summary:        Indic hyphenation patterns.
Version:        svn73410
License:        MIT OR LGPL-3.0-or-later OR GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-as.tex) = %{tl_version}
Provides:       tex(hyph-bn.tex) = %{tl_version}
Provides:       tex(hyph-gu.tex) = %{tl_version}
Provides:       tex(hyph-hi.tex) = %{tl_version}
Provides:       tex(hyph-kn.tex) = %{tl_version}
Provides:       tex(hyph-ml.tex) = %{tl_version}
Provides:       tex(hyph-mr.tex) = %{tl_version}
Provides:       tex(hyph-or.tex) = %{tl_version}
Provides:       tex(hyph-pa.tex) = %{tl_version}
Provides:       tex(hyph-pi.tex) = %{tl_version}
Provides:       tex(hyph-ta.tex) = %{tl_version}
Provides:       tex(hyph-te.tex) = %{tl_version}
Provides:       tex(loadhyph-as.tex) = %{tl_version}
Provides:       tex(loadhyph-bn.tex) = %{tl_version}
Provides:       tex(loadhyph-gu.tex) = %{tl_version}
Provides:       tex(loadhyph-hi.tex) = %{tl_version}
Provides:       tex(loadhyph-kn.tex) = %{tl_version}
Provides:       tex(loadhyph-ml.tex) = %{tl_version}
Provides:       tex(loadhyph-mr.tex) = %{tl_version}
Provides:       tex(loadhyph-or.tex) = %{tl_version}
Provides:       tex(loadhyph-pa.tex) = %{tl_version}
Provides:       tex(loadhyph-pi.tex) = %{tl_version}
Provides:       tex(loadhyph-ta.tex) = %{tl_version}
Provides:       tex(loadhyph-te.tex) = %{tl_version}

%description -n texlive-hyphen-indic
Hyphenation patterns for Assamese, Bengali, Gujarati, Hindi, Kannada,
Malayalam, Marathi, Oriya, Panjabi, Tamil and Telugu for Unicode engines.

%package -n texlive-hyphen-indonesian
Summary:        Indonesian hyphenation patterns.
Version:        svn73410
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-id.tex) = %{tl_version}
Provides:       tex(loadhyph-id.tex) = %{tl_version}

%description -n texlive-hyphen-indonesian
Hyphenation patterns for Indonesian (Bahasa Indonesia) in ASCII encoding. They
are probably also usable for Malay (Bahasa Melayu).

%package -n texlive-hyphen-interlingua
Summary:        Interlingua hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ia.tex) = %{tl_version}
Provides:       tex(loadhyph-ia.tex) = %{tl_version}

%description -n texlive-hyphen-interlingua
Hyphenation patterns for Interlingua in ASCII encoding.

%package -n texlive-hyphen-sanskrit
Summary:        Sanskrit hyphenation patterns.
Version:        svn73410
License:        LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sa.tex) = %{tl_version}
Provides:       tex(loadhyph-sa.tex) = %{tl_version}

%description -n texlive-hyphen-sanskrit
Hyphenation patterns for Sanskrit and Prakrit in transliteration, and in
Devanagari, Bengali, Kannada, Malayalam and Telugu scripts for Unicode engines.

%package -n texlive-hyphen-thai
Summary:        Thai hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-th.lth.tex) = %{tl_version}
Provides:       tex(hyph-th.tex) = %{tl_version}
Provides:       tex(loadhyph-th.tex) = %{tl_version}

%description -n texlive-hyphen-thai
Hyphenation patterns for Thai in LTH and UTF-8 encodings.

%package -n texlive-hyphen-turkmen
Summary:        Turkmen hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-tk.ec.tex) = %{tl_version}
Provides:       tex(hyph-tk.tex) = %{tl_version}
Provides:       tex(loadhyph-tk.tex) = %{tl_version}

%description -n texlive-hyphen-turkmen
Hyphenation patterns for Turkmen in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-vietnamese
Summary:        Vietnamese hyphenation patterns.
Version:        svn74032
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-vi.tex) = %{tl_version}

%description -n texlive-hyphen-vietnamese
Prevents hyphenation in Vietnamese.

%package -n texlive-latex-mr
Summary:        A practical guide to LaTeX and Polyglossia for Marathi and other Indian languages
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-mr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-mr-doc <= 11:%{version}

%description -n texlive-latex-mr
The package provides a short guide to LaTeX and specifically to the polyglossia
package. This document aims to introduce LaTeX and polyglossia for Indian
languages. Though the document often discusses the language Marathi, the
discussion applies to other India languages also, with some minute changes
which are described in Section 1.2. We assume that the user of this document
knows basic (La)TeX or has, at least, tried her hand on it. This document is
not very suitable for first time users.

%package -n texlive-latexbangla
Summary:        Enhanced LaTeX integration for Bangla
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(ucharclasses.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(latexbangla.sty) = %{tl_version}

%description -n texlive-latexbangla
This package simplifies the process of writing Bangla in LaTeX and addresses
most of the associated typesetting issues. Notable features: Automated
transition from Bangla to English and vice versa. Patch for the unproportionate
whitespace issue in popular Bangla fonts. Full support for all the common
commands and environments. Bangla numbering for page, section, chapter,
footnotes etc. (extending polyglossia's support). New theorem, problems,
example, solution and other environments, all of which are in Bangla.

%package -n texlive-latino-sine-flexione
Summary:        LaTeX support for documents written in Peano's Interlingua
Version:        svn69568
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(datetime.sty)
Requires:       tex(fontenc.sty)
Provides:       tex(latino-sine-flexione.sty) = %{tl_version}

%description -n texlive-latino-sine-flexione
Latino sine Flexione (or Interlingua) is a language constructed by Giuseppe
Peano at the beginning of the last century. This simplified Latin is designed
to be an instrument for international cooperation, especially in the academic
sphere. (Note that this "Interlingua" is different from the "Interlingua" that
was created a few decades after Peano's work and which is supported by
babel-interlingua!) This package provides the necessary translations to use the
language within a LaTeX document. It also imports fontenc in order to be able
to use ligatures and quotation marks. Finally, it offers a text in Interlingua
that can be used as a dummy text: Fundamento de intelligentia. This article by
H. Bijlsma was first published in Schola et Vita Anno I (1926).

%package -n texlive-lshort-thai
Summary:        Introduction to LaTeX in Thai
Version:        svn55643
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-thai-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-thai-doc <= 11:%{version}

%description -n texlive-lshort-thai
This is the Thai translation of the Short Introduction to LaTeX2e.

%package -n texlive-lshort-vietnamese
Summary:        Vietnamese version of the LaTeX introduction
Version:        svn55643
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-vietnamese-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-vietnamese-doc <= 11:%{version}

%description -n texlive-lshort-vietnamese
Vietnamese version of A Short Introduction to LaTeX2e.

%package -n texlive-ntheorem-vn
Summary:        Vietnamese translation of documentation of ntheorem
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ntheorem-vn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ntheorem-vn-doc <= 11:%{version}

%description -n texlive-ntheorem-vn
This is a translation of the documentation provided with ntheorem.

%package -n texlive-quran-bn
Summary:        Bengali translations to the quran package
Version:        svn74830
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-bn.sty) = %{tl_version}
Provides:       tex(qurantext-bni.translation.def) = %{tl_version}
Provides:       tex(qurantext-bnii.translation.def) = %{tl_version}

%description -n texlive-quran-bn
The package is prepared for typesetting some Bengali translations of the Holy
Quran. It adds two Bengali translations to the quran package.

%package -n texlive-quran-id
Summary:        Indonesian translation extension to the quran package
Version:        svn74874
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-id.sty) = %{tl_version}
Provides:       tex(qurantext-idi.translation.def) = %{tl_version}
Provides:       tex(qurantext-idii.translation.def) = %{tl_version}

%description -n texlive-quran-id
The package is prepared for typesetting some Indonesian translations of the
Holy Quran. It adds two Indonesian translations to the quran package.

%package -n texlive-quran-ur
Summary:        Urdu translations to the quran package
Version:        svn74829
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-ur.sty) = %{tl_version}
Provides:       tex(qurantext-uri.translation.def) = %{tl_version}
Provides:       tex(qurantext-urii.translation.def) = %{tl_version}
Provides:       tex(qurantext-uriii.translation.def) = %{tl_version}
Provides:       tex(qurantext-uriv.translation.def) = %{tl_version}
Provides:       tex(qurantext-urv.translation.def) = %{tl_version}
Provides:       tex(qurantext-urvi.translation.def) = %{tl_version}
Provides:       tex(qurantext-urvii.translation.def) = %{tl_version}
Provides:       tex(qurantext-urviii.translation.def) = %{tl_version}

%description -n texlive-quran-ur
The package is prepared for typesetting some Urdu translations of the Holy
Quran. It adds eight Urdu translations to the quran package.

%package -n texlive-sanskrit
Summary:        Sanskrit support
Version:        svn76869
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(relsize.sty)
Provides:       tex(skt.sty) = %{tl_version}

%description -n texlive-sanskrit
A font and pre-processor suitable for the production of documents written in
Sanskrit. Type 1 versions of the fonts are available.

%package -n texlive-sanskrit-t1
Summary:        Type 1 version of 'skt' fonts for Sanskrit
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sanskrit-t1
The sanskrit-t1 font package provides Type 1 version of Charles Wikner's skt
font series for the Sanskrit language.

%package -n texlive-thaienum
Summary:        Thai labels in enumerate environments
Version:        svn44140
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(enumitem.sty)
Provides:       tex(thaienum.sty) = %{tl_version}

%description -n texlive-thaienum
This LaTeX package provides a command to use Thai numerals or characters as
labels in enumerate environments. Once the package is loaded with
\usepackage{thaienum} you can use labels such as \thainum* or \thaimultialph*
in conjunction with the package enumitem. Concrete examples are given in the
documentation.

%package -n texlive-thaispec
Summary:        Thai Language Typesetting in XeLaTeX
Version:        svn58019
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mathspec.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(setspace.sty)
Requires:       tex(ucharclasses.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Provides:       tex(thaispec.sty) = %{tl_version}

%description -n texlive-thaispec
This package allows you to input Thai characters directly to LaTeX documents
and choose any (system wide) Thai fonts for typesetting in XeLaTeX. It also
tries to appropriately justify paragraphs with no more external tools. Required
packages are fontspec, ucharclasses, polyglossia, setspace, kvoptions, xstring,
and xpatch.

%package -n texlive-tuzuk
Summary:        Turkish bylaws and regulations document class
Version:        svn74620
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tuzuk
The tuzuk class provides a standardized format for writing bylaws and
regulations in Turkish-governmental style. It includes features for creating
numbered articles, subsections, and signature areas commonly found in legal
documents. Features: Easy creation of numbered articles with the \madde
command, Section titles with \bolumadi, Automatic lettered lists with the fikra
environment, Built-in signature area formatting with \imzalar, Full Turkish
language support. Built originally for creating the regulation for Ozgur
Yazilim Dernegi (The Free Software Association in Turkey), https://oyd.org.tr/.
Explanation of the package name: "tuzuk" in Turkish means "regulations", as a
document. For example, GDPR, which stands for "General Data Protection
Regulation", translates as "Genel Veri Koruma Tuzugu". In Turkish law, the
non-profit associations have a "tuzuk" as their constitution-like governing
document.

%package -n texlive-unicode-alphabets
Summary:        Macros for using characters from Unicode's Private Use Area
Version:        svn66225
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(csvsimple.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(xparse.sty)
Provides:       tex(unicode-alphabets.sty) = %{tl_version}

%description -n texlive-unicode-alphabets
While Unicode supports the vast majority of use cases, there are certain
specialized niches which require characters and glyphs not (yet) represented in
the standard. Thus the Private Use Area (PUA) at code points E000-F8FF, which
enables third parties to define arbitrary character sets. This package allows
configuring a number of macros for using various PUA character sets in LaTeX
(AGL, CYFI, MUFI, SIL, TITUS, UCSUR, UNZ), to enable transcription and display
of medieval and other documents.

%package -n texlive-vntex
Summary:        Support for Vietnamese
Version:        svn62837
License:        GPL-1.0-or-later AND LGPL-2.1-or-later AND LPPL-1.3c AND LicenseRef-Utopia
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cmap.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(ucs.sty)
Provides:       tex(dblaccnt.sty) = %{tl_version}
Provides:       tex(dblaccnt.tex) = %{tl_version}
Provides:       tex(mcviscii.def) = %{tl_version}
Provides:       tex(pd1supp.def) = %{tl_version}
Provides:       tex(swpvntex.sty) = %{tl_version}
Provides:       tex(t5code.tex) = %{tl_version}
Provides:       tex(t5enc.def) = %{tl_version}
Provides:       tex(tcvn.def) = %{tl_version}
Provides:       tex(varioref-vi.sty) = %{tl_version}
Provides:       tex(vietnam.sty) = %{tl_version}
Provides:       tex(viscii.def) = %{tl_version}
Provides:       tex(vncaps.tex) = %{tl_version}
Provides:       tex(vntex.sty) = %{tl_version}
Provides:       tex(vntexinfo.tex) = %{tl_version}
Provides:       tex(vps.def) = %{tl_version}

%description -n texlive-vntex
The vntex bundle provides fonts, Plain TeX, texinfo and LaTeX macros for
typesetting documents in Vietnamese. Users of the fonts (in both Metafont and
Adobe Type 1 format) of this bundle may alternatively use the lm fonts bundle,
for which map files are available to provide a Vietnamese version.

%package -n texlive-wnri
Summary:        Ridgeway's fonts
Version:        svn22459
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-wnri
Fonts (as Metafont source) for Old English, Indic languages in Roman
transliteration and Puget Salish (Lushootseed) and other Native American
languages.

%package -n texlive-wnri-latex
Summary:        LaTeX support for wnri fonts
Version:        svn22338
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(wnri.def) = %{tl_version}
Provides:       tex(wnri.sty) = %{tl_version}

%description -n texlive-wnri-latex
LaTeX support for the wnri fonts.

%package -n texlive-xetex-devanagari
Summary:        XeTeX input map for Unicode Devanagari
Version:        svn34296
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xetex-devanagari
The package provides a map for use with Jonathan Kew's TECkit, to translate
Devanagari (encoded according to the Harvard/Kyoto convention) to Unicode
(range 0900-097F).

%post -n texlive-hyphen-afrikaans
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/afrikaans.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "afrikaans loadhyph-af.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{afrikaans}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{afrikaans}{loadhyph-af.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-afrikaans
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/afrikaans.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{afrikaans}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-armenian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/armenian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "armenian loadhyph-hy.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{armenian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{armenian}{loadhyph-hy.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-armenian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/armenian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{armenian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-coptic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/coptic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "coptic loadhyph-cop.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{coptic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{coptic}{loadhyph-cop.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-coptic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/coptic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{coptic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-esperanto
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/esperanto.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "esperanto loadhyph-eo.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{esperanto}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{esperanto}{loadhyph-eo.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-esperanto
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/esperanto.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{esperanto}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-ethiopic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/ethiopic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ethiopic loadhyph-mul-ethi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=amharic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=amharic" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=geez.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=geez" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ethiopic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ethiopic}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{amharic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{amharic}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{geez}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{geez}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ethiopic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/ethiopic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=amharic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=geez.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ethiopic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{amharic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{geez}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-georgian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/georgian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "georgian loadhyph-ka.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{georgian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{georgian}{loadhyph-ka.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-georgian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/georgian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{georgian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-hebrew
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/hebrew.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "hebrew hyph-he.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{hebrew}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{hebrew}{hyph-he.tex}{}{0}{0}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-hebrew
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/hebrew.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{hebrew}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-indic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/assamese.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "assamese loadhyph-as.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{assamese}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{assamese}{loadhyph-as.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/bengali.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "bengali loadhyph-bn.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{bengali}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{bengali}{loadhyph-bn.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/gujarati.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "gujarati loadhyph-gu.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{gujarati}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{gujarati}{loadhyph-gu.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/hindi.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "hindi loadhyph-hi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{hindi}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{hindi}{loadhyph-hi.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/kannada.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "kannada loadhyph-kn.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{kannada}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{kannada}{loadhyph-kn.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/malayalam.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "malayalam loadhyph-ml.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{malayalam}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{malayalam}{loadhyph-ml.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/marathi.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "marathi loadhyph-mr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{marathi}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{marathi}{loadhyph-mr.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/oriya.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "oriya loadhyph-or.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{oriya}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{oriya}{loadhyph-or.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/pali.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "pali loadhyph-pi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{pali}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{pali}{loadhyph-pi.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/panjabi.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "panjabi loadhyph-pa.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{panjabi}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{panjabi}{loadhyph-pa.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/tamil.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "tamil loadhyph-ta.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{tamil}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{tamil}{loadhyph-ta.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/telugu.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "telugu loadhyph-te.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{telugu}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{telugu}{loadhyph-te.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-indic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/assamese.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{assamese}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/bengali.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{bengali}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/gujarati.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{gujarati}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/hindi.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{hindi}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/kannada.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{kannada}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/malayalam.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{malayalam}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/marathi.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{marathi}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/oriya.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{oriya}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/pali.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{pali}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/panjabi.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{panjabi}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/tamil.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{tamil}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/telugu.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{telugu}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-indonesian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/indonesian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "indonesian loadhyph-id.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{indonesian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{indonesian}{loadhyph-id.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-indonesian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/indonesian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{indonesian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-interlingua
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/interlingua.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "interlingua loadhyph-ia.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{interlingua}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{interlingua}{loadhyph-ia.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-interlingua
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/interlingua.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{interlingua}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-sanskrit
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/sanskrit.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "sanskrit loadhyph-sa.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{sanskrit}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{sanskrit}{loadhyph-sa.tex}{}{1}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-sanskrit
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/sanskrit.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{sanskrit}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-thai
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/thai.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "thai loadhyph-th.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{thai}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{thai}{loadhyph-th.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-thai
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/thai.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{thai}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-turkmen
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/turkmen.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "turkmen loadhyph-tk.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{turkmen}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{turkmen}{loadhyph-tk.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-turkmen
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/turkmen.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{turkmen}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-vietnamese
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/vietnamese.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "vietnamese hyph-vi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{vietnamese}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{vietnamese}{hyph-vi.tex}{}{0}{0}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-vietnamese
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/vietnamese.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{vietnamese}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%prep
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-akshar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/akshar/
%doc %{_texmf_main}/doc/latex/akshar/

%files -n texlive-amsldoc-vn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amsldoc-vn/

%files -n texlive-aramaic-serto
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/aramaic-serto/
%{_texmf_main}/fonts/map/dvips/aramaic-serto/
%{_texmf_main}/fonts/source/public/aramaic-serto/
%{_texmf_main}/fonts/tfm/public/aramaic-serto/
%{_texmf_main}/fonts/type1/public/aramaic-serto/
%{_texmf_main}/tex/latex/aramaic-serto/
%doc %{_texmf_main}/doc/latex/aramaic-serto/

%files -n texlive-babel-azerbaijani
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-azerbaijani/
%doc %{_texmf_main}/doc/generic/babel-azerbaijani/

%files -n texlive-babel-esperanto
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-esperanto/
%doc %{_texmf_main}/doc/generic/babel-esperanto/

%files -n texlive-babel-georgian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-georgian/
%doc %{_texmf_main}/doc/generic/babel-georgian/

%files -n texlive-babel-hebrew
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-hebrew/
%doc %{_texmf_main}/doc/generic/babel-hebrew/

%files -n texlive-babel-indonesian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-indonesian/
%doc %{_texmf_main}/doc/generic/babel-indonesian/

%files -n texlive-babel-interlingua
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-interlingua/
%doc %{_texmf_main}/doc/generic/babel-interlingua/

%files -n texlive-babel-malay
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-malay/
%doc %{_texmf_main}/doc/generic/babel-malay/

%files -n texlive-babel-sorbian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-sorbian/
%doc %{_texmf_main}/doc/generic/babel-sorbian/

%files -n texlive-babel-thai
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-thai/
%doc %{_texmf_main}/doc/generic/babel-thai/

%files -n texlive-babel-vietnamese
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-vietnamese/
%doc %{_texmf_main}/doc/generic/babel-vietnamese/

%files -n texlive-bangla
%license lppl1.3c.txt
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/bangla/
%{_texmf_main}/tex/latex/bangla/
%doc %{_texmf_main}/doc/latex/bangla/

%files -n texlive-bangtex
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/bangtex/
%{_texmf_main}/fonts/tfm/public/bangtex/
%{_texmf_main}/tex/latex/bangtex/
%doc %{_texmf_main}/doc/latex/bangtex/

%files -n texlive-bengali
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/bengali/
%{_texmf_main}/fonts/tfm/public/bengali/
%{_texmf_main}/tex/latex/bengali/
%doc %{_texmf_main}/doc/fonts/bengali/

%files -n texlive-burmese
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/burmese/
%{_texmf_main}/fonts/tfm/public/burmese/
%{_texmf_main}/fonts/type1/public/burmese/
%{_texmf_main}/tex/latex/burmese/
%doc %{_texmf_main}/doc/fonts/burmese/

%files -n texlive-cjhebrew
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/cjhebrew/
%{_texmf_main}/fonts/enc/dvips/cjhebrew/
%{_texmf_main}/fonts/map/dvips/cjhebrew/
%{_texmf_main}/fonts/tfm/public/cjhebrew/
%{_texmf_main}/fonts/type1/public/cjhebrew/
%{_texmf_main}/fonts/vf/public/cjhebrew/
%{_texmf_main}/tex/latex/cjhebrew/
%doc %{_texmf_main}/doc/latex/cjhebrew/

%files -n texlive-ctib
%license gpl2.txt
%{_texmf_main}/fonts/source/public/ctib/
%{_texmf_main}/fonts/tfm/public/ctib/
%{_texmf_main}/tex/latex/ctib/
%doc %{_texmf_main}/doc/latex/ctib/

%files -n texlive-culmus
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/culmus/
%{_texmf_main}/fonts/enc/dvips/culmus/
%{_texmf_main}/fonts/map/dvips/culmus/
%{_texmf_main}/fonts/opentype/public/culmus/
%{_texmf_main}/fonts/tfm/public/culmus/
%{_texmf_main}/fonts/truetype/public/culmus/
%{_texmf_main}/fonts/type1/public/culmus/
%{_texmf_main}/fonts/type3/culmus/
%{_texmf_main}/fonts/vf/public/culmus/
%{_texmf_main}/tex/latex/culmus/
%doc %{_texmf_main}/doc/fonts/culmus/

%files -n texlive-ethiop
%license gpl2.txt
%{_texmf_main}/fonts/ofm/public/ethiop/
%{_texmf_main}/fonts/ovf/public/ethiop/
%{_texmf_main}/fonts/ovp/public/ethiop/
%{_texmf_main}/fonts/source/public/ethiop/
%{_texmf_main}/fonts/tfm/public/ethiop/
%{_texmf_main}/omega/ocp/ethiop/
%{_texmf_main}/omega/otp/ethiop/
%{_texmf_main}/tex/latex/ethiop/
%doc %{_texmf_main}/doc/latex/ethiop/

%files -n texlive-ethiop-t1
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/ethiop-t1/
%{_texmf_main}/fonts/type1/public/ethiop-t1/
%doc %{_texmf_main}/doc/latex/ethiop-t1/

%files -n texlive-fc
%license gpl2.txt
%{_texmf_main}/fonts/source/jknappen/fc/
%{_texmf_main}/fonts/tfm/jknappen/fc/
%{_texmf_main}/tex/latex/fc/
%doc %{_texmf_main}/doc/fonts/fc/

%files -n texlive-fonts-tlwg
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/fonts-tlwg/
%{_texmf_main}/fonts/enc/dvips/fonts-tlwg/
%{_texmf_main}/fonts/map/dvips/fonts-tlwg/
%{_texmf_main}/fonts/opentype/public/fonts-tlwg/
%{_texmf_main}/fonts/tfm/public/fonts-tlwg/
%{_texmf_main}/fonts/type1/public/fonts-tlwg/
%{_texmf_main}/fonts/vf/public/fonts-tlwg/
%{_texmf_main}/tex/latex/fonts-tlwg/
%doc %{_texmf_main}/doc/fonts/fonts-tlwg/

%files -n texlive-hebrew-fonts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hebrew-fonts/
%doc %{_texmf_main}/doc/latex/hebrew-fonts/

%files -n texlive-hindawi-latex-template
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/hindawi-latex-template/

%files -n texlive-hyphen-afrikaans
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-armenian
%license lgpl.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-coptic
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-esperanto
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-ethiopic
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-georgian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-hebrew
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-indic
%license mit.txt
%license lgpl.txt
%license gpl3.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-indonesian
%license gpl2.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-interlingua
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-sanskrit
%{_texmf_main}/tex/generic/hyph-utf8/
%doc %{_texmf_main}/doc/generic/hyph-utf8/

%files -n texlive-hyphen-thai
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-turkmen
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-vietnamese
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-latex-mr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-mr/

%files -n texlive-latexbangla
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/latexbangla/
%doc %{_texmf_main}/doc/latex/latexbangla/

%files -n texlive-latino-sine-flexione
%license pd.txt
%{_texmf_main}/tex/latex/latino-sine-flexione/
%doc %{_texmf_main}/doc/latex/latino-sine-flexione/

%files -n texlive-lshort-thai
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-thai/

%files -n texlive-lshort-vietnamese
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/lshort-vietnamese/

%files -n texlive-ntheorem-vn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/ntheorem-vn/

%files -n texlive-quran-bn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quran-bn/
%doc %{_texmf_main}/doc/latex/quran-bn/

%files -n texlive-quran-id
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/quran-id/
%doc %{_texmf_main}/doc/xelatex/quran-id/

%files -n texlive-quran-ur
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quran-ur/
%doc %{_texmf_main}/doc/latex/quran-ur/

%files -n texlive-sanskrit
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/sanskrit/
%{_texmf_main}/fonts/tfm/public/sanskrit/
%{_texmf_main}/tex/latex/sanskrit/
%doc %{_texmf_main}/doc/latex/sanskrit/

%files -n texlive-sanskrit-t1
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/sanskrit-t1/
%{_texmf_main}/fonts/type1/public/sanskrit-t1/
%doc %{_texmf_main}/doc/fonts/sanskrit-t1/

%files -n texlive-thaienum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thaienum/
%doc %{_texmf_main}/doc/latex/thaienum/

%files -n texlive-thaispec
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thaispec/
%doc %{_texmf_main}/doc/latex/thaispec/

%files -n texlive-tuzuk
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tuzuk/
%doc %{_texmf_main}/doc/latex/tuzuk/

%files -n texlive-unicode-alphabets
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/unicode-alphabets/
%doc %{_texmf_main}/doc/latex/unicode-alphabets/

%files -n texlive-vntex
%license gpl.txt
%license lgpl2.1.txt
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/vntex/chartervn/
%{_texmf_main}/fonts/afm/vntex/grotesqvn/
%{_texmf_main}/fonts/afm/vntex/urwvn/
%{_texmf_main}/fonts/afm/vntex/vntopia/
%{_texmf_main}/fonts/enc/dvips/vntex/
%{_texmf_main}/fonts/enc/pdftex/vntex/
%{_texmf_main}/fonts/map/dvips/vntex/
%{_texmf_main}/fonts/source/vntex/vnr/
%{_texmf_main}/fonts/tfm/vntex/arevvn/
%{_texmf_main}/fonts/tfm/vntex/chartervn/
%{_texmf_main}/fonts/tfm/vntex/cmbrightvn/
%{_texmf_main}/fonts/tfm/vntex/concretevn/
%{_texmf_main}/fonts/tfm/vntex/grotesqvn/
%{_texmf_main}/fonts/tfm/vntex/txttvn/
%{_texmf_main}/fonts/tfm/vntex/urwvn/
%{_texmf_main}/fonts/tfm/vntex/vnr/
%{_texmf_main}/fonts/tfm/vntex/vntopia/
%{_texmf_main}/fonts/type1/vntex/arevvn/
%{_texmf_main}/fonts/type1/vntex/chartervn/
%{_texmf_main}/fonts/type1/vntex/cmbrightvn/
%{_texmf_main}/fonts/type1/vntex/concretevn/
%{_texmf_main}/fonts/type1/vntex/grotesqvn/
%{_texmf_main}/fonts/type1/vntex/txttvn/
%{_texmf_main}/fonts/type1/vntex/urwvn/
%{_texmf_main}/fonts/type1/vntex/vnr/
%{_texmf_main}/fonts/type1/vntex/vntopia/
%{_texmf_main}/fonts/vf/vntex/chartervn/
%{_texmf_main}/fonts/vf/vntex/urwvn/
%{_texmf_main}/fonts/vf/vntex/vntopia/
%{_texmf_main}/tex/latex/vntex/
%{_texmf_main}/tex/plain/vntex/
%doc %{_texmf_main}/doc/generic/vntex/

%files -n texlive-wnri
%license gpl2.txt
%{_texmf_main}/fonts/source/public/wnri/
%{_texmf_main}/fonts/tfm/public/wnri/
%doc %{_texmf_main}/doc/fonts/wnri/

%files -n texlive-wnri-latex
%license gpl2.txt
%{_texmf_main}/tex/latex/wnri-latex/
%doc %{_texmf_main}/doc/latex/wnri-latex/

%files -n texlive-xetex-devanagari
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%doc %{_texmf_main}/doc/xetex/xetex-devanagari/

%changelog
%autochangelog
