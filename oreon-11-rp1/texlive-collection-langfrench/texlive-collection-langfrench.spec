%global source0_hash 7724b3a90a9217a6992f91c2eddbfafd01255fcf3581a3601f7ea1531ea7d4ff990d91ec070b50b6bbdd99672c4ff4017bbda3fed3e44a3adbb9e593df38afc2

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langfrench
Epoch:          12
Version:        svn72499
Release:        4%{?dist}
Summary:        French

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash da8b49478602dba58a01d445064c6b10a5a4ffd807e5164f5ec9cca0cae170a40c59dc6b7662b452e60d68eba79c11d71d8d61b839bb48dffe9756f25a9cb30f
%global source3_hash 9cd504f18411f3b85363d3f22141d276068bda3315751c28caafe8b84f336751cdd5f9f9a6edaf972c14afc874cf212ed0674ed1a7c3d6051ef80498af94769c
%global source4_hash 8642bf0df6f59da0c5479d22aec9371067a57ae8c0b2a8809e2f41a3bd43e5f00cb8e98590c9f23dac8644dedc21e66c3e9fa8ba866103422cacc7439c669014
%global source5_hash 5b1512506276b96663f577ba6a46934b798553aa423b77c36e34f9c84492362fd71b87e22c28d6908d31679a85db22360255e3f2954aa1b0613cef019e1ef1e4
%global source6_hash 7242519633315afcb86584b5c76ba2890673e038c39711f7beb38e9f5adbb3d78cebc9c45069f5f19d774763df3012ec10cb3ae435aec4963c97bf8efba11d82
%global source7_hash e1ec44580c0470483462f328efd1696e93f41c681eeb9511683bef3f6e452b33160bb2450b276e8e4ef34cd823b9ff67777e58dbfd7cb59f56b168d48eb29020
%global source8_hash b1d711f84ae42dd96e61601e80ce02fd5e7b23c15c08b6af7b5a6f988622bfd52556cced9b9fba51f2346a4b7370adae068c5f712f0df1de5aff439150750eaa
%global source9_hash 0d71e390fa85170fde617fee6c0445a6cf28dbfbe370457eb78d7482b71cbf757f2beca1d1e6d73e4d58cd5b06c8f71703fea89613cfdbeee0c9cd143726e363
%global source10_hash 880b7630d91f5c8b4bd50f6e8d69d501c981bcc37cd17639fe8a765b11930fa6ca54604a2c271dbc7214babbb97cae915faa2815a5ae52f5499e197cad271349
%global source11_hash 63cff14cb14ee5a08ebc6dbcb73f581c54ecd8778db0526f6599c9a13f34bc92263c77b390ee399c4baa35762c0db5b8b48c18a4a50f84eff65791abf796724c
%global source12_hash dcce2c321abffedbb2f868d57557ccb75920cfe45ab0433bb6dae94f71f957330c5bd74a221c6198e4619fc676d0eb338eeb379bdd976e853b2f41bf9e9b6c21
%global source13_hash 29b21fa2f94095df3ac6d15fefd492d9c57151e4514659c92d70e7f0b811404df9b8ee09290edced56acdcbf754f964f530bac07bc584228970fdaddaa1f3fb4
%global source14_hash 645d55362506a1bcf563a12ddb7616f085d5cc75a45cb2f0dcdf551158b48f595cd71278caf9a0c35f1d85ca66b880e6f59f9ee416fb9bf15cd7c18bf6fda2b9
%global source15_hash 7954b1c86ddac3a1409bf16cc7db5470332fb86459257756200dc794a3443b137e6013a7e904bbf63e8fceae64850418e56ad08af12a448c1fe507e29221c7be
%global source16_hash 2f0cdfa78c3b75dddc5ab9ed15f651308dad4e598f9623eea50929c48d6f15318f768b95d55ba124eb048129447ce1e629febbb3fa6925677b2a46ac94d82654
%global source17_hash 249bfaabe93c4306c32c698eede8835cac334a27802253dc6ce1f380eaafa5c79fc3b86ee34ddd7b98df043cc0ccec137ae3d342cd3904f39203b0ffba2fc9b7
%global source18_hash 41e7f8f30f662c37d87f937143c72453033138e27631ea7afde23e5e5a67ddb3f587ee6c26c538092c42b79d9a96a6e4f0bb123f1b04d6735afa10d908b35ea5
%global source19_hash 81c4cabdb60326b0ec6e7bf8d2bbfa301a531ffcd8a322e0e03c5dd1ff93b34ebee2bc3addd6126c5db6da4ef242c0bbc6229c339405b277f45c7956a08ab3c2
%global source20_hash 55fbb556378f3774314d19634edce15d8826e07d99564fd49de9e0132cbf1276ca92f4f02f030f62710d4fc8dc9300ef7a5a4deecc593c5ac78a025797941ab6
%global source21_hash dece319458295004a7e86fe9e78e1b0331ff37437888383b375e3b6a014fb62cbd749b638c58bcf88e80d7c5a88dfe4d26e8175062e7949716cfe2c83c6ed716
%global source22_hash 3610afae228604ae88c8763ec70d3672e012d2a07477b02df438dd45f7a0340d89fea29ad196313f36bc33417476fdd6cde37cccb520e19406379ec735c519c2
%global source23_hash 692b4a27b1cd458dca8df9da17e9f967240cde227823ea70e46b97706b97d1dac8154321533d04a315f244a355158b9eefbd6583d75ebb00c7a01efb62777231
%global source24_hash d8e9e0449af1ac2d24fb4bcff4d1843e4a365c16c8f7a90b763b683c93bf054f9237ddcbca07b2d4682fbe755dec7197fc2df34617ba54f2c0b55d2d08a6b4d8
%global source25_hash a4603be67e19205009c73a0685ae84585ee87eb0f88880332065ff5846f4fb2abbdf6304bef87e0de10cbc7315483913c5d88f374e5f1f6c29e760151c24df42
%global source26_hash c00a38da494c78c9fe636f8f811c3522f9b9403fa83b9fd4be19df5afd30562e9920a69a042e49f3a377be217eb864ce6928bdc1014f0b4bd8fe43807caa4c81
%global source27_hash 633e2d782b462669530dd462dda3694e8cecc770e4c388ca34c7678688ceb2be6f8feaad22c030c51836c6dddc9a2d1cb22a6439ebb538495d037848f4e06bab
%global source28_hash 76c928be0648ae7bddc76f654b65a99ae6670cb17b0ae9a54596599ff655636d4520b31d4e802a15af65637c5bf956d41a2095762a3c4bb77052c9f74da5e7af
%global source29_hash 6129658aad2fae20dd12252941ee774393e262d9322ec2163ebc964ec27c4ffb63f2ce0faf9b74a90717c137065e9af238d45c623cc58d52b1e4776da221e231
%global source30_hash a7e05422916119940559f8e10a0b2e6aa667bbb78aefff17b0d596077c9d373fa31343649744ccf47a6689704591efe0db68d9985f7f132349c9d77a379debfe
%global source31_hash 9fb835ef2f2127b3b7e4b0537298274fb2432b85ac46973f679082e2f903ba6f17214ac3221f4a51896e46841882bd1fd2892748183e74ad32102f89a01abd49
%global source32_hash f3e90ecb487259301c20ab4c4c28702b9cadfa844a49361fee0881a26f827ae602f954e4a3e824e910d2e098097c387aa5311c5f32cb58df5a0a1e2fcd9d2364
%global source33_hash 7965e6094535d22b04193619842bc0bd090c2b47139e65498dcdf428f4ce2ec54e7da5edbdf9015c9d8f2013642d11347373e625a3884c629d9d807af2a9880a
%global source34_hash d50cb8467dd4568c082adf80bfb44369f9131e5c03673b307459ec2226227fd78e851f4ecce3dbfa84a2db4d7c3d9017ae51e24cc41948bfe05b7d47c132e1dd
%global source35_hash c4738ceb1c279bf55b513add8f08b115f8558e0503cac823f23287e124db6ed120ad6af4df105fc722258b49715caa0ea9bf82f391c0a1f7418677d3efdafda6
%global source36_hash 30ed6e76f8801f61eeea27679c8c23c050c7d17c334eabe0a00984b1117f046314e59c2c52225ca7d38eb71b93efa57dd563fd582eed500fdf238fac9540b606
%global source37_hash c84aeae53d8324b9e4f1d386dbbc8774d1b9266ca5c8b893a7280bdbc2578dc9e2ca9975874f4d0cbfc5dc10455cac322d9642534b0fc1384a6d7d192a816d51
%global source38_hash 870b8a0c3273bea9fe5a9b975d8eeb38f4d1e312a68da9997f0213ab5845bff7500f247aa526273c70c4b9b93a1e890416930050c096784e8b2a7d2d484bb1d6
%global source39_hash b060193a00dcd7fb927710275a4fab8d4e5c8c2141d9b14b8ff18fb71bb2f2cf9458ece92ba97495cc3d0e68ae99e9fc7de7cfd30db18d4a6a9bf80b4079c699
%global source40_hash 0e69a8a401f87792db4bd0b5040e8254a36302c55d26222386d7d9c97c8857630afbdf3660cd6afddead1baf1d0da7011b2e3739b62e0407a1057534808a4c12
%global source41_hash a7f3efedccf757fbe98835b3e6103f933209b67734a6366f8bb148258de0020885a274b2c79ffc76ccb51eab615db5753fbc477f403f516d184f32c41229950f
%global source42_hash 3ed218145d84e0c087600ba6caa00036cdf3f78032ce6ce0e355166eafa1a26192bf1df044f9f205a6e1b73a851caa454b37fd9df0c76048810fcb699e9a0174
%global source43_hash b6d9c9c49d445a8d30bd4d415f6edeb9888668f0174f5c8b3161273dc7ff443b8cf10ea0c9f8ce5c7479b5f9cf72514155cd764ee7eba5f8bbaa1cec64e0c923
%global source44_hash e6a6780876392fea06187437e6ebd06933f7bab1808dbed342c0a5a9d6c0e362f4b2b4dd47436f636bd563c9ddd602d16a6d60c3fd35827c951e8b7b2e4d270d
%global source45_hash dd0ffeca213fa87e02637b76ca96b5090612c6694ff76af869ba8e64c93d3136c98cb0d2b1d150a71e33bf17bcc1205d428509c35af3b463aa9ad604f62de66a
%global source46_hash 5f6c61585ab0626931cf7f19d18138ec70572f3531f36cf94eecd82d93855a2ec8ed2ed0146971e035f8b5119df7c602c6279a9976e024ac85869953448d51de
%global source47_hash 36fbbc422eed8e577e054067e7b442cc84b640fcbd0706e3d8cb503884a5208e0a5bbe0c40b67cb5b495bcdd0ba7a78855338588757e5a9d26dce21f9bedcf3e
%global source48_hash b49a4b7a8748035c64349c122ef9106cd154c0e037cdfad53dd40f0b5725057db6217fc9650b18ec365fb539f1b971499cb44d8ff15764cbd23c35102daf3e0a
%global source49_hash fdebf132b3e52b09ac33df0d446daab6c2b1ffd632a1b6f89dcdf17ec5130ed1171a738ddad299e9897bc1cc928f64298fc380e83cc72d77889a9a73a03f450f
%global source50_hash 0604832d7fafec1366ce84298949db8fa929e49d1c4bf613e56234fa6d05206333ca4c49c95b9c3db3140b31671aaba36b28d3ed2184cb6123c21e00de9c2dd1
%global source51_hash ccd1440846f328df01958c1daaf8d23d8db4468efd9567845baf466bedda4d9864b4ccc7d0c788e2870f37824282dfe710a850b53c91effa06d3e99c0ac9d5b1
%global source52_hash f6a9a69ded33199fcd46d518fe8ed7dca48677c78fac5f90cdbbed2290558c4a9d7c9b0721c188023384acc97ad95df29565b06abc16fa33deb04490ca50b4ac
%global source53_hash 963a379e3fbf422f4f4d53a41d6bd074fd077360908eb0db1db0a50699e12f37dc6b3ec8b42812604de4ea444ecb38cbfc81d3445cd67626a65fa9b520fb8550
%global source54_hash 19fc20650cb10b9ec271d745a3e1399f734056d92e937336985ce525179e4ee4eac1c60accc78f6096bc19e6285405dccb4c63ccaa1839b95b5afbb7019292bb
%global source55_hash 1a19fa9714e6e4908e2ac0b4c0c0566c3285b79bea37db3c7439948b27a9eb024121f6c1dbb471ab4087cdaf008f57a06251bd6588f16a80a6df03fc61ed11b6
%global source56_hash 8478211e871e38765cbbd36f8f571e63b5cfb9dc652107a4a9178c11a16b419eba7314246878507f22bf7f66818f8c5d1516a527deda5a2dc6c30f9260f23b59
%global source57_hash f489b0bd07b60797b53fc9010c699029dabccbf326767948dd815224f1c591cb59d6da7bbac0d0385ddfb6f0e885e187b2385bfcdbb88933588b06dfc34f640c
%global source58_hash 96366ea420532f56ae076da48f5402c2ee78ca27fae8180795d6cd18aae118a8c7060208ff43ab64526addcdce9e4d90790583842b20c751f37865cf616e04e4
%global source59_hash 52f6aea9ac2393a73d7dc7ce8ad4d6f08e0a224397199d5def97412502026717e8cb966552368899c50718a1049b1ad4610d2d23150a45bee55cc2c776003db7
%global source60_hash bcc2dde6df25ffa69b7d0ecf75fb1a023cb290697be628a9a6db7ed0240fca1c5a8361c84e9a349237a126f1a215a38bafb6f7e92eabe91930692b21d413ffb2
%global source61_hash 371902173f64606a882df7a4c13e02f4510337719886ae3b851770f54f69765823cdf717b0f0d3fd9abf7d31ee2e6792e4e6a36e99e7b7fe899cceab60a2907d
%global source62_hash de92a38d7cfa3daf1aefff06965e2e135ee01b96b120b7f360a8f8c7b0b07395e47abd18237aeb83a5c9ffd9a60f48bef93e4b2113b0a4e41789ac5f52f81da9
%global source63_hash 08bfeb6066ec134c6acc426d3ec833d9a65942a4c2f791b93ba7835505a9ba44a9c94e56ecb84a2cdac64c6f0c9a6342fbc5b05c520a04872e5be7080d474ff8
%global source64_hash 802d108e7deaaa1a42b7f1eca5059f9547f0f4edb2eb5f8f3f0b68d03c05662f37d2bf7b25844dcec6b89d6d1f0babe93614cbc87fe1e2ca0ac2153602c0cad7
%global source65_hash 5e3a0c42944944fc467e09751c1881dfd16ee526c78e509acbad394725703771893770d11e5aa16b09b6b5d1059331b72ce0f1e85c6ec61677d101276398624c
%global source66_hash 27a852a1a43b13a88a64d4354014b1ab305ecb1114d3906823c9c357c9e50d2ecea5736098d3909485e366e890672f728abb9de750901c0a67bd8490aa80ebc5
%global source67_hash 92b9b81e62b9501b60ccef084b6094a2a4cb1e3e79dfd4ad57ad0a79ab936c953a6537f522c618952944d915c8b010931bf370dd634ab338e243e7ec05450689
%global source68_hash d9c866e17a24e66f1b30cb0bc0da35c54a60918aec4bb615494734b955ca001a57b8bd330c67edaccab2ebc91b5a36576122c781a9545615a4bb663855888778
%global source69_hash 9eb130720e99f6c2baaef38420b577165787759d1db04a4ef73a2865d8f7593005468506d0fee0297d98a51cf7cafad157f4ac2942d6953e69c5970484a71c01
%global source70_hash 80dbc9b2d0face36a0cb1db5966a2c002391e4546ebf7f14506f52f1cf686f2c719edaa79bddce0fe3fa0ff3d661c9765bf75d1ffea5eb95c3d1783712827bff
%global source71_hash 20ee48afcd1bde302dd5e4b0e3ff960d0aa56c4ba807287e6d910673a99fe58e8276d7a0b248bb35222238f6e342e37ff10abf142b5bd4c6023bd80bc41b7020
%global source72_hash 7270b65b821c303e84eec760126ad421dd65fbb5ff81309142690f8820c4865c3b1ff39b22b2cf700a10920b973e18085a1e73ea3f6c9d90da984d48a19bbca7
%global source73_hash 567ba9cd2d7eb724fd4ab20ec417f6804a795ff506bf8df582df9d7ace7ef2c5a8f95b46ff374391fed44918c6a536f6b14348ea3e0f3ff149fbe4fdafba9fa8
%global source74_hash 8dc95cb00885810d4053004de770b99ed60471bf31777dcf24eab0fd87f9b8a7da14e06aeb7a5c222a5227092860eb171a7d96e7807fc58cd5f7f6981dc7d5a5
%global source75_hash 8f4a26f5ebaf7472eb0c6aa04917f672be0d179fdbd146f6cfe1c2932e36eeb1bb8c958f8fb90002cff8cb7017aa65151787eb74ce160a3a61d739b879d0b2ca
%global source76_hash 46aa76cd513e9558766fa0bc223c51aa8af6cbb86ddfe59285cd59b21a5bcf952c90bd5ddb7479dca54121bfe723f5eaea4aeebed51b463c4c0719b869e13527
%global source77_hash f8b2486dfc41081ecf4111ef422f50afd21e4d888146c56de6b727fc787deb1c9e62081dc398927afc31881de8560dab1d9e6f32c367fd4ea8c0f76ff51eaa67
%global source78_hash 255b93a8eda59386b798e85741422c529903acfc0d06cb77f4b128c2e32e4a68ef32097888e921397c3e22434b581de30bb79c8cc6dc8357eaef94f26e6da04f
%global source79_hash 117158275aef7f9e5ee3e423e65d9ada5c2f6d28b660941a3d5d80ebb9716f4e35658e070911280e375b29290e2056ad3521acefa1eabfeda95ca9051d64a0c4
%global source80_hash cf422e49af71178867dce774f5b7302c7395f016a2f3af9da99e7a0313eafb86079ab87400f054b4c3ac15756eee2b9bb102696e001d55d1d1e73bb677ef9c39
%global source81_hash 55c7d4069fac9e12a543e56c1467d0f52641578e281f69606abac163985addad7539c9a3ebe3fdc08a5b9042af940fdfac9d062dcc238cf6923e01f3f9c90347
%global source82_hash 8e715ff1db84f65f54645ed68a92b2a68ce49867fee09ebb6d0e4858a27cd6cb1ef1226675f7877b26df2eef91563fd838ed27bfd1a7a84c9f84a5448138faa4
%global source83_hash 008473cdee41e124ec318e088106bffc7953e7593092d41371d62ebe45940f4ab22b39177fa2c9f3eadbd311a379be20f6b16c78f738b670bb301adb660c55c6
%global source84_hash 5c302185c51d8930d836930503d955518c534ba826e21caa44a211d5c2038d0d787025d3fa3b01b7621d427aad5176cff1d2c107eee122dcbe4395658efdc9dd
%global source85_hash af37237693dc2368ba301e85601f388f40f3d04119ee7797c5e6fe6b8dcf9b13c82809db3a06d378c43626bb36ace7e64fca10feb284f13ae74a85b9cc61a415
%global source86_hash 8da323820f60edb97fe77cb55d853cb7f2e34346a65a31060a02e8ce8a287a13e13dbd307ca424a2d4dc0bf65d669986a6ebc2f319042da8001e1e746461cf37
%global source87_hash e62866413b1a667b3c03d3dea333f58ba0fab68e27ca16ff131db7a71ad6feb25d6d1a1231f13c8ea4e2ec7f74580c9f724e750d570d82efabf89d8dcf1cf1f1
%global source88_hash eb843d533419848c675a202fd6d059270fe9961688644a510f2beda0ac21d5699b51b21774b47db75bad30186c81dd3ad4aa2c461c582ae1e171f5a7c826e15b
%global source89_hash 756a2437e107aea1bfb31c47fa1174d01222123070a4c8090a48833774b7f12ff5aa73218caf4e7b7054ad9aec992be7ace28ad0caa21284af97dee1d77cf8b8
%global source90_hash 76f1c6318cd964b94d5a1d836b1a40fc58de49566cdc30b1ea60fc29fbcc8c6b01a477f4739a5fd9bb24998325dbf42817ad016fff27207e710bfc4b51b29985
%global source91_hash ae2f1aa60162512287f15c770a465c2e39abe1fa5d1223d96c524dc81bf065d62f307893d22dfc06fc50da8d63d817ed60c8f07fd4fede984b6febe9c8b7b710
%global source92_hash 71252475aec013adf9bf41460753a648420ea70fb093cadc667500a6884adcf0c6661a2d81053a733844a3f8595ccffb5ac5f7680689575d8485c47a1cc1e469
%global source93_hash 75d6d8afd13f6751bad23d0adc58355d75e355554dd95971dc16ac148150990e1362ec211a3f3e6fd832ce231dbd08e50ed9d44856c763e47ddb5374b1b182ff
%global source94_hash 6d70bc9c973b5bea6be8f4c13d855578f4ac72821328170576f3dbf5d53aa51dd2dd4179f5e946229771d4aeb4231e6d0dc189fc097584027362fc189bfcaede
%global source95_hash 33485829b1e85c44062a2c3ff276e6f7ee0023742183765aa78da44868ed5318bdf6bca5c7ad20f8c0079bc65e68a9b44c3d0d32df90b3f8c9d2ffe09ccc9e16
%global source96_hash fbd3f158e72dd8b0ebd3fe9c33fe47127ecfd38bc0feac3312d569718672e9f88165856fa61389b307a211071467c10ef73981178cc9afd8ecd720cdf627dc1b
%global source97_hash 16a32e64ef4d00d2bf6f99fa05b35a071539d71944227eaa5b37762e838a62b80ee4b227a8bb9cc49b831bf19976421684872f8eb104f37365669907e9621a6b

Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/collection-langfrench.tar.xz#/collection-langfrench.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/aeguill.tar.xz#/aeguill.or11.tar.xz
Source3:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/aeguill.doc.tar.xz#/aeguill.doc.or11.tar.xz
Source4:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/annee-scolaire.tar.xz#/annee-scolaire.or11.tar.xz
Source5:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/annee-scolaire.doc.tar.xz#/annee-scolaire.doc.or11.tar.xz
Source6:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/apprendre-a-programmer-en-tex.tar.xz#/apprendre-a-programmer-en-tex.or11.tar.xz
Source7:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/apprendre-a-programmer-en-tex.doc.tar.xz#/apprendre-a-programmer-en-tex.doc.or11.tar.xz
Source8:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/apprends-latex.tar.xz#/apprends-latex.or11.tar.xz
Source9:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/apprends-latex.doc.tar.xz#/apprends-latex.doc.or11.tar.xz
Source10:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-basque.tar.xz#/babel-basque.or11.tar.xz
Source11:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-basque.doc.tar.xz#/babel-basque.doc.or11.tar.xz
Source12:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-french.tar.xz#/babel-french.or11.tar.xz
Source13:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-french.doc.tar.xz#/babel-french.doc.or11.tar.xz
Source14:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/basque-book.tar.xz#/basque-book.or11.tar.xz
Source15:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/basque-book.doc.tar.xz#/basque-book.doc.or11.tar.xz
Source16:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/basque-date.tar.xz#/basque-date.or11.tar.xz
Source17:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/basque-date.doc.tar.xz#/basque-date.doc.or11.tar.xz
Source18:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bib-fr.tar.xz#/bib-fr.or11.tar.xz
Source19:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bib-fr.doc.tar.xz#/bib-fr.doc.or11.tar.xz
Source20:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bibleref-french.tar.xz#/bibleref-french.or11.tar.xz
Source21:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bibleref-french.doc.tar.xz#/bibleref-french.doc.or11.tar.xz
Source22:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/booktabs-fr.tar.xz#/booktabs-fr.or11.tar.xz
Source23:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/booktabs-fr.doc.tar.xz#/booktabs-fr.doc.or11.tar.xz
Source24:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/cahierprof.tar.xz#/cahierprof.or11.tar.xz
Source25:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/cahierprof.doc.tar.xz#/cahierprof.doc.or11.tar.xz
Source26:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/couleurs-fr.tar.xz#/couleurs-fr.or11.tar.xz
Source27:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/couleurs-fr.doc.tar.xz#/couleurs-fr.doc.or11.tar.xz
Source28:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/droit-fr.tar.xz#/droit-fr.or11.tar.xz
Source29:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/droit-fr.doc.tar.xz#/droit-fr.doc.or11.tar.xz
Source30:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/e-french.tar.xz#/e-french.or11.tar.xz
Source31:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/e-french.doc.tar.xz#/e-french.doc.or11.tar.xz
Source32:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/epslatex-fr.tar.xz#/epslatex-fr.or11.tar.xz
Source33:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/epslatex-fr.doc.tar.xz#/epslatex-fr.doc.or11.tar.xz
Source34:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/expose-expl3-dunkerque-2019.tar.xz#/expose-expl3-dunkerque-2019.or11.tar.xz
Source35:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/expose-expl3-dunkerque-2019.doc.tar.xz#/expose-expl3-dunkerque-2019.doc.or11.tar.xz
Source36:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/facture.tar.xz#/facture.or11.tar.xz
Source37:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/facture.doc.tar.xz#/facture.doc.or11.tar.xz
Source38:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/faq-fr.tar.xz#/faq-fr.or11.tar.xz
Source39:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/faq-fr.doc.tar.xz#/faq-fr.doc.or11.tar.xz
Source40:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/faq-fr-gutenberg.tar.xz#/faq-fr-gutenberg.or11.tar.xz
Source41:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/faq-fr-gutenberg.doc.tar.xz#/faq-fr-gutenberg.doc.or11.tar.xz
Source42:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/formation-latex-ul.tar.xz#/formation-latex-ul.or11.tar.xz
Source43:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/formation-latex-ul.doc.tar.xz#/formation-latex-ul.doc.or11.tar.xz
Source44:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/frenchmath.tar.xz#/frenchmath.or11.tar.xz
Source45:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/frenchmath.doc.tar.xz#/frenchmath.doc.or11.tar.xz
Source46:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/frletter.tar.xz#/frletter.or11.tar.xz
Source47:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/frletter.doc.tar.xz#/frletter.doc.or11.tar.xz
Source48:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/frpseudocode.tar.xz#/frpseudocode.or11.tar.xz
Source49:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/frpseudocode.doc.tar.xz#/frpseudocode.doc.or11.tar.xz
Source50:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/hyphen-basque.tar.xz#/hyphen-basque.or11.tar.xz
Source51:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/hyphen-french.tar.xz#/hyphen-french.or11.tar.xz
Source52:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/impatient-fr.tar.xz#/impatient-fr.or11.tar.xz
Source53:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/impatient-fr.doc.tar.xz#/impatient-fr.doc.or11.tar.xz
Source54:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/impnattypo.tar.xz#/impnattypo.or11.tar.xz
Source55:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/impnattypo.doc.tar.xz#/impnattypo.doc.or11.tar.xz
Source56:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/l2tabu-french.tar.xz#/l2tabu-french.or11.tar.xz
Source57:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/l2tabu-french.doc.tar.xz#/l2tabu-french.doc.or11.tar.xz
Source58:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/latex2e-help-texinfo-fr.tar.xz#/latex2e-help-texinfo-fr.or11.tar.xz
Source59:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/latex2e-help-texinfo-fr.doc.tar.xz#/latex2e-help-texinfo-fr.doc.or11.tar.xz
Source60:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/letgut.tar.xz#/letgut.or11.tar.xz
Source61:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/letgut.doc.tar.xz#/letgut.doc.or11.tar.xz
Source62:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/lshort-french.tar.xz#/lshort-french.or11.tar.xz
Source63:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/lshort-french.doc.tar.xz#/lshort-french.doc.or11.tar.xz
Source64:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/mafr.tar.xz#/mafr.or11.tar.xz
Source65:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/mafr.doc.tar.xz#/mafr.doc.or11.tar.xz
Source66:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/matapli.tar.xz#/matapli.or11.tar.xz
Source67:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/matapli.doc.tar.xz#/matapli.doc.or11.tar.xz
Source68:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/panneauxroute.tar.xz#/panneauxroute.or11.tar.xz
Source69:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/panneauxroute.doc.tar.xz#/panneauxroute.doc.or11.tar.xz
Source70:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/profcollege.tar.xz#/profcollege.or11.tar.xz
Source71:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/profcollege.doc.tar.xz#/profcollege.doc.or11.tar.xz
Source72:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/proflabo.tar.xz#/proflabo.or11.tar.xz
Source73:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/proflabo.doc.tar.xz#/proflabo.doc.or11.tar.xz
Source74:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/proflycee.tar.xz#/proflycee.or11.tar.xz
Source75:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/proflycee.doc.tar.xz#/proflycee.doc.or11.tar.xz
Source76:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/profsio.tar.xz#/profsio.or11.tar.xz
Source77:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/profsio.doc.tar.xz#/profsio.doc.or11.tar.xz
Source78:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tabvar.tar.xz#/tabvar.or11.tar.xz
Source79:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tabvar.doc.tar.xz#/tabvar.doc.or11.tar.xz
Source80:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tdsfrmath.tar.xz#/tdsfrmath.or11.tar.xz
Source81:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tdsfrmath.doc.tar.xz#/tdsfrmath.doc.or11.tar.xz
Source82:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-fr.tar.xz#/texlive-fr.or11.tar.xz
Source83:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-fr.doc.tar.xz#/texlive-fr.doc.or11.tar.xz
Source84:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/translation-array-fr.tar.xz#/translation-array-fr.or11.tar.xz
Source85:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/translation-array-fr.doc.tar.xz#/translation-array-fr.doc.or11.tar.xz
Source86:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/translation-dcolumn-fr.tar.xz#/translation-dcolumn-fr.or11.tar.xz
Source87:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/translation-dcolumn-fr.doc.tar.xz#/translation-dcolumn-fr.doc.or11.tar.xz
Source88:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/translation-natbib-fr.tar.xz#/translation-natbib-fr.or11.tar.xz
Source89:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/translation-natbib-fr.doc.tar.xz#/translation-natbib-fr.doc.or11.tar.xz
Source90:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/translation-tabbing-fr.tar.xz#/translation-tabbing-fr.or11.tar.xz
Source91:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/translation-tabbing-fr.doc.tar.xz#/translation-tabbing-fr.doc.or11.tar.xz
Source92:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/variations.tar.xz#/variations.or11.tar.xz
Source93:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/variations.doc.tar.xz#/variations.doc.or11.tar.xz
Source94:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/visualfaq-fr.tar.xz#/visualfaq-fr.or11.tar.xz
Source95:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/visualfaq-fr.doc.tar.xz#/visualfaq-fr.doc.or11.tar.xz
Source96:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/visualtikz.tar.xz#/visualtikz.or11.tar.xz
Source97:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/visualtikz.doc.tar.xz#/visualtikz.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-aeguill
Requires:       texlive-annee-scolaire
Requires:       texlive-apprendre-a-programmer-en-tex
Requires:       texlive-apprends-latex
Requires:       texlive-babel-basque
Requires:       texlive-babel-french
Requires:       texlive-basque-book
Requires:       texlive-basque-date
Requires:       texlive-bib-fr
Requires:       texlive-bibleref-french
Requires:       texlive-booktabs-fr
Requires:       texlive-cahierprof
Requires:       texlive-collection-basic
Requires:       texlive-couleurs-fr
Requires:       texlive-droit-fr
Requires:       texlive-e-french
Requires:       texlive-epslatex-fr
Requires:       texlive-expose-expl3-dunkerque-2019
Requires:       texlive-facture
Requires:       texlive-faq-fr
Requires:       texlive-faq-fr-gutenberg
Requires:       texlive-formation-latex-ul
Requires:       texlive-frenchmath
Requires:       texlive-frletter
Requires:       texlive-frpseudocode
Requires:       texlive-hyphen-basque
Requires:       texlive-hyphen-french
Requires:       texlive-impatient-fr
Requires:       texlive-impnattypo
Requires:       texlive-l2tabu-french
Requires:       texlive-latex2e-help-texinfo-fr
Requires:       texlive-letgut
Requires:       texlive-lshort-french
Requires:       texlive-mafr
Requires:       texlive-matapli
Requires:       texlive-panneauxroute
Requires:       texlive-profcollege
Requires:       texlive-proflabo
Requires:       texlive-proflycee
Requires:       texlive-profsio
Requires:       texlive-tabvar
Requires:       texlive-tdsfrmath
Requires:       texlive-texlive-fr
Requires:       texlive-translation-array-fr
Requires:       texlive-translation-dcolumn-fr
Requires:       texlive-translation-natbib-fr
Requires:       texlive-translation-tabbing-fr
Requires:       texlive-variations
Requires:       texlive-visualfaq-fr
Requires:       texlive-visualtikz

%description
Support for French and Basque.

%package -n texlive-aeguill
Summary:        Add several kinds of guillemets to the ae fonts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ae.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(latexsym.sty)
Provides:       tex(aeguill.sty) = %{tl_version}

%description -n texlive-aeguill
The package enables the user to add guillemets from several source (Polish cmr,
Cyrillic cmr, lasy and ec) to the ae fonts. This was useful when the ae fonts
were used to produce PDF files, since the additional guillemets exist in fonts
available in Adobe Type 1 format.

%package -n texlive-annee-scolaire
Summary:        Automatically typeset the academic year (French way)
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(annee-scolaire.sty) = %{tl_version}

%description -n texlive-annee-scolaire
This package provides a macro \anneescolaire to automatically write the
academic year in the French way, according to the date of compilation, two
other macros to obtain the first and the second calendar year of the academic
year, a macro to be redefined to change the presentation of the years.

%package -n texlive-apprendre-a-programmer-en-tex
Summary:        The book "Apprendre a programmer en TeX"
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-apprendre-a-programmer-en-tex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-apprendre-a-programmer-en-tex-doc <= 11:%{version}

%description -n texlive-apprendre-a-programmer-en-tex
This book explains the basic concepts required for programming in TeX and
explains the programming methods, providing many examples. The package makes
the compilable source code as well as the compiled pdf file accessible to
everyone. Ce livre expose les concepts de base requis pour programmer en TeX et
decrit les methodes de programmation en s'appuyant sur de nombreux exemples. Ce
package met a disposition de tous le code source compilable ainsi que le
fichier pdf du livre.

%package -n texlive-apprends-latex
Summary:        Apprends LaTeX!
Version:        svn19306
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-apprends-latex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-apprends-latex-doc <= 11:%{version}

%description -n texlive-apprends-latex
Apprends LaTeX! ("Learn LaTeX", in English) is French documentation for LaTeX
beginners.

%package -n texlive-babel-basque
Summary:        Babel contributed support for Basque
Version:        svn30256
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(basque.ldf) = %{tl_version}

%description -n texlive-babel-basque
The package establishes Basque conventions in a document.

%package -n texlive-babel-french
Summary:        Babel contributed support for French
Version:        svn76067
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(acadian.ldf) = %{tl_version}
Provides:       tex(canadien.ldf) = %{tl_version}
Provides:       tex(francais.ldf) = %{tl_version}
Provides:       tex(french.ldf) = %{tl_version}
Provides:       tex(french3.ldf) = %{tl_version}
Provides:       tex(frenchb.ldf) = %{tl_version}

%description -n texlive-babel-french
The package, formerly known as frenchb, establishes French conventions in a
document (or a subset of the conventions, if French is not the main language of
the document).

%package -n texlive-basque-book
Summary:        Class for book-type documents written in Basque
Version:        svn32924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-basque-book
The class is derived from the LaTeX book class. The extensions solve
grammatical and numeration issues that occur when book-type documents are
written in Basque. The class is useful for writing books, PhD and Master
Theses, etc., in Basque.

%package -n texlive-basque-date
Summary:        Print the date in Basque
Version:        svn26477
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(basque-date.sty) = %{tl_version}

%description -n texlive-basque-date
The package provides two LaTeX commands to print the current date in Basque
according to the correct forms ruled by The Basque Language Academy
(Euskaltzaindia). The commands automatically solve the complex declination
issues of numbers in Basque.

%package -n texlive-bib-fr
Summary:        French translation of classical BibTeX styles
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bib-fr
These files are French translations of the classical BibTeX style files. The
translations can easily be modified by simply redefining FUNCTIONs named fr.*,
at the beginning (lines 50-150) of each file.

%package -n texlive-bibleref-french
Summary:        French translations for bibleref
Version:        svn75246
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bibleref.sty)
Requires:       tex(etoolbox.sty)
Provides:       tex(bibleref-french.sty) = %{tl_version}

%description -n texlive-bibleref-french
The package provides translations and alternative typesetting conventions for
use of bibleref in French.

%package -n texlive-booktabs-fr
Summary:        French translation of booktabs documentation
Version:        svn21948
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-booktabs-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-booktabs-fr-doc <= 11:%{version}

%description -n texlive-booktabs-fr
The translation comes from a collection provided by Benjamin Bayart.

%package -n texlive-cahierprof
Summary:        Schedule and grade books for French teachers
Version:        svn76102
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(microtype.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(cahierprof.sty) = %{tl_version}

%description -n texlive-cahierprof
This package provide tools to help teachers in France to produce weekly
schedules and grade books.

%package -n texlive-couleurs-fr
Summary:        French version of colour definitions from xcolor
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xcolor.sty)
Provides:       tex(couleurs-fr.sty) = %{tl_version}

%description -n texlive-couleurs-fr
This package provides colours with French names, based on xcolor (svgnames,
dvipsnames) and xkcd.

%package -n texlive-droit-fr
Summary:        Document class and bibliographic style for French law
Version:        svn39802
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(verbose-ibid.bbx)
Requires:       tex(verbose-ibid.cbx)
Provides:       tex(droit-fr.bbx) = %{tl_version}
Provides:       tex(droit-fr.cbx) = %{tl_version}

%description -n texlive-droit-fr
The bundle provides a toolkit intended for students writing a thesis in French
law. It features: a LaTeX document class; a bibliographic style for BibLaTeX
package; a practical example of french thesis document; and documentation. The
class assumes use of biber and BibLaTeX.

%package -n texlive-e-french
Summary:        Comprehensive LaTeX support for French-language typesetting
Version:        svn52027
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(german.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(msg.sty)
Requires:       tex(ngerman.sty)
Provides:       tex(efrench.sty) = %{tl_version}
Provides:       tex(efrenchu.tex) = %{tl_version}
Provides:       tex(epreuve.sty) = %{tl_version}
Provides:       tex(fenglish.sty) = %{tl_version}
Provides:       tex(frabbrev-u8.tex) = %{tl_version}
Provides:       tex(frabbrev.tex) = %{tl_version}
Provides:       tex(french-msg.tex) = %{tl_version}
Provides:       tex(french.sty) = %{tl_version}
Provides:       tex(french_french-msg.tex) = %{tl_version}
Provides:       tex(frenchle.sty) = %{tl_version}
Provides:       tex(frenchpro.sty) = %{tl_version}
Provides:       tex(frhyphex.tex) = %{tl_version}
Provides:       tex(fxabbrev.tex) = %{tl_version}
Provides:       tex(german_french-msg.tex) = %{tl_version}
Provides:       tex(mlp-01.sty) = %{tl_version}
Provides:       tex(mlp-33.sty) = %{tl_version}
Provides:       tex(mlp-49.sty) = %{tl_version}
Provides:       tex(mlp-49n.sty) = %{tl_version}
Provides:       tex(mlp-opts.sty) = %{tl_version}
Provides:       tex(mlp.sty) = %{tl_version}
Provides:       tex(pmfrench.sty) = %{tl_version}

%description -n texlive-e-french
E-french is a distribution that keeps alive the work of Bernard Gaulle (now
deceased), under a free licence. It replaces the old "full" frenchpro (the
"professional" distribution) and the light-weight frenchle packages.

%package -n texlive-epslatex-fr
Summary:        French version of "graphics in LaTeX"
Version:        svn19440
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-epslatex-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-epslatex-fr-doc <= 11:%{version}

%description -n texlive-epslatex-fr
This is the French translation of epslatex, and describes how to use imported
graphics in LaTeX(2e) documents.

%package -n texlive-expose-expl3-dunkerque-2019
Summary:        Using expl3 to implement some numerical algorithms
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-expose-expl3-dunkerque-2019-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-expose-expl3-dunkerque-2019-doc <= 11:%{version}

%description -n texlive-expose-expl3-dunkerque-2019
An article, in French, based on a presentation made in Dunkerque for the "stage
LaTeX" on 12 June 2019. The articles gives three examples of code in expl3 with
(lots of) comments: Knuth's algorithm to create a list of primes, the sieve of
Eratosthenes, Kaprekar sequences. The package contains the code itself, the
documentation as a PDF file, and all the files needed to produce it.

%package -n texlive-facture
Summary:        Generate an invoice
Version:        svn67538
License:        CC-BY-SA-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-facture
Une classe simple permettant de produire une facture, avec ou sans TVA, avec
gestion d'une adresse differente pour la livraison et pour la facturation. A
simple class that allows production of an invoice, with or without VAT;
different addresses for delivery and for billing are permitted.

%package -n texlive-faq-fr
Summary:        French LaTeX FAQ (sources)
Version:        svn71182
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-faq-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-faq-fr-doc <= 11:%{version}

%description -n texlive-faq-fr
(English version below) Ce package contient les sources de la faq LaTeX
francophone, actuellement maintenue a jour sur un wiki ouvert a tous:
https://www.latex-fr.net/ Si vous souhaitez lire la FAQ, nous vous conseillons
de consulter URL ci-dessus. Vous pourrez egalement vous ouvrir un compte sur le
wiki pour participer au projet (en francais). Toutes les contributions sont les
bienvenues. Ce package est essentiellement mis a disposition sur le CTAN pour
encourager la reutilisation de ce contenu, et pour en conserver une copie
perenne. Le fichier "REUSE" contient les informations techniques pour la
reutilisation. English version: This package contains the source files of the
French-speaking FAQ, now hosted on an open wiki: https://www.latex-fr.net/ If
you just want to read the FAQ, please visit the URL above. You're also welcome
if you want to contribute to this resource (in French): just request an
account, it's open to everyone. This package is on CTAN mostly to encourage
reuse, and for archival purposes. Read the "REUSE" file to get technical data
about reusing the contents.

%package -n texlive-faq-fr-gutenberg
Summary:        Sources of the GUTenberg French LaTeX FAQ and PDF files
Version:        svn75712
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-faq-fr-gutenberg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-faq-fr-gutenberg-doc <= 11:%{version}

%description -n texlive-faq-fr-gutenberg
# French-speaking GUTenberg LaTeX FAQ -- Frequently Asked Questions (French
version below) This package contains the sources of the GUTenberg French LaTeX
FAQ (French (La)TeX users group), currently maintained as an Git repository
open to all: https://gitlab.gutenberg-asso.fr If you'd like to read the FAQ,
please visit the URL above. This package also contains two PDF versions of this
FAQ: faqlatexgutenberg.pdf with code verbatim in clear mode
faqlatexgutenberg-sombre.pdf with code verbatim in dark mode ## Participate You
can also open an account on the association's Gitlab forge:
https://gitlab.gutenberg-asso.fr and ask to join the repository
https://gitlab.gutenberg-asso.fr/gutenberg/faq-gut All contributions are
welcome: corrections of small errors, updating answers to questions, or adding
new questions! These files are made available on CTAN only to encourage reuse
of this content, and to preserve a permanent copy. ## Contact us For questions
and comments: faq@gutenberg-asso.fr ## Version 2024-10-07 # FAQ LaTeX
francophone GUTenberg -- Foire aux Questions Ce package contient les sources de
la FAQ LaTeX francophone GUTenberg (groupe des utilisateurs francophones de
(La)TeX), actuellement maintenue a jour sous forme d'un depot Git ouvert a
tous: https://gitlab.gutenberg-asso.fr Si vous souhaitez lire la FAQ, nous vous
conseillons de consulter l'URL ci-dessus. Ce package contient aussi deux
versions PDF de cette FAQ: faqlatexgutenberg.pdf avec verbatim des codes en
mode clair faqlatexgutenberg-sombre.pdf avec verbatim des codes en mode sombre
## Participer Vous pouvez egalement ouvrir un compte sur la forge Gitlab de
l'association GUTenberg: https://gitlab.gutenberg-asso.fr et demander a
rejoindre le depot: https://gitlab.gutenberg-asso.fr/gutenberg/faq-gut Toutes
les contributions sont les bienvenues: corrections des petites erreurs, mises a
jour des reponses aux questions, ou ajout de nouvelles questions ! Ces fichiers
ne sont mis a disposition sur le CTAN que pour encourager la reutilisation de
ce contenu, et pour en conserver une copie perenne. ## Nous contacter Pour
toutes questions et remarques: faq@gutenberg-asso.fr

%package -n texlive-formation-latex-ul
Summary:        Introductory LaTeX course in French
Version:        svn70507
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-formation-latex-ul-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-formation-latex-ul-doc <= 11:%{version}

%description -n texlive-formation-latex-ul
This package contains the supporting documentation, slides, exercise files, and
templates for an introductory LaTeX course (in French) prepared for Universite
Laval, Quebec, Canada.

%package -n texlive-frenchmath
Summary:        Typesetting mathematics according to French rules
Version:        svn71205
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsopn.sty)
Requires:       tex(amstext.sty)
Requires:       tex(decimalcomma.sty)
Requires:       tex(dotlessj.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ibrackets.sty)
Requires:       tex(mathgreeks.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(xspace.sty)
Provides:       tex(frenchmath.sty) = %{tl_version}

%description -n texlive-frenchmath
The package provides: capital letters in roman (upright shape) in mathematical
mode according to French rule (can be optionally disabled), correct spacing in
math mode after commas, before a semicolon and around square brackets, some
useful macros and aliases for symbols used in France: \infeg, \supeg, \paral,
... several macros for writing french operator names like pgcd, ppcm, Card, rg,
Vect, ... optionally lowercase Greek letters in upright shape,

%package -n texlive-frletter
Summary:        Typeset letters in the French style
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-frletter
A small class for typesetting letters in France. No assumption is made about
the language in use. The class represents a small modification of the beletter
class, which is itself a modification of the standard LaTeX letter class.

%package -n texlive-frpseudocode
Summary:        French translation for the algorithmicx package
Version:        svn56088
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algpseudocode.sty)
Provides:       tex(frpseudocode.sty) = %{tl_version}

%description -n texlive-frpseudocode
This package is intended for use alongside Szasz Janos' algorithmicx package.
Its aim is to provide a French translation of terms and words used in
algorithms to make it integrate seamlessly in a French written document.

%package -n texlive-hyphen-basque
Summary:        Basque hyphenation patterns.
Version:        svn73410
License:        Unicode-DFS-2015
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-eu.ec.tex) = %{tl_version}
Provides:       tex(hyph-eu.tex) = %{tl_version}
Provides:       tex(loadhyph-eu.tex) = %{tl_version}

%description -n texlive-hyphen-basque
Hyphenation patterns for Basque in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-french
Summary:        French hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-fr.ec.tex) = %{tl_version}
Provides:       tex(hyph-fr.tex) = %{tl_version}
Provides:       tex(hyph-quote-fr.tex) = %{tl_version}
Provides:       tex(loadhyph-fr.tex) = %{tl_version}

%description -n texlive-hyphen-french
Hyphenation patterns for French in T1/EC and UTF-8 encodings.

%package -n texlive-impatient-fr
Summary:        Free edition of the book "TeX for the Impatient"
Version:        svn54080
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-impatient-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-impatient-fr-doc <= 11:%{version}

%description -n texlive-impatient-fr
"TeX for the Impatient" is a book (of around 350 pages) on TeX, Plain TeX and
Eplain. The book is also available in French and Chinese translations.

%package -n texlive-impnattypo
Summary:        Support typography of l'Imprimerie Nationale Francaise
Version:        svn50227
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(impnattypo.sty) = %{tl_version}

%description -n texlive-impnattypo
The package provides useful macros implementing recommendations by the French
Imprimerie Nationale.

%package -n texlive-l2tabu-french
Summary:        French translation of l2tabu
Version:        svn31315
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l2tabu-french-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l2tabu-french-doc <= 11:%{version}

%description -n texlive-l2tabu-french
French translation of l2tabu.

%package -n texlive-latex2e-help-texinfo-fr
Summary:        A French translation of "latex2e-help-texinfo"
Version:        svn64228
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex2e-help-texinfo-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex2e-help-texinfo-fr-doc <= 11:%{version}

%description -n texlive-latex2e-help-texinfo-fr
This package provides a complete French translation of latex2e-help-texinfo.

%package -n texlive-letgut
Summary:        Class for the newsletter "La Lettre GUTenberg" of the French TeX User Group GUTenberg
Version:        svn76652
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(accsupp.sty)
Requires:       tex(numeric.cbx)
Requires:       tex(xcolor.sty)
Provides:       tex(informations-gut.tex) = %{tl_version}
Provides:       tex(letgut-acronyms.tex) = %{tl_version}
Provides:       tex(letgut-banner.sty) = %{tl_version}
Provides:       tex(letgut-lstlang.sty) = %{tl_version}
Provides:       tex(letgut.cbx) = %{tl_version}

%description -n texlive-letgut
The French TeX User Group GUTenberg has been publishing "The GUTenberg Letter",
its irregular newsletter, since February 1993. For this purpose, a dedicated,
in-house (La)TeX class was gradually created but, depending on new needs and on
the people who were publishing the Newsletter, its development was somewhat
erratic; in particular, it would not have been possible to publish its code as
it was. In addition, its documentation was non-existent. The Board of Directors
of the association, elected in November 2020, wished to provide a better
structured, more perennial and documented class, able to be published on the
CTAN. This is now done with the present 'letgut' class. # French L'association
GUTenberg publie "La Lettre GUTenberg", son bulletin irregulomestriel, depuis
fevrier 1993. Pour ce faire, une classe (La)TeX dediee, maison, a peu a peu vu
le jour mais, au gre des nouveaux besoins et des personnes qui ont assure la
publication de la Lettre, son developpement a ete quelque peu erratique ; il
n'aurait notamment pas ete possible de publier son code en l'etat. En outre, sa
documentation etait inexistante. Le Conseil d'Administration de l'association,
elu en novembre 2020, a souhaite fournir une classe mieux structuree, davantage
perenne et documentee, a meme d'etre publiee sur le CTAN. C'est desormais chose
faite avec la presente classe letgut.

%package -n texlive-lshort-french
Summary:        Short introduction to LaTeX, French translation
Version:        svn23332
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-french-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-french-doc <= 11:%{version}

%description -n texlive-lshort-french
French version of A Short Introduction to LaTeX2e.

%package -n texlive-mafr
Summary:        Mathematics in accord with French usage
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(fontenc.sty)
Provides:       tex(mafr.sty) = %{tl_version}

%description -n texlive-mafr
The package provides settings and macros for typesetting mathematics with LaTeX
in compliance with French usage. It comes with two document classes, 'fiche'
and 'cours', useful to create short high school documents such as tests or
lessons. The documentation is in French.

%package -n texlive-matapli
Summary:        Class for the french journal "MATAPLI"
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-matapli
This is a class for the french journal "MATAPLI" of the Societe de
Mathematiques Appliquees et Industrielles (SMAI).

%package -n texlive-panneauxroute
Summary:        Commands to display French road signs (vector graphics)
Version:        svn73069
License:        LPPL-1.3c AND CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(PanneauxRoute.sty) = %{tl_version}

%description -n texlive-panneauxroute
The package provides commands to insert French road signs as vector graphics:
\AffPanneau[graphicx options]{code} \prcode[graphicx options]

%package -n texlive-profcollege
Summary:        A LaTeX package for French maths teachers in college
Version:        svn77090
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(cancel.sty)
Requires:       tex(datatool.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(gmp.sty)
Requires:       tex(hhline.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(longtable.sty)
Requires:       tex(luacas.sty)
Requires:       tex(luamplib.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(modulus.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multido.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(pifont.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xlop.sty)
Requires:       tex(xstring.sty)
Provides:       tex(PfCAireSimple.tex) = %{tl_version}
Provides:       tex(PfCAllumettes.tex) = %{tl_version}
Provides:       tex(PfCArbreCalcul.tex) = %{tl_version}
Provides:       tex(PfCArbreChiffre.tex) = %{tl_version}
Provides:       tex(PfCAssemblagesSolides.tex) = %{tl_version}
Provides:       tex(PfCAutomatismes.tex) = %{tl_version}
Provides:       tex(PfCAutonomie.tex) = %{tl_version}
Provides:       tex(PfCBalance.tex) = %{tl_version}
Provides:       tex(PfCBandeNumerique.tex) = %{tl_version}
Provides:       tex(PfCBarreNiveaux.tex) = %{tl_version}
Provides:       tex(PfCBarresCalculs.tex) = %{tl_version}
Provides:       tex(PfCBillard.tex) = %{tl_version}
Provides:       tex(PfCBoiteADix.tex) = %{tl_version}
Provides:       tex(PfCBonSortie.tex) = %{tl_version}
Provides:       tex(PfCBonbon.tex) = %{tl_version}
Provides:       tex(PfCCAN.tex) = %{tl_version}
Provides:       tex(PfCCalculatrice.tex) = %{tl_version}
Provides:       tex(PfCCalculsCroises.tex) = %{tl_version}
Provides:       tex(PfCCalculsDetailles.tex) = %{tl_version}
Provides:       tex(PfCCalculsFractions.tex) = %{tl_version}
Provides:       tex(PfCCalisson.tex) = %{tl_version}
Provides:       tex(PfCCartesJeux.tex) = %{tl_version}
Provides:       tex(PfCCartesMentales.tex) = %{tl_version}
Provides:       tex(PfCCartographie.tex) = %{tl_version}
Provides:       tex(PfCCheque.tex) = %{tl_version}
Provides:       tex(PfCCible.tex) = %{tl_version}
Provides:       tex(PfCCibleQOp.tex) = %{tl_version}
Provides:       tex(PfCColorilude.tex) = %{tl_version}
Provides:       tex(PfCCompteBon.tex) = %{tl_version}
Provides:       tex(PfCConversion.tex) = %{tl_version}
Provides:       tex(PfCCritere.tex) = %{tl_version}
Provides:       tex(PfCCryptarithme.tex) = %{tl_version}
Provides:       tex(PfCDeAJouer.tex) = %{tl_version}
Provides:       tex(PfCDecDeci.tex) = %{tl_version}
Provides:       tex(PfCDecompFrac.tex) = %{tl_version}
Provides:       tex(PfCDecompFracDeci.tex) = %{tl_version}
Provides:       tex(PfCDecomposerNombrePremier.tex) = %{tl_version}
Provides:       tex(PfCDefiCalc.tex) = %{tl_version}
Provides:       tex(PfCDefiTables.tex) = %{tl_version}
Provides:       tex(PfCDessinAlgo.tex) = %{tl_version}
Provides:       tex(PfCDessinGradue.tex) = %{tl_version}
Provides:       tex(PfCDessinerRatio.tex) = %{tl_version}
Provides:       tex(PfCDiagrammeRadar.tex) = %{tl_version}
Provides:       tex(PfCDistributivite.tex) = %{tl_version}
Provides:       tex(PfCDobble.tex) = %{tl_version}
Provides:       tex(PfCDomino.tex) = %{tl_version}
Provides:       tex(PfCDontCountDots.tex) = %{tl_version}
Provides:       tex(PfCEcrireunQCM.tex) = %{tl_version}
Provides:       tex(PfCEcritureLettres.tex) = %{tl_version}
Provides:       tex(PfCEcritureUnites.tex) = %{tl_version}
Provides:       tex(PfCEngrenagesBase.tex) = %{tl_version}
Provides:       tex(PfCEnigmeAire.tex) = %{tl_version}
Provides:       tex(PfCEnquete.tex) = %{tl_version}
Provides:       tex(PfCEquationBalance.tex) = %{tl_version}
Provides:       tex(PfCEquationComposition2.tex) = %{tl_version}
Provides:       tex(PfCEquationLaurent1.tex) = %{tl_version}
Provides:       tex(PfCEquationModeleBarre.tex) = %{tl_version}
Provides:       tex(PfCEquationPose1.tex) = %{tl_version}
Provides:       tex(PfCEquationSoustraction2.tex) = %{tl_version}
Provides:       tex(PfCEquationSymbole1.tex) = %{tl_version}
Provides:       tex(PfCEquationTerme1.tex) = %{tl_version}
Provides:       tex(PfCEratosthene.tex) = %{tl_version}
Provides:       tex(PfCFactorisation.tex) = %{tl_version}
Provides:       tex(PfCFicheMemo.tex) = %{tl_version}
Provides:       tex(PfCFonctionAffine.tex) = %{tl_version}
Provides:       tex(PfCFractionAireCarre.tex) = %{tl_version}
Provides:       tex(PfCFractionNombre.tex) = %{tl_version}
Provides:       tex(PfCFrise.tex) = %{tl_version}
Provides:       tex(PfCFubuki.tex) = %{tl_version}
Provides:       tex(PfCFutoshiki.tex) = %{tl_version}
Provides:       tex(PfCGaram.tex) = %{tl_version}
Provides:       tex(PfCGeometrie.tex) = %{tl_version}
Provides:       tex(PfCGrades.tex) = %{tl_version}
Provides:       tex(PfCGrimuku.tex) = %{tl_version}
Provides:       tex(PfCHiddenMessage.tex) = %{tl_version}
Provides:       tex(PfCHorloge.tex) = %{tl_version}
Provides:       tex(PfCInfixRPN.sty) = %{tl_version}
Provides:       tex(PfCIteration.tex) = %{tl_version}
Provides:       tex(PfCJeton.tex) = %{tl_version}
Provides:       tex(PfCJeuRangement.tex) = %{tl_version}
Provides:       tex(PfCKakurasu.tex) = %{tl_version}
Provides:       tex(PfCKakuro.tex) = %{tl_version}
Provides:       tex(PfCKenKen.tex) = %{tl_version}
Provides:       tex(PfCLabyrintheJeu.tex) = %{tl_version}
Provides:       tex(PfCLabyrintheNombre.tex) = %{tl_version}
Provides:       tex(PfCLego.tex) = %{tl_version}
Provides:       tex(PfCLignesBrisees.tex) = %{tl_version}
Provides:       tex(PfCMentalo.tex) = %{tl_version}
Provides:       tex(PfCMidpoint.tex) = %{tl_version}
Provides:       tex(PfCModeleBarre.tex) = %{tl_version}
Provides:       tex(PfCMonnaieEuro.tex) = %{tl_version}
Provides:       tex(PfCMosaique.tex) = %{tl_version}
Provides:       tex(PfCMotsCodes.tex) = %{tl_version}
Provides:       tex(PfCMotsCroises.tex) = %{tl_version}
Provides:       tex(PfCMotsEmpiles.tex) = %{tl_version}
Provides:       tex(PfCMulArt.tex) = %{tl_version}
Provides:       tex(PfCMulEthiopie.tex) = %{tl_version}
Provides:       tex(PfCMulJal.tex) = %{tl_version}
Provides:       tex(PfCMulJap.tex) = %{tl_version}
Provides:       tex(PfCMulPiecesPuzzle.tex) = %{tl_version}
Provides:       tex(PfCNombreAstral.tex) = %{tl_version}
Provides:       tex(PfCNonogramme.tex) = %{tl_version}
Provides:       tex(PfCNotionFonction.tex) = %{tl_version}
Provides:       tex(PfCNumberHive.tex) = %{tl_version}
Provides:       tex(PfCNumerationsAnciennes.tex) = %{tl_version}
Provides:       tex(PfCOpCroisees.tex) = %{tl_version}
Provides:       tex(PfCOperationsTrou.tex) = %{tl_version}
Provides:       tex(PfCPanneauxRoutiers.tex) = %{tl_version}
Provides:       tex(PfCPapiers.tex) = %{tl_version}
Provides:       tex(PfCPatronPaves.tex) = %{tl_version}
Provides:       tex(PfCPattern.tex) = %{tl_version}
Provides:       tex(PfCPatternJeton.tex) = %{tl_version}
Provides:       tex(PfCPavage.tex) = %{tl_version}
Provides:       tex(PfCPavageAvecMotifImage.tex) = %{tl_version}
Provides:       tex(PfCPixelArt.tex) = %{tl_version}
Provides:       tex(PfCPointsBlancs.tex) = %{tl_version}
Provides:       tex(PfCPourcentage.tex) = %{tl_version}
Provides:       tex(PfCProbaFrequence.tex) = %{tl_version}
Provides:       tex(PfCProbabilites.tex) = %{tl_version}
Provides:       tex(PfCProgrammeCalcul.tex) = %{tl_version}
Provides:       tex(PfCPropor.tex) = %{tl_version}
Provides:       tex(PfCProprietesDroites.tex) = %{tl_version}
Provides:       tex(PfCPuissanceQuatre.tex) = %{tl_version}
Provides:       tex(PfCPuzzleSommePyramide.tex) = %{tl_version}
Provides:       tex(PfCPyraVoca.tex) = %{tl_version}
Provides:       tex(PfCPyramideCalculs.tex) = %{tl_version}
Provides:       tex(PfCPythagore.tex) = %{tl_version}
Provides:       tex(PfCQuestionsFlash.tex) = %{tl_version}
Provides:       tex(PfCQuestionsRelier.tex) = %{tl_version}
Provides:       tex(PfCQuiSuisJe.tex) = %{tl_version}
Provides:       tex(PfCRLE.tex) = %{tl_version}
Provides:       tex(PfCRangementNombres.tex) = %{tl_version}
Provides:       tex(PfCRapido.tex) = %{tl_version}
Provides:       tex(PfCRappelsFormules.tex) = %{tl_version}
Provides:       tex(PfCRecyclage.tex) = %{tl_version}
Provides:       tex(PfCReperage.tex) = %{tl_version}
Provides:       tex(PfCRepresentationGraphique.tex) = %{tl_version}
Provides:       tex(PfCRepresenterEntier.tex) = %{tl_version}
Provides:       tex(PfCRepresenterFraction.tex) = %{tl_version}
Provides:       tex(PfCRepresenterTableur.tex) = %{tl_version}
Provides:       tex(PfCReseauxSociaux.tex) = %{tl_version}
Provides:       tex(PfCResoudreEquation.tex) = %{tl_version}
Provides:       tex(PfCRondeInfernale.tex) = %{tl_version}
Provides:       tex(PfCRose.tex) = %{tl_version}
Provides:       tex(PfCRullo.tex) = %{tl_version}
Provides:       tex(PfCScrabble.tex) = %{tl_version}
Provides:       tex(PfCScratch.tex) = %{tl_version}
Provides:       tex(PfCSerpent.tex) = %{tl_version}
Provides:       tex(PfCShikaku.tex) = %{tl_version}
Provides:       tex(PfCSimplifierFraction.tex) = %{tl_version}
Provides:       tex(PfCSolides.tex) = %{tl_version}
Provides:       tex(PfCSommeAngles.tex) = %{tl_version}
Provides:       tex(PfCSquaro.tex) = %{tl_version}
Provides:       tex(PfCStatistiques.tex) = %{tl_version}
Provides:       tex(PfCSystemeImage.tex) = %{tl_version}
Provides:       tex(PfCTableauDoubleEntree.tex) = %{tl_version}
Provides:       tex(PfCTableauxUnites.tex) = %{tl_version}
Provides:       tex(PfCTablesOperations.tex) = %{tl_version}
Provides:       tex(PfCTectonic.tex) = %{tl_version}
Provides:       tex(PfCThales.tex) = %{tl_version}
Provides:       tex(PfCTicketCaisse.tex) = %{tl_version}
Provides:       tex(PfCTortueBase.tex) = %{tl_version}
Provides:       tex(PfCTrigonometrie.tex) = %{tl_version}
Provides:       tex(PfCTrio.tex) = %{tl_version}
Provides:       tex(PfCTriominos.tex) = %{tl_version}
Provides:       tex(PfCUrneProba.tex) = %{tl_version}
Provides:       tex(PfCVisualisationMulDeci.tex) = %{tl_version}
Provides:       tex(PfCVueCubes.tex) = %{tl_version}
Provides:       tex(PfCYohaku.tex) = %{tl_version}
Provides:       tex(ProfCollege.sty) = %{tl_version}

%description -n texlive-profcollege
This package provides some commands to help French mathematics teachers for
11-16 years olds, for example: \Tableau[Metre] to write the tabular km|hm|...
with some facilities, \Pythagore{ABC}{5}{7} to write the entire calculation of
AC with the Pythagorean theorem, \Trigo[Cosinus]{ABC}{3}{}{60} to write the
entire calculation of AC with cosine, ... and some others.

%package -n texlive-proflabo
Summary:        Draw laboratory equipment
Version:        svn63147
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(pgf.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(ProfLabo.sty) = %{tl_version}

%description -n texlive-proflabo
This package was developed to help French chemistry teachers to create drawings
(using TikZ) for laboratory stuff.

%package -n texlive-proflycee
Summary:        A LaTeX package for French maths teachers in high school
Version:        svn77424
License:        LPPL-1.3c AND CC0-1.0 AND MIT AND CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(nicefrac.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(pythontex.sty)
Requires:       tex(randomlist.sty)
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-tab.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xintbinhex.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ProfLycee-Light.sty) = %{tl_version}
Provides:       tex(ProfLycee-Macros.sty) = %{tl_version}
Provides:       tex(ProfLycee-Pictosbac.sty) = %{tl_version}
Provides:       tex(ProfLycee.sty) = %{tl_version}
Provides:       tex(proflycee-tools-aleatoire.tex) = %{tl_version}
Provides:       tex(proflycee-tools-analyse.tex) = %{tl_version}
Provides:       tex(proflycee-tools-arithm.tex) = %{tl_version}
Provides:       tex(proflycee-tools-cliparts.tex) = %{tl_version}
Provides:       tex(proflycee-tools-competences.tex) = %{tl_version}
Provides:       tex(proflycee-tools-complexes.tex) = %{tl_version}
Provides:       tex(proflycee-tools-ecritures.tex) = %{tl_version}
Provides:       tex(proflycee-tools-espace.tex) = %{tl_version}
Provides:       tex(proflycee-tools-exams.tex) = %{tl_version}
Provides:       tex(proflycee-tools-geom.tex) = %{tl_version}
Provides:       tex(proflycee-tools-graphiques.tex) = %{tl_version}
Provides:       tex(proflycee-tools-listings.tex) = %{tl_version}
Provides:       tex(proflycee-tools-minted.tex) = %{tl_version}
Provides:       tex(proflycee-tools-piton.tex) = %{tl_version}
Provides:       tex(proflycee-tools-probas.tex) = %{tl_version}
Provides:       tex(proflycee-tools-pythontex.tex) = %{tl_version}
Provides:       tex(proflycee-tools-recreat.tex) = %{tl_version}
Provides:       tex(proflycee-tools-stats.tex) = %{tl_version}
Provides:       tex(proflycee-tools-suites.tex) = %{tl_version}
Provides:       tex(proflycee-tools-trigo.tex) = %{tl_version}

%description -n texlive-proflycee
This package provides some commands to help French mathematics teachers for
15-18 years olds, for example: solve equations to approximation ; calculate an
approximate value of an integral ; present Python code or pseudocode, a Python
execution console ; simplify calculations in fractional form, simplify roots ;
display and use a trigonometric circle ; display a small diagram for the sign
of an affine function or a trinomial ; ...

%package -n texlive-profsio
Summary:        Commands (with TikZ) to work with French "BTS SIO" maths themes
Version:        svn76398
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(luacode.sty)
Requires:       tex(lualinalg.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(systeme.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintbinhex.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ProfSio.sty) = %{tl_version}

%description -n texlive-profsio
This package provides some commands (in French) to work with: tables of
Karnaugh ; MPM graphs ; simple graphs.

%package -n texlive-tabvar
Summary:        Typesetting tables showing variations of functions
Version:        svn63921
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(varwidth.sty)
Provides:       tex(tabvar.sty) = %{tl_version}

%description -n texlive-tabvar
This LaTeX package is meant to ease the typesetting of tables showing
variations of functions as they are used in France.

%package -n texlive-tdsfrmath
Summary:        Macros for French teachers of mathematics
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tdsfrmath.sty) = %{tl_version}

%description -n texlive-tdsfrmath
A collection of macros for French maths teachers in colleges and lycees (and
perhaps elsewhere). It is hoped that the package will facilitate the everyday
use of LaTeX by mathematics teachers.

%package -n texlive-texlive-fr
Summary:        TeX Live manual (French)
Version:        svn74301
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-fr-doc <= 11:%{version}

%description -n texlive-texlive-fr
TeX Live manual (French)

%package -n texlive-translation-array-fr
Summary:        French translation of the documentation of array
Version:        svn24344
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-array-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-array-fr-doc <= 11:%{version}

%description -n texlive-translation-array-fr
A French translation of the documentation of array.

%package -n texlive-translation-dcolumn-fr
Summary:        French translation of the documentation of dcolumn
Version:        svn24345
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-dcolumn-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-dcolumn-fr-doc <= 11:%{version}

%description -n texlive-translation-dcolumn-fr
A French translation of the documentation of dcolumn.

%package -n texlive-translation-natbib-fr
Summary:        French translation of the documentation of natbib
Version:        svn25105
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-natbib-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-natbib-fr-doc <= 11:%{version}

%description -n texlive-translation-natbib-fr
A French translation of the documentation of natbib.

%package -n texlive-translation-tabbing-fr
Summary:        French translation of the documentation of Tabbing
Version:        svn24228
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-tabbing-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-tabbing-fr-doc <= 11:%{version}

%description -n texlive-translation-tabbing-fr
A translation to French (by the author) of the documentation of the Tabbing
package.

%package -n texlive-variations
Summary:        Typeset tables of variations of functions
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(variations.sty) = %{tl_version}
Provides:       tex(variations.tex) = %{tl_version}

%description -n texlive-variations
The package provides macros for typesetting tables showing variations of
functions according to French usage. These macros may be used by both LaTeX and
plain TeX users.

%package -n texlive-visualfaq-fr
Summary:        FAQ LaTeX visuelle francophone
Version:        svn71053
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-visualfaq-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-visualfaq-fr-doc <= 11:%{version}

%description -n texlive-visualfaq-fr
(French version below.) The Visual LaTeX FAQ is an innovative new search
interface on LaTeX Frequently Asked Questions. This version is a French
translation, offering links to the French-speaking LaTeX FAQ. Vous avez du mal
a trouver la reponse a une question sur LaTeX ou meme a trouver les mots pour
exprimer votre question? La FAQ LaTeX visuelle est une interface de recherche
innovante qui presente plus d'une centaine d'exemples de mises en forme de
documents frequemment demandees. Il suffit de cliquer sur l'hyperlien qui
correspond a ce que vous souhaitez faire - ou ne pas faire - et la FAQ LaTeX
visuelle enverra votre navigateur web a la page correspondante de la FAQ LaTeX
francophone.

%package -n texlive-visualtikz
Summary:        Visual help for TikZ based on images with minimum text
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-visualtikz-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-visualtikz-doc <= 11:%{version}

%description -n texlive-visualtikz
Visual help for TikZ based on images with minimum text: an image per command or
parameter. The document is in French, but will be translated into English
later.

%post -n texlive-hyphen-basque
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/basque.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "basque loadhyph-eu.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{basque}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{basque}{loadhyph-eu.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-basque
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/basque.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{basque}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-french
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/french.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "french loadhyph-fr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=patois.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=patois" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=francais.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=francais" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{french}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{french}{loadhyph-fr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{patois}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{patois}{loadhyph-fr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{francais}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{francais}{loadhyph-fr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-french
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/french.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=patois.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=francais.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{french}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{patois}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{francais}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-aeguill
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/aeguill/
%doc %{_texmf_main}/doc/latex/aeguill/

%files -n texlive-annee-scolaire
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/annee-scolaire/
%doc %{_texmf_main}/doc/latex/annee-scolaire/

%files -n texlive-apprendre-a-programmer-en-tex
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/plain/apprendre-a-programmer-en-tex/

%files -n texlive-apprends-latex
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/apprends-latex/

%files -n texlive-babel-basque
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-basque/
%doc %{_texmf_main}/doc/generic/babel-basque/

%files -n texlive-babel-french
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-french/
%doc %{_texmf_main}/doc/generic/babel-french/

%files -n texlive-basque-book
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/basque-book/
%doc %{_texmf_main}/doc/latex/basque-book/

%files -n texlive-basque-date
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/basque-date/
%doc %{_texmf_main}/doc/latex/basque-date/

%files -n texlive-bib-fr
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/bib-fr/
%doc %{_texmf_main}/doc/bibtex/bib-fr/

%files -n texlive-bibleref-french
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-french/
%doc %{_texmf_main}/doc/latex/bibleref-french/

%files -n texlive-booktabs-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/booktabs-fr/

%files -n texlive-cahierprof
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cahierprof/
%doc %{_texmf_main}/doc/latex/cahierprof/

%files -n texlive-couleurs-fr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/couleurs-fr/
%doc %{_texmf_main}/doc/latex/couleurs-fr/

%files -n texlive-droit-fr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/droit-fr/
%doc %{_texmf_main}/doc/latex/droit-fr/

%files -n texlive-e-french
%license lppl1.3c.txt
%{_texmf_main}/makeindex/e-french/
%{_texmf_main}/tex/generic/e-french/
%doc %{_texmf_main}/doc/generic/e-french/

%files -n texlive-epslatex-fr
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/epslatex-fr/

%files -n texlive-expose-expl3-dunkerque-2019
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/expose-expl3-dunkerque-2019/

%files -n texlive-facture
%license other-free.txt
%{_texmf_main}/tex/xelatex/facture/
%doc %{_texmf_main}/doc/xelatex/facture/

%files -n texlive-faq-fr
%license cc-by-sa-4.txt
%doc %{_texmf_main}/doc/latex/faq-fr/

%files -n texlive-faq-fr-gutenberg
%license cc-by-sa-4.txt
%doc %{_texmf_main}/doc/latex/faq-fr-gutenberg/

%files -n texlive-formation-latex-ul
%license cc-by-4.txt
%doc %{_texmf_main}/doc/latex/formation-latex-ul/

%files -n texlive-frenchmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/frenchmath/
%doc %{_texmf_main}/doc/latex/frenchmath/

%files -n texlive-frletter
%license pd.txt
%{_texmf_main}/tex/latex/frletter/
%doc %{_texmf_main}/doc/latex/frletter/

%files -n texlive-frpseudocode
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/frpseudocode/
%doc %{_texmf_main}/doc/latex/frpseudocode/

%files -n texlive-hyphen-basque
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-french
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-impatient-fr
%license fdl.txt
%doc %{_texmf_main}/doc/plain/impatient-fr/

%files -n texlive-impnattypo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/impnattypo/
%doc %{_texmf_main}/doc/latex/impnattypo/

%files -n texlive-l2tabu-french
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/l2tabu-french/

%files -n texlive-latex2e-help-texinfo-fr
%license pd.txt
%doc %{_texmf_main}/doc/info/
%doc %{_texmf_main}/doc/latex/latex2e-help-texinfo-fr/

%files -n texlive-letgut
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/letgut/
%doc %{_texmf_main}/doc/lualatex/letgut/

%files -n texlive-lshort-french
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-french/

%files -n texlive-mafr
%license gpl2.txt
%{_texmf_main}/tex/latex/mafr/
%doc %{_texmf_main}/doc/latex/mafr/

%files -n texlive-matapli
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/matapli/
%doc %{_texmf_main}/doc/latex/matapli/

%files -n texlive-panneauxroute
%license lppl1.3c.txt
%license other-free.txt
%{_texmf_main}/tex/latex/panneauxroute/
%doc %{_texmf_main}/doc/latex/panneauxroute/

%files -n texlive-profcollege
%license lppl1.3c.txt
%{_texmf_main}/metapost/profcollege/
%{_texmf_main}/tex/latex/profcollege/
%doc %{_texmf_main}/doc/latex/profcollege/

%files -n texlive-proflabo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/proflabo/
%doc %{_texmf_main}/doc/latex/proflabo/

%files -n texlive-proflycee
%license lppl1.3c.txt
%license cc-zero-1.txt
%license mit.txt
%license other-free.txt
%{_texmf_main}/metapost/proflycee/
%{_texmf_main}/tex/latex/proflycee/
%doc %{_texmf_main}/doc/latex/proflycee/

%files -n texlive-profsio
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/profsio/
%doc %{_texmf_main}/doc/latex/profsio/

%files -n texlive-tabvar
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/tabvar/
%{_texmf_main}/fonts/map/dvips/tabvar/
%{_texmf_main}/fonts/tfm/public/tabvar/
%{_texmf_main}/fonts/type1/public/tabvar/
%{_texmf_main}/metapost/tabvar/
%{_texmf_main}/tex/latex/tabvar/
%doc %{_texmf_main}/doc/latex/tabvar/

%files -n texlive-tdsfrmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tdsfrmath/
%doc %{_texmf_main}/doc/latex/tdsfrmath/

%files -n texlive-texlive-fr
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-fr/

%files -n texlive-translation-array-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-array-fr/

%files -n texlive-translation-dcolumn-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-dcolumn-fr/

%files -n texlive-translation-natbib-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-natbib-fr/

%files -n texlive-translation-tabbing-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-tabbing-fr/

%files -n texlive-variations
%license gpl2.txt
%{_texmf_main}/tex/generic/variations/
%doc %{_texmf_main}/doc/generic/variations/

%files -n texlive-visualfaq-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/visualfaq-fr/

%files -n texlive-visualtikz
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/visualtikz/

%changelog
%autochangelog
