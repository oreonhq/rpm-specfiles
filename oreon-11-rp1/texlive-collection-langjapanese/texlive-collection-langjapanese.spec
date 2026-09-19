%global source0_hash c49849ed672ba528f4f23fcf835b08d530b4f888954976ce216c45e7d2561663b972621817fc21ba97c3190f283c60b12f4683fae4d7f71181d10de64a5ae389

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langjapanese
Epoch:          12
Version:        svn76651
Release:        2%{?dist}
Summary:        Japanese

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash a756fe38499b5534f5dca964c298cab39aba071dca4ddbfa77ee4a074f56dbe865dc058c8620a828f2803307742d60f6fc6f79d85b8ce680046446b04e268181
%global source3_hash 706ae7cd16205334f28471eefcb8b008e055a755494f0bdef3a38b258af7b2d3313c58553559870830e4afb08081aae33cb54ea4956bdd0b0f1217246b9edeec
%global source4_hash bb1939b53b892744c323bd28f84cbe07d94c30c3f824e9d611f8b044fe8b9b07990fe7709607e7212ac8252d6eaef9a989447f270e26f16e074af0b9bd92cfd4
%global source5_hash 31b443d1ad05880fa5c6878fed144a2b1cf20fe855188ca8d879c5d18b7285f16dceb76b2ab7dd6be2f401b898752a674f810af6d3b9ff906a6cd75a80cf51c0
%global source6_hash dae227c586eea1b56fc88937f8a99803994622c07cf54290ca1b5ef6cbfe53ade8aec7064820044284cfd70fb6ee2ba908bbb74dedb54bf3c2f0085815c7eb43
%global source7_hash cbcda3267222cbf5c38d8e7e8ea5440b94c3d7d0ca70b4f635b0751e824c690a4d495f0906b0d646de5f1ee08c74f72482020baf99d39ad0089002d5e523ccb5
%global source8_hash a9089834348dd2ecf0670766219d129a400c337c1bc9b9c119a311576784eaad5af83ba2ef01e168b8860342a1228b7db1ad06493b5a652295e816d0a75fe43d
%global source9_hash 166b9156cd7e9f9b3e4bbc221320d5e918559ab261fcd55724f9f01e10fba10ec710a0227cda5ec00b605e6762cc32da4fe8508d2dc963669c5be5178b440446
%global source10_hash b81a8b1698a6a4cfaf981c813d5a534c0ca2c1dee9a90c6c6b6edb62e4b54c8284f9b73307cb17507910d53b4068a6cb21389a08a5dfd45188136c292bb8b2c8
%global source11_hash 258c609a656eeb55d4c724646e67e3b58d0e2d20719f595c8d48cf9a6d7cdb5d12771b76cf8d5af20db52bdbddcf51a5bc133433b566ff5973e3ece5753bf55a
%global source12_hash 4adcc20af1052bf1539f0f57ccb0b9a824942f077094ce9a6c28abb63362c3ee35b07debe92b3374ce4b41ab84667626394bbae95faa49a211e7d5c5556ff5e8
%global source13_hash 45b8dbc8b3bad2c67b8727a9cfc21d328b1150334b2e379fe004980e2cfc99f7100310be954af95c08c4766120126bead802d754b2761f6b51dfc1e3523379f8
%global source14_hash 7998dc34a7d46ce1df7a8faa10b199b80dd23a1d198f78ebc791a8f0a0e15b3bf65c69a06eb42729e7d622deab5a118d84bd767ba9cc1d840ef87ae8103c4ce7
%global source15_hash 4c23b19484e45db701f1a04595e8b7cead08d6617c5caa98c6b3f78d3ebc4d67da8dbbafb435527260ae27531fc858ac87b2d95a8d3c6112719b236184ff663f
%global source16_hash f356f98b93c0330c611ae2ae5b0c7df7f4659634456243655e8a861a363a1c6c631c6f0edda9d805cc08e9e7e182691c8372a9ddee576f270c5440133c7468ee
%global source17_hash a81a45f95bd6d8490442f32c52a43e79709037585e6a84e5c520a4d6d127c94266a96c2b487e14b9e0e0aeedfea91fad1f1c5c71f1625405f955c2aec7371a7a
%global source18_hash 6d553adbc3efe4ae48b3cdf837d12ce58e7cf7d03f0ea4385082fbf6ab9a95ed265a23455176b5fefa64ac713d66aea89d1603bc3a47828843a9c292b5fc97f7
%global source19_hash afb7a474d05b9e8b0596625f96969b11cdfc175b9139ed875367c85021a4c3775a0e2cc7b2bb4dab358ff2ba432bca6cf4c4081b36bee6c0a2ac6411c727b7dc
%global source20_hash 03e3af87228d4e942c23aa5dd7712e4075ada1b1bbc1373cab56e1969a2a9086ad806db9f6a1ba573dc36f02174e06a940cf0898ccf54224b1fb3ced357ec4ac
%global source21_hash a20804a956a7439241f0cf6eaaf70ad8d5e71c76b58c9194ae5e8d31095a023e5290ac01a71834bcd5eab409aae829737b83534875d0ce7b45a8b9c91a62899a
%global source22_hash bc34cb4dc94e0c2fef1ec1c032c8e79e8e8f887a84ad9ba035d005eb886c6906474eea2837615f63d4bc601672fb22519f2b1024671eed0c6d85e2bcebaad9bb
%global source23_hash f4e1beed0e23b3951af97ef873508e4243b340128ca453b13c792971e7cafad7c556841f5d6f852cd1d0b468deadb9293780baa8ea852c30cd6ce491da63c6eb
%global source24_hash 4d283a27905d3f0aec5ed627d960bdec7a1fd6af903d62de8bf27b35d77f8319b19c5e8fcdf1ba00bdfefcf97ac40374781d1c02fb5187871d9024fc4200ba35
%global source25_hash 2fdb46a84156058b0818875727b37ee874910c4b8dd4d1aa80f70a98d3ae3abdfb363881d07a0a0735fec5ca87158bd0fc7552544867e1a9c9783bbd4a65c027
%global source26_hash 7e289a64afeb7957e6020c8da1e6f98526a26fa901a459abe07bffc82cda0f4f29a5fc1eb250dbcfe0319ed90292c2fef40be6801b9c53ece0f9a75419491571
%global source27_hash 848cced813870a2b5750550e05fd6cdaab2089b6ff1317b0585e8e6e19fe5e4312b1853765b3285baf6b9e6e75faffbffc10df312ad192e6c2dc2a5f35f9dc1e
%global source28_hash 8b0b28c3bf796ba4c4d0c36200f11122c24c2973eb76735e824ba953de90c8f1aa0970b478f995d5cfbc87abc0be503957bb729154aef3d0664325cb583cb675
%global source29_hash b7f8b1740836e2de54caebf4276ccfa27a6a94891bb1d9076ebcffee32838eb81936dfa0776f1b8ee928443a0697863187e4605179d7aa871ed7d41e9ad4b649
%global source30_hash 92b85604484b0c8b7911064cd0549be6020a289f24cd471b2be136b43d944d48146dfbcea3084a274560c6a9c35a2f75cbd27f8b9ef1c5e28b906fc3d9e19131
%global source31_hash 9d81bf3e6899a3e19cb4cf72de8cc0d99e402d95e83e580adf8fa4c4e7d51863ddd9cdc395fb6dddece8e7e0e715651fd64dd4e64fc26ebf3433800edb21e687
%global source32_hash 6355d5d778cf6d59278de4bd6c3fb4959c5540f0e5a4459683f6d30f924b8bba8e8c7eaaca1e631180288befaa8a5a3f29ac70276cd4fbc4d91e8e9b65f5a9dd
%global source33_hash 6c3c69618330c4478b044cd144902553f47cf0ab9e12c32414df6b07ac7843b93d56d49bd2799cca3a20cda60327c3008140f62503f8d0e09cab7d19927a3ab4
%global source34_hash a8e0acd843a19f937635d5cdcceba6658a1969243c3e4198c49948d465bb8d25bb57b18885dfb97e97d86ec06307f42e91da6a05fcc896ba0df5fc279001d200
%global source35_hash b89bfb352264a0a65c38e18fb93b5cdc8d63107e2e5385a1fdb54c9f38f0e10c17fad275c1e393d6f826ae3f9e7c8a7690b820a45141af8f589bdc56a9057ea7
%global source36_hash faebc75a894b7ab58064488dc0b166095bcdf82937d61643fd9e8d38c1ccb586355d5bac55ea4dd6b4cd039847a2908db4f1a2e9c70776afe39619fc26b12ad9
%global source37_hash 039f061ee1d1bd8dd2b1cecc5df926930863df2468691fccef999ed23c1a8d5a6b8731acadbfac4ae30937e35987056e976e6bce92e9b687d019fdc65523e5ac
%global source38_hash 5a3a5c6e7b1aca09e602d0e0b76bcb59b53acb564e3b66ddbd45d2bdcda948c62dbfdd00f70fe670338d96d15273f9585143ea7595a543ae62ffbd2ada78212c
%global source39_hash 58e37cde05fe0cf26171f526f7fa524e4e8af911569746ca1db1528264b369dc8733791b93f426e1691b54eb10aaf06a15f6bfdbb4c6b936c4c9f76f05ccd4dd
%global source40_hash 929c2d95d8ea2f04d336d1da4e5926d8edfc0ed8119b9b690c37607407ba19b804a9cd03a4127a6591c2b8752e45834a0eb038826694e8ad847b4e00c52fc26c
%global source41_hash 44103e14792e8a7559caa1c907e4d467c5f71036c01413ec96ecc5e7971b9abdb5f3547c88a8893e7d1848d8353acf5fa5be1e2320c9c210e6a3b316fff9dc01
%global source42_hash 735987e66fb9ef3f3def1257f670b17e9e8065d9a11d9cc541cdfa6ef2a3dfbacc7fad593b3b51fc9e0000a4d87f8429f977d7838833797e2f36ed7810179b52
%global source43_hash 9974b9964e8e3307492752de1b31ff2c2a7bac1f3919905cae7ccd425c1bf227acfc67ddc078330ab8d08a7b0af643fba87997571a814ff146c45eb3e37a12d1
%global source44_hash 7077160a09ba3a16f1710778bca37399c1af4e8e2eb5f933ed647d12ff877735502021aaa5e2d1c89437c97e562f7be83bb7de8a47a3449d7c94a9f2abd4d616
%global source45_hash 54549be56a29bb91aa48c8487a8b5527ffeddba2101851670cd75d0b306676b2518aa8d89e3a0beab9963334357d66a3d774ca6d6fe4f5c96739b38dd626d3eb
%global source46_hash dc01af9b74f7e20803b5aa9dcaff01f80d3d831ba89925191f9b9ca3b6ae86effad75086a58c6e1e0155d91fa4d675b0a6230c15e60defef9e4b6f5636b3d886
%global source47_hash c5cd76ddebb3935830c943f654fa30a4c2dc913cd838a9e4748676aa10d0afba09ce49d1796b148882f0f5f5ca095fa0bd3226eb34906d5ea0eca37b3e653775
%global source48_hash 7bc52847fe21879614ffe673ebec74c735c70e07d63649def00f70d22db80faa920f0764f76c5094ef982abbff8202ca55410ee92d033c45ec43fd25adabb23b
%global source49_hash 1bc4feaacbdd33ba6f46c699969638cdc8a4b962287332476d0d163a10141136f9b913027ccc3418033dee0862d5e572957dbe07d47371c1d932103958151e27
%global source50_hash dec0527223fdb0f897ccf54e96691cd68b933ac61de4c036e21fd35bff93d32766444fe6971492ce64328f92621bd2949ebb669ab33b6b6f4ede88280351292d
%global source51_hash c53cf11bc81d9a8f5aa19c264a1970d4819400ceaffa20b688d0709546113f932b82b6b6d12cf9fb31b2a3d2c0d45b6b33ee3cb3bd0060c961360389839b1475
%global source52_hash 35245333f0ad08ba0772aff54e5ed1b252ad1b1d298c55934ade4a0e33dec29fc67adfebcce22f10b61b9469a2a2d208c4b9977519271457f1538c4bba8bce24
%global source53_hash cfa07138896028186773970685309030f587fc39f95b2fb0d993e2827a124ae4172acc91f9276ae65b32fdc614cd9525d557505b2f1fc11750a982a5c9cebb42
%global source54_hash 5bd0133833979011ea643e8b54ad7b0e116abf1dab0ba83656168afd35d397c19c0486efb4e48111a9bb009c5061bc94aee69769cf519b0eb0aebb168679ac6e
%global source55_hash f1c7eaba6f87d61b46ede616a9b9fa7edc7d9f0fc472ade3bd839cb10b1a0893ddbbf035668cb301cf98fa9e732499a12b19fa8b46a49d413771b533bbecc2e0
%global source56_hash da6f2147763c49489f52b5d62581488c60c25298f72428a2560b66765a4ffed28eb5d4e5a5a9f8cbc25785a07e881e4e2c08c26277b5505ee76450f52821ed65
%global source57_hash f7aed125cda224a131afa7dbca171ad752cccf4e895fd8bd339a13692111891ebdacf870760eb7ecec2fd6bcc22e7eed01939f8134b40d76b71806f7f614caac
%global source58_hash e53ea28beb8ac55a76234295aec77061c27c5031e1902566962782a751c21ff1729008a9fc810695ed44ce760ea3f8c2bc157fde551ead058da938836d3633ef
%global source59_hash 33d70506034b593bc6221a590036f2ad73ff8cbae6f898ab129654d9fe6cefe64281e468493432aed4a2dce1c7df3d982ad97b357ab657b73f6e97ec85bc3c1f
%global source60_hash c9b858d759611cf8a55afbf0f1471607ac00264c140c4172a183968538cf43bb1dbe56fb7b1909f77a3679e8a2ae15dad47e4799a5dc3bb00948fb2e2a8586c0
%global source61_hash 3ab48be24aebbaadbdc44b06fa627683bdae8c9a81075506c4cae7b6a8cb623f0b9dac04aa598b92f5db2fb2fcf9f25609fad7fd7de9048414bcee991978fb16
%global source62_hash 86a6d325c9bfeeccda2b0f134fd6756fc68f0d529f56dcd3f7df33d9ce02452bd71a8a55faae8644d71e8602b13f325e6a5f6670bf3e65d5f3e6ebc3ad97796d
%global source63_hash 84e5c54c731976ec8b5e2bd105856299bf170d203a490955bc11429d142fccac509062dd0efded4e033ad590a3a8b0a0f81e6c675c4af57b4e2370328f7d1362
%global source64_hash cf0abee615f54cfd47727cc22ce350389fd7a41aab8eb09d11150078c2fb0269efd776ab7431ef323cee0d29ddd42f0e6bd9ec9805b9624bf3042789d20a3ccd
%global source65_hash 1a52b61f409a249e7a283750ddeb8a5208e6ef4160cf5a3f7168e664d087ccfeacad92fc31ad17cb26e4b039785bf40be612b3251430e0479e135497200482b3
%global source66_hash a80a73d76d8e41f617e0ef1fdb3c4f7d8563880adf1b228401d0db5d848052396bd00d4ed25e761b08e0a6c86f10c5259161204c3bddca59298c3e6009e8025a
%global source67_hash 3ab3060a34ad3fd6820becdf0291b6c0952edafa6592bf73a579964adc1f7f59d04294b4ebb25af5f6ffc5df6af213460a53e42d6fd7ecfedb4be54fb5f6fdcd
%global source68_hash 642c4407d8c3f9de970864b96aa3aade68f0d01c30c7b209f196625bd45ddf4d3af6452be6fbf5cf68626493db05536ab29dd04f8285ee2c8b729619467d52d1
%global source69_hash b6469be08484d7662e4e1c583423bdb40c132a8d519f624e175d2ccaeae6a4c35a19b93d8126a5222c11eb29058a9a90cc35ec6c30723efb13734276742a03c4
%global source70_hash 402da4b132077db3a66d29d44fdda78e8c424dc628d982e6007376bcd03bb88760279f1e500ae620042f3a48313b3f5c30d4afec7722ba4486d5331d4a285966
%global source71_hash 2a41eafc5f89fcb41ef69bb5575d43b62b94f14265b01a9f237b690933fee0be45c5c7c28629ff974509693e33c9040cf1cf873a07cdf2a20f1112f5108e1993
%global source72_hash 85db5b58c56d16d2cf71fc79078650d1b5c7fbf5305f38fb17fee97016017236faaca29a2495ed52d270a5f2a1fefe6bfee623dea75e9c29bd3fbf96b088f0fb
%global source73_hash 65e14cfa366660dc409ac9a2853da534f262a08bf0d279b507a48feba6df88968bbe113117d1e1adc2e49efff3996f1204f19ceb882a842eef5520418d3ab2b4
%global source74_hash 3c62ce192b2af77f947c25a2bca3115acbabcbb455b80397a47afbfa2a97ea3bb24e9582ed300d41505a1d170497726e8aa8b1628d2cca2b089bc4cb5ca1a26e
%global source75_hash 44e4e4a8b61f3cca373606f30e28cddfcd6c01c9eb7572db4a17cfb6176215013264c7e52120e4c8b6eead0496c059fa5dde0c3d5dce93b7fb8e04e19dbeafb1
%global source76_hash 285648eaf82a4cd458cfdfc0fc6b1eb5fb2d501ec76ddcd73a6ccc481be80f007490e74faf410ed8a45eaea94bbc69b4a7930dcdec7706a88066c346814467cf
%global source77_hash 82bb6807d3310c6e4960ee6b4fcb285345c75dd792471849597cdcf9b7a3acba25bc7d7713f69860a3d8ee26e85d9c44563899725fac9233b2ba1fbf7ce8149e
%global source78_hash d966a9c102be5350a8301826ce0a20cdcf2184eb136a9d4d203dfcd65cb23879b129625a049f5979b79d07f63cdd084527bcc9a14e0b467bba526dfb75aca6c9
%global source79_hash 64d1102dfa0c264e5f73eaf1ec77d62f94e8be5c1f9d26f0e9ef78f4f177616787644ef6d8c019d7c728fdee72784d9b374fccea8a17b938b18b280ab038033b
%global source80_hash 89c7b6e045fb5981dcf76e3bb4f799923522bc24f3a90b621760c1eb087143536dba4e1bfae289561fa543c48d5eb44e5c9a587833394e0a95ab33a62afee3d7
%global source81_hash 58130e996b96219c04ae342cb3534b7dfd446fbd32dbf9af167c8b499ed6a31fed4bcf507ce97145569d60f5f54c0f0048c63dd4e5b789af8e94ae589f667175
%global source82_hash 6be03a9f18741e16104d620effc7c0669e12ccde1aaa7d4332ada2fee95ceb1a6b30db4df41386995367b565b437174c0d4cae6e330c8181ee47095fb9bd5a5d
%global source83_hash 69a7e564464d8b1c31474ca37b5e9fadeb4c2d4f4d25dad5f884317b226c6b7f8f467cd1809e1330cb64fe2006f1ab397cf4f163e469a14fb8de5b778dc70c08
%global source84_hash ca4690e0ce37561dcb877d17310f498b5b528cf6892beb075b4ed87f1a4432957c2ac56ad29f66da1452794c587f2d9343fdf7715c670ac7c3f7880f620f698e
%global source85_hash 152ac93c6e1bf07d90434581a8891f293527d4ff93f7d439e7e15c99d53b0cf43872c9f8a6935fe314614b9c3fe3cbe7bb3dfdbba486dc7248fffc60742f37a0
%global source86_hash 30c8b730e095662c5d751296b463417610dedbc34d29320d24eb0517ec14366864dc4cef9295ff5f7eba43a5c88be4dc3d2d07ee8adbe1421396d907971ef252
%global source87_hash 3d1418d833fcd878309a18ffc6e657b286b16ab3223c43131a2c022496b097c8c509b46eddebb11d408f9133afac5575b3471c631eb7222ad521e8e5c829bfb6
%global source88_hash ef0f2f55858364f3d45e94677ba66a90c22bd2095ef78ead503fdc0986e1fbbfb72fac25b2d096c699208f672da63070269bbeacb46255cefda611c8c010004e
%global source89_hash d3448577c6cabe34b2d3e0614c2cceddc1d049c7f111e29d8b63959969033d0213af2de6d9eaeac5d1a4413a65a24054d69f7947655cdc8ae31b3d27b25b740d
%global source90_hash 1409c7311eaa82811236d869b04e9f55fa2a96804faacef4820072a4813055e70ecce0e8c155ec19016f1ed4e57bebe0b362c5457d1258f317a40fc475d42aff
%global source91_hash bfe47b947a915099de15e5519a3aff201b327c31d29c1966d4fd3e9b73581792d918b461ed1944aaf5e8a5eb7956c38579a3fd972f189b1e3abb903c7c904cbe
%global source92_hash 178650f001ac7e9e140ec4b3e16949dacbf10a10bc09c191b3a4a9edaf553e017d5430cb0780dce46bee787c319980ca644960e4720645e464ce262043ccf8b1
%global source93_hash b843ec5d03a6e466e61dede7ed516debd3852620f7c4cc3dd2f2eab2cc092d035e3b370bac579004d89c6a98557774a54e4fb6efcfa70444691cacead570d3c7
%global source94_hash b937359bde7ade3645edb6435a824ee6af66e51e7cb518694706224e63e4d92391911f01745d331cb92e62c34c085aa5f284babacf6f7ab0a0474cbf06b00859
%global source95_hash 85b6422630754144e4f9c552899e588f1650af2837cf88e8f47106e2919bee8dd956002e102f83dd76107edb0e61e2a6d4ebfaaf6fc06289942fdb32385454ba
%global source96_hash d625f45f7211eca1152a16814ce87814cc19eb7d6646d4f66971eb08eeec50bcf91ddcc253f4ffe24418a3e2a989ce10c03a3536730ac286980742cdfa22fe67
%global source97_hash 3a07313f79f31d09bf96c78a574d00d57641df75b9eeb89c76425ee3d6cd51d1e6ad6574fffdeb834d2bc2fa8c41511561aec34ca6be2be43d55da6227d19a19
%global source98_hash 5007735efdbcd5f8eb59b712b5e0ba5a3e3fecac19c65afb8526c3590fa17f3349ae4e42284cfecd1cba915962467e2a4ae394abc0c56c75c84b8c5673ba3699
%global source99_hash 56289dc2aade8c7a14073689f7beea8b6d689d36abdb7e08d07bd1132e0f780fbe3834c6c879e6930768b26fa712e80800c5c80eeae2fab2daa3bbb54006ad93
%global source100_hash 80efbc3f121a8ec072b4f93b3c385d8110763658cd3643c63b9297de1f58efb3c8090d84cee756b12fc1afd4105471cb98ab256627c9405b6ff08c2aa8eca14a
%global source101_hash 0a541a10157b1a820b79d2a4c38123ba31490e2ee77e2e440b42a6aff1468a44821d1760b4a6c329c483d2363ea8af897863ba30534954afe90acc55c53c7a8c
%global source102_hash fd8eec45d51a7171d1acc55309a999b7a03b8cd9535380cea49391996f0dfb4b874cbd6f97b91ac5ee46c0fd31a351091f7722103b4cc966f18db27ac48bcc07
%global source103_hash 0a7e65038ae6056e37c5ac99674301aa159807b5a883fd6559d4fa45d0e2c720e256fb3bcd69db1f2297f17026dd6310219c9b24e1f016f89f55f16e6923fda8
%global source104_hash bf58bc7dc12375c48cdef98b552290cb360f1c81641df61585f7fe234585b2cb486dd0a0db31ba3681a9fbf2250b84de190910c70e0750955c4c0e0980c3e3b3
%global source105_hash cba2299b5a4639149e616628a7f7ff371ab05c78863fd2e4446f95ec5cf7dad8ea0c6939009c556e85ba7dfff00a18a9bef61709ee3175feda459a221333ef1b
%global source106_hash 4c5d7676974cd899a348f4f200f5f9f635251591abf54627f5dab264b1fc8519b3b96cfa3e77cd11453dd4839940ba9a0ec3f9988330cafd4008bed856487f1f
%global source107_hash 2dab3f35ae6d3b17bd126eff7fbf910c2c71db22a57e7fae03ae7a14d56185fe6e380372a65d384d6ebd4dcf5082bb255b1a9f243b51869ab64ff5e4db53a921
%global source108_hash c8df76e28d3d403e598a17dca53442a5aa57100caa32e202abe5b4a557a6c14edc214d70f5be6e3729a482e416f8659f3f981696c6336c26a1aa485013fbe938
%global source109_hash 34ade4c0b4670328435a5146ee9f3d9b2bd65137878d9e9fcfcced053045cad8d360bbd09cb4108c8c9a9806835b90cd36fe2ba7b5f809ab185b1b975f6f2d40
%global source110_hash c93ab8b351d3786953f20580e5dd3e123c4a7821da6fc01db5fa19135fdf08adc949435c34201c433a3b42e1cf6bf1d236fe8b30b6b6db0f0cbf719004036403
%global source111_hash 8c1022c0ac5e34d54c3e296b8605943283bea872473cb51414f28fd7b2af428f5b71dcc6656ecd40d73943f6286a18bbc48a0151fca525561ac5c0fde6ba834d
%global source112_hash d9717a1e2d7626523cbd907abf36fc422368c8268a058c6c2ac0a5703ab07b73a8b427079d98b7222de6ec4238cfb5152cc0b8b29e3d3fd8ebf19bf2652b7c66
%global source113_hash 158bbe704098584c52cdb99109e22a73ba584638374c1ea82a1e74d111be0be2e018c0ce20e03d4f8f5afd569f6e001db2b606040b1823646f0a393dbe87dad1
%global source114_hash 5e66867b24ea4f2aa30bb5397e2d3379b590288abe2f048c447ccf20a8b37e90138d939f504cc3339b6bce88dbf9b1891e510f9644306576053689a0dbd31451
%global source115_hash 40a54fb7ac8c6dcae6d747eb0005894b2255dba29d41d41051e50df369054dffb8e5cdf81b4153ffea3e521a29f04caab28b6dd53eb173677d4af86749b81e85
%global source116_hash 3e30ef7f14bb136c8ba3029077502f4c854c6d231e4776a412a0c02926d9475225c54af2d897445506e5cbf719ef37177898798513db5108f5a5c96c10ce10f2
%global source117_hash 1974cf5e8ba3989e72a59b250012b880da357d08756a2a13dda7fad56623a3bad4b5b2d16494db51a6cef924a1e6b872f8fd59a39d62a792f6e15a3497c61904
%global source118_hash 358149c060042968eb11748e778499c419eb68419a86842a4228c18b95cc1c474095d9ce75885bcf1493242fa11849bd209a7e0c21f4cfdfa09ebc3ebeaf0021
%global source119_hash 94089a84b829692a9edcb101e37655c039d86404cc7b0ec803ea955235233a1e3e2ae6f7a801190b7f33da436d53ad7bdfbe7b58eea1a75f13eaffabbee4f497
%global source120_hash 2d603ccfa92e8ef9abe91f5afaf490c7c8476061679f7a54c22879bb90b4d874f9e0e533e25aafb94fee2ff512f689ec96d25ed7ed42d0ae90c5e05985daadeb
%global source121_hash f9c35379b396dfb563c66a05d200c405f03de96e22ec94de3a9f0c99ada057db21d31b43d59391bc0175479b5f150435f8e704fa40f6b58f2c116bbda3ec4603
%global source122_hash 2b2fb15aedf51efd57a685a9223c93b2088aef93298f174a1e362ac75bb3e30c6fb34807dd136302f82221430e7c9b3221624a0766ada23e40c5feea8aa76a21
%global source123_hash b7aec320306d9420aec3efdb9fa01d31a4632ca0ee66193cb377948ce183abc638f1c26922aa0b33eeab6650470f622c43e2f386cfcb925a2efca8fcfb7e9d63
%global source124_hash 7ee5c9b62bfec4c4526fe7ef28bc63cb1ec5acb629c51f3c3b3b321dc89e5611af51a6365cb7706acf2972a4eccd1b78b7033a69ed3921a8d801110c1bb54fb8
%global source125_hash eb2c8c0d6f627be053570aea0c3743f13f0901243eab248f762fb3c09ed8bc427c7f9d267b949f4f68328c7a5fb9f83c3a585d70ba0e4f084277f17f80597699

Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/collection-langjapanese.tar.xz#/collection-langjapanese.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ascmac.tar.xz#/ascmac.or11.tar.xz
Source3:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ascmac.doc.tar.xz#/ascmac.doc.or11.tar.xz
Source4:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/asternote.tar.xz#/asternote.or11.tar.xz
Source5:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/asternote.doc.tar.xz#/asternote.doc.or11.tar.xz
Source6:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-japanese.tar.xz#/babel-japanese.or11.tar.xz
Source7:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-japanese.doc.tar.xz#/babel-japanese.doc.or11.tar.xz
Source8:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxbase.tar.xz#/bxbase.or11.tar.xz
Source9:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxbase.doc.tar.xz#/bxbase.doc.or11.tar.xz
Source10:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxcjkjatype.tar.xz#/bxcjkjatype.or11.tar.xz
Source11:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxcjkjatype.doc.tar.xz#/bxcjkjatype.doc.or11.tar.xz
Source12:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxcoloremoji.tar.xz#/bxcoloremoji.or11.tar.xz
Source13:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxcoloremoji.doc.tar.xz#/bxcoloremoji.doc.or11.tar.xz
Source14:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxghost.tar.xz#/bxghost.or11.tar.xz
Source15:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxghost.doc.tar.xz#/bxghost.doc.or11.tar.xz
Source16:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjaholiday.tar.xz#/bxjaholiday.or11.tar.xz
Source17:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjaholiday.doc.tar.xz#/bxjaholiday.doc.or11.tar.xz
Source18:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjalipsum.tar.xz#/bxjalipsum.or11.tar.xz
Source19:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjalipsum.doc.tar.xz#/bxjalipsum.doc.or11.tar.xz
Source20:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjaprnind.tar.xz#/bxjaprnind.or11.tar.xz
Source21:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjaprnind.doc.tar.xz#/bxjaprnind.doc.or11.tar.xz
Source22:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjatoucs.tar.xz#/bxjatoucs.or11.tar.xz
Source23:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjatoucs.doc.tar.xz#/bxjatoucs.doc.or11.tar.xz
Source24:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjscls.tar.xz#/bxjscls.or11.tar.xz
Source25:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxjscls.doc.tar.xz#/bxjscls.doc.or11.tar.xz
Source26:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxorigcapt.tar.xz#/bxorigcapt.or11.tar.xz
Source27:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxorigcapt.doc.tar.xz#/bxorigcapt.doc.or11.tar.xz
Source28:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxwareki.tar.xz#/bxwareki.or11.tar.xz
Source29:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bxwareki.doc.tar.xz#/bxwareki.doc.or11.tar.xz
Source30:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/chuushaku.tar.xz#/chuushaku.or11.tar.xz
Source31:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/chuushaku.doc.tar.xz#/chuushaku.doc.or11.tar.xz
Source32:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/convert-jpfonts.tar.xz#/convert-jpfonts.or11.tar.xz
Source33:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/convert-jpfonts.doc.tar.xz#/convert-jpfonts.doc.or11.tar.xz
Source34:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/endnotesj.tar.xz#/endnotesj.or11.tar.xz
Source35:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/endnotesj.doc.tar.xz#/endnotesj.doc.or11.tar.xz
Source36:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/gckanbun.tar.xz#/gckanbun.or11.tar.xz
Source37:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/gckanbun.doc.tar.xz#/gckanbun.doc.or11.tar.xz
Source38:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/gentombow.tar.xz#/gentombow.or11.tar.xz
Source39:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/gentombow.doc.tar.xz#/gentombow.doc.or11.tar.xz
Source40:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/haranoaji.tar.xz#/haranoaji.or11.tar.xz
Source41:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/haranoaji.doc.tar.xz#/haranoaji.doc.or11.tar.xz
Source42:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/haranoaji-extra.tar.xz#/haranoaji-extra.or11.tar.xz
Source43:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/haranoaji-extra.doc.tar.xz#/haranoaji-extra.doc.or11.tar.xz
Source44:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ieejtran.tar.xz#/ieejtran.or11.tar.xz
Source45:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ieejtran.doc.tar.xz#/ieejtran.doc.or11.tar.xz
Source46:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ifptex.tar.xz#/ifptex.or11.tar.xz
Source47:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ifptex.doc.tar.xz#/ifptex.doc.or11.tar.xz
Source48:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ifxptex.tar.xz#/ifxptex.or11.tar.xz
Source49:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ifxptex.doc.tar.xz#/ifxptex.doc.or11.tar.xz
Source50:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ipaex.tar.xz#/ipaex.or11.tar.xz
Source51:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ipaex.doc.tar.xz#/ipaex.doc.or11.tar.xz
Source52:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/japanese-mathformulas.tar.xz#/japanese-mathformulas.or11.tar.xz
Source53:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/japanese-mathformulas.doc.tar.xz#/japanese-mathformulas.doc.or11.tar.xz
Source54:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/japanese-otf.tar.xz#/japanese-otf.or11.tar.xz
Source55:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/japanese-otf.doc.tar.xz#/japanese-otf.doc.or11.tar.xz
Source56:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jieeetran.tar.xz#/jieeetran.or11.tar.xz
Source57:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jieeetran.doc.tar.xz#/jieeetran.doc.or11.tar.xz
Source58:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jlreq.tar.xz#/jlreq.or11.tar.xz
Source59:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jlreq.doc.tar.xz#/jlreq.doc.or11.tar.xz
Source60:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jlreq-deluxe.tar.xz#/jlreq-deluxe.or11.tar.xz
Source61:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jlreq-deluxe.doc.tar.xz#/jlreq-deluxe.doc.or11.tar.xz
Source62:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jpneduenumerate.tar.xz#/jpneduenumerate.or11.tar.xz
Source63:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jpneduenumerate.doc.tar.xz#/jpneduenumerate.doc.or11.tar.xz
Source64:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jpnedumathsymbols.tar.xz#/jpnedumathsymbols.or11.tar.xz
Source65:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jpnedumathsymbols.doc.tar.xz#/jpnedumathsymbols.doc.or11.tar.xz
Source66:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jsclasses.tar.xz#/jsclasses.or11.tar.xz
Source67:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/jsclasses.doc.tar.xz#/jsclasses.doc.or11.tar.xz
Source68:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/kanbun.tar.xz#/kanbun.or11.tar.xz
Source69:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/kanbun.doc.tar.xz#/kanbun.doc.or11.tar.xz
Source70:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/lshort-japanese.tar.xz#/lshort-japanese.or11.tar.xz
Source71:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/lshort-japanese.doc.tar.xz#/lshort-japanese.doc.or11.tar.xz
Source72:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/luatexja.tar.xz#/luatexja.or11.tar.xz
Source73:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/luatexja.doc.tar.xz#/luatexja.doc.or11.tar.xz
Source74:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/luwa-ul.tar.xz#/luwa-ul.or11.tar.xz
Source75:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/luwa-ul.doc.tar.xz#/luwa-ul.doc.or11.tar.xz
Source76:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/mendex-doc.tar.xz#/mendex-doc.or11.tar.xz
Source77:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/mendex-doc.doc.tar.xz#/mendex-doc.doc.or11.tar.xz
Source78:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/morisawa.tar.xz#/morisawa.or11.tar.xz
Source79:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/morisawa.doc.tar.xz#/morisawa.doc.or11.tar.xz
Source80:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/outoruby.tar.xz#/outoruby.or11.tar.xz
Source81:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/outoruby.doc.tar.xz#/outoruby.doc.or11.tar.xz
Source82:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pbibtex-base.tar.xz#/pbibtex-base.or11.tar.xz
Source83:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pbibtex-base.doc.tar.xz#/pbibtex-base.doc.or11.tar.xz
Source84:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pbibtex-manual.tar.xz#/pbibtex-manual.or11.tar.xz
Source85:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pbibtex-manual.doc.tar.xz#/pbibtex-manual.doc.or11.tar.xz
Source86:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/platex.tar.xz#/platex.or11.tar.xz
Source87:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/platex.doc.tar.xz#/platex.doc.or11.tar.xz
Source88:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/platex-tools.tar.xz#/platex-tools.or11.tar.xz
Source89:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/platex-tools.doc.tar.xz#/platex-tools.doc.or11.tar.xz
Source90:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/platexcheat.tar.xz#/platexcheat.or11.tar.xz
Source91:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/platexcheat.doc.tar.xz#/platexcheat.doc.or11.tar.xz
Source92:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/plautopatch.tar.xz#/plautopatch.or11.tar.xz
Source93:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/plautopatch.doc.tar.xz#/plautopatch.doc.or11.tar.xz
Source94:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ptex-base.tar.xz#/ptex-base.or11.tar.xz
Source95:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ptex-base.doc.tar.xz#/ptex-base.doc.or11.tar.xz
Source96:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ptex-fonts.tar.xz#/ptex-fonts.or11.tar.xz
Source97:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ptex-fonts.doc.tar.xz#/ptex-fonts.doc.or11.tar.xz
Source98:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ptex-manual.tar.xz#/ptex-manual.or11.tar.xz
Source99:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ptex-manual.doc.tar.xz#/ptex-manual.doc.or11.tar.xz
Source100:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxbase.tar.xz#/pxbase.or11.tar.xz
Source101:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxbase.doc.tar.xz#/pxbase.doc.or11.tar.xz
Source102:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxchfon.tar.xz#/pxchfon.or11.tar.xz
Source103:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxchfon.doc.tar.xz#/pxchfon.doc.or11.tar.xz
Source104:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxcjkcat.tar.xz#/pxcjkcat.or11.tar.xz
Source105:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxcjkcat.doc.tar.xz#/pxcjkcat.doc.or11.tar.xz
Source106:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxjahyper.tar.xz#/pxjahyper.or11.tar.xz
Source107:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxjahyper.doc.tar.xz#/pxjahyper.doc.or11.tar.xz
Source108:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxjodel.tar.xz#/pxjodel.or11.tar.xz
Source109:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxjodel.doc.tar.xz#/pxjodel.doc.or11.tar.xz
Source110:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxrubrica.tar.xz#/pxrubrica.or11.tar.xz
Source111:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxrubrica.doc.tar.xz#/pxrubrica.doc.or11.tar.xz
Source112:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxufont.tar.xz#/pxufont.or11.tar.xz
Source113:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxufont.doc.tar.xz#/pxufont.doc.or11.tar.xz
Source114:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-ja.tar.xz#/texlive-ja.or11.tar.xz
Source115:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-ja.doc.tar.xz#/texlive-ja.doc.or11.tar.xz
Source116:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/uptex-base.tar.xz#/uptex-base.or11.tar.xz
Source117:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/uptex-base.doc.tar.xz#/uptex-base.doc.or11.tar.xz
Source118:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/uptex-fonts.tar.xz#/uptex-fonts.or11.tar.xz
Source119:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/uptex-fonts.doc.tar.xz#/uptex-fonts.doc.or11.tar.xz
Source120:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/wadalab.tar.xz#/wadalab.or11.tar.xz
Source121:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/wadalab.doc.tar.xz#/wadalab.doc.or11.tar.xz
Source122:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zxjafbfont.tar.xz#/zxjafbfont.or11.tar.xz
Source123:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zxjafbfont.doc.tar.xz#/zxjafbfont.doc.or11.tar.xz
Source124:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zxjatype.tar.xz#/zxjatype.or11.tar.xz
Source125:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zxjatype.doc.tar.xz#/zxjatype.doc.or11.tar.xz

# AppStream metadata for font components
Source126:        haranoaji.metainfo.xml
Source127:        haranoaji-extra.metainfo.xml
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-ascmac
Requires:       texlive-asternote
Requires:       texlive-babel-japanese
Requires:       texlive-bxbase
Requires:       texlive-bxcjkjatype
Requires:       texlive-bxcoloremoji
Requires:       texlive-bxghost
Requires:       texlive-bxjaholiday
Requires:       texlive-bxjalipsum
Requires:       texlive-bxjaprnind
Requires:       texlive-bxjatoucs
Requires:       texlive-bxjscls
Requires:       texlive-bxorigcapt
Requires:       texlive-bxwareki
Requires:       texlive-chuushaku
Requires:       texlive-collection-langcjk
Requires:       texlive-convbkmk
Requires:       texlive-convert-jpfonts
Requires:       texlive-endnotesj
Requires:       texlive-gckanbun
Requires:       texlive-gentombow
Requires:       texlive-haranoaji
Requires:       texlive-haranoaji-extra
Requires:       texlive-ieejtran
Requires:       texlive-ifptex
Requires:       texlive-ifxptex
Requires:       texlive-ipaex
Requires:       texlive-japanese-mathformulas
Requires:       texlive-japanese-otf
Requires:       texlive-jieeetran
Requires:       texlive-jlreq
Requires:       texlive-jlreq-deluxe
Requires:       texlive-jpneduenumerate
Requires:       texlive-jpnedumathsymbols
Requires:       texlive-jsclasses
Requires:       texlive-kanbun
Requires:       texlive-lshort-japanese
Requires:       texlive-luatexja
Requires:       texlive-luwa-ul
Requires:       texlive-mendex-doc
Requires:       texlive-morisawa
Requires:       texlive-outoruby
Requires:       texlive-pbibtex-base
Requires:       texlive-pbibtex-manual
Requires:       texlive-platex
Requires:       texlive-platex-tools
Requires:       texlive-platexcheat
Requires:       texlive-plautopatch
Requires:       texlive-ptex
Requires:       texlive-ptex-base
Requires:       texlive-ptex-fontmaps
Requires:       texlive-ptex-fonts
Requires:       texlive-ptex-manual
Requires:       texlive-ptex2pdf
Requires:       texlive-pxbase
Requires:       texlive-pxchfon
Requires:       texlive-pxcjkcat
Requires:       texlive-pxjahyper
Requires:       texlive-pxjodel
Requires:       texlive-pxrubrica
Requires:       texlive-pxufont
Requires:       texlive-texlive-ja
Requires:       texlive-uplatex
Requires:       texlive-uptex
Requires:       texlive-uptex-base
Requires:       texlive-uptex-fonts
Requires:       texlive-wadalab
Requires:       texlive-zxjafbfont
Requires:       texlive-zxjatype

%description
Support for Japanese; additional packages are in collection-langcjk.

%package -n texlive-ascmac
Summary:        Boxes and picture macros with Japanese vertical writing support
Version:        svn53411
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ascmac.sty) = %{tl_version}
Provides:       tex(tascmac.sty) = %{tl_version}

%description -n texlive-ascmac
The bundle provides boxes and picture macros with Japanese vertical writing
support. It uses only native picture macros and fonts for drawing boxes and is
thus driver-independent. Formerly part of the Japanese pLaTeX bundle, it now
supports all LaTeX engines.

%package -n texlive-asternote
Summary:        Annotation symbols enclosed in square brackets and marked with an asterisk
Version:        svn63838
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(asternote.sty) = %{tl_version}

%description -n texlive-asternote
This LaTeX package can output annotation symbols enclosed in square brackets
and marked with an asterisk.

%package -n texlive-babel-japanese
Summary:        Babel support for Japanese
Version:        svn57733
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(japanese.ldf) = %{tl_version}

%description -n texlive-babel-japanese
This package provides a japanese option for the babel package. It defines all
the language definition macros in Japanese. Currently this package works with
pLaTeX, upLaTeX, XeLaTeX and LuaLaTeX.

%package -n texlive-bxbase
Summary:        BX bundle base components
Version:        svn66115
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifxetex.sty)
Provides:       tex(bxbase.def) = %{tl_version}
Provides:       tex(bxbase.sty) = %{tl_version}
Provides:       tex(bxtoolbox-ext.def) = %{tl_version}
Provides:       tex(bxtoolbox-ja.def) = %{tl_version}
Provides:       tex(bxtoolbox.def) = %{tl_version}
Provides:       tex(bxtoolbox.sty) = %{tl_version}
Provides:       tex(bxutf8.def) = %{tl_version}
Provides:       tex(bxutf8x.def) = %{tl_version}
Provides:       tex(zxbase.sty) = %{tl_version}

%description -n texlive-bxbase
The main purpose of this bundle is to serve as an underlying library for other
packages created by the same author (their names start with "BX" or "PX").
However bxbase package contains a few user-level commands and is of some use by
itself.

%package -n texlive-bxcjkjatype
Summary:        Typeset Japanese with pdfLaTeX and CJK
Version:        svn67705
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(CJK.sty)
Requires:       tex(CJKpunct.sty)
Requires:       tex(CJKspace.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(keyval.sty)
Provides:       tex(bxcjkjatype.sty) = %{tl_version}

%description -n texlive-bxcjkjatype
The package provides a working configuration of the CJK package, suitable for
Japanese typesetting of moderate quality. Moreover, it facilitates use of the
CJK package for pLaTeX users, by providing commands that are similar to those
used by the pLaTeX kernel and some other packages used with it.

%package -n texlive-bxcoloremoji
Summary:        Use color emojis more conveniently
Version:        svn74806
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-twemojis
Requires:       tex(bxghost-lib.sty)
Requires:       tex(bxghost.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(twemojis.sty)
Provides:       tex(bxcoloremoji-names.def) = %{tl_version}
Provides:       tex(bxcoloremoji.sty) = %{tl_version}

%description -n texlive-bxcoloremoji
This package lets users output color emojis in LaTeX documents. Compared to
other packages with similar functionality, this package has the following
merits: It supports all major LaTeX engines. Emojis can be entered as the
characters themselves, as their Unicode code values, or as their short names.
It works reasonably well in PDF strings when using hyperref. Emojis can be
handled properly even in Japanese typesetting environments. This package has
been widely used among the Japanese LaTeX community, but there are already many
emoji packages on CTAN and in TeX Live. To avoid uploading a large amount of
emoji image data that are essentially identical, the package was revised in
version 1.0 so that the image output was delegated to the twmojis package.
Therefore, this package now contains no image data.

%package -n texlive-bxghost
Summary:        Ghost insertion for proper xkanjiskip
Version:        svn66147
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luatexja-adjust.sty)
Requires:       tex(luatexja.sty)
Provides:       tex(bxghost-lib.sty) = %{tl_version}
Provides:       tex(bxghost.sty) = %{tl_version}

%description -n texlive-bxghost
The package provides two commands to help authors for documents in Japanese to
insert proper xkanjiskips. It supports LuaTeX, XeTeX, pTeX, upTeX, and ApTeX
(pTeX-ng).

%package -n texlive-bxjaholiday
Summary:        Support for Japanese holidays
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bxjaholiday.sty) = %{tl_version}

%description -n texlive-bxjaholiday
This LaTeX package provides a command to convert dates to names of Japanese
holidays. Another command, converting dates to the day of the week in Japanese,
is available as a free gift. Further (lower-level) APIs are provided for expl3.
The package supports pdfTeX, XeTeX, LuaTeX, pTeX, and upTeX.

%package -n texlive-bxjalipsum
Summary:        Dummy text in Japanese
Version:        svn67620
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(intcalc.sty)
Provides:       tex(bxjalipsum.sty) = %{tl_version}

%description -n texlive-bxjalipsum
This package enables users to print some Japanese text that can be used as
dummy text. It is a Japanese counterpart of the lipsum package. Since there is
no well-known nonsense text like Lipsum in the Japanese language, the package
uses some real text in public domain.

%package -n texlive-bxjaprnind
Summary:        Adjust the position of parentheses at paragraph head
Version:        svn59641
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bxtoolbox.sty)
Requires:       tex(everyhook.sty)
Provides:       tex(bxjaprnind.sty) = %{tl_version}

%description -n texlive-bxjaprnind
In Japanese typesetting, opening parentheses placed at the beginning of
paragraphs or lines are treated specially; for example, while the paragraph
indent before normal kanji characters is 1em, the indent before parentheses can
be 0.5em, 1em or 1.5em deoending on the local rule in effect.

%package -n texlive-bxjatoucs
Summary:        Convert Japanese character code to Unicode
Version:        svn71870
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Provides:       tex(bxjatoucs.sty) = %{tl_version}

%description -n texlive-bxjatoucs
This package is meant for macro/package developers: It provides function-like
(fully-expandable) macros that convert a character code value in one of several
Japanese encodings to a Unicode value. Supported source encodings are:
ISO-2022-JP (jis), EUC-JP (euc), Shift_JIS (sjis), and the Adobe-Japan1 glyph
set.

%package -n texlive-bxjscls
Summary:        Japanese document class collection for all major engines
Version:        svn75447
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
# Ignoring dependency on bxpandola.sty - not part of TeX Live
Requires:       tex(inputenc.sty)
Provides:       tex(bxjscjkcat.sty) = %{tl_version}
Provides:       tex(bxjscompat.sty) = %{tl_version}
Provides:       tex(bxjsja-minimal.def) = %{tl_version}
Provides:       tex(bxjsja-modern.def) = %{tl_version}
Provides:       tex(bxjsja-pandoc.def) = %{tl_version}
Provides:       tex(bxjsja-standard.def) = %{tl_version}
Provides:       tex(bxjspandoc.sty) = %{tl_version}

%description -n texlive-bxjscls
This package provides an extended version of the Japanese document class
collection provided by jsclasses. While the original version supports only
pLaTeX and upLaTeX, the extended version also supports pdfLaTeX, XeLaTeX and
LuaLaTeX, with the aid of suitable packages that provide capability of Japanese
typesetting.

%package -n texlive-bxorigcapt
Summary:        To retain the original caption names when using Babel
Version:        svn64072
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(bxorigcapt.sty) = %{tl_version}

%description -n texlive-bxorigcapt
This package forces the caption names (\chaptername, \today, etc) declared by
the document class in use to be used as the caption names for a specific
language introduced by the Babel package.

%package -n texlive-bxwareki
Summary:        Convert dates from Gregorian to Japanese calender
Version:        svn67594
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bxwareki-cd.def) = %{tl_version}
Provides:       tex(bxwareki.sty) = %{tl_version}

%description -n texlive-bxwareki
This LaTeX package provides commands to convert from the Gregorian calendar (e.
g. 2018/8/28) to the Japanese rendering of the Japanese calendar (e. g. Heisei
30 nen 8 gatsu 28 nichi; actually with kanji characters). You can choose
whether the numbers are written in Western numerals or kanji numerals. Note
that the package only deals with dates in the year 1873 or later, where the
Japanese calendar is really a Gregorian calendar with a different notation of
years.

%package -n texlive-chuushaku
Summary:        Flexible book notes in Japanese
Version:        svn73263
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(framed.sty)
Requires:       tex(tikz.sty)
Provides:       tex(chuushaku.sty) = %{tl_version}

%description -n texlive-chuushaku
This style file is designed for compiling book notes in Japanese as part of the
body text. ("Chuushaku" means "booknotes" in Japanese.) The "remember picture"
feature automatically calculates coordinates, eliminating the need for manual
adjustment of note positions. The main packages used in chuushaku.sty are TikZ,
amsmath, framed, and calc.

%package -n texlive-convert-jpfonts
Summary:        Convert half-width Japanese to full-width beautifully
Version:        svn73551
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xparse.sty)
Provides:       tex(convert-jpfonts.sty) = %{tl_version}

%description -n texlive-convert-jpfonts
This style file is designed for converting Japanese half-width characters to
full-width characters beautifully. This is useful when alphabet characters
don't render properly in a Japanese font.

%package -n texlive-endnotesj
Summary:        Japanese-style endnotes
Version:        svn47703
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(endnotes.sty)
Requires:       tex(luatexja-otf.sty)
Requires:       tex(otf.sty)
# Ignoring dependency on utf.sty - not part of TeX Live
Provides:       tex(endnotesj.sty) = %{tl_version}

%description -n texlive-endnotesj
This package provides customized styles for endnotes to be used with Japanese
documents. It can be used on pLaTeX, upLaTeX, and LuaLaTeX (LuaTeX-ja).

%package -n texlive-gckanbun
Summary:        Kanbun typesetting for (u)pLaTeX and LuaLaTeX
Version:        svn77307
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bxghost.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifuptex.sty)
Requires:       tex(keyval.sty)
Requires:       tex(luatexja-adjust.sty)
Provides:       tex(gckanbun.sty) = %{tl_version}

%description -n texlive-gckanbun
This package provides a Kanbun (Han Wen , "Chinese writing") typesetting for
(u)pLaTeX and LuaLaTeX.

%package -n texlive-gentombow
Summary:        Generate Japanese-style crop marks
Version:        svn64333
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(filehook.sty)
Requires:       tex(pxatbegshi.sty)
Requires:       tex(pxeveryshi.sty)
Requires:       tex(textpos.sty)
Provides:       tex(bounddvi.sty) = %{tl_version}
Provides:       tex(gentombow.sty) = %{tl_version}
Provides:       tex(pxesopic.sty) = %{tl_version}
Provides:       tex(pxgentombow.sty) = %{tl_version}
Provides:       tex(pxpdfpages.sty) = %{tl_version}
Provides:       tex(pxtextpos.sty) = %{tl_version}

%description -n texlive-gentombow
This bundle provides a LaTeX package for generating Japanese-style crop marks
(called 'tombow' in Japanese) for practical use in self-publishing. The bundle
contains the following packages: gentombow.sty: Generate crop marks (called
'tombow' in Japanese) for practical use in self-publishing. It provides the
core 'tombow' feature if not available. pxgentombow.sty: Superseded by
gentombow.sty; kept for compatibility only. bounddvi.sty: Set papersize special
to DVI file. Can be used on LaTeX/pLaTeX/upLaTeX (with DVI output mode) with
dvips or dvipdfmx drivers.

%package -n texlive-haranoaji
Summary:        Harano Aji Fonts
Version:        svn76078
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-haranoaji
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are fonts obtained
by replacing Adobe-Identity-0 (AI0) CIDs of Source Han fonts (Source Han Serif
and Source Han Sans) with Adobe-Japan1 (AJ1) CIDs. There are 14 fonts, 7
weights each for Mincho and Gothic.

%package -n texlive-haranoaji-extra
Summary:        Harano Aji Fonts
Version:        svn76079
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-haranoaji-extra
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are fonts obtained
by replacing Adobe-Identity-0 (AI0) CIDs of Source Han fonts (Source Han Serif
and Source Han Sans) with Adobe-Japan1 (AJ1) CIDs. There are 14 fonts, 7
weights each for Mincho and Gothic.

%package -n texlive-ieejtran
Summary:        Unofficial bibliography style file for the Institute of Electrical Engineers of Japan
Version:        svn76790
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ieejtran
This package provides an unofficial BibTeX style for authors of the Institute
of Electrical Engineers of Japan (IEEJ) transactions journals and conferences.

%package -n texlive-ifptex
Summary:        Check if the engine is pTeX or one of its derivatives
Version:        svn66803
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Provides:       tex(ifptex.sty) = %{tl_version}
Provides:       tex(ifuptex.sty) = %{tl_version}

%description -n texlive-ifptex
The ifptex package is a counterpart of ifxetex, ifluatex, etc. for the ptex
engine. The ifuptex package is an alias to ifptex provided for backward
compatibility.

%package -n texlive-ifxptex
Summary:        Detect pTeX and its derivatives
Version:        svn46153
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ifxptex.sty) = %{tl_version}

%description -n texlive-ifxptex
The package provides commands for detecting pTeX and its derivatives (e-pTeX,
upTeX, e-upTeX, and ApTeX). Both LaTeX and plain TeX are supported.

%package -n texlive-ipaex
Summary:        IPA (Japanese) fonts
Version:        svn61719
License:        IPA
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ipaex
The fonts provide fixed-width glyphs for Kana and Kanji characters,
proportional width glyphs for Western characters.

%package -n texlive-japanese-mathformulas
Summary:        Compiling basic math formulas in Japanese using LuaLaTeX
Version:        svn64678
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(esvect.sty)
Requires:       tex(graphics.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(luatexja-fontspec.sty)
Requires:       tex(luatexja-otf.sty)
Requires:       tex(luatexja.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(japanese-mathformulas.sty) = %{tl_version}

%description -n texlive-japanese-mathformulas
This is a style file for compiling basic maths formulas in Japanese using
LuaLaTeX. \NewDocumentCommand allows you to specify whether the formula should
be used within a sentence or on a new line. The main packages used in
japanese-mathformulas.sty are amsmath, amssymb, siunitx, ifthen, xparse, TikZ,
mathtools, and graphics.

%package -n texlive-japanese-otf
Summary:        Advanced font selection for platex and its friends
Version:        svn77048
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(ajmacros.sty) = %{tl_version}
Provides:       tex(mlcid.sty) = %{tl_version}
Provides:       tex(mlutf.sty) = %{tl_version}
Provides:       tex(otf.sty) = %{tl_version}
Provides:       tex(redeffont.sty) = %{tl_version}

%description -n texlive-japanese-otf
The package contains pLaTeX support files and virtual fonts for supporting a
wide variety of fonts in LaTeX using the pTeX engine.

%package -n texlive-jieeetran
Summary:        Unofficial BibTeX style for citing Japanese articles in IEEE format
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jieeetran
This package provides an unofficial BibTeX style for authors trying to cite
Japanese articles in the Institute of Electrical and Electronics Engineers
(IEEE) format.

%package -n texlive-jlreq
Summary:        Japanese document class based on requirements for Japanese text layout
Version:        svn76924
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(filehook.sty)
Provides:       tex(jlreq-complements.sty) = %{tl_version}
Provides:       tex(jlreq-helpers.sty) = %{tl_version}
Provides:       tex(jlreq-trimmarks.sty) = %{tl_version}

%description -n texlive-jlreq
This package provides a Japanese document class based on requirements for
Japanese text layout. The class file and the JFM (Japanese font metric) files
for LuaTeX-ja / pLaTeX / upLaTeX are provided.

%package -n texlive-jlreq-deluxe
Summary:        Multi-weight Japanese font support for the jlreq class
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pxjodel.sty)
Provides:       tex(jlreq-deluxe.sty) = %{tl_version}

%description -n texlive-jlreq-deluxe
This package provides multi-weight Japanese font support for the jlreq class.

%package -n texlive-jpneduenumerate
Summary:        Enumerative expressions in Japanese education
Version:        svn72898
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(enumitem.sty)
Requires:       tex(luatexja-otf.sty)
Requires:       tex(otf.sty)
Requires:       tex(refcount.sty)
Provides:       tex(jpneduenumerate.sty) = %{tl_version}

%description -n texlive-jpneduenumerate
Mathematical equation representation in Japanese education differs somewhat
from the standard LaTeX writing style. This package introduces enumerative
expressions in Japanese education.

%package -n texlive-jpnedumathsymbols
Summary:        Mathematical equation representation in Japanese education
Version:        svn72959
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(empheq.sty)
Requires:       tex(luatexja-otf.sty)
Requires:       tex(otf.sty)
Requires:       tex(xparse.sty)
Provides:       tex(jpnedumathsymbols.sty) = %{tl_version}

%description -n texlive-jpnedumathsymbols
Mathematical equation representation in Japanese education differs somewhat
from the standard LaTeX writing style. This package introduces mathematical
equation representation in Japanese education.

%package -n texlive-jsclasses
Summary:        Classes tailored for use with Japanese
Version:        svn75174
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(jslogo.sty) = %{tl_version}
Provides:       tex(jsverb.sty) = %{tl_version}
Provides:       tex(minijs.sty) = %{tl_version}
Provides:       tex(okumacro.sty) = %{tl_version}
Provides:       tex(okuverb.sty) = %{tl_version}

%description -n texlive-jsclasses
Classes jsarticle and jsbook are provided, together with packages okumacro and
okuverb. These classes are designed to work under ASCII Corporation's Japanese
TeX system ptex.

%package -n texlive-kanbun
Summary:        Typeset kanbun-kundoku with support for kanbun annotation
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(xparse.sty)
Provides:       tex(kanbun.sty) = %{tl_version}

%description -n texlive-kanbun
This package allows users to manually input macros for elements in a
kanbun-kundoku (Han Wen Xun Du ) paragraph. More importantly, it accepts plain
text input in the "kanbun annotation" form when used with LuaLaTeX, which
allows typesetting kanbun-kundoku paragraphs efficiently.

%package -n texlive-lshort-japanese
Summary:        Japanese version of A Short Introduction to LaTeX2e
Version:        svn36207
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-japanese-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-japanese-doc <= 11:%{version}

%description -n texlive-lshort-japanese
Japanese version of A Short Introduction to LaTeX2e

%package -n texlive-luatexja
Summary:        Typeset Japanese with Lua(La)TeX
Version:        svn77538
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-luatexbase
Requires:       tex(array.sty)
Requires:       tex(collcell.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(everyhook.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(listings.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(luaotfload.sty)
Requires:       tex(luatexbase-cctb.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(preview.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(stfloats.sty)
Requires:       tex(tascmac.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xunicode.sty)
Provides:       tex(lltjcore-241201.sty) = %{tl_version}
Provides:       tex(lltjcore.sty) = %{tl_version}
Provides:       tex(lltjdefs.sty) = %{tl_version}
Provides:       tex(lltjext.sty) = %{tl_version}
Provides:       tex(lltjfont.sty) = %{tl_version}
Provides:       tex(lltjp-array.sty) = %{tl_version}
Provides:       tex(lltjp-atbegshi.sty) = %{tl_version}
Provides:       tex(lltjp-collcell.sty) = %{tl_version}
Provides:       tex(lltjp-everyshi.sty) = %{tl_version}
Provides:       tex(lltjp-fontspec.sty) = %{tl_version}
Provides:       tex(lltjp-footmisc.sty) = %{tl_version}
Provides:       tex(lltjp-geometry.sty) = %{tl_version}
Provides:       tex(lltjp-listings.sty) = %{tl_version}
Provides:       tex(lltjp-microtype.sty) = %{tl_version}
Provides:       tex(lltjp-preview.sty) = %{tl_version}
Provides:       tex(lltjp-siunitx.sty) = %{tl_version}
Provides:       tex(lltjp-stfloats.sty) = %{tl_version}
Provides:       tex(lltjp-tascmac.sty) = %{tl_version}
Provides:       tex(lltjp-unicode-math.sty) = %{tl_version}
Provides:       tex(lltjp-xunicode.sty) = %{tl_version}
Provides:       tex(ltj-base.sty) = %{tl_version}
Provides:       tex(ltj-kinsoku.tex) = %{tl_version}
Provides:       tex(ltj-latex.sty) = %{tl_version}
Provides:       tex(ltj-plain.sty) = %{tl_version}
Provides:       tex(luatexja-adjust.sty) = %{tl_version}
Provides:       tex(luatexja-ajmacros.sty) = %{tl_version}
Provides:       tex(luatexja-compat.sty) = %{tl_version}
Provides:       tex(luatexja-core.sty) = %{tl_version}
Provides:       tex(luatexja-fontspec-29e.sty) = %{tl_version}
Provides:       tex(luatexja-fontspec.sty) = %{tl_version}
Provides:       tex(luatexja-otf.sty) = %{tl_version}
Provides:       tex(luatexja-preset.sty) = %{tl_version}
Provides:       tex(luatexja-ruby.sty) = %{tl_version}
Provides:       tex(luatexja-zhfonts.sty) = %{tl_version}
Provides:       tex(luatexja.sty) = %{tl_version}

%description -n texlive-luatexja
The package offers support for typesetting Japanese documents with LuaTeX.
Either of the Plain and LaTeX2e formats may be used with the package.

%package -n texlive-luwa-ul
Summary:        Provides underlines and other highlighting which can be used in vertical mode
Version:        svn77595
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(lua-ul.sty)
Requires:       tex(luacolor.sty)
Requires:       tex(luatexja-adjust.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(luwa-ul.sty) = %{tl_version}

%description -n texlive-luwa-ul
This package provides underlining and highlighting that remain intact even in
vertical writing environments and when used together with ruby text. It
internally uses lua-ul package, so it can be used only under LuaLaTeX.

%package -n texlive-mendex-doc
Summary:        Documentation for Mendex index processor
Version:        svn75172
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mendex-doc
This package provides documentation for Mendex (Japanese index processor). The
source code of the program is not included, it can be obtained from TeX Live
subversion repository.

%package -n texlive-morisawa
Summary:        Enables selection of 5 standard Japanese fonts for pLaTeX + dvips
Version:        svn46946
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(morisawa.sty) = %{tl_version}

%description -n texlive-morisawa
The package enables selection of 5 standard Japanese fonts for pLaTeX + dvips.
It was originally written by Haruhiko Okumura as part of jsclasses bundle, and
the TFM/VF files were previously distributed as part of the ptex-fonts package.

%package -n texlive-outoruby
Summary:        Ruby with line break support for Japanese text
Version:        svn74638
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-pxrubrica
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pxrubrica.sty)
Provides:       tex(outoruby.sty) = %{tl_version}

%description -n texlive-outoruby
This package provides the \outoruby command, which supports line breaks when
typesetting ruby anotations. It automatically switches between appropriate ruby
forms at the beginning and the end of lines according to JIS X 4051 and JLReq.
This package depends on pxrubrica and supports any engine that is supported by
that package.

%package -n texlive-pbibtex-base
Summary:        Bibliography styles and miscellaneous files for pBibTeX
Version:        svn66085
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pbibtex-base
These are miscellaneous files, including bibliography styles (.bst), for
pBibTeX, which is a Japanese extended version of BibTeX contained in TeX Live.
The bundle is a redistribution derived from the ptex-texmf distribution by
ASCII MEDIA WORKS.

%package -n texlive-pbibtex-manual
Summary:        Documentation files for (u)pBibTeX
Version:        svn66181
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pbibtex-manual-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pbibtex-manual-doc <= 11:%{version}

%description -n texlive-pbibtex-manual
The bundle contains documentation files for Japanese pBibTeX and upBibTeX. For
historical reasons, this also contains old documentation files for JBibTeX.

%package -n texlive-platex
Summary:        PLaTeX2e and miscellaneous macros for pTeX
Version:        svn73848
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-babel
Requires:       texlive-cm
Requires:       texlive-firstaid
Requires:       texlive-hyphen-base
Requires:       texlive-knuth-lib
Requires:       texlive-l3kernel
Requires:       texlive-l3kernel-dev
Requires:       texlive-l3kernel
Requires:       texlive-l3kernel-dev
Requires:       texlive-latex
Requires:       texlive-latex-base-dev
Requires:       texlive-latex-firstaid-dev
Requires:       texlive-latex-fonts
Requires:       texlive-platex
Requires:       texlive-ptex
Requires:       texlive-ptex-fonts
Requires:       texlive-tex-ini-files
Requires:       texlive-unicode-data
Requires:       texlive-uptex
Requires:       tex(oldlfont.sty)
Requires:       tex(plautopatch.sty)
Provides:       tex(exppl2e.sty) = %{tl_version}
Provides:       tex(jarticle.sty) = %{tl_version}
Provides:       tex(jbook.sty) = %{tl_version}
Provides:       tex(jreport.sty) = %{tl_version}
Provides:       tex(kinsoku.tex) = %{tl_version}
Provides:       tex(oldpfont.sty) = %{tl_version}
Provides:       tex(pfltrace.sty) = %{tl_version}
Provides:       tex(pl209.def) = %{tl_version}
Provides:       tex(platexrelease.sty) = %{tl_version}
Provides:       tex(plexpl3.sty) = %{tl_version}
Provides:       tex(plext.sty) = %{tl_version}
Provides:       tex(ptrace.sty) = %{tl_version}
Provides:       tex(tarticle.sty) = %{tl_version}
Provides:       tex(tbook.sty) = %{tl_version}
Provides:       tex(treport.sty) = %{tl_version}

%description -n texlive-platex
The bundle provides pLaTeX2e and miscellaneous macros for pTeX and e-pTeX. This
is a community edition forked from the original ASCII edition (ptex-texmf-2.5).

%package -n texlive-platex-tools
Summary:        PLaTeX standard tools bundle
Version:        svn72097
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(delarray.sty)
Requires:       tex(doc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(everysel.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(ftnright.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(plext.sty)
Requires:       tex(ptrace.sty)
# Ignoring dependency on uptrace.sty - not part of TeX Live
Requires:       tex(xspace.sty)
Provides:       tex(plarray.sty) = %{tl_version}
Provides:       tex(pldocverb.sty) = %{tl_version}
Provides:       tex(plextarray.sty) = %{tl_version}
Provides:       tex(plextcolortbl.sty) = %{tl_version}
Provides:       tex(plextdelarray.sty) = %{tl_version}
Provides:       tex(pxatbegshi.sty) = %{tl_version}
Provides:       tex(pxeverysel.sty) = %{tl_version}
Provides:       tex(pxeveryshi.sty) = %{tl_version}
Provides:       tex(pxftnright.sty) = %{tl_version}
Provides:       tex(pxmulticol.sty) = %{tl_version}
Provides:       tex(pxxspace.sty) = %{tl_version}

%description -n texlive-platex-tools
This bundle is an extended version of the latex-tools bundle developed by the
LaTeX team, mainly intended to support pLaTeX2e and upLaTeX2e. Currently
patches for the latex-tools bundle and Martin Schroder's ms bundle are
included.

%package -n texlive-platexcheat
Summary:        A LaTeX cheat sheet, in Japanese
Version:        svn49557
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-platexcheat-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-platexcheat-doc <= 11:%{version}

%description -n texlive-platexcheat
This is a translation to Japanese of Winston Chang's LaTeX cheat sheet (a
reference sheet for writing scientific papers). It has been adapted to Japanese
standards using pLaTeX, and also attached additional information of "standard
LaTeX" (especially about math-mode).

%package -n texlive-plautopatch
Summary:        Automated patches for pLaTeX/upLaTeX
Version:        svn64072
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(arydshln.sty)
Requires:       tex(filehook.sty)
Requires:       tex(pgfrcs.sty)
Requires:       tex(plarray.sty)
Requires:       tex(plext.sty)
Requires:       tex(plextarray.sty)
Requires:       tex(plextcolortbl.sty)
Requires:       tex(plextdelarray.sty)
Requires:       tex(pxeveryshi.sty)
Requires:       tex(stfloats.sty)
Provides:       tex(plarydshln.sty) = %{tl_version}
Provides:       tex(plautopatch.sty) = %{tl_version}
Provides:       tex(plcollcell.sty) = %{tl_version}
Provides:       tex(plextarydshln.sty) = %{tl_version}
Provides:       tex(plsiunitx.sty) = %{tl_version}
Provides:       tex(pxpgfrcs.sty) = %{tl_version}
Provides:       tex(pxstfloats.sty) = %{tl_version}

%description -n texlive-plautopatch
Japanese pLaTeX/upLaTeX formats and packages often conflict with other LaTeX
packages which are unaware of pLaTeX/upLaTeX. In the worst case, such packages
throw a fatal error or end up with a wrong output. The goal of this package is
that there should be no need to worry about such incompatibilities, because
specific patches are loaded automatically whenever necessary. This helps not
only to simplify source files, but also to make the appearance of working
pLaTeX/upLaTeX sources similar to those of ordinary LaTeX ones.

%package -n texlive-ptex-base
Summary:        Plain TeX format for pTeX and e-pTeX
Version:        svn64072
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ascii-jplain.tex) = %{tl_version}
Provides:       tex(kinsoku.tex) = %{tl_version}
Provides:       tex(ptex.tex) = %{tl_version}

%description -n texlive-ptex-base
The bundle contains the plain TeX format for pTeX and e-pTeX.

%package -n texlive-ptex-fonts
Summary:        Fonts for use with pTeX
Version:        svn64330
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ptex-fonts
The bundle contains fonts for use with pTeX and the documents for the makejvf
program. This is a redistribution derived from the ptex-texmf distribution by
ASCII MEDIA WORKS.

%package -n texlive-ptex-manual
Summary:        Japanese pTeX manual
Version:        svn75173
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ptex-manual-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ptex-manual-doc <= 11:%{version}

%description -n texlive-ptex-manual
This package contains the Japanese pTeX manual. Feedback is welcome!

%package -n texlive-pxbase
Summary:        Tools for use with (u)pLaTeX
Version:        svn66187
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(ifptex.sty)
Requires:       tex(ifuptex.sty)
Provides:       tex(pxbabel.sty) = %{tl_version}
Provides:       tex(pxbase.def) = %{tl_version}
Provides:       tex(pxbase.sty) = %{tl_version}
Provides:       tex(pxbasenc.def) = %{tl_version}
Provides:       tex(pxbsjc.def) = %{tl_version}
Provides:       tex(pxbsjc1.def) = %{tl_version}
Provides:       tex(pxjsfenc.def) = %{tl_version}
Provides:       tex(upkcat.sty) = %{tl_version}

%description -n texlive-pxbase
The main purpose of this package is to provide auxiliary functions which are
utilized by other packages created by the same author. It also provides a few
user commands to assist in creating Japanese documents using (u)pLaTeX.

%package -n texlive-pxchfon
Summary:        Japanese font setup for pLaTeX and upLaTeX
Version:        svn72097
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pxufont-ruby.sty)
Requires:       tex(pxufont.sty)
Provides:       tex(pxchfon.sty) = %{tl_version}
Provides:       tex(pxchfon0.def) = %{tl_version}

%description -n texlive-pxchfon
This package enables users to declare in their document which physical fonts
should be used for the standard Japanese (logical) fonts of pLaTeX and upLaTeX.
Font setup is realized by changing the font mapping of dvipdfmx, and thus users
can use any (monospaced) physical fonts they like, once they properly install
this package, without creating helper files for each new font. This package
also supports setup for the fonts used in the japanese-otf package. System
requirements: TeX format: LaTeX. TeX engine: pTeX or upTeX. DVIware: dvipdfmx.
Prerequisite packages: atbegshi.

%package -n texlive-pxcjkcat
Summary:        LaTeX interface for the CJK category codes of upTeX
Version:        svn74144
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(pxcjkcat.sty) = %{tl_version}

%description -n texlive-pxcjkcat
The package provides management of the CJK category code ('kcatcode'> table of
the upTeX extended TeX engine. Package options are available for tailored use
in the cases of documents that are principally written in Japanese, or
principally written in English or other Western languages.

%package -n texlive-pxjahyper
Summary:        Hyperref support for pLaTeX
Version:        svn72114
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(bxjatoucs.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(keyval.sty)
Requires:       tex(ltxcmds.sty)
Provides:       tex(pxjahyper-ajm.def) = %{tl_version}
Provides:       tex(pxjahyper-enc.sty) = %{tl_version}
Provides:       tex(pxjahyper-uni.def) = %{tl_version}
Provides:       tex(pxjahyper.sty) = %{tl_version}

%description -n texlive-pxjahyper
This package adjusts the behavior of hyperref on (u)pLaTeX so that authors can
properly create PDF documents that contain document information in Japanese.

%package -n texlive-pxjodel
Summary:        Help change metrics of fonts from japanese-otf
Version:        svn76323
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifuptex.sty)
Requires:       tex(otf.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(pxjodel.sty) = %{tl_version}

%description -n texlive-pxjodel
This package changes the setup of the japanese-otf package so that the TFMs for
direct input are all replaced by new ones with prefixed names; for example,
nmlminr-h will be replaced by foo--nmlminr-h, where foo is a prefix specified
by the user. This function will assist users who want to use the japanese-otf
package together with tailored TFMs of Japanese fonts. The "jodel" part of the
package name stands for "japanese-otf deluxe". Here "deluxe" is the name of
japanese-otf's option for employing multi-weight Japanese font families. This
option is probably the most likely reason for using japanese-otf. So pxjodel is
really about japanese-otf's "deluxe" option, hence the name. It is not related
to yodel singing, although some sense of word-play is intended.

%package -n texlive-pxrubrica
Summary:        Ruby annotations according to JIS X 4051
Version:        svn66298
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(pxrubrica.sty) = %{tl_version}

%description -n texlive-pxrubrica
This package provides a function to add ruby annotations (furigana) that follow
the style conventional in Japanese typography as described in the W3C technical
note "Requirements for Japanese Text Layout" ([JLREQ]) and the JIS
specification JIS X 4051. Starting with version 1.3, this package also provides
a function to add kenten (emphasis marks) to Japanese text.

%package -n texlive-pxufont
Summary:        Emulate non-Unicode Japanese fonts using Unicode fonts
Version:        svn67573
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifuptex.sty)
Provides:       tex(pxufont-ruby.sty) = %{tl_version}
Provides:       tex(pxufont.sty) = %{tl_version}

%description -n texlive-pxufont
The set of the Japanese logical fonts (JFMs) that are used as standard fonts in
pTeX and upTeX contains both Unicode JFMs and non-Unicode JFMs. This bundle
provides an alternative set of non-Unicode JFMs that are tied to the virtual
fonts (VFs) that refer to the glyphs in the Unicode JFMs. Moreover it provides
a LaTeX package that redefines the NFSS settings of the Japanese fonts of
(u)pLaTeX so that the new set of non-Unicode JFMs will be employed. As a whole,
this bundle allows users to dispense with the mapping setup on non-Unicode
JFMs. Such a setup is useful in particular when users want to use OpenType
fonts (such as Source Han Serif) that have a glyph encoding different from
Adobe-Japan1, because mapping setups from non-Unicode JFMs to such physical
fonts are difficult to prepare.

%package -n texlive-texlive-ja
Summary:        TeX Live manual (Japanese)
Version:        svn74739
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-ja-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-ja-doc <= 11:%{version}

%description -n texlive-texlive-ja
TeX Live manual (Japanese)

%package -n texlive-uptex-base
Summary:        Plain TeX formats and documents for upTeX
Version:        svn76790
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ukinsoku.tex) = %{tl_version}
Provides:       tex(uptex.tex) = %{tl_version}

%description -n texlive-uptex-base
The bundle contains plain TeX format files and documents for upTeX and e-upTeX.

%package -n texlive-uptex-fonts
Summary:        Fonts for use with upTeX
Version:        svn74119
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uptex-fonts
The bundle contains fonts (TFM and VF) for use with upTeX. This is a
redistribution derived from the upTeX distribution by Takuji Tanaka.

%package -n texlive-wadalab
Summary:        Wadalab (Japanese) font packages
Version:        svn42428
License:        LicenseRef-Wadalab
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-wadalab
These are font bundles for the Japanese Wadalab fonts which work with the CJK
package. All subfonts now have glyph names compliant to the Adobe Glyph List,
making ToUnicode CMaps in PDF documents (created automatically by dvipdfmx)
work correctly. All font bundles now contain virtual Unicode subfonts.

%package -n texlive-zxjafbfont
Summary:        Fallback CJK font support for xeCJK
Version:        svn28539
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xeCJK.sty)
Provides:       tex(zxjafbfont.sty) = %{tl_version}

%description -n texlive-zxjafbfont
Fallback CJK font support for xeCJK

%package -n texlive-zxjatype
Summary:        Standard conforming typesetting of Japanese, for XeLaTeX
Version:        svn53500
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xeCJK.sty)
Requires:       tex(xparse.sty)
Provides:       tex(zxjatype.sty) = %{tl_version}

%description -n texlive-zxjatype
Standard conforming typesetting of Japanese, for XeLaTeX

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
test "%{source118_hash}" = "none" || { f="%{SOURCE118}"; test -f "$f" || { echo "oreon: missing Source118 $f" >&2; exit 1; }; h_expected="%{source118_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source118_hash}" || { echo "oreon: Source118 hash mismatch" >&2; exit 1; }; }
test "%{source119_hash}" = "none" || { f="%{SOURCE119}"; test -f "$f" || { echo "oreon: missing Source119 $f" >&2; exit 1; }; h_expected="%{source119_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source119_hash}" || { echo "oreon: Source119 hash mismatch" >&2; exit 1; }; }
test "%{source120_hash}" = "none" || { f="%{SOURCE120}"; test -f "$f" || { echo "oreon: missing Source120 $f" >&2; exit 1; }; h_expected="%{source120_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source120_hash}" || { echo "oreon: Source120 hash mismatch" >&2; exit 1; }; }
test "%{source121_hash}" = "none" || { f="%{SOURCE121}"; test -f "$f" || { echo "oreon: missing Source121 $f" >&2; exit 1; }; h_expected="%{source121_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source121_hash}" || { echo "oreon: Source121 hash mismatch" >&2; exit 1; }; }
test "%{source122_hash}" = "none" || { f="%{SOURCE122}"; test -f "$f" || { echo "oreon: missing Source122 $f" >&2; exit 1; }; h_expected="%{source122_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source122_hash}" || { echo "oreon: Source122 hash mismatch" >&2; exit 1; }; }
test "%{source123_hash}" = "none" || { f="%{SOURCE123}"; test -f "$f" || { echo "oreon: missing Source123 $f" >&2; exit 1; }; h_expected="%{source123_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source123_hash}" || { echo "oreon: Source123 hash mismatch" >&2; exit 1; }; }
test "%{source124_hash}" = "none" || { f="%{SOURCE124}"; test -f "$f" || { echo "oreon: missing Source124 $f" >&2; exit 1; }; h_expected="%{source124_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source124_hash}" || { echo "oreon: Source124 hash mismatch" >&2; exit 1; }; }
test "%{source125_hash}" = "none" || { f="%{SOURCE125}"; test -f "$f" || { echo "oreon: missing Source125 $f" >&2; exit 1; }; h_expected="%{source125_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source125_hash}" || { echo "oreon: Source125 hash mismatch" >&2; exit 1; }; }
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
tar -xf %{SOURCE40} -C %{buildroot}%{_texmf_main} --strip-components=1
tar -xf %{SOURCE41} -C %{buildroot}%{_texmf_main} --strip-components=1
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
tar -xf %{SOURCE86} -C %{buildroot}%{_texmf_main} --strip-components=1
tar -xf %{SOURCE87} -C %{buildroot}%{_texmf_main} --strip-components=1
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
tar -xf %{SOURCE123} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE124} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE125} -C %{buildroot}%{_texmf_main}

# Install AppStream metadata for font components
cp %{SOURCE126} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE127} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Remove tlp* files from special install components
rm -rf %{buildroot}%{_texmf_main}/tlp*

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/haranoaji %{buildroot}%{_datadir}/fonts/haranoaji
ln -sf %{_texmf_main}/fonts/opentype/public/haranoaji-extra %{buildroot}%{_datadir}/fonts/haranoaji-extra

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-ascmac
%license bsd.txt
%{_texmf_main}/fonts/map/dvips/ascmac/
%{_texmf_main}/fonts/source/public/ascmac/
%{_texmf_main}/fonts/tfm/public/ascmac/
%{_texmf_main}/fonts/type1/public/ascmac/
%{_texmf_main}/tex/latex/ascmac/
%doc %{_texmf_main}/doc/latex/ascmac/

%files -n texlive-asternote
%license mit.txt
%{_texmf_main}/tex/latex/asternote/
%doc %{_texmf_main}/doc/latex/asternote/

%files -n texlive-babel-japanese
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-japanese/
%doc %{_texmf_main}/doc/generic/babel-japanese/

%files -n texlive-bxbase
%license mit.txt
%{_texmf_main}/tex/latex/bxbase/
%doc %{_texmf_main}/doc/latex/bxbase/

%files -n texlive-bxcjkjatype
%license mit.txt
%{_texmf_main}/tex/latex/bxcjkjatype/
%doc %{_texmf_main}/doc/latex/bxcjkjatype/

%files -n texlive-bxcoloremoji
%license mit.txt
%{_texmf_main}/tex/latex/bxcoloremoji/
%doc %{_texmf_main}/doc/latex/bxcoloremoji/

%files -n texlive-bxghost
%license mit.txt
%{_texmf_main}/tex/latex/bxghost/
%doc %{_texmf_main}/doc/latex/bxghost/

%files -n texlive-bxjaholiday
%license mit.txt
%{_texmf_main}/tex/latex/bxjaholiday/
%doc %{_texmf_main}/doc/latex/bxjaholiday/

%files -n texlive-bxjalipsum
%license mit.txt
%{_texmf_main}/tex/latex/bxjalipsum/
%doc %{_texmf_main}/doc/latex/bxjalipsum/

%files -n texlive-bxjaprnind
%license mit.txt
%{_texmf_main}/tex/latex/bxjaprnind/
%doc %{_texmf_main}/doc/latex/bxjaprnind/

%files -n texlive-bxjatoucs
%license mit.txt
%{_texmf_main}/fonts/tfm/public/bxjatoucs/
%{_texmf_main}/tex/latex/bxjatoucs/
%doc %{_texmf_main}/doc/latex/bxjatoucs/

%files -n texlive-bxjscls
%license bsd2.txt
%{_texmf_main}/tex/latex/bxjscls/
%doc %{_texmf_main}/doc/latex/bxjscls/

%files -n texlive-bxorigcapt
%license mit.txt
%{_texmf_main}/tex/latex/bxorigcapt/
%doc %{_texmf_main}/doc/latex/bxorigcapt/

%files -n texlive-bxwareki
%license mit.txt
%{_texmf_main}/tex/latex/bxwareki/
%doc %{_texmf_main}/doc/latex/bxwareki/

%files -n texlive-chuushaku
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chuushaku/
%doc %{_texmf_main}/doc/latex/chuushaku/

%files -n texlive-convert-jpfonts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/convert-jpfonts/
%doc %{_texmf_main}/doc/latex/convert-jpfonts/

%files -n texlive-endnotesj
%license bsd.txt
%{_texmf_main}/tex/latex/endnotesj/
%doc %{_texmf_main}/doc/latex/endnotesj/

%files -n texlive-gckanbun
%license mit.txt
%{_texmf_main}/tex/latex/gckanbun/
%doc %{_texmf_main}/doc/latex/gckanbun/

%files -n texlive-gentombow
%license bsd.txt
%{_texmf_main}/tex/latex/gentombow/
%doc %{_texmf_main}/doc/latex/gentombow/

%files -n texlive-haranoaji
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/haranoaji/
%{_texmf_main}/tex/latex/haranoaji/
%doc %{_texmf_main}/doc/fonts/haranoaji/
%{_datadir}/fonts/haranoaji
%{_datadir}/appdata/haranoaji.metainfo.xml

%files -n texlive-haranoaji-extra
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/haranoaji-extra/
%doc %{_texmf_main}/doc/fonts/haranoaji-extra/
%{_datadir}/fonts/haranoaji-extra
%{_datadir}/appdata/haranoaji-extra.metainfo.xml

%files -n texlive-ieejtran
%license mit.txt
%{_texmf_main}/bibtex/bst/ieejtran/
%doc %{_texmf_main}/doc/bibtex/ieejtran/

%files -n texlive-ifptex
%license mit.txt
%{_texmf_main}/tex/generic/ifptex/
%doc %{_texmf_main}/doc/generic/ifptex/

%files -n texlive-ifxptex
%license knuth.txt
%{_texmf_main}/tex/generic/ifxptex/
%doc %{_texmf_main}/doc/generic/ifxptex/

%files -n texlive-ipaex
%license other-free.txt
%{_texmf_main}/fonts/truetype/public/ipaex/
%doc %{_texmf_main}/doc/fonts/ipaex/

%files -n texlive-japanese-mathformulas
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/japanese-mathformulas/
%doc %{_texmf_main}/doc/lualatex/japanese-mathformulas/

%files -n texlive-japanese-otf
%license bsd.txt
%{_texmf_main}/fonts/tfm/public/japanese-otf/
%{_texmf_main}/fonts/vf/public/japanese-otf/
%{_texmf_main}/tex/platex/japanese-otf/
%doc %{_texmf_main}/doc/fonts/japanese-otf/

%files -n texlive-jieeetran
%license mit.txt
%{_texmf_main}/bibtex/bst/jieeetran/
%doc %{_texmf_main}/doc/bibtex/jieeetran/

%files -n texlive-jlreq
%license bsd2.txt
%{_texmf_main}/fonts/tfm/public/jlreq/
%{_texmf_main}/fonts/vf/public/jlreq/
%{_texmf_main}/tex/latex/jlreq/
%{_texmf_main}/tex/luatex/jlreq/
%doc %{_texmf_main}/doc/latex/jlreq/

%files -n texlive-jlreq-deluxe
%license mit.txt
%{_texmf_main}/fonts/tfm/public/jlreq-deluxe/
%{_texmf_main}/fonts/vf/public/jlreq-deluxe/
%{_texmf_main}/tex/platex/jlreq-deluxe/
%doc %{_texmf_main}/doc/platex/jlreq-deluxe/

%files -n texlive-jpneduenumerate
%license mit.txt
%{_texmf_main}/tex/latex/jpneduenumerate/
%doc %{_texmf_main}/doc/latex/jpneduenumerate/

%files -n texlive-jpnedumathsymbols
%license mit.txt
%{_texmf_main}/tex/latex/jpnedumathsymbols/
%doc %{_texmf_main}/doc/latex/jpnedumathsymbols/

%files -n texlive-jsclasses
%license bsd.txt
%{_texmf_main}/tex/platex/jsclasses/
%doc %{_texmf_main}/doc/platex/jsclasses/

%files -n texlive-kanbun
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kanbun/
%doc %{_texmf_main}/doc/latex/kanbun/

%files -n texlive-lshort-japanese
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-japanese/

%files -n texlive-luatexja
%license bsd.txt
%{_texmf_main}/tex/luatex/luatexja/
%doc %{_texmf_main}/doc/luatex/luatexja/

%files -n texlive-luwa-ul
%license mit.txt
%{_texmf_main}/tex/lualatex/luwa-ul/
%doc %{_texmf_main}/doc/lualatex/luwa-ul/

%files -n texlive-mendex-doc
%license bsd.txt
%{_texmf_main}/makeindex/mendex-doc/
%doc %{_texmf_main}/doc/support/mendex-doc/

%files -n texlive-morisawa
%license bsd.txt
%{_texmf_main}/fonts/map/dvipdfmx/morisawa/
%{_texmf_main}/fonts/tfm/public/morisawa/
%{_texmf_main}/fonts/vf/public/morisawa/
%{_texmf_main}/tex/latex/morisawa/
%doc %{_texmf_main}/doc/fonts/morisawa/

%files -n texlive-outoruby
%license gpl3.txt
%{_texmf_main}/tex/latex/outoruby/
%doc %{_texmf_main}/doc/latex/outoruby/

%files -n texlive-pbibtex-base
%license bsd.txt
%{_texmf_main}/pbibtex/bib/
%{_texmf_main}/pbibtex/bst/
%doc %{_texmf_main}/doc/ptex/pbibtex/

%files -n texlive-pbibtex-manual
%license bsd.txt
%doc %{_texmf_main}/doc/latex/pbibtex-manual/

%files -n texlive-platex
%license bsd.txt
%{_texmf_main}/tex/platex/base/
%{_texmf_main}/tex/platex/config/
%doc %{_texmf_main}/doc/man/man1/
%doc %{_texmf_main}/doc/platex/base/

%files -n texlive-platex-tools
%license bsd.txt
%{_texmf_main}/tex/latex/platex-tools/
%doc %{_texmf_main}/doc/latex/platex-tools/

%files -n texlive-platexcheat
%license mit.txt
%doc %{_texmf_main}/doc/latex/platexcheat/

%files -n texlive-plautopatch
%license bsd.txt
%{_texmf_main}/tex/latex/plautopatch/
%doc %{_texmf_main}/doc/latex/plautopatch/

%files -n texlive-ptex-base
%license bsd.txt
%{_texmf_main}/tex/ptex/ptex-base/
%doc %{_texmf_main}/doc/ptex/ptex-base/

%files -n texlive-ptex-fonts
%license bsd.txt
%{_texmf_main}/fonts/source/ptex-fonts/jis/
%{_texmf_main}/fonts/source/ptex-fonts/nmin-ngoth/
%{_texmf_main}/fonts/source/ptex-fonts/standard/
%{_texmf_main}/fonts/tfm/ptex-fonts/dvips/
%{_texmf_main}/fonts/tfm/ptex-fonts/jis/
%{_texmf_main}/fonts/tfm/ptex-fonts/nmin-ngoth/
%{_texmf_main}/fonts/tfm/ptex-fonts/standard/
%{_texmf_main}/fonts/vf/ptex-fonts/jis/
%{_texmf_main}/fonts/vf/ptex-fonts/nmin-ngoth/
%{_texmf_main}/fonts/vf/ptex-fonts/standard/
%doc %{_texmf_main}/doc/fonts/ptex-fonts/

%files -n texlive-ptex-manual
%license bsd.txt
%doc %{_texmf_main}/doc/ptex/ptex-manual/

%files -n texlive-pxbase
%license mit.txt
%{_texmf_main}/tex/platex/pxbase/
%doc %{_texmf_main}/doc/platex/pxbase/

%files -n texlive-pxchfon
%license mit.txt
%{_texmf_main}/fonts/sfd/pxchfon/
%{_texmf_main}/fonts/tfm/public/pxchfon/
%{_texmf_main}/fonts/vf/public/pxchfon/
%{_texmf_main}/tex/platex/pxchfon/
%doc %{_texmf_main}/doc/platex/pxchfon/

%files -n texlive-pxcjkcat
%license mit.txt
%{_texmf_main}/tex/latex/pxcjkcat/
%doc %{_texmf_main}/doc/latex/pxcjkcat/

%files -n texlive-pxjahyper
%license mit.txt
%{_texmf_main}/tex/platex/pxjahyper/
%doc %{_texmf_main}/doc/platex/pxjahyper/

%files -n texlive-pxjodel
%license mit.txt
%{_texmf_main}/fonts/tfm/public/pxjodel/
%{_texmf_main}/fonts/vf/public/pxjodel/
%{_texmf_main}/tex/latex/pxjodel/
%doc %{_texmf_main}/doc/latex/pxjodel/

%files -n texlive-pxrubrica
%license mit.txt
%{_texmf_main}/tex/platex/pxrubrica/
%doc %{_texmf_main}/doc/platex/pxrubrica/

%files -n texlive-pxufont
%license mit.txt
%{_texmf_main}/fonts/tfm/public/pxufont/
%{_texmf_main}/fonts/vf/public/pxufont/
%{_texmf_main}/tex/latex/pxufont/
%doc %{_texmf_main}/doc/latex/pxufont/

%files -n texlive-texlive-ja
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-ja/

%files -n texlive-uptex-base
%license bsd.txt
%{_texmf_main}/tex/uptex/uptex-base/
%doc %{_texmf_main}/doc/uptex/uptex-base/

%files -n texlive-uptex-fonts
%license bsd.txt
%{_texmf_main}/fonts/cmap/uptex-fonts/
%{_texmf_main}/fonts/source/uptex-fonts/
%{_texmf_main}/fonts/tfm/uptex-fonts/jis/
%{_texmf_main}/fonts/tfm/uptex-fonts/min/
%{_texmf_main}/fonts/vf/uptex-fonts/jis/
%{_texmf_main}/fonts/vf/uptex-fonts/min/
%doc %{_texmf_main}/doc/fonts/uptex-fonts/

%files -n texlive-wadalab
%license other-free.txt
%{_texmf_main}/fonts/afm/wadalab/dgj/
%{_texmf_main}/fonts/afm/wadalab/dmj/
%{_texmf_main}/fonts/afm/wadalab/mc2j/
%{_texmf_main}/fonts/afm/wadalab/mcj/
%{_texmf_main}/fonts/afm/wadalab/mr2j/
%{_texmf_main}/fonts/afm/wadalab/mrj/
%{_texmf_main}/fonts/map/dvips/wadalab/
%{_texmf_main}/fonts/tfm/wadalab/dgj/
%{_texmf_main}/fonts/tfm/wadalab/dmj/
%{_texmf_main}/fonts/tfm/wadalab/mc2j/
%{_texmf_main}/fonts/tfm/wadalab/mcj/
%{_texmf_main}/fonts/tfm/wadalab/mr2j/
%{_texmf_main}/fonts/tfm/wadalab/mrj/
%{_texmf_main}/fonts/tfm/wadalab/udgj/
%{_texmf_main}/fonts/tfm/wadalab/udmj/
%{_texmf_main}/fonts/tfm/wadalab/umcj/
%{_texmf_main}/fonts/tfm/wadalab/umrj/
%{_texmf_main}/fonts/type1/wadalab/dgj/
%{_texmf_main}/fonts/type1/wadalab/dmj/
%{_texmf_main}/fonts/type1/wadalab/mc2j/
%{_texmf_main}/fonts/type1/wadalab/mcj/
%{_texmf_main}/fonts/type1/wadalab/mr2j/
%{_texmf_main}/fonts/type1/wadalab/mrj/
%{_texmf_main}/fonts/vf/wadalab/udgj/
%{_texmf_main}/fonts/vf/wadalab/udmj/
%{_texmf_main}/fonts/vf/wadalab/umcj/
%{_texmf_main}/fonts/vf/wadalab/umrj/
%doc %{_texmf_main}/doc/fonts/wadalab/

%files -n texlive-zxjafbfont
%license mit.txt
%{_texmf_main}/tex/latex/zxjafbfont/
%doc %{_texmf_main}/doc/latex/zxjafbfont/

%files -n texlive-zxjatype
%license mit.txt
%{_texmf_main}/tex/latex/zxjatype/
%doc %{_texmf_main}/doc/latex/zxjatype/

%changelog
%autochangelog
