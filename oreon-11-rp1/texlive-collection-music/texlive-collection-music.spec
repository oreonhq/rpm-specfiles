%global source0_hash d9acc852d934360f8d5c8a2cfa08a9809b971f20fd6c7bb7fc5aca5318e86c5e1b68c6d2c06399a19cdea5af1358cecab64e3365b319a6dcac19659197c0f919

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-music
Epoch:          12
Version:        svn76267
Release:        1%{?dist}
Summary:        Music packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 8b1ccd152ed2ad90810551a36f0fa7f114625784fa967f70b67559f9f1e8eb32d7edd08efc9e55dd92723df4039d1bdcc212200d712e99f27de84a153c2a3777
%global source3_hash 5f127f8e1ec104b40ac4d5e9bb22965e9376033892362073cdea9f65f1f10a4152f237b4f27bf52dbbe1389f59d3da673434c39a2b3f43d6f17aa60caabd5584
%global source4_hash 7d815e23e9b5d686e0df54c4a0ad51c85360c7b3879695977fb9be2b69cb343e1c9043c2595ac5554e87e0a568b2441bd16a43b334af4b43e5302eba19bc33d8
%global source5_hash 696047cc4965a06388a61232af9336f2010fdb0b869914cf66ac9b052d1efd85ff05119a277aa127cf05f56e03b63060956c7c284df78e93b0f0beabd691d33a
%global source6_hash 8f0e2619e35b40852f8c7f9d7e20cf47ff8c62cc12f1f5e132f0609033fdeb59fab4c9f04361b5f71f2192feaeb554565a0a2dbcc1db586445775c87d8bba4a2
%global source7_hash bab572050139cb08a95551d575d77fac97fb551ff2ff60107a9bdcd97d64ba92a8af66528d116ef7ffe06f4afb2536b7de1c2d55b6f12d7ad65f8d40001cccb3
%global source8_hash 0e07cae95a8ee5f040b4df4d94f996f772f0780bbe47c77db891fbf44b08f20e28ba8442dee3e981a052b0ccebb0d630e0f0917eb7c65a490c844a65f3b2e3f4
%global source9_hash 0826513579953ea80047d596b6c577e4b6f00fcdddb7a06bdc953bccd72e09ec2fd9123995c1e04260ad880bc860454abd283885817a9eb359ec7cb5beba3cc5
%global source10_hash 4f24136d55035a38ababae0254618857f4670a51a3f15cf451b1ee562800b2638e0518bb1458504b2b9646ca28cc7dfafd019edfe8cf43c2346f64a171645621
%global source11_hash 62735218a1555a64073d729bcee34b35b1fedac3030d1ce15bcd8b308338c855e3d4abf0c6d71409ca4dfb88002e532b1339a7d7e7bdaf6e23bc0e7e64d507fa
%global source12_hash 2fdc1114b03123c35eccd6b617310c714f37015620551538458a1a49b1e9a583aa55b3cb661f204bb9168cee0a7325b066d64315a15a94daa01e43d05bbb2561
%global source13_hash 7dc8140b3b545d2683c471e2e2907a58e2c995f23acea26d763da8989c3288940dcc154ffc0f81ea99169ce574bf90543e94f86bf8217996b7c83474a300806e
%global source14_hash e8f99e452e4816b915d9983ecd0b5dae1c4b6114186661a6c00f61af19465d7c6db678f5815dcb2c809909774924b7dd417efae2289526327ba6de07a871cc14
%global source15_hash 977897d4589040a41ca61f676bd129476f6192094e0c1883bc676a7edf35512697e4309c33b76838c89afc0ec10861982893e236b889a575434e86a637e7abc7
%global source16_hash 3067b7b38d03318cc2cf199ade3688e56c275e6dede4db09e92d1478f53b937b78806927c887c4b2c0d32b772afd697e5098513bd3825ec759c9cfc8c2501aac
%global source17_hash 78a5b7c9a5e71f36e8258923465397070dd64d6d4124f9a30ea967d65995f16d5fb267ff5704c1383b2cd9dd4fe8454ec3e72e12f20de342683c7dcf6c390495
%global source18_hash dabadc0fba92f6da23830069e533e8d4fb234bb679aa355382c03bd3ac13924328ea8fcece3186f36d33b7d7f6cceaebb23f1158b855673160f183991e880796
%global source19_hash d8e715d1c4d9c7ebb0c34c690a82e338733501012ad19cd9e2c52e6b39dff352a4e042bdc5f54e63a03a38eb9c76b5aed2ec3afae88ccd63f56663ada32e828b
%global source20_hash fed7be24d0bff6d2a0022374e4cbb60cda508b0f99a5a96d59060247aad561c1124728f00a6d0a51b3b22f4490c6153df740a5e9d8106da23c85bb18db385195
%global source21_hash 4a2012e693257c2bdb4daf46a2402882caf0c8efbc65bd6679c9eb11440ae75f09d31369839f84312bd1028207d8aa23a745847be1e762dea977ecd7f73b4a87
%global source22_hash 777af4d4ad1a35bef3f0075e2df707c3a3c98969ee688b71c3d13449b04ecfcb2d82ed9332a8aae81a3bd825462c2cbbf840b16a72fc6e3f65e7565ef6b1b164
%global source23_hash f7508a78fd341e4d4d0fa8a0f89a14420ca50d590bc4a1f5208d4130a3aa84048faa8720545c24e8f0243b1f062a6f40cb5cccdd9ed7db583a11fff1a40c7eeb
%global source24_hash a4866683cb639b63d455f40da2ef58ee4c69d0e29e5071437a07922a0a45598677557ce609905dd8fc5c3e40a98bceb9a753cf4506342585e6cc2c37fa591271
%global source25_hash ef5f516db586d1473d949f44a2eb9fb307b84ea5a7dcc3c9419298203b41c54ff4dad75d3b24cf30fbc24f4c60ad4b79b9c1fd58804667732a66b0ccb52cc3b4
%global source26_hash ecacc9ccb513c745f92ec47533028bae32751eea9180fcfd5999e51fbb4639c054556503044bb0be9f2c586c2d46af63da302da4c9be3554dd60b89c29a67717
%global source27_hash 439d9c3bd53fb0715417e4a6a01d33aa088945bcbc460713d76d8d5bb35a9ab6a159e5f1ee6660949e461749952ad40f22a87440c2d7eb32530dc1027fb56c10
%global source28_hash a37c75d55857e9680b8e4b0f59f1889f3b5198477212ea531aa6bbf9ea11dbae06fef7fdba9e706f016c6c0618eebe4ddb81ba73b48979683a22592a0adb119a
%global source29_hash 738c2c467d9df87cb1eccf0442b5c94a97a3c4c2b329d78d80b05d2adf9e3be11aaf2fb407ebc29f07e6455e6533464d981ae65122b080aebabdfaa29cf71b61
%global source30_hash 026e310ee9617108ac60fca69b0f08b2031d9c9dc583a400095765458bc72681c5c39332602994fd8a7dd4757b5214924d4f5d75bc5861365ef65e8e33b6e143
%global source31_hash dafae48e690e6f0a2272d268204cbe58967eec5dc895987ecbff563061f23a53bf9d0d39f4a269b852524c1cad8de08fb121aa8291d2c723c01615f4c83b3231
%global source32_hash b981e9cc05c113c4a50715b27d3ee2ac9e862c7c806ca8830590cb99c8564d8df339ff69d0268405e290cbc1902975ad4d801aee7f56f18433f286526f3cb906
%global source33_hash da286e0e7c8f87a71f3c3270cfa8dd27c3a4b1e768d2fd0924b3b594cdeceef3cde36373aae8e52cb7cc8695b23ae99d5b7546f20e02f0899975e7060afc4591
%global source34_hash 4bb8bd0781cd49950f2a80ed9527de1b0e49ef6eefea5787d1d13efa3893d57b48a9b69ddf0f62bd2695a61d9b785cfa1dfad2217f8cd97929e1dfefac9333c6
%global source35_hash c06f45815ff65fa7c492575731bf1aec0e774cf5a81907d1e381ac8ab366c167ada688b8c8fc82293c96980c5361a688eda666b130c1ac3f39976d49bf78f60c
%global source36_hash 65ec293bbb5d48d3023f83a68f736727f526ccc72f7ded00a978929f38e4a7de6d4893a4f80762c1277ccbe51c3cecd536dfb54d233db393162e0bba4b493c56
%global source37_hash 5ec16c3378dfc59ed9e49593b23f5cfbd0c1c6ed39f118c9d58386b8251413ca79a268fbe25396c6a5891a37103c3771d8e319232af5e98db7d12a0066465096
%global source38_hash 6262e1b447f517680ddfd9e5e076ea384dfa7fc8d219e7a2613a80ba66a0f0435d9dc31502f6abbfc150fa1e2de001afbdec25dd5778e3ffe559ea389d57208a
%global source39_hash 8a6c9a42383d6b35c1300b958a7629306a6883bec1bd68751165eb3514f8f069c9995247142bad459e06fa42378a9ddd23093cb749bb2ccd58743312f83425dd
%global source40_hash 53c6f1b80b789608ad1187a2d593474c12d71b27ce9bd8c9c0cc7d2ba1bf3501c2dbab6375f51eb4841646b1f0dc7ed1c641efef6bc32dbaae3cec56f6583e09
%global source41_hash eff2e4596dd426f1f57003d6441eb0632f7b9bbbb216ab4e2b069a1a624e77e06f032f191ba13afd2e55b472f5a719936f34fcf2ba6997336a3c3716c4d936c3
%global source42_hash 99bcfa3ba4e39e321d0a42595cad15c966b581f3d2689d2694c47be5fdf9b1f9fcc9bf8667a90483c580d1c5726831e334fefa4a478e332eecf34c27deeb41c4
%global source43_hash 48c8b951bdbbafabbe29fef04ebb2877cc8c90210bca4b69dcae770bd324b4c59106df7b73ac69eb33ea6cf92de22e5af8aae46c2e464bd942a2c6830602dba8
%global source44_hash a4c94835af4cbd05b47e3e5b045d8247ca0ed2e05186e11f146a02e9cc3279774f53a804ddfeef1ca804aea8f41305d3108a9eafbb3c2d1a68acdb90fc8e8a6d
%global source45_hash dd6bdcb32d663d7cfa147f0416753460c7e2d8c783cf02b940afcf25b6a202ec801f0e247ef73462cd7da970c6a2bfa1ffce8678011f14c6ff7cfee9ba3f2565
%global source46_hash c971f6d21c54b3fc61937c68dc9a9f0db39c14cd16d3e4ae863177c682fe4b09685a2d2502c0ce76221b2e3540f8a29ab2fd7629163f1bfc3944462e0065a864
%global source47_hash cf51fd28a95bbb84e6520875652f43b5e302723e35dd711b9014967364e591da41f293a35babf91f79ac0efbb333d140ae7a3ca09c1c5730da585c6f853acdf0
%global source48_hash f7a3673e71d1231a815bd3063cca218f48b4ce4302a2eaed70e0e890f9b1bf6b79f2ce098ea2b38f80a8aba17ae7fd374e74c5258ce508f294e511391fc19541
%global source49_hash 36f0dab37a72f0ba8fee20330f6cf717f9efe6ab1c5573b8aa1fa212f3969d4c92810238b4720eeab2a25f6d5517e77894f604b9bd2fa500318c720b48f4e8a4
%global source50_hash b98f8981529b6a5813a20f4405831ff6af21d7bfe35a807ca488ab5dcfcd00b5ee76188bba5341832f6c13069e797e8cca7bf03f792527e39bc483c74b827de6
%global source51_hash c94a3e7d755ce30075c4ff62a8386d5ce651ac42511b713a5dbab475ff0856eb2e4df1d89d966d3301e3911e8a0e1e61c1e9763f0c215fb73eea2341754dadc2
%global source52_hash 1429739a09b0d712e93337d0cffb9b2191f1edd058a359894fff8780272650baba1db9895f354899f07822a531fa2b0f2f62e6ef3e58c7d634d91e9f5d9efc6f
%global source53_hash 212e283595f65bd8468e079a949aa255a71163e5b005b955645561e60a044b598fd670a44adcb4f7e1e7de2f579a669130c21bf1406fd2f9a2a06c5949ac2444
%global source54_hash 933038ebcded30e59b2075a064c35a00e5523fae80a6a7091d8a0c44a043d4e9150b68f1cdd6814b3a0346286086b8f5af7b68b2de2c32be1c38684672afc848
%global source55_hash bdb12e362af8ff816c0cc43a76974a8f1ab326486a6b103430fb2139f22cddd27514d2e486cd969179be75684bb6e5fc0bf959f8d8c868ce3d5fe466097a0224
%global source56_hash b732e4059687bd9448adc7a89819c85656031ee6b7e3f87d6da1043979c570dea9e464dd0268e1992912c4c9c2af66711baac1961719b4b86a98b9048d0ce55f
%global source57_hash 0788040caad4f288a004a7cac02bc455f6a078782b40b63119e910b9b257ba48543736cdf41c86b5450d2c90816014dffde1d9e490714c7ab9a5481f837ac51e

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-music.tar.xz#/collection-music.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abc.tar.xz#/abc.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abc.doc.tar.xz#/abc.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bagpipe.tar.xz#/bagpipe.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bagpipe.doc.tar.xz#/bagpipe.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chordbars.tar.xz#/chordbars.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chordbars.doc.tar.xz#/chordbars.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chordbox.tar.xz#/chordbox.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chordbox.doc.tar.xz#/chordbox.doc.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ddphonism.tar.xz#/ddphonism.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ddphonism.doc.tar.xz#/ddphonism.doc.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figbas.tar.xz#/figbas.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figbas.doc.tar.xz#/figbas.doc.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fretplot.tar.xz#/fretplot.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fretplot.doc.tar.xz#/fretplot.doc.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gchords.tar.xz#/gchords.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gchords.doc.tar.xz#/gchords.doc.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gtrcrd.tar.xz#/gtrcrd.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gtrcrd.doc.tar.xz#/gtrcrd.doc.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitar.tar.xz#/guitar.or11.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitar.doc.tar.xz#/guitar.doc.or11.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitarchordschemes.tar.xz#/guitarchordschemes.or11.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitarchordschemes.doc.tar.xz#/guitarchordschemes.doc.or11.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitartabs.tar.xz#/guitartabs.or11.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitartabs.doc.tar.xz#/guitartabs.doc.or11.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harmony.tar.xz#/harmony.or11.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harmony.doc.tar.xz#/harmony.doc.or11.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex4musicians.tar.xz#/latex4musicians.or11.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex4musicians.doc.tar.xz#/latex4musicians.doc.or11.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/leadsheets.tar.xz#/leadsheets.or11.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/leadsheets.doc.tar.xz#/leadsheets.doc.or11.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liederbuch.tar.xz#/liederbuch.or11.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liederbuch.doc.tar.xz#/liederbuch.doc.or11.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musical.tar.xz#/musical.or11.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musical.doc.tar.xz#/musical.doc.or11.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musicography.tar.xz#/musicography.or11.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musicography.doc.tar.xz#/musicography.doc.or11.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixguit.tar.xz#/musixguit.or11.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixguit.doc.tar.xz#/musixguit.doc.or11.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixtex-fonts.tar.xz#/musixtex-fonts.or11.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixtex-fonts.doc.tar.xz#/musixtex-fonts.doc.or11.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/octave.tar.xz#/octave.or11.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/octave.doc.tar.xz#/octave.doc.or11.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piano.tar.xz#/piano.or11.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piano.doc.tar.xz#/piano.doc.or11.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/recorder-fingering.tar.xz#/recorder-fingering.or11.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/recorder-fingering.doc.tar.xz#/recorder-fingering.doc.or11.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songbook.tar.xz#/songbook.or11.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songbook.doc.tar.xz#/songbook.doc.or11.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songproj.tar.xz#/songproj.or11.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songproj.doc.tar.xz#/songproj.doc.or11.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songs.tar.xz#/songs.or11.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songs.doc.tar.xz#/songs.doc.or11.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undar-digitacion.tar.xz#/undar-digitacion.or11.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undar-digitacion.doc.tar.xz#/undar-digitacion.doc.or11.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpiano.tar.xz#/xpiano.or11.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpiano.doc.tar.xz#/xpiano.doc.or11.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-abc
Requires:       texlive-autosp
Requires:       texlive-bagpipe
Requires:       texlive-chordbars
Requires:       texlive-chordbox
Requires:       texlive-collection-latex
Requires:       texlive-ddphonism
Requires:       texlive-figbas
Requires:       texlive-fretplot
Requires:       texlive-gchords
Requires:       texlive-gregoriotex
Requires:       texlive-gtrcrd
Requires:       texlive-guitar
Requires:       texlive-guitarchordschemes
Requires:       texlive-guitartabs
Requires:       texlive-harmony
Requires:       texlive-latex4musicians
Requires:       texlive-leadsheets
Requires:       texlive-liederbuch
Requires:       texlive-lilyglyphs
Requires:       texlive-lyluatex
Requires:       texlive-m-tx
Requires:       texlive-musical
Requires:       texlive-musicography
Requires:       texlive-musixguit
Requires:       texlive-musixtex
Requires:       texlive-musixtex-fonts
Requires:       texlive-musixtnt
Requires:       texlive-octave
Requires:       texlive-piano
Requires:       texlive-pmx
Requires:       texlive-pmxchords
Requires:       texlive-recorder-fingering
Requires:       texlive-songbook
Requires:       texlive-songproj
Requires:       texlive-songs
Requires:       texlive-undar-digitacion
Requires:       texlive-xml2pmx
Requires:       texlive-xpiano

%description
Music-related fonts and packages.

%package -n texlive-abc
Summary:        Support ABC music notation in LaTeX
Version:        svn41157
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(abc.sty) = %{tl_version}
Provides:       tex(mup.sty) = %{tl_version}

%description -n texlive-abc
The abc package lets you include lines of music written in the ABC Plus
language. The package will then employ the \write18 facility to convert your
notation to PostScript (using the established utility abcm2ps) and hence to the
format needed for inclusion in your document.

%package -n texlive-bagpipe
Summary:        Support for typesetting bagpipe music
Version:        svn34393
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bagpipe.tex) = %{tl_version}

%description -n texlive-bagpipe
Typesetting bagpipe music in MusixTeX is needlessly tedious. This package
provides specialized and re-defined macros to simplify this task.

%package -n texlive-chordbars
Summary:        Print chord grids for pop/jazz tunes
Version:        svn70392
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(relsize.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-euclide.sty)
Requires:       tex(wasysym.sty)
Provides:       tex(chordbars.sty) = %{tl_version}

%description -n texlive-chordbars
This Tikz-based music-related package is targeted at pop/jazz guitar/bass/piano
musicians. They usually need only the chords and the song structure. This
package produces rectangular song patterns with "one square per bar", with the
chord shown inside the square. It also handles the song structure by showing
the bar count and the repetitions of the patterns.

%package -n texlive-chordbox
Summary:        Draw chord diagrams
Version:        svn51000
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xstring.sty)
Provides:       tex(chordbox.sty) = %{tl_version}

%description -n texlive-chordbox
This package provides two macros for drawing chord diagrams, as may be found
for example in chord charts/books and educational materials. They are composed
as TikZ pictures and have several options to modify their appearance.

%package -n texlive-ddphonism
Summary:        Dodecaphonic diagrams: twelve-tone matrices, clock diagrams, etc.
Version:        svn75201
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(ddphonism.sty) = %{tl_version}

%description -n texlive-ddphonism
This music-related package focuses on notation from the Twelve-Tone System,
also called Dodecaphonism. It provides LaTeX algorithms to generate common
dodecaphonic diagrams based off a musical series, or row sequence, of arbitrary
length. The package requires TikZ.

%package -n texlive-figbas
Summary:        Mini-fonts for figured-bass notation in music
Version:        svn28943
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-figbas
This package consists of three mini-fonts (and associated metrics) of
conventional ligatures for the figured-bass notations 2+, 4+, 5+, 6+ and 9+ in
music manuscripts. The fonts are usable with Computer Modern Roman and Sans,
and Palatino/Palladio, respectively.

%package -n texlive-fretplot
Summary:        Create scale and chord diagrams for guitar-like instruments
Version:        svn76337
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(fretplot.sty) = %{tl_version}

%description -n texlive-fretplot
This LuaLaTeX package provides batch generation of scale and chord diagrams for
plucked string instruments, such as the guitar. Flexible and Automated: Highly
customizable and automatable via simple, powerful file formats for describing
fretboard diagrams. Easily generate batches of diagrams. Attractive Defaults:
Comes with sensible, visually appealing default settings. Music Theory Aware:
Includes easy-to-use LaTeX macros that understand music theory. Render guitar
scale diagrams by specifying the musical scale or scale type via built-in
macros or directly via degree, pitch class, or interval formulae.

%package -n texlive-gchords
Summary:        Typeset guitar chords
Version:        svn29803
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gchords.sty) = %{tl_version}

%description -n texlive-gchords
A LaTeX package for typesetting of guitar chord diagrams, including options for
chord names, finger numbers and typesetting above lyrics. The bundle also
includes a TCL script (chordbox.tcl) that provides a graphical application
which creates LaTeX files that use gchords.sty.

%package -n texlive-gtrcrd
Summary:        Add chords to lyrics
Version:        svn32484
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gtrcrd.sty) = %{tl_version}

%description -n texlive-gtrcrd
The package provides the means to specify guitar chords to be played with each
part of the lyrics of a song. The syntax of the macros reduces the chance of
failing to provide a chord where one is needed, and the structure of the macros
ensures that the chord specification appears immediately above the start of the
lyric.

%package -n texlive-guitar
Summary:        Guitar chords and song texts
Version:        svn32258
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(toolbox.sty)
Provides:       tex(guitar.sty) = %{tl_version}

%description -n texlive-guitar
(La)TeX macros for typesetting guitar chords over song texts. The toolbox
package is required. Note that this package only places arbitrary TeX code over
the lyrics. To typeset the chords graphically (and not only by name), the
author recommends use of an additional package such as gchords by K. Peeters.

%package -n texlive-guitarchordschemes
Summary:        Guitar Chord and Scale Tablatures
Version:        svn54512
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cnltx-base.sty)
Requires:       tex(tikz.sty)
Provides:       tex(guitarchordschemes.sty) = %{tl_version}

%description -n texlive-guitarchordschemes
This package provides two commands (\chordscheme and \scales). With those
commands it is possible to draw schematic diagrams of guitar chord tablatures
and scale tablatures. Both commands know a range of options that allow wide
customization of the output. The package's drawing is done with the help of
TikZ.

%package -n texlive-guitartabs
Summary:        A class for drawing guitar tablatures easily
Version:        svn48102
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-guitartabs
This package provides is a simple LaTeX2e class that allows guitarists to
create basic guitar tablatures using LaTeX. Create music and do not be bothered
with macro programming. The class depends on the LaTeX packages geometry,
harmony, inputenc, intcalc, musixtex, tikz, and xifthen, as well as the article
class.

%package -n texlive-harmony
Summary:        Typeset harmony symbols, etc., for musicology
Version:        svn72045
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Provides:       tex(harmony.sty) = %{tl_version}

%description -n texlive-harmony
The package harmony.sty uses the packages ifthen and amssymb from the amsfonts
bundle, together with the LaTeX font lcirclew10 and the font musix13 from
musixtex.

%package -n texlive-latex4musicians
Summary:        A guide for combining LaTeX and music
Version:        svn49759
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex4musicians-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex4musicians-doc <= 11:%{version}

%description -n texlive-latex4musicians
This guide, "LaTeX for Musicians", explains how to create LaTeX documents that
include several kinds of music elements: music symbols, song lyrics, guitar
chords diagrams, lead sheets, music excerpts, guitar tablatures, multi-page
scores.

%package -n texlive-leadsheets
Summary:        Typesetting leadsheets and songbooks
Version:        svn61504
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(translations.sty)
Requires:       tex(xparse.sty)
Provides:       tex(leadsheets.library.chordnames.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.chords.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.external.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.musejazz.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.musicsymbols.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.properties.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.shorthands.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.songs.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.templates.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.translations.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.transposing.code.tex) = %{tl_version}
Provides:       tex(leadsheets.sty) = %{tl_version}

%description -n texlive-leadsheets
This LaTeX package offers support for typesetting simple leadsheets of songs,
i.e. song lyrics and the corresponding chords.

%package -n texlive-liederbuch
Summary:        A LaTeX package for storing songs or other content, and repeated reuse in documents
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(xparse.sty)
Provides:       tex(liederbuch-babel.sty) = %{tl_version}
Provides:       tex(liederbuch-listofsongs.sty) = %{tl_version}
Provides:       tex(liederbuch.sty) = %{tl_version}
Provides:       tex(printliederbuch.sty) = %{tl_version}

%description -n texlive-liederbuch
This package is meant for content which you reuse regularly, like songs in
small booklets. For example the booklets used at church, weddings or similar
events. It has two major parts: You typeset your content once (most likely a
song), garnish it with some meta data and put it into a sty-file. From there
you can insert this content into your document with one single line. The
inserted content can have header and footer that use the meta data (i.e. title,
composer, lyricist). Inside these content fragments, you can use the
\notenzeile (stave line) command to combine an image of a stave line with song
lyrics. If correctly used, the lyrics are placed correctly below the notes and
need most often no or only minor adjustments. With that you can combine any
stave image with LaTeX fonts. You can find resources and inspiration in a demo
project.

%package -n texlive-musical
Summary:        Typeset (musical) theatre scripts
Version:        svn54758
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xspace.sty)
Provides:       tex(musical.sty) = %{tl_version}

%description -n texlive-musical
This package is designed to simplify the development and distribution of
scripts for theatrical musicals, especially ones under development. The output
is formatted to follow generally accepted script style[1] while also
maintaining a high level of typographic integrity, and includes commands for
dialog, lyrics, stage directions, music and dance cues, rehearsal marks, and
more. It gracefully handles dialog that crosses page breaks, and can generate
lists of songs and lists of dances in the show. [1] There are lots of
references for the One True Way to format a script. Naturally, none of them
agree.

%package -n texlive-musicography
Summary:        Accessing symbols for music writing with pdfLaTeX
Version:        svn68220
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(setspace.sty)
Requires:       tex(stackengine.sty)
Provides:       tex(musicography.sty) = %{tl_version}

%description -n texlive-musicography
This package makes available the most commonly used symbols in writing about
music in a way that can be used with pdfLaTeX and looks consistent and
attractive. It includes accidentals, meters, and notes of different rhythmic
values. The package builds on the approach used in the harmony package, where
the symbols are taken from the MusiXTeX fonts. But it provides a larger range
of symbols and a more flexible, user-friendly interface written using xparse
and stackengine.

%package -n texlive-musixguit
Summary:        Easy notation for guitar music, in MusixTeX
Version:        svn21649
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(musixtex.sty)
Requires:       tex(setspace.sty)
Provides:       tex(musixguit.sty) = %{tl_version}

%description -n texlive-musixguit
The package provides commands for typesetting notes for guitar, especially for
simplifying guitar notation with MusixTeX.

%package -n texlive-musixtex-fonts
Summary:        Fonts used by MusixTeX
Version:        svn65517
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-musixtex-fonts
These are fonts for use with MusixTeX; they are provided both as original
Metafont source, and as converted Adobe Type 1. The bundle renders the older
(Type 1 fonts only) bundle musixtex-t1fonts obsolete.

%package -n texlive-octave
Summary:        Typeset musical pitches with octave designations
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(octave.sty) = %{tl_version}

%description -n texlive-octave
This package typesets musical pitch names with designation for the octave in
either the Helmholtz system (with octave numbers), or the traditional system
(with prime symbols). Authors can just write \pitch{C}{4} and the pitches will
be rendered correctly depending on which package option was selected. The
system can also be changed mid-document.

%package -n texlive-piano
Summary:        Typeset a basic 2-octave piano diagram
Version:        svn21574
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xargs.sty)
Provides:       tex(piano.sty) = %{tl_version}

%description -n texlive-piano
This package adds the \keyboard[1][2]..[7] command to your project. When used,
it draws a small 2 octaves piano keyboard on your document, with up to 7 keys
highlighted. Keys go : Co, Cso, Do, Dso, Eo, Fo, Fso, Go, Gso, Ao, Aso, Bo, Ct,
Cst, Dt, Dst, Et, Ft, Fst, Gt, Gst, At, Ast and Bt. (A working example is
included in the README file.)

%package -n texlive-recorder-fingering
Summary:        Package to display recorder fingering diagrams
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Provides:       tex(recorder-fingering.sty) = %{tl_version}

%description -n texlive-recorder-fingering
This package provides support for generating and displaying fingering diagrams
for baroque fingering recorders and the tin whistle. Standard fingerings are
provided for recorders in both C and F, and the tin whistle in D, along with
methods to create and display alternate fingerings for trills, etc.

%package -n texlive-songbook
Summary:        Package for typesetting song lyrics and chord books
Version:        svn18136
License:        LGPL-2.1-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multicol.sty)
Requires:       tex(xstring.sty)
Provides:       tex(conditionals.sty) = %{tl_version}
Provides:       tex(songbook.sty) = %{tl_version}

%description -n texlive-songbook
The package provides an all purpose songbook style. Three types of output may
be created from a single input file: "words and chords" books for the musicians
to play from, "words only" songbooks for the congregation to sing from, and
overhead transparency masters for congregational use. The package will also
print a table of contents, an index sorted by title and first line, and an
index sorted by key, or by artist/composer. The package attempts to handle
songs in multiple keys, as well as songs in multiple languages.

%package -n texlive-songproj
Summary:        Generate Beamer slideshows with song lyrics
Version:        svn76924
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(verse.sty)
Requires:       tex(xparse.sty)
Provides:       tex(songproj.sty) = %{tl_version}

%description -n texlive-songproj
This package, together with the Beamer class, is used to generate slideshows
with song lyrics. This is typically used in religious services in churches
equipped with a projector, for which this package has been written, but it can
be useful for any type of singing assembly. It provides environments to
describe a song in a natural way, and formatting it into slides with overlays.
The package comes with an additional Python script that can be used to convert
plain-text song lyrics to the expected LaTeX markup.

%package -n texlive-songs
Summary:        Produce song books for church or fellowship
Version:        svn51494
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(etex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Provides:       tex(songs.sty) = %{tl_version}

%description -n texlive-songs
The package provides a means of producing beautiful song books for church or
fellowship. It offers: a very easy chord-entry syntax; multiple modes
(words-only; words+chords; slides; handouts); measure bars; guitar tablatures;
automatic transposition; scripture quotations; multiple indexes (sorted by
title, author, important lyrics, or scripture references); and projector-style
output generation, for interactive use. A set of example documents is provided.

%package -n texlive-undar-digitacion
Summary:        Musical fingering diagrams of Pinkullo Huanuqueno, Flute (Recorder), Quena and Saxophone
Version:        svn69742
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(musicography.sty)
Requires:       tex(musixtex.sty)
Requires:       tex(recorder-fingering.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(undar-digitacion.sty) = %{tl_version}

%description -n texlive-undar-digitacion
The package provides tools for generating: Pinkullo Huanuqueno Flute Quena
Saxophone The result will often be a PDF (or set of PDFs) that contain
everything one will need for musical fingering diagrams of the Pinkullo
Huanuqueno, Flute, Quena and Saxophone. The package uses TikZ for most things
and MusixTeX for music symbols.

%package -n texlive-xpiano
Summary:        An extension of the piano package
Version:        svn61719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(xpiano.sty) = %{tl_version}

%description -n texlive-xpiano
This package provides macros for typesetting virtual keyboards limited to two
octaves for showing notes represented by a colored circle. Optionally, the
number used for pitch analysis can be shown. It is an extension of piano.sty by
Emile Daneault, written in expl3 in answer to a couple of questions on
TeX.StackExchange: https://tex.stackexchange.com/questions/162184/
https://tex.stackexchange.com/questions/246276/. It features extended syntax
and several options, like setting the color, adding numbers for pitch analysis,
one or two octaves, and others.

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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-abc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/abc/
%doc %{_texmf_main}/doc/latex/abc/

%files -n texlive-bagpipe
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/bagpipe/
%doc %{_texmf_main}/doc/generic/bagpipe/

%files -n texlive-chordbars
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chordbars/
%doc %{_texmf_main}/doc/latex/chordbars/

%files -n texlive-chordbox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chordbox/
%doc %{_texmf_main}/doc/latex/chordbox/

%files -n texlive-ddphonism
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ddphonism/
%doc %{_texmf_main}/doc/latex/ddphonism/

%files -n texlive-figbas
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/figbas/
%{_texmf_main}/fonts/map/dvips/figbas/
%{_texmf_main}/fonts/tfm/public/figbas/
%{_texmf_main}/fonts/type1/public/figbas/
%doc %{_texmf_main}/doc/fonts/figbas/

%files -n texlive-fretplot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fretplot/
%doc %{_texmf_main}/doc/latex/fretplot/

%files -n texlive-gchords
%license gpl2.txt
%{_texmf_main}/tex/latex/gchords/
%doc %{_texmf_main}/doc/latex/gchords/

%files -n texlive-gtrcrd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gtrcrd/
%doc %{_texmf_main}/doc/latex/gtrcrd/

%files -n texlive-guitar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/guitar/
%doc %{_texmf_main}/doc/latex/guitar/

%files -n texlive-guitarchordschemes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/guitarchordschemes/
%doc %{_texmf_main}/doc/latex/guitarchordschemes/

%files -n texlive-guitartabs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/guitartabs/
%doc %{_texmf_main}/doc/latex/guitartabs/

%files -n texlive-harmony
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/harmony/
%doc %{_texmf_main}/doc/latex/harmony/

%files -n texlive-latex4musicians
%license fdl.txt
%doc %{_texmf_main}/doc/latex/latex4musicians/

%files -n texlive-leadsheets
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/leadsheets/
%doc %{_texmf_main}/doc/latex/leadsheets/

%files -n texlive-liederbuch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/liederbuch/
%doc %{_texmf_main}/doc/latex/liederbuch/

%files -n texlive-musical
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musical/
%doc %{_texmf_main}/doc/latex/musical/

%files -n texlive-musicography
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musicography/
%doc %{_texmf_main}/doc/latex/musicography/

%files -n texlive-musixguit
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musixguit/
%doc %{_texmf_main}/doc/latex/musixguit/

%files -n texlive-musixtex-fonts
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/musixtex-fonts/
%{_texmf_main}/fonts/opentype/public/musixtex-fonts/
%{_texmf_main}/fonts/source/public/musixtex-fonts/
%{_texmf_main}/fonts/tfm/public/musixtex-fonts/
%{_texmf_main}/fonts/type1/public/musixtex-fonts/
%doc %{_texmf_main}/doc/fonts/musixtex-fonts/

%files -n texlive-octave
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/octave/
%doc %{_texmf_main}/doc/latex/octave/

%files -n texlive-piano
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/piano/
%doc %{_texmf_main}/doc/latex/piano/

%files -n texlive-recorder-fingering
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/recorder-fingering/
%doc %{_texmf_main}/doc/latex/recorder-fingering/

%files -n texlive-songbook
%license lgpl2.1.txt
%{_texmf_main}/makeindex/songbook/
%{_texmf_main}/tex/latex/songbook/
%doc %{_texmf_main}/doc/latex/songbook/

%files -n texlive-songproj
%license bsd.txt
%{_texmf_main}/tex/latex/songproj/
%doc %{_texmf_main}/doc/latex/songproj/

%files -n texlive-songs
%license gpl2.txt
%{_texmf_main}/tex/latex/songs/
%doc %{_texmf_main}/doc/latex/songs/

%files -n texlive-undar-digitacion
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/undar-digitacion/
%doc %{_texmf_main}/doc/latex/undar-digitacion/

%files -n texlive-xpiano
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xpiano/
%doc %{_texmf_main}/doc/latex/xpiano/

%changelog
%autochangelog
