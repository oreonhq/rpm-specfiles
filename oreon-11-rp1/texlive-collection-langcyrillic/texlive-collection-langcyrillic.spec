%global source0_hash f381a48cd6aa89fef6ec477a781355ca4a75bc5a143a34edb93e0bb01eed68c959fd4c5cf45588b1cb032fef01e238c72ac49cd0e3bb06ef36c451f155c932ca

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langcyrillic
Epoch:          12
Version:        svn69727
Release:        5%{?dist}
Summary:        Cyrillic

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 5856582f8bf6a98a4fbd560bfca82ccb226267e249f0caf8afc775875d50ec204ea613320534a63062dffd0e050905adb24763a95fec2ef4e8faed70a400d976
%global source3_hash 247d5a3b99cd5a377534a94fedf47f6710d32d875d3208b1516fdc9acafee70a14ef1dc37600f9da53f806323d0519ebb2c4e288e471363756b7b819751373c8
%global source4_hash 0c838e5c5cd010fddaec385376f9eb5fb10730e918dd28f58987f855a444d91ed2e66c0de46c74637d134d72f7e348e538836df33f6255a14ed51d0e8d5e8a3e
%global source5_hash 4dcd92a2088e737972f0663fe5161883cae901dc82aafd1bd33f2d80a852fb51d6229c95cc655826bd17599a7152b8a7bf0031eb046530a135e8bc5c9c74b2dd
%global source6_hash 5acec3460294e71e6def384a7863a849e8a5d431dde49c77a4a7803af5373b56fcd376f6e73b237dd230728ab5b536f903b6a1bb19fc478dd5e742293a6e6ca8
%global source7_hash 387919d8bc226b00492f9924486a2591d15083a5a8e2293889f6532ef28fdd6409e2a777e728bee7f7b9796a304f440d8cc5fca246588d2b3ef0c84c79b701ce
%global source8_hash 0067de0fddd73a7c68cd2b3a12b4eb620c6b95886c4c34ec1766ff9b3c174ed2a8cbb1dae72cd8adcfe55bf01e4d24e47668e76babdc57ca9eb59704a5ee7cd5
%global source9_hash e83a8db6c60853dea918d226fe643fd06c1cd65bd3b9e29fac962c029a263e75821dcf6a5a3b33ba44b12321d5e19633f704885e77017cb43e9555a4e060394b
%global source10_hash c4c4bf91fb22d0766bbab6a9980b0faa19f4031cabd044a309478f9ee700bc26247a10051f10d36c8cd88425820d2f800d3947d005fa9fb8b54429efdeb3c8c8
%global source11_hash a173daa03c9da413b4f200a0427e5293676ff3bc64dfd21d945977fc78fa9172ebcd73bad2c7ebd8976ee252cebe3c78d03ac9aa10b2be9984bc34b66ac5ac66
%global source12_hash 6a1a70436f8c47766f851c6d4dbdea193d085f5c4b2c65c5b818b7e653337547368fa64f6aa1377b2faa41174d7245233410028ffc8e0f194ab949d145236953
%global source13_hash 1993f173b119a1d8a6ffe767a9b0e012e1035b9760677174bd6c4fe64d46ac85f023232ec1e8bc39b0c80b1917c91d600a0312d3e1d763b54b42f5114d4997b8
%global source14_hash 6b312822caec9f9d71396b8737010e59521cc59a744c6d2e0633ac26b24ab0ea97ef29472a83b49448e8d82225ccb63926cd91ffdacc523ebf37bfbd2d4cf6b9
%global source15_hash a56e9927434f6d29db7c1ec20c0c3d20cd24241a9883fff160cba111eb5c11181d5ad1b9ec8cb66dedc649b8c8d25b9cb8670f1a28474174b31cfed380a2327a
%global source16_hash c42006e8d596b231c3ef7f3f7123292a9563f6bb0881a7807625bd05e49a67ffd37d6e0965e6da36cdff816cdbf780e54b79b999ee5d0a18fad315f2724cc839
%global source17_hash 153db17097c5a1e6bbad3e13e7bbfaf13bd8380633f62e9323d2c0514a2649b001c997bad9e7495a88f5cf9c1289f2987d147e22bdca6100e7adc1d88561d443
%global source18_hash c9adea5e1bae55b58486984797ad6360218b54693825d78cca3cfdf6e832909cb3a305265a8b7e71b7ba2a3fd45e65c94da350bd1017db82fc45e5c54ab2253d
%global source19_hash 98c497bd8d422cacf639cb38ff3a489b5fcda3f92cb5a734287fc930666867eb0e9e6f6014ad42df527d3999eb5a87da28d7178b47cc53eb44a338567f952ca4
%global source20_hash ed0c04c0afccd7f9f68bb8f65a6497b9cbfb2bbcb5333852da7b790083e71ceec8348f6893f1e0f16bef7e4b5ca0b9d1a58ca46898dc58a02f0324a62971b916
%global source21_hash c890a1d644674b72efdd3060f5ff1f66bf0d44187f11bc4757fe60c48b004a74fc7812e22087545226ce9531274e5a8d46524dc74ce77d925b554f82536ddf2c
%global source22_hash 35991c71454140b8a01ed53a53fb58ee27212bb5948385e772f984eb1611f20ab347d3a56a69928554567dbb6adf9dec0af936cadfe7fab06bde9fb5e344fe23
%global source23_hash e5ef11cba6b0251844200093445f5183de60e0c0198da9c7000ef5c05a2a9a4303a15dc77ed03e9874e452ffdd283016cedb8901e78cd0312ea5bbcc529b74d5
%global source24_hash 748dec387a09546b28718e943e05772cd56c75a0066793332b343e7f604e607efd37a071c1f4f32fbd20d7427277bf2d598b355b8ea3a0a04943ccb90f4f249d
%global source25_hash baffe2691ae82354ce0f9af18f90f3f25112f6d5634abd41ddad74d13773a24d21a5b8448e812f4076a1d98eae9ecd10046d72edd324384e2411ca2b6aa42527
%global source26_hash 7544bfab257666fefed3e23579e44c39db664e2a394f0904e9fba6e926ea32c50c24ecab2c628c017fddf32d8febe6fbf0c9c677450c8f5f0a060186e8c21454
%global source27_hash 88533d558299c2af60f7bb71c88e3d453cfc16aca78b2fb91dd68a8bce322c8552451698dec40d2d6c04125cf8529f8728a615b60fc4b269e453d4ddbd2c0d64
%global source28_hash cd598ab39d157167cb6199aef5b5291e741e740c9b9640243b514d035407da879edd5e295182fb3355d4e74716d9784b9a87e13eb172928a2ad55cc4585c3def
%global source29_hash 2a983f50514b8e1abc7927dc3b861f3a10b919809054cc286a2157fac049ffc7439e37010806ffa2bedf3be5992f6afa23a15f4272708f22fed43489f169b551
%global source30_hash ad3e26dfa9966e68d55182ca1fbfdf054bd8aad73d7a65f93d7d91c628116e5d59a36874d26769b648edf095b9d2d4b26249c4b3b2aeced370d7d67c9ef217c6
%global source31_hash e117b8f6d33bc8dcb0af3c77c55c4ea9c8ec3918c2eaf1be7cf1f81f89d5ad9757ddb000c7f4900e5dad71d548395aeda2e410396a69a695505c9e14c0029e5c
%global source32_hash fb8fcaa267876c90762416e59039946b1705ded4260e306d84663d493aa80320968d78570995e3964f5a30f7fec605363dfa96ce29a9e9b3fa72a0caf08d7a50
%global source33_hash b767d00fe5ec0e804e4e3a851f9486fee1202cba1c793499b7da5c773fe8eb7b8cf26e16e832c806b4e2fe9171682b952c0d8f66484ef68e60229ef1660815a9
%global source34_hash 324a9eb8f1a68124888ad7d4f35dd0446c917e643e2cdcfa041ca26b719ccdc541b9b89857aa05dea2d599912c506561c762d288ccc86d637fd927cc70bf910d
%global source35_hash c063b6b5d23bd0a7197f5bd3121c93237c24f0a77fbc72cb370a7cd535282151731ef03098c36d8152707c50808c1b996fd1adaf16185bd3d0e3589e85b67981
%global source36_hash 299fd6bb3539acc95cb1823f325277f19c10f6f71d419aaf5937f7d98b5f7f7780df702aa8c07398923a803a2380f1b075b1a85205d8da1abdba90ea446ad776
%global source37_hash 42e24c7bc4974b6a143a0bc78f9c4e8b1abf9edd125485139aa64816e9fc98cc0a0159200374e7c1731961f677a941e9e107d2c0d40c048cf738aa222db79dad
%global source38_hash aeac66c80d99cc0e9d4539de7c386f271d7dde459e5c3b2d25816e4f95bd8ce85e30c1c7d26265a09f284ee0a8839de0d26f2d86cfbb9ec3817c01484a02e107
%global source39_hash ab4d430b29d22c5dd05f229786205ca5e01ba4eacb70cda655f480712c315adb8b8fff02f0c4f5adc5294be183c312129da4d65cd972f9445729c215d9ad2148
%global source40_hash 987253956015df12ae9b4a9a3fbd8d487651dd8a74355aab8fa69712320409da0f149c13cbd7a5b5c1cbef2384e1e12025041d619aa603d2510cded9dd6fdc0b
%global source41_hash bd2b51f9aab7d52accbc0d323bdf49e7b96f999711c8f7bc270c67e7ba1581c82be79f67a5769ef1d2ea67f8b7530f95452343452170f805a184507932ca3aea
%global source42_hash acdb040be74102561f233d7dbab90a6143407be4e3abdb74deb1b6afa49d8aeb3c3e39da0539a705b29c3fb9ea8e4fcb36414fdb8663259c47eacae5a1a65ff4
%global source43_hash 3c22989a2d90a084ce6b3b3ec592166793ae412b0bf541cc8a7a6d67b773a40dd96af5a765fc7012cd912379111ac01c7b71a3dd3701bd55a0b740f55feef5ce
%global source44_hash c6a8750ec7f5148e73a066e553767058693818ac303480c31ed56ded802712c92486434cec967375d99359431a6f2da88a50dae82e29ec3f89b8f18dbd5ebf03
%global source45_hash 82600643c91120d732d50dcc6e14a4b4b4c471bf6c0031890487215d952cbb9675210f11fc40b039aff529bef90282d432966ef9547fc7d0272f85c02a288f4c
%global source46_hash f707d0491bb6a246243035d1cad265787ec4aeb7cbcc73e3500295dc67bf3a3a06b316f9f82d559502b7f108ab636b90fd01c3d1b0ee5f13fa3418910557c8b3
%global source47_hash e580c984d9a2242eb7f3a356b222dc6fc4f2fb1e6194f09086e265e253746ba1d94cff324a30c473724410d1d6b0bb7b8bc162cadb63ed96f0837e996c39f988
%global source48_hash 3645bb53bc2aff292dd5a70e3020898b969422b9e21fd11354e2ce60a6c7e668afe149263ee02e3588e0c3803c9568d999a6a6bb067a5941ec288923e167b2f6
%global source49_hash aba0224e2f5fe0e574e5a529ea0538f29ca4a8c95af8b2986954d8a55517e15885ee6f21a53f26a08b0c24b32a98a57642f36b7e45dfd26d75fdeca836f55ebb
%global source50_hash d8be762d3fae4a90991ea2ab8c0bd249ba34786b6aae84b504924f569f2eb6e45df3ecdde5b75d1eaaddc13d18c190e485331eb0de05fa19b646324de22574be
%global source51_hash 9676cef9e0fbe7a0196b1ea0fb3ea4f0399a3ee8ed76ef06e824848a57922dc4f7cc1f50a1fcea47fc265465407653447ab80e80dbac3c4bc00488d0929f87bc
%global source52_hash 1965f31e28a9f54d86a495b4b8cea50dc59f409d066918dedf77f86448b60ea547565dcf2069ee0e0a646d53f34d244868600951c4b1a4d4e099fe50e3c2b477
%global source53_hash e234fc25e9d8e5aa89a59e21186a16de3c695ce45c9ee8d132546381cb18e9be681bd4ee9c70bb10b4769ada5e5874b500d2a3cd7d264d89610dcda35fcba9a1
%global source54_hash 57f2449eaed3651b808095348f056fdfa90b00979ba2e21fad120efe096dca9a9e48474e9dbb539f347ffe20ccd5582f4815ff4552c54e9ea5f9df391dd75edb
%global source55_hash c6f92a720fc5baf6f55c3bc18e22113de0f7cad8a051c2019360f5f3c64eaa450bb12d6c361c52a5a802f558ff8d2cbfaa35897682d6ad218e9adbbc788f3c57
%global source56_hash 5e67f1908356e1f21e672e63a8873e46ebb36af39e55a64c174c3bc5c49057c6d19ac36523c34a7f1c1fc53346f6ddde8fd239ca88b5790ebba1eb8b7dbeb0ed
%global source57_hash ba2a7a76db77f4db3a548654e53d587b8f5b3dab9fef56b1f8c2640bcace64237e0bea5129025a07a490a2660ccd019fc5e83e3db504c6cd30b12b19df755f8d
%global source58_hash 9f6d0153e79a205d0fce5b289fa43317ded0b70abc06139a503b98199584e8cb12b083c8235b6b53ff2a80cf249a4a43cefd3e0b39a9a406c62c1e684bcb35eb
%global source59_hash 505f21709bfa977584649f0caab88002f0e1d3744fc5c0d1d1f92884b75ee44d9bb60d62b4d68a70b4f3c9c2095cb0ef23a913daa0e9d0194c36af96cede5d7b
%global source60_hash 11bceea67aae767037d728ab7892eedab312e9477f1f9f7501f9702fca4ceea4e21bd575b1589fb545abdbdc5f5f5315243f77adb4c9b9a2507fb255481c5541
%global source61_hash 876cba326071d0f347d9a1a4c1eca692ca743729b9604a51bb5b53de96da6006ff24168040e77df60b1999cb22901b7318669c32378a869081956dde40974802
%global source62_hash 4e3998b6c3f5578929204c0b5f131b0ad4526057b50811253b6a90367327c63af5bec386aef54ae6c80be7a1ecdcc6875bbdca532fab864e61837cf16855750f
%global source63_hash 38c8ac74b304ac992bad807f2727a3e75a727a77c5bfe5042e24a39ad305162e828ca0333963a3f91c5f26ca0324e7feea97dc6ab84c1cfdb6c26b05ed5f4fd5
%global source64_hash 420b77a36a08e75f8020edffed704ff0398115a6bfe694fa46957ad8b35c58435ecde4c16176a72bbcbcd16139502f8fb679399852bfc9000df6d5f305fbb04e
%global source65_hash 5c10fe13a4e1d6117ebfe8d737d50047dc97483c7a0cc287a9e79d367af50ec1cbdc0800161919b92c6d82774c9e756970db71344259028c254fbf2c1fe86219
%global source66_hash 6cbd1da1160519914db1a2269a54f1f81442d84750b15179e4a0f4e5373512c959542a789ef39a2803b68030bd6a8001fde777e907e85852703ff696ec9e5113
%global source67_hash 0f2a2fb44eaef8e0eb01e12260fa310d661501c3e1dacde2882199ce4bd5323c837704fd50e8db5b4ba567a38038b37be28fd834874262de2e3ad36b65816498
%global source68_hash d9b5d42c565d5704ab516302534238961ad42e971d3c3b4b4672d4cc19927ac22a871735d88c362b753640d457597911fa269ec30edb5c1c0af96820299c6720
%global source69_hash 6ed0551c176ddd34e1a4eb4449fd78ca38c166efd41b31c78dc1e192a714fdc81b195cf83587f256462b610681136b69960867d5f1a571a5b1b47256fca88f05
%global source70_hash 7425b3bab2d1a29a1ccb57349b40acd2ad0b40b40e3f3e7f26f85462a55d2b0c9896b875ef642a132f1f148f1ec20b12bc852d21bb4ceb095487f6ac60804b7c
%global source71_hash 505f8d9c2f0122836f9d2309b68824e98d52db5425d1896d9d65b910f0b019d6c5c27acdbbdf80ef48e27cbb8477c1056907a6096e2105f46abaea70299aa8ba
%global source72_hash 7658ab0d98a505eda9a86e9ecd64b0e35d9cd332b03066b46825c2a6252b9aa8edb24eb4af2bfc267127b349f741709ada836104dbfc2becadfd97d22e737365
%global source73_hash 40e8b29f29ed61addc2b9e7ce4b73d12bf2e59f1c50c65e59e9c8cac5e6c3ef264ce2071b0d54e15f5029c101a51d0efcda0144e113aaedc714eb1300aa9635d
%global source74_hash de99d6d13c6b68f8327c0b72dd3ab8aef92d07085f3eb59d94aaf8901d11d542c0795a33cb2bff1ff0dfb1acc99e43fc767150956abd873536a7d4e3b8f031f7
%global source75_hash 4e07f6f015a023af113822e409e03405f49b9786f854308c14f2060cac75d8420ddab090696044860be75f1337b6d3b6e7a45fc0d56969b0894efce3a8c60ae7
%global source76_hash de8b279e91e6aadc7e47b446f57296e3626fce4a9a969f01d10179b7019d6ec260d1131bd164c16d75a1951624a216b97eb4a71c4d4074dfa845afc26108c72f
%global source77_hash 756126c26d7d7c27de276a890ae22bb5272bdb034de367389e8a16aff078fe250c3f68ba562fe8e6cf082ac5c086caf40478bed0794f0213fa329d4f3b6da566
%global source78_hash 2faeeadc81ca7f6fba45b6b237fb604a6eb6e8888117f759f6d369ed354b20b35dd007eb11c017e4f0ebcfa99627f519b291eecd1b41505d7f4ecbfc23307784
%global source79_hash 11b9d4a92c6df44dfc629c7385b56463dcb13564e819cf1bde005e228040a9f675cfb5818ca9f5c5d59a3db7a0d42a5584d9a3a530d772ba2b4bf3145534bc0c

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langcyrillic.tar.xz#/collection-langcyrillic.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-belarusian.tar.xz#/babel-belarusian.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-belarusian.doc.tar.xz#/babel-belarusian.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-bulgarian.tar.xz#/babel-bulgarian.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-bulgarian.doc.tar.xz#/babel-bulgarian.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-russian.tar.xz#/babel-russian.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-russian.doc.tar.xz#/babel-russian.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-serbian.tar.xz#/babel-serbian.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-serbian.doc.tar.xz#/babel-serbian.doc.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-serbianc.tar.xz#/babel-serbianc.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-serbianc.doc.tar.xz#/babel-serbianc.doc.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-ukrainian.tar.xz#/babel-ukrainian.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-ukrainian.doc.tar.xz#/babel-ukrainian.doc.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/churchslavonic.tar.xz#/churchslavonic.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/churchslavonic.doc.tar.xz#/churchslavonic.doc.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmcyr.tar.xz#/cmcyr.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmcyr.doc.tar.xz#/cmcyr.doc.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyrplain.tar.xz#/cyrplain.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/disser.tar.xz#/disser.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/disser.doc.tar.xz#/disser.doc.or11.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eskd.tar.xz#/eskd.or11.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eskd.doc.tar.xz#/eskd.doc.or11.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eskdx.tar.xz#/eskdx.or11.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eskdx.doc.tar.xz#/eskdx.doc.or11.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gost.tar.xz#/gost.or11.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gost.doc.tar.xz#/gost.doc.or11.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-belarusian.tar.xz#/hyphen-belarusian.or11.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-bulgarian.tar.xz#/hyphen-bulgarian.or11.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-churchslavonic.tar.xz#/hyphen-churchslavonic.or11.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-mongolian.tar.xz#/hyphen-mongolian.or11.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-russian.tar.xz#/hyphen-russian.or11.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-serbian.tar.xz#/hyphen-serbian.or11.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-ukrainian.tar.xz#/hyphen-ukrainian.or11.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lcyw.tar.xz#/lcyw.or11.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lcyw.doc.tar.xz#/lcyw.doc.or11.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lh.tar.xz#/lh.or11.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lh.doc.tar.xz#/lh.doc.or11.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lhcyr.tar.xz#/lhcyr.or11.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-bulgarian.tar.xz#/lshort-bulgarian.or11.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-bulgarian.doc.tar.xz#/lshort-bulgarian.doc.or11.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-mongol.tar.xz#/lshort-mongol.or11.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-mongol.doc.tar.xz#/lshort-mongol.doc.or11.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-russian.tar.xz#/lshort-russian.or11.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-russian.doc.tar.xz#/lshort-russian.doc.or11.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-ukr.tar.xz#/lshort-ukr.or11.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-ukr.doc.tar.xz#/lshort-ukr.doc.or11.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnhyphn.tar.xz#/mnhyphn.or11.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnhyphn.doc.tar.xz#/mnhyphn.doc.or11.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mongolian-babel.tar.xz#/mongolian-babel.or11.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mongolian-babel.doc.tar.xz#/mongolian-babel.doc.or11.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/montex.tar.xz#/montex.or11.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/montex.doc.tar.xz#/montex.doc.or11.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpman-ru.tar.xz#/mpman-ru.or11.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpman-ru.doc.tar.xz#/mpman-ru.doc.or11.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numnameru.tar.xz#/numnameru.or11.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numnameru.doc.tar.xz#/numnameru.doc.or11.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-eucl-translation-bg.tar.xz#/pst-eucl-translation-bg.or11.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-eucl-translation-bg.doc.tar.xz#/pst-eucl-translation-bg.doc.or11.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ruhyphen.tar.xz#/ruhyphen.or11.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/russ.tar.xz#/russ.or11.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/russ.doc.tar.xz#/russ.doc.or11.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-apostrophe.tar.xz#/serbian-apostrophe.or11.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-apostrophe.doc.tar.xz#/serbian-apostrophe.doc.or11.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-date-lat.tar.xz#/serbian-date-lat.or11.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-date-lat.doc.tar.xz#/serbian-date-lat.doc.or11.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-def-cyr.tar.xz#/serbian-def-cyr.or11.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-def-cyr.doc.tar.xz#/serbian-def-cyr.doc.or11.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-lig.tar.xz#/serbian-lig.or11.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-lig.doc.tar.xz#/serbian-lig.doc.or11.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/t2.tar.xz#/t2.or11.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/t2.doc.tar.xz#/t2.doc.or11.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-ru.tar.xz#/texlive-ru.or11.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-ru.doc.tar.xz#/texlive-ru.doc.or11.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-sr.tar.xz#/texlive-sr.or11.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-sr.doc.tar.xz#/texlive-sr.doc.or11.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ukrhyph.tar.xz#/ukrhyph.or11.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ukrhyph.doc.tar.xz#/ukrhyph.doc.or11.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecyrmongolian.tar.xz#/xecyrmongolian.or11.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecyrmongolian.doc.tar.xz#/xecyrmongolian.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-babel-belarusian
Requires:       texlive-babel-bulgarian
Requires:       texlive-babel-russian
Requires:       texlive-babel-serbian
Requires:       texlive-babel-serbianc
Requires:       texlive-babel-ukrainian
Requires:       texlive-churchslavonic
Requires:       texlive-cmcyr
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-cyrillic
Requires:       texlive-cyrillic-bin
Requires:       texlive-cyrplain
Requires:       texlive-disser
Requires:       texlive-eskd
Requires:       texlive-eskdx
Requires:       texlive-gost
Requires:       texlive-hyphen-belarusian
Requires:       texlive-hyphen-bulgarian
Requires:       texlive-hyphen-churchslavonic
Requires:       texlive-hyphen-mongolian
Requires:       texlive-hyphen-russian
Requires:       texlive-hyphen-serbian
Requires:       texlive-hyphen-ukrainian
Requires:       texlive-lcyw
Requires:       texlive-lh
Requires:       texlive-lhcyr
Requires:       texlive-lshort-bulgarian
Requires:       texlive-lshort-mongol
Requires:       texlive-lshort-russian
Requires:       texlive-lshort-ukr
Requires:       texlive-mnhyphn
Requires:       texlive-mongolian-babel
Requires:       texlive-montex
Requires:       texlive-mpman-ru
Requires:       texlive-numnameru
Requires:       texlive-pst-eucl-translation-bg
Requires:       texlive-ruhyphen
Requires:       texlive-russ
Requires:       texlive-serbian-apostrophe
Requires:       texlive-serbian-date-lat
Requires:       texlive-serbian-def-cyr
Requires:       texlive-serbian-lig
Requires:       texlive-t2
Requires:       texlive-texlive-ru
Requires:       texlive-texlive-sr
Requires:       texlive-ukrhyph
Requires:       texlive-xecyrmongolian

%description
Support for Cyrillic scripts (Bulgarian, Russian, Serbian, Ukrainian), even if
Latin alphabets may also be used.

%package -n texlive-babel-belarusian
Summary:        Babel support for Belarusian
Version:        svn49022
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(belarusian.ldf) = %{tl_version}

%description -n texlive-babel-belarusian
The package provides support for use of Babel in documents written in
Belarusian.

%package -n texlive-babel-bulgarian
Summary:        Babel contributed support for Bulgarian
Version:        svn31902
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bulgarian.ldf) = %{tl_version}

%description -n texlive-babel-bulgarian
The package provides support for documents in Bulgarian (or simply containing
some Bulgarian text).

%package -n texlive-babel-russian
Summary:        Russian language module for Babel
Version:        svn57376
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(russianb.ldf) = %{tl_version}

%description -n texlive-babel-russian
The package provides support for use of Babel in documents written in Russian
(in both "traditional" and modern forms). The support is adapted for use both
under 'traditional' TeX engines, and under XeTeX and LuaTeX.

%package -n texlive-babel-serbian
Summary:        Babel/Polyglossia support for Serbian
Version:        svn64571
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(serbian.ldf) = %{tl_version}

%description -n texlive-babel-serbian
The package provides support for Serbian documents written in Latin, in babel.

%package -n texlive-babel-serbianc
Summary:        Babel module to support Serbian Cyrillic
Version:        svn64588
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(serbianc.ldf) = %{tl_version}

%description -n texlive-babel-serbianc
The package provides support for Serbian documents written in Cyrillic, in
babel.

%package -n texlive-babel-ukrainian
Summary:        Babel support for Ukrainian
Version:        svn56674
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ukraineb.ldf) = %{tl_version}

%description -n texlive-babel-ukrainian
The package provides support for use of babel in documents written in
Ukrainian. The support is adapted for use under legacy TeX engines as well as
XeTeX and LuaTeX.

%package -n texlive-churchslavonic
Summary:        Typeset documents in Church Slavonic language using Unicode
Version:        svn67474
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-etoolbox
Requires:       texlive-fonts-churchslavonic
Requires:       texlive-hyphen-churchslavonic
Requires:       texlive-oberdiek
Requires:       texlive-xcolor
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(luacolor.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(churchslavonic.sty) = %{tl_version}
Provides:       tex(cu-calendar.sty) = %{tl_version}
Provides:       tex(cu-kinovar.sty) = %{tl_version}
Provides:       tex(cu-kruk.sty) = %{tl_version}
Provides:       tex(cu-num.sty) = %{tl_version}
Provides:       tex(cu-util.sty) = %{tl_version}
Provides:       tex(gloss-churchslavonic.ldf) = %{tl_version}

%description -n texlive-churchslavonic
The package provides fonts, hyphenation patterns, and supporting macros to
typeset Church Slavonic texts. It depends on the following other packages:
fonts-churchslavonic, hyph-utf8, intcalc, etoolbox, and xcolor.

%package -n texlive-cmcyr
Summary:        Computer Modern fonts with cyrillic extensions
Version:        svn68681
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cmcyr
These are the Computer Modern fonts extended with Russian letters, in Metafont
sources and ATM Compatible Type 1 format. The fonts are provided in KOI-7, but
virtual fonts are available to recode them to three other Russian 8-bit
encodings.

%package -n texlive-cyrplain
Summary:        Support for using T2 encoding
Version:        svn45692
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cyrcmfnt.tex) = %{tl_version}
Provides:       tex(cyrecfnt.tex) = %{tl_version}
Provides:       tex(cyrtex.tex) = %{tl_version}
Provides:       tex(plainenc.tex) = %{tl_version}
Provides:       tex(txxdefs.tex) = %{tl_version}
Provides:       tex(txxextra.tex) = %{tl_version}

%description -n texlive-cyrplain
The T2 bundle provides a variety of separate support functions for using
Cyrillic characters in LaTeX: the mathtext package, for using Cyrillic letters
'transparently' in formulae; the citehack package, for using Cyrillic (or
indeed any non-ascii) characters in citation keys; support for Cyrillic in
BibTeX; support for Cyrillic in Makeindex; and various items of font support.

%package -n texlive-disser
Summary:        Class and templates for typesetting dissertations in Russian
Version:        svn43417
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(disser.cls) = %{tl_version}
Provides:       tex(gost732.cls) = %{tl_version}

%description -n texlive-disser
Disser comprises a document class and set of templates for typesetting
dissertations in Russian. One of its primary advantages is a simplicity of
format specification for titlepage, headers and elements of automatically
generated lists (table of contents, list of figures, etc). Bibliography styles,
that conform to the requirements of the Russian standard GOST R 7.0.11-2011,
are provided.

%package -n texlive-eskd
Summary:        Modern Russian typesetting
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(eskd.cls) = %{tl_version}

%description -n texlive-eskd
The class offers modern Russian text formatting, in accordance with accepted
design standards. Fonts not (apparently) available on CTAN are required for use
of the class.

%package -n texlive-eskdx
Summary:        Modern Russian typesetting
Version:        svn29235
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(chngpage.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(geometry.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(longtable.sty)
Requires:       tex(lscape.sty)
Requires:       tex(rotating.sty)
Requires:       tex(zref-perpage.sty)
Provides:       tex(eskdafterpkg.sty) = %{tl_version}
Provides:       tex(eskdappsheet.sty) = %{tl_version}
Provides:       tex(eskdbiblist.sty) = %{tl_version}
Provides:       tex(eskdcap.sty) = %{tl_version}
Provides:       tex(eskdchngsheet.sty) = %{tl_version}
Provides:       tex(eskddstu.sty) = %{tl_version}
Provides:       tex(eskdexplan.sty) = %{tl_version}
Provides:       tex(eskdfont.sty) = %{tl_version}
Provides:       tex(eskdfootnote.sty) = %{tl_version}
Provides:       tex(eskdfreesize.sty) = %{tl_version}
Provides:       tex(eskdgraph.cls) = %{tl_version}
Provides:       tex(eskdhash.sty) = %{tl_version}
Provides:       tex(eskdindent.sty) = %{tl_version}
Provides:       tex(eskdinfo.sty) = %{tl_version}
Provides:       tex(eskdlang.sty) = %{tl_version}
Provides:       tex(eskdlist.sty) = %{tl_version}
Provides:       tex(eskdpara.sty) = %{tl_version}
Provides:       tex(eskdplain.sty) = %{tl_version}
Provides:       tex(eskdrussian.def) = %{tl_version}
Provides:       tex(eskdsect.sty) = %{tl_version}
Provides:       tex(eskdspec.sty) = %{tl_version}
Provides:       tex(eskdspecii.sty) = %{tl_version}
Provides:       tex(eskdstamp.sty) = %{tl_version}
Provides:       tex(eskdtab.cls) = %{tl_version}
Provides:       tex(eskdtext.cls) = %{tl_version}
Provides:       tex(eskdtitle.sty) = %{tl_version}
Provides:       tex(eskdtitlebase.sty) = %{tl_version}
Provides:       tex(eskdtotal.sty) = %{tl_version}
Provides:       tex(eskdukrainian.def) = %{tl_version}

%description -n texlive-eskdx
Eskdx is a collection of LaTeX classes and packages to typeset textual and
graphical documents in accordance with Russian (and probably post USSR)
standards for designers.

%package -n texlive-gost
Summary:        BibTeX styles to format according to GOST
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gost
BibTeX styles to format bibliographies in English, Russian or Ukrainian
according to GOST 7.0.5-2008 or GOST 7.1-2003. Both 8-bit and Unicode (UTF-8)
versions of each BibTeX style, in each case offering a choice of sorted and
unsorted. Further, a set of three styles (which do not conform to current
standards) are retained for backwards compatibility.

%package -n texlive-hyphen-belarusian
Summary:        Belarusian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-be.t2a.tex) = %{tl_version}
Provides:       tex(hyph-be.tex) = %{tl_version}
Provides:       tex(hyph-quote-be.tex) = %{tl_version}
Provides:       tex(loadhyph-be.tex) = %{tl_version}

%description -n texlive-hyphen-belarusian
Belarusian hyphenation patterns in T2A and UTF-8 encodings

%package -n texlive-hyphen-bulgarian
Summary:        Bulgarian hyphenation patterns.
Version:        svn73410
License:        LicenseRef-Unknown
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-bg.t2a.tex) = %{tl_version}
Provides:       tex(hyph-bg.tex) = %{tl_version}
Provides:       tex(loadhyph-bg.tex) = %{tl_version}

%description -n texlive-hyphen-bulgarian
Hyphenation patterns for Bulgarian in T2A and UTF-8 encodings.

%package -n texlive-hyphen-churchslavonic
Summary:        Church Slavonic hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-cu.tex) = %{tl_version}
Provides:       tex(loadhyph-cu.tex) = %{tl_version}

%description -n texlive-hyphen-churchslavonic
Hyphenation patterns for Church Slavonic in UTF-8 encoding

%package -n texlive-hyphen-mongolian
Summary:        Mongolian hyphenation patterns in Cyrillic script.
Version:        svn74203
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-mn-cyrl-x-lmc.lmc.tex) = %{tl_version}
Provides:       tex(hyph-mn-cyrl-x-lmc.tex) = %{tl_version}
Provides:       tex(hyph-mn-cyrl.t2a.tex) = %{tl_version}
Provides:       tex(hyph-mn-cyrl.tex) = %{tl_version}
Provides:       tex(loadhyph-mn-cyrl-x-lmc.tex) = %{tl_version}
Provides:       tex(loadhyph-mn-cyrl.tex) = %{tl_version}

%description -n texlive-hyphen-mongolian
Hyphenation patterns for Mongolian in T2A, LMC and UTF-8 encodings. LMC
encoding is used in MonTeX. The package includes two sets of patterns that will
hopefully be merged in future.

%package -n texlive-hyphen-russian
Summary:        Russian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Requires:       texlive-ruhyphen
Provides:       tex(hyph-ru.t2a.tex) = %{tl_version}
Provides:       tex(hyph-ru.tex) = %{tl_version}
Provides:       tex(loadhyph-ru.tex) = %{tl_version}

%description -n texlive-hyphen-russian
Hyphenation patterns for Russian in T2A and UTF-8 encodings. For 8-bit engines,
the 'ruhyphen' package provides a number of different pattern sets, as well as
different (8-bit) encodings, that can be chosen at format-generation time. The
UTF-8 version only provides the default pattern set. A mechanism similar to the
one used for 8-bit patterns may be implemented in the future.

%package -n texlive-hyphen-serbian
Summary:        Serbian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sh-cyrl.t2a.tex) = %{tl_version}
Provides:       tex(hyph-sh-cyrl.tex) = %{tl_version}
Provides:       tex(hyph-sh-latn.ec.tex) = %{tl_version}
Provides:       tex(hyph-sh-latn.tex) = %{tl_version}
Provides:       tex(hyph-sr-cyrl.tex) = %{tl_version}
Provides:       tex(loadhyph-sr-cyrl.tex) = %{tl_version}
Provides:       tex(loadhyph-sr-latn.tex) = %{tl_version}

%description -n texlive-hyphen-serbian
Hyphenation patterns for Serbian in T1/EC, T2A and UTF-8 encodings. For 8-bit
engines the patterns are available separately as 'serbian' in T1/EC encoding
for Latin script and 'serbianc' in T2A encoding for Cyrillic script. Unicode
engines should only use 'serbian' which has patterns in both scripts combined.

%package -n texlive-hyphen-ukrainian
Summary:        Ukrainian hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Requires:       texlive-ukrhyph
Provides:       tex(hyph-quote-uk.tex) = %{tl_version}
Provides:       tex(hyph-uk.t2a.tex) = %{tl_version}
Provides:       tex(hyph-uk.tex) = %{tl_version}
Provides:       tex(loadhyph-uk.tex) = %{tl_version}

%description -n texlive-hyphen-ukrainian
Hyphenation patterns for Ukrainian in T2A and UTF-8 encodings. For 8-bit
engines, the 'ukrhyph' package provides a number of different pattern sets, as
well as different (8-bit) encodings, that can be chosen at format-generation
time. The UTF-8 version only provides the default pattern set. A mechanism
similar to the one used for 8-bit patterns may be implemented in the future.

%package -n texlive-lcyw
Summary:        Make Classic Cyrillic CM fonts accessible in LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifpdf.sty)
Provides:       tex(cmap-cyr-vf.sty) = %{tl_version}
Provides:       tex(lcywenc.def) = %{tl_version}

%description -n texlive-lcyw
The package makes the classic CM Cyrillic fonts accessible for use with LaTeX.

%package -n texlive-lh
Summary:        Cyrillic fonts that support LaTeX standard encodings
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-ec
Provides:       tex(lh-lcy.sty) = %{tl_version}
Provides:       tex(lh-lcyccr.sty) = %{tl_version}
Provides:       tex(lh-lcyxccr.sty) = %{tl_version}
Provides:       tex(lh-ot2.sty) = %{tl_version}
Provides:       tex(lh-ot2ccr.sty) = %{tl_version}
Provides:       tex(lh-ot2xccr.sty) = %{tl_version}
Provides:       tex(lh-t2accr.sty) = %{tl_version}
Provides:       tex(lh-t2axccr.sty) = %{tl_version}
Provides:       tex(lh-t2bccr.sty) = %{tl_version}
Provides:       tex(lh-t2bxccr.sty) = %{tl_version}
Provides:       tex(lh-t2cccr.sty) = %{tl_version}
Provides:       tex(lh-t2cxccr.sty) = %{tl_version}
Provides:       tex(lh-x2ccr.sty) = %{tl_version}
Provides:       tex(lh-x2xccr.sty) = %{tl_version}
Provides:       tex(nfssfox.tex) = %{tl_version}
Provides:       tex(testfox.tex) = %{tl_version}
Provides:       tex(testkern.tex) = %{tl_version}

%description -n texlive-lh
The LH fonts address the problem of the wide variety of alphabets that are
written with Cyrillic-style characters. The fonts are the original basis of the
set of T2* and X2 encodings that are now used when LaTeX users need to write in
Cyrillic languages. Macro support in standard LaTeX encodings is offered
through the latex-cyrillic and t2 bundles, and the package itself offers
support for other (more traditional) encodings. The fonts, in the standard T2*
and X2 encodings are available in Adobe Type 1 format, in the CM-Super family
of fonts. The package also offers its own LaTeX support for OT2 encoded fonts,
CM bright shaped fonts and Concrete shaped fonts.

%package -n texlive-lhcyr
Summary:        A non-standard Cyrillic input scheme
Version:        svn77050
License:        LicenseRef-Lhcyr
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(karabas.tex) = %{tl_version}
Provides:       tex(kniga.tex) = %{tl_version}
Provides:       tex(lhcyralt-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyralt.sty) = %{tl_version}
Provides:       tex(lhcyrkoi-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyrkoi.sty) = %{tl_version}
Provides:       tex(lhcyrwin-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyrwin.sty) = %{tl_version}
Provides:       tex(otchet.tex) = %{tl_version}
Provides:       tex(pismo.tex) = %{tl_version}
Provides:       tex(rusfonts.tex) = %{tl_version}
Provides:       tex(statya.tex) = %{tl_version}

%description -n texlive-lhcyr
A collection of three LaTeX2e styles intended for typesetting Russian and
bilingual English-Russian documents, using the lh fonts and without the benefit
of babel's language-switching mechanisms. The packages (lhcyralt and lhcyrwin
for use under emTeX, and lhcyrkoi for use under teTeX) provide mappings between
the input encoding and the font encoding (which is described as OT1). The way
this is done does not match the way inputenc would do the job, for output via
fontenc to one of the T2 series of font encodings.

%package -n texlive-lshort-bulgarian
Summary:        Bulgarian translation of the "Short Introduction to LaTeX2e"
Version:        svn77050
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-bulgarian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-bulgarian-doc <= 11:%{version}

%description -n texlive-lshort-bulgarian
The source files, PostScript and PDF files of the Bulgarian translation of the
"Short Introduction to LaTeX2e".

%package -n texlive-lshort-mongol
Summary:        Short introduction to LaTeX, in Mongolian
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-mongol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-mongol-doc <= 11:%{version}

%description -n texlive-lshort-mongol
A translation of Oetiker's Not so short introduction.

%package -n texlive-lshort-russian
Summary:        Russian introduction to LaTeX
Version:        svn55643
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-russian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-russian-doc <= 11:%{version}

%description -n texlive-lshort-russian
Russian version of A Short Introduction to LaTeX2e.

%package -n texlive-lshort-ukr
Summary:        Ukrainian version of the LaTeX introduction
Version:        svn55643
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-ukr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-ukr-doc <= 11:%{version}

%description -n texlive-lshort-ukr
Ukrainian version of A Short Introduction to LaTeX2e.

%package -n texlive-mnhyphn
Summary:        Mongolian hyphenation patterns in T2A encoding
Version:        svn69727
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mnhyphn.tex) = %{tl_version}

%description -n texlive-mnhyphn
Serves Mongolian written using Cyrillic letters, using T2A-encoded output.
(Note that the montex bundle provides hyphenation patterns for its own encoding
setup.)

%package -n texlive-mongolian-babel
Summary:        A language definition file for Mongolian in Babel
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mn.def) = %{tl_version}
Provides:       tex(mongolian.ldf) = %{tl_version}
Provides:       tex(mongolian.sty) = %{tl_version}

%description -n texlive-mongolian-babel
This package provides support for Mongolian in a Cyrillic alphabet. (The work
derives from the earlier Russian work for babel.)

%package -n texlive-montex
Summary:        Mongolian LaTeX
Version:        svn29349
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cbfonts
Requires:       tex(diagnose.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lscape.sty)
Requires:       tex(rotating.sty)
Provides:       tex(bicig.def) = %{tl_version}
Provides:       tex(bithe.def) = %{tl_version}
Provides:       tex(buryat.def) = %{tl_version}
Provides:       tex(cpctt.def) = %{tl_version}
Provides:       tex(cpdbk.def) = %{tl_version}
Provides:       tex(cpibmrus.def) = %{tl_version}
Provides:       tex(cpkoi.def) = %{tl_version}
Provides:       tex(cpmls.def) = %{tl_version}
Provides:       tex(cpmnk.def) = %{tl_version}
Provides:       tex(cpmos.def) = %{tl_version}
Provides:       tex(cpncc.def) = %{tl_version}
Provides:       tex(english.def) = %{tl_version}
Provides:       tex(kazakh.def) = %{tl_version}
Provides:       tex(lmaenc.def) = %{tl_version}
Provides:       tex(lmcenc.def) = %{tl_version}
Provides:       tex(lmoenc.def) = %{tl_version}
Provides:       tex(lmsenc.def) = %{tl_version}
Provides:       tex(lmuenc.def) = %{tl_version}
Provides:       tex(mls.sty) = %{tl_version}
Provides:       tex(mlsgalig.tex) = %{tl_version}
Provides:       tex(mlstrans.tex) = %{tl_version}
Provides:       tex(mnhyphex.tex) = %{tl_version}
Provides:       tex(rlbicig.sty) = %{tl_version}
Provides:       tex(russian.def) = %{tl_version}
Provides:       tex(xalx.def) = %{tl_version}

%description -n texlive-montex
MonTeX provides Mongolian and Manju support for the TeX/LaTeX community.
Mongolian is a language spoken in North East Asia, namely Mongolia and the
Inner Mongol Autonomous Region of China. Today, it is written in an extended
Cyrillic alphabet in Mongolia whereas the Uighur writing continues to be in use
in Inner Mongolia, though it is also, legally speaking, the official writing
system of Mongolia. Manju is another language of North East Asia, belonging to
the Tungusic branch of the Altaic languages. Though it is hardly spoken
nowadays, it survives in written form as Manju was the native language of the
rulers of the Qing dynasty (1644-1911) in China. Large quantities of documents
of the Imperial Archives survive, as well as some of the finest dictionaries
ever compiled in Asia, like the Pentaglot, a dictionary comprising Manju,
Tibetan, Mongolian, Uighur and Chinese. MonTeX provides all necessary
characters for writing standard Mongolian in Cyrillic and Classical (aka
Traditional or Uighur) writing, and Manju as well as transliterated Tibetan
texts, for which purpose a number of additional characters was created. In
MonTeX, both Mongolian and Manju are entered in romanized form. The
retransliteration (from Latin input to Mongolian and Manju output) is
completely realized in TeX/Metafont so that no external preprocessor is
required. Please note that most of the enhanced functions of MonTeX require a
working e-LaTeX environment. This is especially true when compiling documents
with Mongolian or Manju as the main document language. It is recommended to
choose pdfelatex as the resulting PDF files are truly portable. Vertical text
generated by MonTeX is not supported in DVI.

%package -n texlive-mpman-ru
Summary:        A Russian translation of the MetaPost manual
Version:        svn15878
License:        HPND
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mpman-ru-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mpman-ru-doc <= 11:%{version}

%description -n texlive-mpman-ru
A translation of the user manual, as distributed with MetaPost itself.

%package -n texlive-numnameru
Summary:        Converts a number to the russian spelled out name
Version:        svn44895
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(numnameru.sty) = %{tl_version}

%description -n texlive-numnameru
This package converts a numerical number to the russian spelled out name of the
number. For example, 1 - odin, 2 - dva, 12 - dvenadtsat'.

%package -n texlive-pst-eucl-translation-bg
Summary:        Bulgarian translation of the pst-eucl documentation
Version:        svn19296
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pst-eucl-translation-bg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pst-eucl-translation-bg-doc <= 11:%{version}

%description -n texlive-pst-eucl-translation-bg
The pst-eucl package documentation in Bulgarian language - Euclidean Geometry
with PSTricks.

%package -n texlive-ruhyphen
Summary:        Russian hyphenation
Version:        svn21081
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(catkoi.tex) = %{tl_version}
Provides:       tex(cyryoal.tex) = %{tl_version}
Provides:       tex(cyryoas.tex) = %{tl_version}
Provides:       tex(cyryoct.tex) = %{tl_version}
Provides:       tex(cyryodv.tex) = %{tl_version}
Provides:       tex(cyryomg.tex) = %{tl_version}
Provides:       tex(cyryovl.tex) = %{tl_version}
Provides:       tex(cyryozn.tex) = %{tl_version}
Provides:       tex(enrhm2.tex) = %{tl_version}
Provides:       tex(hypht2.tex) = %{tl_version}
Provides:       tex(koi2koi.tex) = %{tl_version}
Provides:       tex(koi2lcy.tex) = %{tl_version}
Provides:       tex(koi2ot2.tex) = %{tl_version}
Provides:       tex(koi2t2a.tex) = %{tl_version}
Provides:       tex(koi2ucy.tex) = %{tl_version}
Provides:       tex(ruenhyph.tex) = %{tl_version}
Provides:       tex(ruhyphal.tex) = %{tl_version}
Provides:       tex(ruhyphas.tex) = %{tl_version}
Provides:       tex(ruhyphct.tex) = %{tl_version}
Provides:       tex(ruhyphdv.tex) = %{tl_version}
Provides:       tex(ruhyphen.tex) = %{tl_version}
Provides:       tex(ruhyphmg.tex) = %{tl_version}
Provides:       tex(ruhyphvl.tex) = %{tl_version}
Provides:       tex(ruhyphzn.tex) = %{tl_version}

%description -n texlive-ruhyphen
A collection of Russian hyphenation patterns supporting a number of Cyrillic
font encodings, including T2, UCY (Omega Unicode Cyrillic), LCY, LWN (OT2), and
koi8-r.

%package -n texlive-russ
Summary:        LaTeX in Russian, without babel
Version:        svn25209
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(inputenc.sty)
Requires:       tex(xspace.sty)
Provides:       tex(russ.sty) = %{tl_version}

%description -n texlive-russ
The package aims to facilitate Russian typesetting (based on input using
MicroSoft Code Page 1251). Russian hyphenation is selected, and various
mathematical commands are set up in Russian style. Furthermore all Cyrillic
letters' catcodes are set to "letter", so that commands with Cyrillic letters
in their names may be defined.

%package -n texlive-serbian-apostrophe
Summary:        Commands for Serbian words with apostrophes
Version:        svn23799
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tipa.sty)
Requires:       tex(xspace.sty)
Provides:       tex(serbian-apostrophe.sty) = %{tl_version}

%description -n texlive-serbian-apostrophe
The package provides a collection of commands (whose names are Serbian words)
whose expansion is the Serbian word with appropriate apostrophes.

%package -n texlive-serbian-date-lat
Summary:        Updated date typesetting for Serbian
Version:        svn23446
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(serbian-date-lat.sty) = %{tl_version}

%description -n texlive-serbian-date-lat
Babel defines dates for Serbian texts, in Latin script. The style it uses does
not match current practices. The present package defines a \date command that
solves the problem.

%package -n texlive-serbian-def-cyr
Summary:        Serbian cyrillic localization
Version:        svn23734
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(inputenc.sty)
Provides:       tex(serbian-def-cyr.sty) = %{tl_version}

%description -n texlive-serbian-def-cyr
This package provides abstract, chapter, title, date etc, for serbian language
in cyrillic scripts in T2A encoding and cp1251 code pages.

%package -n texlive-serbian-lig
Summary:        Control ligatures in Serbian
Version:        svn53127
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(serbian-lig.sty) = %{tl_version}

%description -n texlive-serbian-lig
The package suppresses fi and fl (and other ligatures) in Serbian text written
using Roman script.

%package -n texlive-t2
Summary:        Support for using T2 encoding
Version:        svn47870
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(enumerate.sty)
Provides:       tex(alias-cmc.tex) = %{tl_version}
Provides:       tex(alias-wncy.tex) = %{tl_version}
Provides:       tex(citehack.sty) = %{tl_version}
Provides:       tex(cyralias.tex) = %{tl_version}
Provides:       tex(fnstcorr.tex) = %{tl_version}
Provides:       tex(mathtext.sty) = %{tl_version}
Provides:       tex(misccorr.sty) = %{tl_version}

%description -n texlive-t2
The T2 bundle provides a variety of separate support functions for using
Cyrillic characters in LaTeX: the mathtext package, for using Cyrillic letters
'transparently' in formulae; the citehack package, for using Cyrillic (or
indeed any non-ascii) characters in citation keys; support for Cyrillic in
BibTeX; support for Cyrillic in Makeindex; and various items of font support.

%package -n texlive-texlive-ru
Summary:        TeX Live manual (Russian)
Version:        svn58426
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-ru-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-ru-doc <= 11:%{version}

%description -n texlive-texlive-ru
TeX Live manual (Russian)

%package -n texlive-texlive-sr
Summary:        TeX Live manual (Serbian)
Version:        svn54594
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-sr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-sr-doc <= 11:%{version}

%description -n texlive-texlive-sr
TeX Live manual (Serbian)

%package -n texlive-ukrhyph
Summary:        Hyphenation Patterns for Ukrainian
Version:        svn21081
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(catlcy.tex) = %{tl_version}
Provides:       tex(lcy2koi.tex) = %{tl_version}
Provides:       tex(lcy2lcy.tex) = %{tl_version}
Provides:       tex(lcy2ot2.tex) = %{tl_version}
Provides:       tex(lcy2t2a.tex) = %{tl_version}
Provides:       tex(lcy2ucy.tex) = %{tl_version}
Provides:       tex(rules60.tex) = %{tl_version}
Provides:       tex(rules90.tex) = %{tl_version}
Provides:       tex(rules_ph.tex) = %{tl_version}
Provides:       tex(ukrenhyp.tex) = %{tl_version}
Provides:       tex(ukrhypfa.tex) = %{tl_version}
Provides:       tex(ukrhyph.tex) = %{tl_version}
Provides:       tex(ukrhypmp.tex) = %{tl_version}
Provides:       tex(ukrhypmt.tex) = %{tl_version}
Provides:       tex(ukrhypsm.tex) = %{tl_version}
Provides:       tex(ukrhypst.tex) = %{tl_version}

%description -n texlive-ukrhyph
A range of patterns, depending on the encoding of the output font (including
the standard T2A, so one can use the patterns with free fonts).

%package -n texlive-xecyrmongolian
Summary:        Basic support for the typesetting of Cyrillic Mongolian documents using (Xe|Lua)LaTeX
Version:        svn53160
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luahyphenrules.sty)
Provides:       tex(xecyrmongolian.sty) = %{tl_version}

%description -n texlive-xecyrmongolian
The 'xecyrmongolian' package can be used to produce documents in Cyrillic
Mongolian using either XeLaTeX or LuaLaTeX. The command \setlanguage can be
used to load alternative hyphenation patterns so to be able to create
multilingual documents.

%post -n texlive-hyphen-belarusian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/belarusian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "belarusian loadhyph-be.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{belarusian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{belarusian}{loadhyph-be.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-belarusian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/belarusian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{belarusian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-bulgarian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/bulgarian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "bulgarian loadhyph-bg.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{bulgarian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{bulgarian}{loadhyph-bg.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-bulgarian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/bulgarian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{bulgarian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-churchslavonic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/churchslavonic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "churchslavonic loadhyph-cu.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{churchslavonic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{churchslavonic}{loadhyph-cu.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-churchslavonic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/churchslavonic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{churchslavonic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-mongolian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/mongolian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "mongolian loadhyph-mn-cyrl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{mongolian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{mongolian}{loadhyph-mn-cyrl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/mongolianlmc.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "mongolianlmc loadhyph-mn-cyrl-x-lmc.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{mongolianlmc}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{mongolianlmc}{loadhyph-mn-cyrl-x-lmc.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-mongolian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/mongolian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{mongolian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/mongolianlmc.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{mongolianlmc}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-russian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/russian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "russian loadhyph-ru.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{russian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{russian}{loadhyph-ru.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-russian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/russian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{russian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-serbian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/serbian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "serbian loadhyph-sr-latn.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{serbian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{serbian}{loadhyph-sr-latn.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/serbianc.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "serbianc loadhyph-sr-cyrl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{serbianc}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{serbianc}{loadhyph-sr-cyrl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-serbian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/serbian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{serbian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/serbianc.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{serbianc}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-ukrainian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/ukrainian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ukrainian loadhyph-uk.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ukrainian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ukrainian}{loadhyph-uk.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ukrainian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/ukrainian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ukrainian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-belarusian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-belarusian/
%doc %{_texmf_main}/doc/generic/babel-belarusian/

%files -n texlive-babel-bulgarian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-bulgarian/
%doc %{_texmf_main}/doc/generic/babel-bulgarian/

%files -n texlive-babel-russian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-russian/
%doc %{_texmf_main}/doc/generic/babel-russian/

%files -n texlive-babel-serbian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-serbian/
%doc %{_texmf_main}/doc/generic/babel-serbian/

%files -n texlive-babel-serbianc
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-serbianc/
%doc %{_texmf_main}/doc/generic/babel-serbianc/

%files -n texlive-babel-ukrainian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-ukrainian/
%doc %{_texmf_main}/doc/generic/babel-ukrainian/

%files -n texlive-churchslavonic
%license mit.txt
%{_texmf_main}/tex/latex/churchslavonic/
%doc %{_texmf_main}/doc/latex/churchslavonic/

%files -n texlive-cmcyr
%license pd.txt
%{_texmf_main}/fonts/map/dvips/cmcyr/
%{_texmf_main}/fonts/source/public/cmcyr/
%{_texmf_main}/fonts/tfm/public/cmcyr/
%{_texmf_main}/fonts/type1/public/cmcyr/
%{_texmf_main}/fonts/vf/public/cmcyr/
%doc %{_texmf_main}/doc/fonts/cmcyr/

%files -n texlive-cyrplain
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/cyrplain/

%files -n texlive-disser
%license lppl1.3c.txt
%{_texmf_main}/makeindex/disser/
%{_texmf_main}/tex/latex/disser/
%doc %{_texmf_main}/doc/latex/disser/

%files -n texlive-eskd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eskd/
%doc %{_texmf_main}/doc/latex/eskd/

%files -n texlive-eskdx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eskdx/
%doc %{_texmf_main}/doc/latex/eskdx/

%files -n texlive-gost
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/gost/
%{_texmf_main}/bibtex/csf/gost/
%doc %{_texmf_main}/doc/bibtex/gost/

%files -n texlive-hyphen-belarusian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-bulgarian
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-churchslavonic
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-mongolian
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-russian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-serbian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-ukrainian
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-lcyw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lcyw/
%doc %{_texmf_main}/doc/latex/lcyw/

%files -n texlive-lh
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/lh/base/
%{_texmf_main}/fonts/source/lh/lh-XSlav/
%{_texmf_main}/fonts/source/lh/lh-conc/
%{_texmf_main}/fonts/source/lh/lh-lcy/
%{_texmf_main}/fonts/source/lh/lh-ot2/
%{_texmf_main}/fonts/source/lh/lh-t2a/
%{_texmf_main}/fonts/source/lh/lh-t2b/
%{_texmf_main}/fonts/source/lh/lh-t2c/
%{_texmf_main}/fonts/source/lh/lh-t2d/
%{_texmf_main}/fonts/source/lh/lh-x2/
%{_texmf_main}/fonts/source/lh/nont2/
%{_texmf_main}/fonts/source/lh/specific/
%{_texmf_main}/tex/latex/lh/
%{_texmf_main}/tex/plain/lh/
%doc %{_texmf_main}/doc/fonts/lh/

%files -n texlive-lhcyr
%license other-free.txt
%{_texmf_main}/tex/latex/lhcyr/

%files -n texlive-lshort-bulgarian
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-bulgarian/

%files -n texlive-lshort-mongol
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/lshort-mongol/

%files -n texlive-lshort-russian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-russian/

%files -n texlive-lshort-ukr
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-ukr/

%files -n texlive-mnhyphn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mnhyphn/
%doc %{_texmf_main}/doc/latex/mnhyphn/

%files -n texlive-mongolian-babel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mongolian-babel/
%doc %{_texmf_main}/doc/latex/mongolian-babel/

%files -n texlive-montex
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/montex/
%{_texmf_main}/fonts/source/public/montex/
%{_texmf_main}/fonts/tfm/public/montex/
%{_texmf_main}/fonts/type1/public/montex/
%{_texmf_main}/tex/latex/montex/
%doc %{_texmf_main}/doc/latex/montex/

%files -n texlive-mpman-ru
%license other-free.txt
%doc %{_texmf_main}/doc/metapost/mpman-ru/

%files -n texlive-numnameru
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/numnameru/
%doc %{_texmf_main}/doc/latex/numnameru/

%files -n texlive-pst-eucl-translation-bg
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/pst-eucl-translation-bg/

%files -n texlive-ruhyphen
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ruhyphen/

%files -n texlive-russ
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/russ/
%doc %{_texmf_main}/doc/latex/russ/

%files -n texlive-serbian-apostrophe
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/serbian-apostrophe/
%doc %{_texmf_main}/doc/latex/serbian-apostrophe/

%files -n texlive-serbian-date-lat
%license gpl2.txt
%{_texmf_main}/tex/latex/serbian-date-lat/
%doc %{_texmf_main}/doc/latex/serbian-date-lat/

%files -n texlive-serbian-def-cyr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/serbian-def-cyr/
%doc %{_texmf_main}/doc/latex/serbian-def-cyr/

%files -n texlive-serbian-lig
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/serbian-lig/
%doc %{_texmf_main}/doc/latex/serbian-lig/

%files -n texlive-t2
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/t2/
%{_texmf_main}/tex/generic/t2/
%{_texmf_main}/tex/latex/t2/
%doc %{_texmf_main}/doc/generic/t2/

%files -n texlive-texlive-ru
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-ru/

%files -n texlive-texlive-sr
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-sr/

%files -n texlive-ukrhyph
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ukrhyph/
%doc %{_texmf_main}/doc/generic/ukrhyph/

%files -n texlive-xecyrmongolian
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xecyrmongolian/
%doc %{_texmf_main}/doc/latex/xecyrmongolian/

%changelog
%autochangelog
