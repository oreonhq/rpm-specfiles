%global source0_hash 8d69c4697c25bce7949926b383cb49177a6e47f89198c55cafbeb63b911c1471de66e964dfc6d23eef32c49faece37bfba83e88bf0b4f5216edec8bb2f34e514

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langchinese
Epoch:          12
Version:        svn77432
Release:        5%{?dist}
Summary:        Chinese

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 2d4c0f91dd483df95bf91056e4d7cbc28b681fc9f42704cdbff297ceb4f8110affbed879cc8b15061c309764e1fdcce01fd47c2d742df441ed191f83a065538b
%global source3_hash 327dbc2cc7b4bad5e410dbb07dd2a2d5052dcb54c98310ffc3596c1e5b4121c1a12e3067b7074f209a3972cb51280f057cfe718eb963869bf05a76e17c528dee
%global source4_hash f0559968e2659a4e899bb0ee1e6236f4bf7f4133c96c146a189b42fe0ce7f375ffc5c62efd8acffa68b36c92159c28eb54167a7625b606cf7644c0a072d7f8e9
%global source5_hash 000030c21bf1ccd74ebc1c6bf8e46dc5d9f884480b2c31407353a3ff45a4d1072f759e9e31abbe5c9de7dfc68820fa359d42c5e980bfb7e9d408f015f8944aab
%global source6_hash 34608d6412d7936a15bf649555683ff03c5021e1688c99285a6b7ecdfc3a43eac4ed32108626243d6e9b07c23c557f07762897a96501a27412c7c5d039747553
%global source7_hash a0087e5be69962c671e1972d9e7be12f76be64582182afe042693cbad92cf3fd027422c605dcf7860cd2e61f0b925860a50e94523b9ae2d1af7a8aa6d356c3a7
%global source8_hash 1efc7098392ac5cad5eeaa0dcf527bd158e3f7497ff1992603b833ff63d5cfa61fe5e7bc33c5cc0c441c13fc03dfe1e18a334411be6ad2f5acc94c902e9ccf2c
%global source9_hash b7dbcf256cffae9cc8f5027934946929b4be7a8794fb8364892802eeff4e7cf970ca8549ef442a35f173ada61533b51c2da301bf2ce931107a7ce0c564ce0c60
%global source10_hash c04fc953a0a9035c238b9f80873d9fc605b23b322e898ae55b8eda7537f0172076e512022b163e3cd397ce2e4e721afa2e981454db53511c1a7347a017185df5
%global source11_hash 0f82e25773a14b0f81b34354f16931834d0496b2c6636c498c6af686f46e7ff93a274739a1a4c189433c9df1ae91ca010f0887081c81f2ac9006a105c7fd4ac9
%global source12_hash 0b3645da07e0fc9482cfeddd93f949e18dc12b6aa02e5a6c45669f3d5f7f25d5fa7ff4992f40b9b71894e21b5b1855999ba8e1b130be27e8b7001444ed30db0f
%global source13_hash 264c64f2ae29bff96b428500af07a81402434d9422792a36ee0da74e9821f161cf8281d38317787c0db78109d2eeaaff4e62730855ae1f1e1f250f4173740d35
%global source14_hash 79364716f5edaafe18185b6bd22a66b81bd8bfc8b6e9061496f0844a3ba6bb73dc8534ff7391b2736f5f12c44ffb241e1a7cf3a92656674dff3961284eb114a2
%global source15_hash bc7fd6eeca1d748bc4fff784b022924c0e936902fe34fec33e015c3f20c7ab8f1ce416131ccd96d692a315b60b033389dea22e572c44c607c6cd98ca4e45dc1b
%global source16_hash 39ff8931e0007a78e4fa0788d7c7fcd8f25dd4cf4fa3f34b694e681e10dfb3d804842daf45a6e56b5ff450bb965bc322dcf593bdce176ffec27f4696c1c99fc0
%global source17_hash 0942a249a30f97d56bf5cbac2eb4de285a63406620b825a36d9ff8d46fbccd614af488f89e2af7472f1a9075a0e2b7228bb65a5804451df6945ce6bf4287b0a2
%global source18_hash bb05e97334ba5821f496f1015939251df8bd91755cbea21340e2ed932355998a60eebfcf14c1b0d5af91905e8588d05e5d9e8250855ae5c5815fa6ba7b192719
%global source19_hash 647bc6ff26f249a2392749b311942c6b32f7535c0c3b138defa895e857142712bf5861bbcd6a6ddd3e3c2ad0ce9117732ac8a42bdc060508c7f00772b5271c98
%global source20_hash 309b19d6bff9d3e009610d698a73ba191da70cabd57157f274dfca7583a9e9b31fc30ea52b2b2ab3386be7290a680f8eb47dc92381c3da8251b01d8c6a65c3ff
%global source21_hash d74e78a1c863d3865ec4b21a4c762bf6e2c30a8656fe0ec830d1e56b9fcb48861f316ccf8d8641e7c674e25f1ac2292d10ff2127315275347096ad325828d7e5
%global source22_hash e495c127884aecc1856b99705c262882b390f9e800dca59c2fa1200ae584a424ef4ce7752a9bb5dd7aad9a94c4a685af557163f2b07327e80f5b99153532d915
%global source23_hash 31a91fa609f3ef8631d6ed57526e932d5c110e4d84cc78862d1bf4c682f8de97c080a1e2d82e60842b731e33505b99dd2a85ae899705ebc45de44e526358703b
%global source24_hash 12e607680e1708760d7c370f5180ab447cb0e922af5100ed61ba44a2ee5e03169acae560502812248eeba65625addc553bdf744be1f8349899ef4569ceca93ba
%global source25_hash d50cd83eaca1905f6b43631cb999b9f6d7b723fa73886854b9a1cade3dbf48628493c86d4afc6550e1d835c8d2e442584c0b191c4a6fc6cea323d0c1c96c64b0
%global source26_hash db933b365a2235fae36a19059c9c78a9d34252302298d8367ea52e9c99aa362ea774c230ffa9f5664e85331a8107c44baa7936e197e0e5677773521850d8da42
%global source27_hash e75363bb36568ec42f13217dc740b839e109529e41ac9cc713e8c7eb620e557dcc08d20f36cbdb5f0e3145d9201d659fc8478d40fae4862fefd3eec005a3463b
%global source28_hash ea0918afe1c785d864bc280a6b64a87cc62cabb02540cdf64a7cbf4b8f81afcef9ac85a6f28b5bdbb42a75b6ce1e12139c12d0e1af4183a28115f8d740c6e78e
%global source29_hash ad8a302bcf87edfad5c657aae9755ab1ce71126450ec38811e9376640343509417b97419c71a1e4c3eb27f5a6434108a2128ccf5168cd2ee65fcc7783ff72782
%global source30_hash 192b242cbffd70dd637d4b128d646c3509cf174b4ce5735318374c76318ac24de6d71a63002bce7a01f10f480366f721e17a5fadd6fea16d78623ce2d2170360
%global source31_hash 5e5b3bb01456fec3dc22cb5d0d4f521b4d4f5f8f3119fdd76ea9cc55a70a2ad8a2b72e36471894ee448c1d40d887d20ac8fda39c4a3fe2cd111d2850eec12071
%global source32_hash 477df31445a2991db3c2b8cafaa97662d722f3f7171c2f756cf025717cb3b896c1773adadbc42c22cb360f7542a0e658547f15cd71c54e9b79f76fb1e2097e90
%global source33_hash b5681877031871595ce106993668b0e2a5346740eb15a4062bcf019aaabbc034275b1aabcb2a078a887e1d048fa18c1d7d5d5b0624ce63ef48884bf287dc8e01
%global source34_hash 5c425b3c76ea373d97693b81bbe4a6da423772271530e23ca1cc2160b463177f5a8e109e7010b5004b2dc627c2a5080b47d4c6506ea06c29ece97aa8d16c7ddd
%global source35_hash bdd395fe3ee9e24cb8abd40758454f1631f1036c34f9fe55feaf0b5fc6cdecace161843f9841b3fc07953537c1bd7e562c926b5c1ee1e63c0e26dbc3178497c1
%global source36_hash 8948bdfd0f33801e58ed83384388e5bdcfcb585f7ceb1e0738a169e0406fe1436ece645e940ceb6f8021d76fd0cb72f5b0a6419c8de0c1af3a745bccc9b83fa1
%global source37_hash a399e026e7f2436e80213dce2b30ae5f39ec2501a40e4485b36f45344f05b0726b2622bbe690532faa57e8185e176da1598ec4ffcf3c409410635e301c7dd743
%global source38_hash d5e415438d7c8a0d1a6d395f0c191ede468a4c86d6426c533af4f909fe6c479ed22483ed910d1d2cdac2e3a190fd7c1ed87eaa0cbe43784cae9fac7b1709bd4a
%global source39_hash e9f90cb21730e34fe03961281527cfdea0f7c15e349b9d441747be7ba591c40ac876ebed92f884bd502c3cf7a99f2f6f6328bce515680100c2f9a3d7e04a4aa4
%global source40_hash 3d159eb9fd84aa8bc6c183ae6a42aefc331b9bd606abbc1b2c3c53776d5b8f1554a4ad304d0555b8d2c95be2e8000eab0a3ec6a167e089292099bac6751782d2
%global source41_hash a62efcf4630d7c26bbedb19e0c4405e730733b71361cbec9abed7a06a377c230bee561d8b48427104bef8dbd4e0bd56b0eaf9f0f7bbcdc8b289c726cd7b6cef7
%global source42_hash 61f32efbea3b94749fa0cfc3ef2a3b3a34ccfb4ed3b6b09afa74e4f6dbd2540c1a263c81ca6406288f015303250f51acab0b6a4a4d51c95a2f9bbf1f3360f8e9
%global source43_hash 5cd220d0d25f11dcbd50b0762a3f5e6f0c7e5f9455190e5fbf5e302522c978076f75b726d27530c3510cd996c4bf495bc9ec0ee1790c1bdcfd766ac5ba9741d1
%global source44_hash a357286792f5135cdf7428470518d3d33132b6e2ef229c953fba9ced864cbaa8b11cb21e8fb4a9e18fdb921e72cd7e99f367de2b5703d93f9d58d211f868a84c
%global source45_hash f98b6f35b6bb1f9195a6aeae1925a5b3d1911bd71a12fd96fef431c55014a0f307b0637f182bfff59c02ee02dcbcff8e9af0e308aa141c2379ab2f1ca5780397
%global source46_hash f7b2efaed1c7bbc0acff6248fed22e64525ecd41afafa003cc3fbd82a4e4ea9fddba8c41457173a5b10dc9bd64818ef4d8ac236d23b50583e55ed48cf46b3193
%global source47_hash 6d60454cdbd0bbff3f4e1d0cba6a8e5edfb131980628443b64dce735d5878008cca253dae16a93f02fc7bf46467ac4efe36f1aee57778cb2fb5c96b8ac9c2f33
%global source48_hash 1a1eb5e17d8220caf577e29a4963e455e03711046cd54281f486a931de42bcf564fb7adf27db6d3453d3e3c7bbac1a450462c2494b9eab31b233472d00f477b5
%global source49_hash d2d28dcf5986107c89d769bed0e4af190d7b1883622680f4f580507df4ec2cdc7f408525c94d861352dfd94e1e00642e0b166e4e152c376865b606ea29f832ea
%global source50_hash 064b0453263d05ce4d9296f09f627fa0820c59efccad9798ef60f9f5a8b7edfa81ef1f9a239d2ca750caa89e37d28c2a06574b9fff2351d5a66a45410d84507c
%global source51_hash e45c6b793101811d3ce1bea48457e8e16120b5fdbb55da2a3fe45680f517f7ef2452ed1b350b860c15cc80daf9d8608a72d0e334c5c76c10e0fdb1a1b569058c
%global source52_hash cb616689004c3056c6dc4c0e46caee7151da0d8242a09315fa4488f18ed5af2da97a5df97b0933bc6c1518581435681f116d2b36f32af7802d454e32af66853a
%global source53_hash 19265b32271b8603d8baf8b16f043c3228606230c1151a33e243e493b6306faa839860f2b07ec9d5d43c57f49e984134e760342bc6302186924e5c95cc1f3380
%global source54_hash 70c04643ced459099ae095c88c0316e96c75e99bba0877198c7800d3b5cc9ac872f74b36adfb03dde968150abb3cb99131fb52ecaff56dfbf1aa85379718a74f
%global source55_hash a89c2f99ad63c8352462ef7139b36e8563e1db815dcb06bd2e0f8b96554c380b574f7d856aa6bffb3c972bd68e9505d7864d87cfb7bcfef1bdebacd10f14a96a
%global source56_hash 2b5a7672c600eb2f4cbfb2810090e4383a7032d851f35a74e36c75914d9813566603019f232715e2e39ab6d2f8a60273c01e5cbdcb345892b0bf8c99995e3d4d
%global source57_hash 03dcf2b73ca644f8e9e2589082d49a4d502adb51944fcd9ee5cf737ae782611b35ef2eda4242b7eec2b8033014ddbbbea3abb52b1bfe90be9cc1634345223d53
%global source58_hash d4c038d864b40603281f3186e21110ec96530e84a9ff88be4241cad165d09cd091b28bd768ca8ca0a28575dd850bb68ff88ab553cf9caaee6edd8d311c6fc9e2
%global source59_hash 424b7ba89128c2bf927ca52eb55fdb22d2b6a2cec71e537100958b81062de767e3a493c2b4cde875c72158ef0268934409555cb185df6807530e32b053a85bc0
%global source60_hash 84517026d64b2b756dd5c4507f053aeee2238036764bb7e46c044e5864fbe558f9e8831bac19efea3fbc8868636a499c8f9e7b3dd20a36fbbcddb47a90c01469
%global source61_hash 5d9081b8d197952aa5ff58b1cbd490bb529cbbc1b72956cca8dd28b1b6bc12c6248d3d04fd457349b30df7594aa1872ce9c8438feb67af1b93ff0fd33eefcb7d
%global source62_hash 96e94598e3e397a9657a83496d940aa2525fdbe1ec2cf820b05e5493b1f3e1c45568e16b62c22d4ee25afe2bd0657848a433477e82cc8038895c2195139ca065
%global source63_hash aced84aaaf593343c94048b8a7b5517564ece781c5e7227dee3d3bfa358283408474f30e269da4f0655b9b847a09d1a5456a73d918be07cee67f600368752fa0
%global source64_hash 0feb9bcc8eb3ec377a478c6b24421e3fa94d3973f182d85cf1da941007d0c68ec0df74b5000508d856e54961d4d0a5e24c1df607f1d4e299a0dc24f63d82f55b
%global source65_hash 46d807f79b86b778e4b3c98aa54822cee8aadb862d5db89942bc051975f6a16bbb360eb05274aa71905466f323e5bfd786c1676deb01c8d48b3f7e682167ce35
%global source66_hash 86c08e3685ec339e81f95a4b399c8fa1cfc9cf1f14eb685b58f99b56e17c50cf3e0de1a97989d77830bbbbc134840cc9423218b981f681d0f0466e50bdfd4448
%global source67_hash 351dea4f4a8d09945d5bfac4abf605b06697a6666463bf968068dfc3b034c0cbd137a2856847ef692351162da88f3d9da07eae4b6d25c1930ebaed16c0c8a728
%global source68_hash 01a12dd1aa191d53d34cc03ba24ca6513a454f3720675c2b41b551e72476fc25fbe8b7f55da92b2552d96af80516cde5d535b92667db03f77ada2eaca338de33
%global source69_hash 1e068a0b402a5c69b44a86d797cb24266b2883c698decd8b8464c99b131d292cc5ac44249ba8e89dc0a414d6f12d73d4c069ffc3081cfa4b9926ca412bfc3dd6
%global source70_hash f9ac2953877cd830e1cf3402f3f2bac1f8159d05a4a74e89047c494ae04dc8930f1c09701f83871b4361976572ae7d1c5fbdaf3af3d9e6db12347a207f1b82cb
%global source71_hash 68fff717d021971424e40595db094183a80a5698a084e6cfee9e5132cec17fed6b1b7b42a111fa3325bde59f8357f4112435eae11e9ccc1d07d6475b1fd2e638
%global source72_hash 49031f2c2b863d6275a35f23936486b10f5a692f06289fef5353d75868c99e36b1523d3a1cb66aa5e7753332701382f102847df557d4404c9abf85634b148147
%global source73_hash b1e06d9f22eb5cf3d7c2723d0310c8ed45a98a7d5fd71fa7449650dc6f53c20f24120ca4b5a592be6fcad9c377c911867f88284df94434c1497dadd23c742758
%global source74_hash e2c0105e7897b8bb202a829c5df67c49dc78f9124cef7d5c64cc8c193db54e9a4d3cf94f71d98e4da5bccc4cfb868ced6a00d8e0b6a0ae79f11188b18caf2844

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langchinese.tar.xz#/collection-langchinese.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arphic.tar.xz#/arphic.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arphic.doc.tar.xz#/arphic.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arphic-ttf.tar.xz#/arphic-ttf.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arphic-ttf.doc.tar.xz#/arphic-ttf.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-by-example-zh-cn.tar.xz#/asymptote-by-example-zh-cn.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-by-example-zh-cn.doc.tar.xz#/asymptote-by-example-zh-cn.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-faq-zh-cn.tar.xz#/asymptote-faq-zh-cn.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-faq-zh-cn.doc.tar.xz#/asymptote-faq-zh-cn.doc.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-manual-zh-cn.tar.xz#/asymptote-manual-zh-cn.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-manual-zh-cn.doc.tar.xz#/asymptote-manual-zh-cn.doc.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cns.tar.xz#/cns.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cns.doc.tar.xz#/cns.doc.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex.tar.xz#/ctex.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex.doc.tar.xz#/ctex.doc.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex-faq.tar.xz#/ctex-faq.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex-faq.doc.tar.xz#/ctex-faq.doc.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exam-zh.tar.xz#/exam-zh.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exam-zh.doc.tar.xz#/exam-zh.doc.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fandol.tar.xz#/fandol.or11.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fandol.doc.tar.xz#/fandol.doc.or11.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fduthesis.tar.xz#/fduthesis.or11.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fduthesis.doc.tar.xz#/fduthesis.doc.or11.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hanzibox.tar.xz#/hanzibox.or11.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hanzibox.doc.tar.xz#/hanzibox.doc.or11.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-chinese.tar.xz#/hyphen-chinese.or11.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impatient-cn.tar.xz#/impatient-cn.or11.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impatient-cn.doc.tar.xz#/impatient-cn.doc.or11.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/install-latex-guide-zh-cn.tar.xz#/install-latex-guide-zh-cn.or11.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/install-latex-guide-zh-cn.doc.tar.xz#/install-latex-guide-zh-cn.doc.or11.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-notes-zh-cn.tar.xz#/latex-notes-zh-cn.or11.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-notes-zh-cn.doc.tar.xz#/latex-notes-zh-cn.doc.or11.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-chinese.tar.xz#/lshort-chinese.or11.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-chinese.doc.tar.xz#/lshort-chinese.doc.or11.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex-cn.tar.xz#/luatex-cn.or11.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex-cn.doc.tar.xz#/luatex-cn.doc.or11.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lxgw-fonts.tar.xz#/lxgw-fonts.or11.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lxgw-fonts.doc.tar.xz#/lxgw-fonts.doc.or11.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nanicolle.tar.xz#/nanicolle.or11.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nanicolle.doc.tar.xz#/nanicolle.doc.or11.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njurepo.tar.xz#/njurepo.or11.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njurepo.doc.tar.xz#/njurepo.doc.or11.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfornament-han.tar.xz#/pgfornament-han.or11.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfornament-han.doc.tar.xz#/pgfornament-han.doc.or11.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qyxf-book.tar.xz#/qyxf-book.or11.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qyxf-book.doc.tar.xz#/qyxf-book.doc.or11.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sjtutex.tar.xz#/sjtutex.or11.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sjtutex.doc.tar.xz#/sjtutex.doc.or11.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suanpan-l3.tar.xz#/suanpan-l3.or11.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suanpan-l3.doc.tar.xz#/suanpan-l3.doc.or11.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-zh-cn.tar.xz#/texlive-zh-cn.or11.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-zh-cn.doc.tar.xz#/texlive-zh-cn.doc.or11.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texproposal.tar.xz#/texproposal.or11.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texproposal.doc.tar.xz#/texproposal.doc.or11.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlmgr-intro-zh-cn.tar.xz#/tlmgr-intro-zh-cn.or11.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlmgr-intro-zh-cn.doc.tar.xz#/tlmgr-intro-zh-cn.doc.or11.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/upzhkinsoku.tar.xz#/upzhkinsoku.or11.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/upzhkinsoku.doc.tar.xz#/upzhkinsoku.doc.or11.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpinyin.tar.xz#/xpinyin.or11.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpinyin.doc.tar.xz#/xpinyin.doc.or11.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xtuthesis.tar.xz#/xtuthesis.or11.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xtuthesis.doc.tar.xz#/xtuthesis.doc.or11.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhlineskip.tar.xz#/zhlineskip.or11.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhlineskip.doc.tar.xz#/zhlineskip.doc.or11.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhlipsum.tar.xz#/zhlipsum.or11.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhlipsum.doc.tar.xz#/zhlipsum.doc.or11.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics.tar.xz#/zhmetrics.or11.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics.doc.tar.xz#/zhmetrics.doc.or11.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics-uptex.tar.xz#/zhmetrics-uptex.or11.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics-uptex.doc.tar.xz#/zhmetrics-uptex.doc.or11.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhnumber.tar.xz#/zhnumber.or11.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhnumber.doc.tar.xz#/zhnumber.doc.or11.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhspacing.tar.xz#/zhspacing.or11.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhspacing.doc.tar.xz#/zhspacing.doc.or11.tar.xz

# AppStream metadata for font components
Source75:        fandol.metainfo.xml

# Patches
Patch0:         texlive-xtuthesis-use-diagbox.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-arphic
Requires:       texlive-arphic-ttf
Requires:       texlive-asymptote-by-example-zh-cn
Requires:       texlive-asymptote-faq-zh-cn
Requires:       texlive-asymptote-manual-zh-cn
Requires:       texlive-cns
Requires:       texlive-collection-langcjk
Requires:       texlive-ctex
Requires:       texlive-ctex-faq
Requires:       texlive-exam-zh
Requires:       texlive-fandol
Requires:       texlive-fduthesis
Requires:       texlive-hanzibox
Requires:       texlive-hyphen-chinese
Requires:       texlive-impatient-cn
Requires:       texlive-install-latex-guide-zh-cn
Requires:       texlive-latex-notes-zh-cn
Requires:       texlive-lshort-chinese
Requires:       texlive-luatex-cn
Requires:       texlive-lxgw-fonts
Requires:       texlive-nanicolle
Requires:       texlive-njurepo
Requires:       texlive-pgfornament-han
Requires:       texlive-qyxf-book
Requires:       texlive-sjtutex
Requires:       texlive-suanpan-l3
Requires:       texlive-texlive-zh-cn
Requires:       texlive-texproposal
Requires:       texlive-tlmgr-intro-zh-cn
Requires:       texlive-upzhkinsoku
Requires:       texlive-xpinyin
Requires:       texlive-xtuthesis
Requires:       texlive-zhlineskip
Requires:       texlive-zhlipsum
Requires:       texlive-zhmetrics
Requires:       texlive-zhmetrics-uptex
Requires:       texlive-zhnumber
Requires:       texlive-zhspacing

%description
Support for Chinese; additional packages in collection-langcjk.

%package -n texlive-arphic
Summary:        Arphic (Chinese) font packages
Version:        svn15878
License:        Arphic-1999
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-arphic
These are font bundles for the Chinese Arphic fonts which work with the CJK
package. TrueType versions of these fonts for use with XeLaTeX and LuaLaTeX are
provided by the arphic-ttf package. Arphic is actually the name of the company
which created these fonts (and put them under a GPL-like licence).

%package -n texlive-arphic-ttf
Summary:        TrueType version of Chinese Arphic fonts
Version:        svn42675
License:        Arphic-1999
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-arphic-ttf
This package provides TrueType versions of the Chinese Arphic fonts for use
with XeLaTeX and LuaLaTeX. Type1 versions of these fonts, for use with pdfLaTeX
and the cjk package, are provided by the arphic package. Arphic is actually the
name of the company which created these fonts.

%package -n texlive-asymptote-by-example-zh-cn
Summary:        Asymptote by example
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-asymptote-by-example-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-asymptote-by-example-zh-cn-doc <= 11:%{version}

%description -n texlive-asymptote-by-example-zh-cn
This is a tutorial written in Simplified Chinese.

%package -n texlive-asymptote-faq-zh-cn
Summary:        Asymptote FAQ (Chinese translation)
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-asymptote-faq-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-asymptote-faq-zh-cn-doc <= 11:%{version}

%description -n texlive-asymptote-faq-zh-cn
This is a Chinese translation of the Asymptote FAQ

%package -n texlive-asymptote-manual-zh-cn
Summary:        A Chinese translation of the asymptote manual
Version:        svn15878
License:        LGPL-2.1-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-asymptote-manual-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-asymptote-manual-zh-cn-doc <= 11:%{version}

%description -n texlive-asymptote-manual-zh-cn
This is an (incomplete, simplified) Chinese translation of the Asymptote
manual.

%package -n texlive-cns
Summary:        Chinese/Japanese/Korean bitmap fonts
Version:        svn45677
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cns
Fonts to go with the cjk macro package for Chinese, Japanese and Korean with
LaTeX2e. The package aims to supersede HLaTeX fonts bundle.

%package -n texlive-ctex
Summary:        LaTeX classes and packages for Chinese typesetting
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-adobemapping
Requires:       texlive-atbegshi
Requires:       texlive-beamer
Requires:       texlive-cjk
Requires:       texlive-cjkpunct
Requires:       texlive-ec
Requires:       texlive-epstopdf-pkg
Requires:       texlive-etoolbox
Requires:       texlive-everyhook
Requires:       texlive-fandol
Requires:       texlive-fontspec
Requires:       texlive-iftex
Requires:       texlive-infwarerr
Requires:       texlive-kvoptions
Requires:       texlive-kvsetkeys
Requires:       texlive-latex-bin
Requires:       texlive-ltxcmds
Requires:       texlive-luatexja
Requires:       texlive-mptopdf
Requires:       texlive-pdftexcmds
Requires:       texlive-platex-tools
Requires:       texlive-svn-prov
Requires:       texlive-tipa
Requires:       texlive-tools
Requires:       texlive-ttfutils
Requires:       texlive-ulem
Requires:       texlive-uplatex
Requires:       texlive-xcjk2uni
Requires:       texlive-xecjk
Requires:       texlive-xetex
Requires:       texlive-xkeyval
Requires:       texlive-xpinyin
Requires:       texlive-xunicode
Requires:       texlive-zhmetrics
Requires:       texlive-zhmetrics-uptex
Requires:       texlive-zhnumber
Provides:       tex(ctex-engine-aptex.def) = %{tl_version}
Provides:       tex(ctex-engine-luatex.def) = %{tl_version}
Provides:       tex(ctex-engine-pdftex.def) = %{tl_version}
Provides:       tex(ctex-engine-uptex.def) = %{tl_version}
Provides:       tex(ctex-engine-xetex.def) = %{tl_version}
Provides:       tex(ctex-fontset-adobe.def) = %{tl_version}
Provides:       tex(ctex-fontset-fandol.def) = %{tl_version}
Provides:       tex(ctex-fontset-founder.def) = %{tl_version}
Provides:       tex(ctex-fontset-mac.def) = %{tl_version}
Provides:       tex(ctex-fontset-macnew.def) = %{tl_version}
Provides:       tex(ctex-fontset-macold.def) = %{tl_version}
Provides:       tex(ctex-fontset-ubuntu.def) = %{tl_version}
Provides:       tex(ctex-fontset-windows.def) = %{tl_version}
Provides:       tex(ctex-heading-article.def) = %{tl_version}
Provides:       tex(ctex-heading-beamer.def) = %{tl_version}
Provides:       tex(ctex-heading-book.def) = %{tl_version}
Provides:       tex(ctex-heading-report.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-article.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-beamer.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-book.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-report.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-article.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-beamer.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-book.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-report.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain.def) = %{tl_version}
Provides:       tex(ctex-spa-macro.tex) = %{tl_version}
Provides:       tex(ctex-spa-make.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-adobe.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-fandol.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-founder.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-mac.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-ubuntu.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-windows.tex) = %{tl_version}
Provides:       tex(ctex.sty) = %{tl_version}
Provides:       tex(ctexart.cls) = %{tl_version}
Provides:       tex(ctexbeamer.cls) = %{tl_version}
Provides:       tex(ctexbook.cls) = %{tl_version}
Provides:       tex(ctexcap.sty) = %{tl_version}
Provides:       tex(ctexheading.sty) = %{tl_version}
Provides:       tex(ctexhook.sty) = %{tl_version}
Provides:       tex(ctexpatch.sty) = %{tl_version}
Provides:       tex(ctexrep.cls) = %{tl_version}
Provides:       tex(ctexsize.sty) = %{tl_version}
Provides:       tex(ctexspa.def) = %{tl_version}
Provides:       tex(ctxdoc.cls) = %{tl_version}
Provides:       tex(ctxdocstrip.tex) = %{tl_version}

%description -n texlive-ctex
ctex is a collection of macro packages and document classes for LaTeX Chinese
typesetting.

%package -n texlive-ctex-faq
Summary:        LaTeX FAQ by the Chinese TeX Society (ctex.org)
Version:        svn15878
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ctex-faq-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ctex-faq-doc <= 11:%{version}

%description -n texlive-ctex-faq
Most questions were collected on the bbs.ctex.org forum, and were answered in
detail by the author.

%package -n texlive-exam-zh
Summary:        LaTeX template for Chinese exams
Version:        svn76834
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(exam-zh-chinese-english.sty) = %{tl_version}
Provides:       tex(exam-zh-choices.sty) = %{tl_version}
Provides:       tex(exam-zh-font.sty) = %{tl_version}
Provides:       tex(exam-zh-math.sty) = %{tl_version}
Provides:       tex(exam-zh-question.sty) = %{tl_version}
Provides:       tex(exam-zh-symbols.sty) = %{tl_version}
Provides:       tex(exam-zh-textfigure.sty) = %{tl_version}
Provides:       tex(exam-zh.cls) = %{tl_version}

%description -n texlive-exam-zh
Although there are already several excellent exam packages or classes like exam
and bhcexam, these do not fit the Chinese style very well, or they cannot be
customized easily for Chinese exams of all types, like exams in primary school,
junior high school, senior high school and even college. This is the main
reason why this package was created. This package provides a class exam-zh.cls
and several module packages like exam-zh-question.sty and exam-zh-choices.sty,
where these module packages can be used individually. Using exam-zh you can
separate the format and the content very well; use the choices environment to
typeset choice items easily and automatically; design the seal line easily; and
more (see manual).

%package -n texlive-fandol
Summary:        Four basic fonts for Chinese typesetting
Version:        svn37889
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fandol
Fandol fonts designed for Chinese typesetting. The current version contains
four styles: Song, Hei, Kai, Fang. All fonts are in OpenType format.

%package -n texlive-fduthesis
Summary:        LaTeX thesis template for Fudan University
Version:        svn67231
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fdudoc.cls) = %{tl_version}
Provides:       tex(fdulogo.sty) = %{tl_version}
Provides:       tex(fduthesis-en.cls) = %{tl_version}
Provides:       tex(fduthesis.cls) = %{tl_version}
Provides:       tex(fduthesis.def) = %{tl_version}

%description -n texlive-fduthesis
This package is a LaTeX thesis template package for Fudan University. It can
make it easy to write theses both in Chinese and English.

%package -n texlive-hanzibox
Summary:        Boxed Chinese characters with Pinyin above and translation below
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hanzibox.sty) = %{tl_version}

%description -n texlive-hanzibox
This is a LaTeX package written to simplify the input of Chinese with Hanyu
Pinyin and translation. Hanyu Pinyin is placed above Chinese with the xpinyin
package, and the translation is placed below. The package can be used as a
utility for learning to write and pronounce Chinese characters, for Chinese
character learning plans, presentations, exercise booklets and other
documentation work.

%package -n texlive-hyphen-chinese
Summary:        Chinese pinyin hyphenation patterns.
Version:        svn74115
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-zh-latn-pinyin.ec.tex) = %{tl_version}
Provides:       tex(hyph-zh-latn-pinyin.tex) = %{tl_version}
Provides:       tex(loadhyph-zh-latn-pinyin.tex) = %{tl_version}

%description -n texlive-hyphen-chinese
Hyphenation patterns for unaccented transliterated Mandarin Chinese (pinyin) in
T1/EC and UTF-8 encodings. The latter can hyphenate pinyin with or without tone
markers; the former only without.

%package -n texlive-impatient-cn
Summary:        Free edition of the book "TeX for the Impatient"
Version:        svn54080
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-impatient-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-impatient-cn-doc <= 11:%{version}

%description -n texlive-impatient-cn
"TeX for the Impatient" is a book (of around 350 pages) on TeX, Plain TeX and
Eplain. The book is also available in French and Chinese translations.

%package -n texlive-install-latex-guide-zh-cn
Summary:        A short introduction to LaTeX installation written in Chinese
Version:        svn77681
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-install-latex-guide-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-install-latex-guide-zh-cn-doc <= 11:%{version}

%description -n texlive-install-latex-guide-zh-cn
This package will introduce the operations related to installing TeX Live
(introducing MacTeX in macOS), upgrading packages, and compiling simple
documents on Windows 11, Ubuntu 24.04, and macOS systems, and mainly
introducing command line operations.

%package -n texlive-latex-notes-zh-cn
Summary:        Chinese Introduction to TeX and LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-notes-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-notes-zh-cn-doc <= 11:%{version}

%description -n texlive-latex-notes-zh-cn
The document is an introduction to TeX/LaTeX, in Chinese. It covers basic text
typesetting, mathematics, graphics, tables, Chinese language & fonts, and some
miscellaneous features (hyperlinks, long documents, bibliographies, indexes and
page layout).

%package -n texlive-lshort-chinese
Summary:        Introduction to LaTeX, in Chinese
Version:        svn73160
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-chinese-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-chinese-doc <= 11:%{version}

%description -n texlive-lshort-chinese
A Chinese edition of the not so short introduction to LaTeX2e, with additional
information of typesetting Chinese language.

%package -n texlive-luatex-cn
Summary:        A LuaTeX based package to handle Chinese text typesetting
Version:        svn77432
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(enumitem.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(ltc-book.cls) = %{tl_version}
Provides:       tex(ltc-guji.cls) = %{tl_version}
Provides:       tex(luatex-cn-banxin.sty) = %{tl_version}
Provides:       tex(luatex-cn-font-autodetect.sty) = %{tl_version}
Provides:       tex(luatex-cn-splitpage.sty) = %{tl_version}
Provides:       tex(luatex-cn-vertical.sty) = %{tl_version}
Provides:       tex(luatex-cn.sty) = %{tl_version}

%description -n texlive-luatex-cn
A LuaTeX package for Chinese character typesetting, covering
horizontal/vertical, traditional/modern layout. Currently focus on Ancient Book
replication. Implemented core logic of vertical typesetting, decorative
elements of traditional Chinese books, and interlinear notes.

%package -n texlive-lxgw-fonts
Summary:        A CJK font family with a comprehensive character set
Version:        svn77677
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ctex-fontset-lxgw.def) = %{tl_version}
Provides:       tex(ctex-makespa-lxgw.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-lxgw.tex) = %{tl_version}

%description -n texlive-lxgw-fonts
The LXGW Font Family provides an open-source CJK font family with a
comprehensive character set for Chinese (Simplified/Traditional), Cantonese,
and Japanese. A 'fontset' configuration of this font family for the 'ctex-kit'
is also provided in this package.

%package -n texlive-nanicolle
Summary:        Typesetting herbarium specimen labels
Version:        svn56224
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(nanicolle.cls) = %{tl_version}

%description -n texlive-nanicolle
This package provides a LaTeX class nanicolle.cls for typesetting collection
labels and identification labels in Chinese style or in western style for plant
herbarium specimens. So far, documents using this class can only be compiled
with XeLaTeX. Note: The name of the package is a compound of the Japanese
"nani" (meaning "what") and a truncated form of the English "collect", thus
expressing the ideas of identification/classification (taxonomy) and
collection.

%package -n texlive-njurepo
Summary:        Reports for Nanjing University
Version:        svn50492
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(njurepo.cls) = %{tl_version}

%description -n texlive-njurepo
This LaTeX document class provides a thesis template for Nanjing University in
order to make it easy to write experiment reports and homework for the
bachelor's curriculum. NJUrepo stands for Nanjing University versatile Report.

%package -n texlive-pgfornament-han
Summary:        Pgfornament library for Chinese traditional motifs and patterns
Version:        svn72640
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(needspace.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(relsize.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(beamerthemeHeavenlyClouds.sty) = %{tl_version}
Provides:       tex(beamerthemeTianQing.sty) = %{tl_version}
Provides:       tex(beamerthemeXiaoshan.sty) = %{tl_version}
Provides:       tex(cncolours.sty) = %{tl_version}
Provides:       tex(pgflibraryhan.code.tex) = %{tl_version}
Provides:       tex(pgfornament-han.sty) = %{tl_version}

%description -n texlive-pgfornament-han
This package provides a pgfornament library for Chinese traditional motifs and
patterns. The command \pgfornamenthan takes the same options as \pgfornament
from the pgfornament package, but renders Chinese traditional motifs instead.
The list of supported motifs, as well as some examples, can be found in the
accompanying documentation. This bundle also provides three beamer themes
incorporating these motifs; sample .tex files for creating beamer presentations
and posters are included. Yi pgfornament Hong Bao De Ji Zhi ,Shi Xian Hui Zhi
Yi Feng Tu Wen . \pgfornamenthan He \pgfornament De Can Shu Shi Yi Yang De ;
Bian Yi De Chu Lai De Dang Ran Shi Yi Feng Wen Yang Liao . Hong Bao Shou Ce Li
You Wan Zheng De Wen Yang Lie Biao Yi Ji Shi Yong Fan Li . Wo Men Ye Ji Yu Zhe
Xie Wen Yang ,Kai Fa Liao San Kuan beamerZhu Ti , Bing Fu Shang Zhi Zuo
beamerHuan Deng Pian He Hai Bao De Shi Fan .texWen Dang .

%package -n texlive-qyxf-book
Summary:        Book Template for Qian Yuan Xue Fu
Version:        svn75712
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(qyxf-book.cls) = %{tl_version}

%description -n texlive-qyxf-book
qyxf-book is a LaTeX document class (template) developed by Qian Yuan Xue Fu
(QYXF), a student club of Xi'an Jiaotong University (XJTU). Up to now, this
template has been applied to academic counselling material ("course helpers")
written by members of QYXF, including Solutions to University Physics Notes on
Computing Methods Features of the template: Minimalistic document style, as
preferred for "course helpers". Several color schemes are offered, and it is
easy to customize your own scheme. Simple interfaces for users to customize the
style of preface, main part and so on. Currently the template is only designed
for Chinese typesetting.

%package -n texlive-sjtutex
Summary:        LaTeX classes for Shanghai Jiao Tong University
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sjtu-cjk-font-adobe.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-fandol.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-founder.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-hanyi.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-mac.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-ubuntu.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-windows.def) = %{tl_version}
Provides:       tex(sjtu-lang-de.def) = %{tl_version}
Provides:       tex(sjtu-lang-en.def) = %{tl_version}
Provides:       tex(sjtu-lang-ja.def) = %{tl_version}
Provides:       tex(sjtu-lang-zh.def) = %{tl_version}
Provides:       tex(sjtu-math-font-cambria.def) = %{tl_version}
Provides:       tex(sjtu-math-font-libertinus.def) = %{tl_version}
Provides:       tex(sjtu-math-font-lm.def) = %{tl_version}
Provides:       tex(sjtu-math-font-newcm.def) = %{tl_version}
Provides:       tex(sjtu-math-font-newpx.def) = %{tl_version}
Provides:       tex(sjtu-math-font-newtx.def) = %{tl_version}
Provides:       tex(sjtu-math-font-stixtwo.def) = %{tl_version}
Provides:       tex(sjtu-math-font-times.def) = %{tl_version}
Provides:       tex(sjtu-math-font-xits.def) = %{tl_version}
Provides:       tex(sjtu-scheme-de.def) = %{tl_version}
Provides:       tex(sjtu-scheme-en.def) = %{tl_version}
Provides:       tex(sjtu-scheme-ja.def) = %{tl_version}
Provides:       tex(sjtu-scheme-zh.def) = %{tl_version}
Provides:       tex(sjtu-text-font-cambria.def) = %{tl_version}
Provides:       tex(sjtu-text-font-libertinus.def) = %{tl_version}
Provides:       tex(sjtu-text-font-lm.def) = %{tl_version}
Provides:       tex(sjtu-text-font-newcm.def) = %{tl_version}
Provides:       tex(sjtu-text-font-newpx.def) = %{tl_version}
Provides:       tex(sjtu-text-font-newtx.def) = %{tl_version}
Provides:       tex(sjtu-text-font-stixtwo.def) = %{tl_version}
Provides:       tex(sjtu-text-font-times.def) = %{tl_version}
Provides:       tex(sjtu-text-font-xits.def) = %{tl_version}
Provides:       tex(sjtu-thesis-de.def) = %{tl_version}
Provides:       tex(sjtu-thesis-en.def) = %{tl_version}
Provides:       tex(sjtu-thesis-ja.def) = %{tl_version}
Provides:       tex(sjtu-thesis-zh.def) = %{tl_version}
Provides:       tex(sjtuarticle.cls) = %{tl_version}
Provides:       tex(sjtureport.cls) = %{tl_version}
Provides:       tex(sjtuthesis.cls) = %{tl_version}

%description -n texlive-sjtutex
SJTUTeX aims to establish a simple and easy-to-use collection of document
classes for Shanghai Jiao Tong University, including the thesis document class
sjtuthesis, as well as the regular document classes sjtuarticle and sjtureport.

%package -n texlive-suanpan-l3
Summary:        Traditional Chinese 7-bids suanpan (abacus) package based on l3draw
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(suanpan-l3.sty) = %{tl_version}

%description -n texlive-suanpan-l3
This traditional Chinese 7-bids abacus drawing package utilizes l3draw and is
developed with expl3. It can effectively manage both upper and lower bids,
while also considering bottom bid, top bid, and hanging bid. The package offers
a unique environment for drawing abacuses, denoted as suanpan. Within this
environment, 7 specialized macros are available for the creation of abacuses.
The \rod macro is used to lay out a single rod, while the \rod* macro draws a
counting point on this rod's beam. The \rods macro is capable of laying out a
set of rods. The \bid macro colors the specified bid. The \bids macro colors
all inner bids that are near the beam, while the \bids* macro colors all outer
bids that are far from the beam. Lastly, the \lrframe macro is used to lay out
the left and right frames of an abacus. At the same time, the package offers
customization options for abacus, including line width, draw color, fill color,
bid space, rod space, etc. These can be configured through package options,
suanpan environment options, or the \suanpanset macro.

%package -n texlive-texlive-zh-cn
Summary:        TeX Live manual (Chinese)
Version:        svn74098
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-zh-cn-doc <= 11:%{version}

%description -n texlive-texlive-zh-cn
TeX Live manual (Chinese)

%package -n texlive-texproposal
Summary:        A proposal prototype for LaTeX promotion in Chinese universities
Version:        svn43151
License:        CC-BY-4.0 AND MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texproposal-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texproposal-doc <= 11:%{version}

%description -n texlive-texproposal
This package contains the original source code and necessary attachment of the
document "Proposal for Offering TeX Courses and Relevant Resources in Chongqing
University". This proposal could be helpful if one is considering to suggest
his/her university or company to use TeX (or LaTeX, or XeLaTeX) as a
typesetting system, especially for Chinese universities and companies. The
present proposal mainly explains the importance and necessity of introducing
TeX, a typesetting system often used in academic writing, to students and
teachers. This proposal starts from a brief introduction of TeX, then steps
further into its fascinating application to academic writing and dissertation
formatting. Finally, a set of possible implementation strategies with regard to
the proper introduction of TeX and relevant resources to our university, is
proposed.

%package -n texlive-tlmgr-intro-zh-cn
Summary:        A short tutorial on using tlmgr in Chinese
Version:        svn59100
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tlmgr-intro-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tlmgr-intro-zh-cn-doc <= 11:%{version}

%description -n texlive-tlmgr-intro-zh-cn
This is a Chinese translation of the tlmgr documentation. It introduces some of
the common usage of the TeX Live Manager. The original can be found in the
tlmgrbasics package.

%package -n texlive-upzhkinsoku
Summary:        Supplementary Chinese kinsoku for Unicode *pTeX
Version:        svn47354
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(upzhkinsoku.sty) = %{tl_version}

%description -n texlive-upzhkinsoku
This package provides supplementary Chinese kinsoku (line breaking rules etc.)
settings for Unicode (e-)upTeX (when using Unicode as its internal encoding),
and ApTeX. Both LaTeX and plain TeX are supported.

%package -n texlive-xpinyin
Summary:        Automatically add pinyin to Chinese characters
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xpinyin-database.def) = %{tl_version}
Provides:       tex(xpinyin.sty) = %{tl_version}

%description -n texlive-xpinyin
The package is written to simplify the input of Hanyu Pinyin. Macros are
provided that automatically add pinyin to Chinese characters.

%package -n texlive-xtuthesis
Summary:        XTU thesis template
Version:        svn47049
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amscd.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(caption.sty)
Requires:       tex(cite.sty)
Requires:       tex(color.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(diagbox.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(xtuformat.sty) = %{tl_version}

%description -n texlive-xtuthesis
The package provides a thesis template for the Xiangtan University.

%package -n texlive-zhlineskip
Summary:        Line spacing for CJK documents
Version:        svn51142
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(xintexpr.sty)
Provides:       tex(zhlineskip.sty) = %{tl_version}

%description -n texlive-zhlineskip
This package supports typesetting CJK documents. It allows users to specify the
two ratios between the leading and the font size of the body text and the
footnote text. For CJK typesetting, these ratios usually range from 1.5 to
1.67. This package is also capable of restoring the math leading to that of the
Latin text (usually 1.2 times the font size). Finally, it is possible to
achieve the Microsoft Word multiple line spacing style using zhlineskip.

%package -n texlive-zhlipsum
Summary:        Chinese dummy text
Version:        svn54994
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(zhlipsum-big5.def) = %{tl_version}
Provides:       tex(zhlipsum-gbk.def) = %{tl_version}
Provides:       tex(zhlipsum-utf8.def) = %{tl_version}
Provides:       tex(zhlipsum.sty) = %{tl_version}

%description -n texlive-zhlipsum
This package provides an interface to dummy text in Chinese language, which
will be useful for testing Chinese documents. UTF-8, GBK and Big5 encodings are
supported.

%package -n texlive-zhmetrics
Summary:        TFM subfont files for using Chinese fonts in 8-bit TeX
Version:        svn22207
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(zhwinfonts.tex) = %{tl_version}

%description -n texlive-zhmetrics
These are metrics to use existing Chinese TrueType fonts in workflows that use
LaTeX & dvipdfmx, or pdfLaTeX. The fonts themselves are not included in the
package. Six font families are supported: kai, song, lishu, fangsong, youyuan
and hei. Two encodings (GBK and UTF-8) are supported.

%package -n texlive-zhmetrics-uptex
Summary:        Chinese font metrics for upTeX
Version:        svn40728
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-zhmetrics-uptex
The package contains some Chinese font metrics (JFM, VF, etc) for upTeX engine,
together with a simple DVIPDFMx font mapping of Fandol fonts for DVIPDFMx.

%package -n texlive-zhnumber
Summary:        Typeset Chinese representations of numbers
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(zhnumber.sty) = %{tl_version}

%description -n texlive-zhnumber
The package provides commands to typeset Chinese representations of numbers.
The main difference between this package and CJKnumb is that the commands
provided are expandable in the 'proper' way.

%package -n texlive-zhspacing
Summary:        Spacing for mixed CJK-English documents in XeTeX
Version:        svn41145
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(ulem.sty)
Provides:       tex(t-zhspacing.tex) = %{tl_version}
Provides:       tex(zhfont.sty) = %{tl_version}
Provides:       tex(zhmath.sty) = %{tl_version}
Provides:       tex(zhsmyclass.sty) = %{tl_version}
Provides:       tex(zhspacing.sty) = %{tl_version}
Provides:       tex(zhsusefulmacros.sty) = %{tl_version}
Provides:       tex(zhulem.sty) = %{tl_version}

%description -n texlive-zhspacing
The package manages spacing in a CJK document; between consecutive Chinese
letters, spaces are ignored, but a consistent space is inserted between Chinese
text and English (or mathematics). The package may be used by any document
format under XeTeX.

%post -n texlive-hyphen-chinese
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/pinyin.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "pinyin loadhyph-zh-latn-pinyin.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{pinyin}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{pinyin}{loadhyph-zh-latn-pinyin.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-chinese
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/pinyin.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{pinyin}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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

# Install AppStream metadata for font components
cp %{SOURCE75} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/fandol %{buildroot}%{_datadir}/fonts/fandol

# Apply xtuthesis patch
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-xtuthesis-use-diagbox.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-arphic
%license other-free.txt
%{_texmf_main}/dvips/arphic/
%{_texmf_main}/fonts/afm/arphic/bkaiu/
%{_texmf_main}/fonts/afm/arphic/bsmiu/
%{_texmf_main}/fonts/afm/arphic/gbsnu/
%{_texmf_main}/fonts/afm/arphic/gkaiu/
%{_texmf_main}/fonts/map/dvips/arphic/
%{_texmf_main}/fonts/tfm/arphic/bkaimp/
%{_texmf_main}/fonts/tfm/arphic/bkaiu/
%{_texmf_main}/fonts/tfm/arphic/bsmilp/
%{_texmf_main}/fonts/tfm/arphic/bsmiu/
%{_texmf_main}/fonts/tfm/arphic/gbsnlp/
%{_texmf_main}/fonts/tfm/arphic/gbsnu/
%{_texmf_main}/fonts/tfm/arphic/gkaimp/
%{_texmf_main}/fonts/tfm/arphic/gkaiu/
%{_texmf_main}/fonts/type1/arphic/bkaiu/
%{_texmf_main}/fonts/type1/arphic/bsmiu/
%{_texmf_main}/fonts/type1/arphic/gbsnu/
%{_texmf_main}/fonts/type1/arphic/gkaiu/
%{_texmf_main}/fonts/vf/arphic/bkaimp/
%{_texmf_main}/fonts/vf/arphic/bsmilp/
%{_texmf_main}/fonts/vf/arphic/gbsnlp/
%{_texmf_main}/fonts/vf/arphic/gkaimp/
%doc %{_texmf_main}/doc/fonts/arphic/

%files -n texlive-arphic-ttf
%license other-free.txt
%{_texmf_main}/fonts/truetype/public/arphic-ttf/
%doc %{_texmf_main}/doc/fonts/arphic-ttf/

%files -n texlive-asymptote-by-example-zh-cn
%license gpl2.txt
%doc %{_texmf_main}/doc/support/asymptote-by-example-zh-cn/

%files -n texlive-asymptote-faq-zh-cn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/support/asymptote-faq-zh-cn/

%files -n texlive-asymptote-manual-zh-cn
%license lgpl2.1.txt
%doc %{_texmf_main}/doc/support/asymptote-manual-zh-cn/

%files -n texlive-cns
%license pd.txt
%{_texmf_main}/fonts/misc/cns/
%{_texmf_main}/fonts/tfm/cns/c0so12/
%{_texmf_main}/fonts/tfm/cns/c1so12/
%{_texmf_main}/fonts/tfm/cns/c2so12/
%{_texmf_main}/fonts/tfm/cns/c3so12/
%{_texmf_main}/fonts/tfm/cns/c4so12/
%{_texmf_main}/fonts/tfm/cns/c5so12/
%{_texmf_main}/fonts/tfm/cns/c6so12/
%{_texmf_main}/fonts/tfm/cns/c7so12/
%doc %{_texmf_main}/doc/fonts/cns/

%files -n texlive-ctex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ctex/
%{_texmf_main}/tex/latex/ctex/
%{_texmf_main}/tex/luatex/ctex/
%doc %{_texmf_main}/doc/latex/ctex/

%files -n texlive-ctex-faq
%license fdl.txt
%doc %{_texmf_main}/doc/latex/ctex-faq/

%files -n texlive-exam-zh
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/exam-zh/
%doc %{_texmf_main}/doc/xelatex/exam-zh/

%files -n texlive-fandol
%license gpl2.txt
%{_texmf_main}/fonts/opentype/public/fandol/
%doc %{_texmf_main}/doc/fonts/fandol/
%{_datadir}/fonts/fandol
%{_datadir}/appdata/fandol.metainfo.xml

%files -n texlive-fduthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fduthesis/
%doc %{_texmf_main}/doc/latex/fduthesis/

%files -n texlive-hanzibox
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/hanzibox/
%doc %{_texmf_main}/doc/xelatex/hanzibox/

%files -n texlive-hyphen-chinese
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-impatient-cn
%license fdl.txt
%doc %{_texmf_main}/doc/plain/impatient-cn/

%files -n texlive-install-latex-guide-zh-cn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/install-latex-guide-zh-cn/

%files -n texlive-latex-notes-zh-cn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/generic/latex-notes-zh-cn/

%files -n texlive-lshort-chinese
%license fdl.txt
%doc %{_texmf_main}/doc/latex/lshort-chinese/

%files -n texlive-luatex-cn
%license apache2.txt
%{_texmf_main}/tex/lualatex/luatex-cn/
%doc %{_texmf_main}/doc/latex/luatex-cn/

%files -n texlive-lxgw-fonts
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/lxgw-fonts/
%{_texmf_main}/tex/latex/lxgw-fonts/
%doc %{_texmf_main}/doc/fonts/lxgw-fonts/

%files -n texlive-nanicolle
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/nanicolle/
%doc %{_texmf_main}/doc/xelatex/nanicolle/

%files -n texlive-njurepo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/njurepo/
%doc %{_texmf_main}/doc/latex/njurepo/

%files -n texlive-pgfornament-han
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgfornament-han/
%doc %{_texmf_main}/doc/latex/pgfornament-han/

%files -n texlive-qyxf-book
%license mit.txt
%{_texmf_main}/tex/latex/qyxf-book/
%doc %{_texmf_main}/doc/latex/qyxf-book/

%files -n texlive-sjtutex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sjtutex/
%doc %{_texmf_main}/doc/latex/sjtutex/

%files -n texlive-suanpan-l3
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/suanpan-l3/
%doc %{_texmf_main}/doc/latex/suanpan-l3/

%files -n texlive-texlive-zh-cn
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-zh-cn/

%files -n texlive-texproposal
%license cc-by-4.txt
%license mit.txt
%doc %{_texmf_main}/doc/latex/texproposal/

%files -n texlive-tlmgr-intro-zh-cn
%license gpl3.txt
%doc %{_texmf_main}/doc/support/tlmgr-intro-zh-cn/

%files -n texlive-upzhkinsoku
%license knuth.txt
%{_texmf_main}/tex/generic/upzhkinsoku/
%doc %{_texmf_main}/doc/generic/upzhkinsoku/

%files -n texlive-xpinyin
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xpinyin/
%doc %{_texmf_main}/doc/latex/xpinyin/

%files -n texlive-xtuthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xtuthesis/
%doc %{_texmf_main}/doc/latex/xtuthesis/

%files -n texlive-zhlineskip
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/zhlineskip/
%doc %{_texmf_main}/doc/latex/zhlineskip/

%files -n texlive-zhlipsum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/zhlipsum/
%doc %{_texmf_main}/doc/latex/zhlipsum/

%files -n texlive-zhmetrics
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/zhmetrics/cyberb/
%{_texmf_main}/fonts/tfm/zhmetrics/gbk/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkfs/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkhei/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkkai/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkli/
%{_texmf_main}/fonts/tfm/zhmetrics/gbksong/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkyou/
%{_texmf_main}/fonts/tfm/zhmetrics/unifs/
%{_texmf_main}/fonts/tfm/zhmetrics/unihei/
%{_texmf_main}/fonts/tfm/zhmetrics/unikai/
%{_texmf_main}/fonts/tfm/zhmetrics/unili/
%{_texmf_main}/fonts/tfm/zhmetrics/unisong/
%{_texmf_main}/fonts/tfm/zhmetrics/uniyou/
%{_texmf_main}/tex/generic/zhmetrics/
%{_texmf_main}/tex/latex/zhmetrics/
%doc %{_texmf_main}/doc/fonts/zhmetrics/

%files -n texlive-zhmetrics-uptex
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/public/zhmetrics-uptex/
%{_texmf_main}/fonts/vf/public/zhmetrics-uptex/
%doc %{_texmf_main}/doc/fonts/zhmetrics-uptex/

%files -n texlive-zhnumber
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/zhnumber/
%doc %{_texmf_main}/doc/latex/zhnumber/

%files -n texlive-zhspacing
%license lppl1.3c.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/zhspacing/
%{_texmf_main}/tex/xelatex/zhspacing/
%doc %{_texmf_main}/doc/generic/zhspacing/

%changelog
%autochangelog
