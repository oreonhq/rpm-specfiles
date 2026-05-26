%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-latex
Epoch:          12
Version:        svn78733
Release:        4%{?dist}
Summary:        LaTeX fundamental packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-latex.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ae.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ae.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amscls.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amscls.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsmath.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsmath.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atbegshi.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atbegshi.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atveryend.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atveryend.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auxhook.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auxhook.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-english.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-english.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babelbib.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babelbib.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bigintcalc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bigintcalc.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitset.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitset.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookmark.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookmark.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/carlisle.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/carlisle.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/colortbl.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/colortbl.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epstopdf-pkg.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epstopdf-pkg.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etexcmds.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etexcmds.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etoolbox.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etoolbox.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyhdr.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyhdr.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/firstaid.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/firstaid.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fix2col.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fix2col.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/geometry.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/geometry.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gettitlestring.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gettitlestring.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics-cfg.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics-cfg.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grfext.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grfext.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hopatch.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hopatch.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hycolor.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hycolor.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hypcap.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hypcap.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyperref.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyperref.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/intcalc.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/intcalc.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvdefinekeys.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvdefinekeys.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvoptions.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvoptions.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvsetkeys.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvsetkeys.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3backend.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3backend.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3kernel.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3kernel.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3packages.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3packages.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-fonts.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-fonts.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-lab.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-lab.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexconfig.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letltxmacro.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letltxmacro.doc.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltxcmds.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltxcmds.doc.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltxmisc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-uni-algos.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-uni-algos.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfnfss.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfnfss.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/natbib.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/natbib.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pagesel.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pagesel.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfescape.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfescape.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfmanagement.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfmanagement.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftexcmds.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftexcmds.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pslatex.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psnfss.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psnfss.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pspicture.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pspicture.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/refcount.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/refcount.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rerunfilecheck.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rerunfilecheck.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stringenc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stringenc.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tagpdf.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tagpdf.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tools.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tools.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uniquecounter.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uniquecounter.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/url.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/url.doc.tar.xz

# Patches
Patch0:         tools-2026-02-10.patch
# oreon url source checksums begin
%global source0_sha256 1fcd5223c52f9f0823067bac1de4150386f39faefe19f6603092d084727f3cb1
%global source0_file collection-latex.tar.xz
%global source2_sha256 25a3ff72fb0c4e1d57cf0a6dc9c0437aca398f2a88c3bf7dbab3dc05ee6075c2
%global source2_file ae.tar.xz
%global source3_sha256 beea7aed2c4b743384051b16fb45985de2e6485a5bb26b798471c4040a892b0b
%global source3_file ae.doc.tar.xz
%global source4_sha256 6bc23a08e43f0837581486d9ceb2624598fb28f56d88333848327dbc2cf48c2d
%global source4_file amscls.tar.xz
%global source5_sha256 58568b86cd0d4f82a316a3663d32bd5fc0a8f0e0371048361a67cf87f9fa75e7
%global source5_file amscls.doc.tar.xz
%global source6_sha256 2c8015242b4e7c7a7be5183ce03d8c133d2552ba186d5c0e01cb9e9599753c9e
%global source6_file amsmath.tar.xz
%global source7_sha256 ec1e344701f00d9aff34bbab9156f1fe2eacd0f01f3ed1316d89effc950dea43
%global source7_file amsmath.doc.tar.xz
%global source8_sha256 2df65cdfab8217dd87712d3e9ac3f2961d6c0275d446b705700f509f9616a9b1
%global source8_file atbegshi.tar.xz
%global source9_sha256 741b784bf46633c1622ee40ed0c030d480b8789af667b9e7cd2905a693df72c1
%global source9_file atbegshi.doc.tar.xz
%global source10_sha256 16e4ff5db982a6378a087c1b832794bd4cb09b14566ce0ea36a028c60d285aab
%global source10_file atveryend.tar.xz
%global source11_sha256 0431c9fe1ec009177b546e5fa601a2c5f3bfd57639324796b7eee2041f33b7a5
%global source11_file atveryend.doc.tar.xz
%global source12_sha256 b131f4de33865e1463717e6631ea06e636b0884c72c9906f39c06ca267213146
%global source12_file auxhook.tar.xz
%global source13_sha256 4cd196e40a84a35c6d0becc760b6419ccde3f84231157ce5a4a97059a76f8739
%global source13_file auxhook.doc.tar.xz
%global source14_sha256 ccd168592492a1b13aa276f0d8574a5dac3098f41ddc8d9544e683b1d37d958d
%global source14_file babel.tar.xz
%global source15_sha256 9816cdc226bdbbb3e12a47a0e8a2c08d5fb727d397a15980a3a18af6c205b398
%global source15_file babel.doc.tar.xz
%global source16_sha256 615f7373205ae2bd19390a0aa2859d4e7617c0a28e780ccfdcbe9053e1b8d448
%global source16_file babel-english.tar.xz
%global source17_sha256 dc9b15a0a243f0cd3de5adbc7c0f9ac2446982858d3d67edbb80e30f1eb3e481
%global source17_file babel-english.doc.tar.xz
%global source18_sha256 3206b675dc96137d3245fba8e0bb79da24c26075394ffae7b7db44ba93513ab7
%global source18_file babelbib.tar.xz
%global source19_sha256 515909e5a93571f4afbaa1fc9c7f815a0a476d80f1fbee99be7f0cc977886821
%global source19_file babelbib.doc.tar.xz
%global source20_sha256 d9b2dc626ea6f69c5450d7c56d972814ab2c2ccb57b491fd930394424a54b7d7
%global source20_file bigintcalc.tar.xz
%global source21_sha256 f46bfd54e8bf2f0db2c254a4cf86008cfb555ad2b5fb449aae5031d7fb12fef5
%global source21_file bigintcalc.doc.tar.xz
%global source22_sha256 e653d4fbb9c65c46a4ae17efed63a08dc0498576dc4de4f470359feb5462066a
%global source22_file bitset.tar.xz
%global source23_sha256 3b9016a5c07e2fd0fc7c34e1fa8cc80752b3b2153f9e23de0056e6b127691a10
%global source23_file bitset.doc.tar.xz
%global source24_sha256 ade8a71c78233b9f4369fe49ae58037acf92c51475bc273c502bb08b2120a5de
%global source24_file bookmark.tar.xz
%global source25_sha256 0413decdc6b3fe7ecc178bd05c039a24e32923100a49f2afd0d1b2d3d3ac731a
%global source25_file bookmark.doc.tar.xz
%global source26_sha256 5b93192b5e5ca7f41e23a1ec1ff2ef59d5d54fb158201d374cbea4f46c19cc9f
%global source26_file carlisle.tar.xz
%global source27_sha256 9ef1e9c0dffdd947e772d97c7176a1921f81e07306776c0365cea02b500ac8dd
%global source27_file carlisle.doc.tar.xz
%global source28_sha256 f4026d56c4ab20daa44720b5df96e2d8b5be6a321dbb37ae72fcb9ebba6bee0d
%global source28_file colortbl.tar.xz
%global source29_sha256 e4084efd03b5d59d3b30372ef6fdb40cce0999a6092a5704224bedf23fd4bae3
%global source29_file colortbl.doc.tar.xz
%global source30_sha256 8a295400882bd7ec7e3be3c426786bf970ad02a9deb60ea5f8a5ed5112ac6022
%global source30_file epstopdf-pkg.tar.xz
%global source31_sha256 688b471afd8ced0f18d558e2afc03cbbd1f2af44a31e02babc3f8b849b193e29
%global source31_file epstopdf-pkg.doc.tar.xz
%global source32_sha256 117e4b867d9a5b08829520c0ab6153b1113e6fcdda7b50aca6eb21e2b66e3867
%global source32_file etexcmds.tar.xz
%global source33_sha256 0ee7e26f7dbb2c179f9a52fdf42665289cfa6e69b948ede6bd446386a11fd8ea
%global source33_file etexcmds.doc.tar.xz
%global source34_sha256 ffb21fc7073f9cb89dbc0bd999a98b1e9b7285fc1a46056254d4a167707f0658
%global source34_file etoolbox.tar.xz
%global source35_sha256 872868e5c096fef325ecca0794e188cb6590949000bab9f66ab1f43ce96e723d
%global source35_file etoolbox.doc.tar.xz
%global source36_sha256 08acefe6dd7d96f18d6b5f28af58f22c16801f6a031a64441f29ee0656444124
%global source36_file fancyhdr.tar.xz
%global source37_sha256 248356f3052a8168b3781e046ca6be30f7c3c219981f4c82a0c505cd74a9880a
%global source37_file fancyhdr.doc.tar.xz
%global source38_sha256 a61e9c3344373e6d733821c0f3ae806b59cd1039ec2c32da6f39c7bdba7d1694
%global source38_file firstaid.tar.xz
%global source39_sha256 cd0cfcd57ecf6a7718732e03b221afd72924ad144b7b64018f1bdafe1d2a29b3
%global source39_file firstaid.doc.tar.xz
%global source40_sha256 93f52c4685192a324f2510d23bb9ebd6ba449cded3baf39846737cb3e03dfeed
%global source40_file fix2col.tar.xz
%global source41_sha256 4bad37d9e60839efcd669e19db0659d6ec66cec1820b4d66574f70a455a3bd84
%global source41_file fix2col.doc.tar.xz
%global source42_sha256 8ba10e4283961c9b0c5348351e40cd15612a7ea808e297b918528ebdfd07a50c
%global source42_file geometry.tar.xz
%global source43_sha256 9de80856957bc6f1a944141a7a777323812bbd2324e3c7c27288708658180d61
%global source43_file geometry.doc.tar.xz
%global source44_sha256 1bb11f84c8d3d4b703ffc89044b0c693d4b5f2e642a4c5df58a038a666281d29
%global source44_file gettitlestring.tar.xz
%global source45_sha256 07a5d7ae8dc9bfe8285699ea0eb803b0b862e095e7dbbb48f35b630fe5a871ef
%global source45_file gettitlestring.doc.tar.xz
%global source46_sha256 42f21cbf91a06079fcc5006351305e778666458536128d8b130b37433499422a
%global source46_file graphics.tar.xz
%global source47_sha256 51657f002ae2832e03eb311f5c38eb374acbc137ed58f17bf362870113d990ba
%global source47_file graphics.doc.tar.xz
%global source48_sha256 f49fd69ee7b03442e3ce16837e846d1e108e8a71db098fe8eb707c0e3d8e2c6c
%global source48_file graphics-cfg.tar.xz
%global source49_sha256 100d51daf649a36f0b2f4c7b505aa21501e469bda19d63cf4247e1e315a428f5
%global source49_file graphics-cfg.doc.tar.xz
%global source50_sha256 54da4d608fd95ff3eb576eb65464f322b3ddf167c37147f2840deeed12c0fcc2
%global source50_file grfext.tar.xz
%global source51_sha256 3d78f045b4ccd8040b626a0a2f8fcbb78fedebadc7853482e03f3eb7d144d9b5
%global source51_file grfext.doc.tar.xz
%global source52_sha256 63a128ddc8de740fbd2d520425128eb6bdbe115ef51d7030bf0ef406ccb1e1b1
%global source52_file hopatch.tar.xz
%global source53_sha256 fdb51e01d27947a6826e08788b8ae167042ed1ee500cd69a0dff4c89105f5a42
%global source53_file hopatch.doc.tar.xz
%global source54_sha256 ab139b6133a062077d635a2c686f0f9b2aaa03d532ffd70e2d9896adf5f02428
%global source54_file hycolor.tar.xz
%global source55_sha256 575ed201c1bc175b8ad8b83a5bca26e06031e805156bd3d4dd410d2cbbcf8888
%global source55_file hycolor.doc.tar.xz
%global source56_sha256 3f316300b7c1a39b41613c6624ddbf3409757ba06a508f575e701226bad3d3a5
%global source56_file hypcap.tar.xz
%global source57_sha256 1f634fbd7183702865850fc9f9fd110163bd2ea0d61aae9ae51e424b02236153
%global source57_file hypcap.doc.tar.xz
%global source58_sha256 1b1b844b2030db589b4aea1a2760f7e357ee47d458c4db2d60a3975e0519c732
%global source58_file hyperref.tar.xz
%global source59_sha256 89f737343db72843ed1bbed99a39c6243d56ffe7f9548c76d9cb5c7c3d1327b3
%global source59_file hyperref.doc.tar.xz
%global source60_sha256 a0a0a8cbd6505c96d6ad0f2158f76ae655c90e41823acb3dd5486801ced85d28
%global source60_file intcalc.tar.xz
%global source61_sha256 96e7dcddf7a8566eb2dcd4f2c6e1ba7d6acae148b9843bbe775b71fb9ceffadf
%global source61_file intcalc.doc.tar.xz
%global source62_sha256 236c4ffc60835277fd820ec7d8ff85d71a407732d8d4888f5432afeb8f7ef2d8
%global source62_file kvdefinekeys.tar.xz
%global source63_sha256 12aade1b4ac4e120acec5a7794ea9822e736fa79e595de3d11bfe0bc0af3b20d
%global source63_file kvdefinekeys.doc.tar.xz
%global source64_sha256 4229aaf8b374dac8d7034a2381b417934243ebd3b81afc50794b17292f988957
%global source64_file kvoptions.tar.xz
%global source65_sha256 86b380b329c081a437029c652bde190e23d3012ffb9f585aa49d952f512ab78e
%global source65_file kvoptions.doc.tar.xz
%global source66_sha256 8b25ce85ea71f1f81008509026266071370824c2917bc4b4f3f0fe6429f369b3
%global source66_file kvsetkeys.tar.xz
%global source67_sha256 d1dd84c69ce27bcd8fb8c64de1897167d809398cce902ec9944ef20630eb7f2d
%global source67_file kvsetkeys.doc.tar.xz
%global source68_sha256 9d0081fb9fb83948f60f00b451ba17d6131e43fcc915fc9472984a3a2026b78d
%global source68_file l3backend.tar.xz
%global source69_sha256 3bd48bc7b874a33b02f97465523ae465ae21343ce73691a8fb0faf5f5ae5b6f5
%global source69_file l3backend.doc.tar.xz
%global source70_sha256 2b45ed0cdab7606bf5ac030db2843d00a87b57702d2aa3f0492e6c4fbcf885ea
%global source70_file l3kernel.tar.xz
%global source71_sha256 f05853bbc75c11d9391942bf5d5804078244c42ad43a29375499e757df7e487e
%global source71_file l3kernel.doc.tar.xz
%global source72_sha256 dbf8a6c910e8886960d735626bfc5249e08bef7eb611733b054184fe8c321091
%global source72_file l3packages.tar.xz
%global source73_sha256 55b4ddcacd0bb772acbbae4b4f1451a019f51f77bc84e755303ef6249b573069
%global source73_file l3packages.doc.tar.xz
%global source74_sha256 c542058e4dc1dfedc36bd65c44b472f69cf1d85bf271090cb10f698e901ebdbf
%global source74_file latex-fonts.tar.xz
%global source75_sha256 2ab65ef8b005d89ca4241aa49b48f8901125ca9ed8d82dc7327a31b3df32b02d
%global source75_file latex-fonts.doc.tar.xz
%global source76_sha256 8d7be55096eb2e25e53f019dc573bb21b946a1080f8feaf0310a23dcebbcce73
%global source76_file latex-lab.tar.xz
%global source77_sha256 b28af19b71c479d275805fdaae1f402089935547b071860eb91f24e6bd4a0b8c
%global source77_file latex-lab.doc.tar.xz
%global source78_sha256 731e9bbf4829b62b0331de8bec8efd22278e478ec246a5a42125db5196e9bdfc
%global source78_file latexconfig.tar.xz
%global source79_sha256 45a6e37fb4fe964a971fa7f32407387f94f8918b1432d19e4131fddb0f27a956
%global source79_file letltxmacro.tar.xz
%global source80_sha256 d3f6f7baa0d903b385536d55856ff1d2f84bdfdd47d5da04a8517aa9acac24a6
%global source80_file letltxmacro.doc.tar.xz
%global source81_sha256 7641cdc477417f14880be88bee8bae2f49d65301e3275e2bcfa94bb3bee80182
%global source81_file ltxcmds.tar.xz
%global source82_sha256 e36b940375243f570faee441a7afa96c1be95e330527e73b850a6a2e2e365dd1
%global source82_file ltxcmds.doc.tar.xz
%global source83_sha256 1f3b7b3791527ad16dbb56dc1f4984896c3aa162b99dc80b3ed8b0d80c130945
%global source83_file ltxmisc.tar.xz
%global source84_sha256 a7f9a14f2cb5dedd3d67997d9db3de9cfdef7003a797b33892fa8728578dfb95
%global source84_file lua-uni-algos.tar.xz
%global source85_sha256 583f74d7e49510b0bb6518c9b4072d760eda1b579974313facb9d8788bb2bbbd
%global source85_file lua-uni-algos.doc.tar.xz
%global source86_sha256 0e07b5f8af8cb199c8c21448a1664b69ea0c502ee091d98f4a2a272c4c5b8d83
%global source86_file mfnfss.tar.xz
%global source87_sha256 6589b0be7c1a4e53de3569e4eac357c93dc04bd4d136f740eaf7f066598b2730
%global source87_file mfnfss.doc.tar.xz
%global source88_sha256 38d3d95c8750a24ff36813f8616f6102d03728e87b9415708bf86be3172cdf1c
%global source88_file natbib.tar.xz
%global source89_sha256 4af8874caa986041bb2cc7192caf29a6fac00c6eaf40ded14f0ab2180b635b2d
%global source89_file natbib.doc.tar.xz
%global source90_sha256 293252b0ce2f5b442ff12a77b5e9191317f50813c7b4f4073744574c068f323a
%global source90_file pagesel.tar.xz
%global source91_sha256 02268229a08d07b1e692e6c6944964d11e04119a6ff33d4b884236b6fd37126a
%global source91_file pagesel.doc.tar.xz
%global source92_sha256 ce556d76cdff99aa658bfbcba397347b3fc638750787931077c8c3884c1d9dae
%global source92_file pdfescape.tar.xz
%global source93_sha256 13db5869796cf72f09ad50c5945b29b0dd310390ab3617468377e93ba52db61e
%global source93_file pdfescape.doc.tar.xz
%global source94_sha256 62d4f80ad2858badf123700a214d3fe19a955947234ddf630f9ccdf32891b6f4
%global source94_file pdfmanagement.tar.xz
%global source95_sha256 033e4bb6c5329a1432ad7fea033de0780f7c82224f9fccd6d2a6e7412882fdf3
%global source95_file pdfmanagement.doc.tar.xz
%global source96_sha256 edf348a113fe792c3a4d601d637a2f6833b79bb86be895f265fa5411a5d4f69b
%global source96_file pdftexcmds.tar.xz
%global source97_sha256 27e8c626f9163365a68bf17145937fb03e9382023be19d929a6e94246a098987
%global source97_file pdftexcmds.doc.tar.xz
%global source98_sha256 ec842fa032455ab21a57f3469e62adc6ac928ea969e968c1d31d07b0a1ef2c3f
%global source98_file pslatex.tar.xz
%global source99_sha256 25a9a4b0eaa6c6970a9194518f0baba9574d788ed1997cd4bf507cc00ea2996c
%global source99_file psnfss.tar.xz
%global source100_sha256 a445acf9c8ba8b6bb78e7990bb63419d4cbdf766a74220cb483e5b116821dd4d
%global source100_file psnfss.doc.tar.xz
%global source101_sha256 35cbf289734c9b647f2d8b17df23cbc077e224c6b897763072f6c0c774a1af6f
%global source101_file pspicture.tar.xz
%global source102_sha256 682e556e29d0048687fb4f8a0bc9e2b9cc6ded9a31f36e10db3498c1099b4df8
%global source102_file pspicture.doc.tar.xz
%global source103_sha256 7187382f8364172fd80b064235086b0b4076be8942d89f1c8aef2473ca938140
%global source103_file refcount.tar.xz
%global source104_sha256 de595ac4e61dfef95c79c9bca0b962ec718b6f4d0c9001e84f4704941d8e652e
%global source104_file refcount.doc.tar.xz
%global source105_sha256 b63abce92724296bdcca429454b52ca8caaf902acc16c8c4421c286f1b5d0faf
%global source105_file rerunfilecheck.tar.xz
%global source106_sha256 beef31ea6adf162d0df28b63dc3e3f55f2549a368bfb370f1985b79aca4c7bbf
%global source106_file rerunfilecheck.doc.tar.xz
%global source107_sha256 22d01de49bfbc35312b64265024332672c520ce0f33818d60d69f62869b6b348
%global source107_file stringenc.tar.xz
%global source108_sha256 f56b6ec369ebeaff7d9164034aea49d3f07e7a5d3d13719f426b617f5950516a
%global source108_file stringenc.doc.tar.xz
%global source109_sha256 0748c65d3d7154c6b46e5d8328ea2dbb02ac93301dd23e94bfc936f542e05aaa
%global source109_file tagpdf.tar.xz
%global source110_sha256 746fbd2c1e1b4c97fefc0c12b54c40e070a042d6cd819afaf47d23be642441b1
%global source110_file tagpdf.doc.tar.xz
%global source111_sha256 cb3cced7a3ab923bb066ff1e0a14f79e1a02b8b248e4cfb4338079399badded2
%global source111_file tools.tar.xz
%global source112_sha256 40dcaa85bb52d417b6d5e30c5ab8c787b9d451f843d19f875d9e218323446d12
%global source112_file tools.doc.tar.xz
%global source113_sha256 7aa4ca7c417e82c37fe2d551c10d56a59ef3bff30d5cc258f7fb067249e09f51
%global source113_file uniquecounter.tar.xz
%global source114_sha256 72cfa78872e2759c90be9af586e718408ceb2dd8aaf081b3f2f24b3c997d223a
%global source114_file uniquecounter.doc.tar.xz
%global source115_sha256 947284b030f06cfcbc7abb831bb5dff2b19312cf778161ee477348c2dd88fc09
%global source115_file url.tar.xz
%global source116_sha256 21a9d565c228bc8ae0a3afea4d32cd77b8627fab72f16d7ab2f11e58b3733611
%global source116_file url.doc.tar.xz
# oreon url source checksums end
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-ae
Requires:       texlive-amscls
Requires:       texlive-amsmath
Requires:       texlive-atbegshi
Requires:       texlive-atveryend
Requires:       texlive-auxhook
Requires:       texlive-babel
Requires:       texlive-babel-english
Requires:       texlive-babelbib
Requires:       texlive-bigintcalc
Requires:       texlive-bitset
Requires:       texlive-bookmark
Requires:       texlive-carlisle
Requires:       texlive-collection-basic
Requires:       texlive-colortbl
Requires:       texlive-epstopdf-pkg
Requires:       texlive-etexcmds
Requires:       texlive-etoolbox
Requires:       texlive-fancyhdr
Requires:       texlive-firstaid
Requires:       texlive-fix2col
Requires:       texlive-geometry
Requires:       texlive-gettitlestring
Requires:       texlive-graphics
Requires:       texlive-graphics-cfg
Requires:       texlive-grfext
Requires:       texlive-hopatch
Requires:       texlive-hycolor
Requires:       texlive-hypcap
Requires:       texlive-hyperref
Requires:       texlive-intcalc
Requires:       texlive-kvdefinekeys
Requires:       texlive-kvoptions
Requires:       texlive-kvsetkeys
Requires:       texlive-l3backend
Requires:       texlive-l3kernel
Requires:       texlive-l3packages
Requires:       texlive-latex
Requires:       texlive-latex-bin
Requires:       texlive-latex-fonts
Requires:       texlive-latex-lab
Requires:       texlive-latexconfig
Requires:       texlive-letltxmacro
Requires:       texlive-ltxcmds
Requires:       texlive-ltxmisc
Requires:       texlive-lua-uni-algos
Requires:       texlive-mfnfss
Requires:       texlive-mptopdf
Requires:       texlive-natbib
Requires:       texlive-oberdiek
Requires:       texlive-pagesel
Requires:       texlive-pdfescape
Requires:       texlive-pdfmanagement
Requires:       texlive-pdftexcmds
Requires:       texlive-pslatex
Requires:       texlive-psnfss
Requires:       texlive-pspicture
Requires:       texlive-refcount
Requires:       texlive-rerunfilecheck
Requires:       texlive-stringenc
Requires:       texlive-tagpdf
Requires:       texlive-tools
Requires:       texlive-uniquecounter
Requires:       texlive-url

%description
These packages are either mandated by the core LaTeX team, or very widely used
and strongly recommended in practice.


%package -n texlive-ae
Summary:        Virtual fonts for T1 encoded CMR-fonts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ae-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ae-doc <= 11:%{version}
Requires:       tex(fontenc.sty)

%description -n texlive-ae
A set of virtual fonts which emulates T1 coded fonts using the standard CM
fonts. The package name, AE fonts, supposedly stands for "Almost European". The
main use of the package was to produce PDF files using Adobe Type 1 versions of
the CM fonts instead of bitmapped EC fonts. Note that direct substitutes for
the bitmapped EC fonts are now available, via the CM-super, Latin Modern and
(in a restricted way) CM-LGC font sets.

%package -n texlive-amscls
Summary:        AMS document classes for LaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amscls-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amscls-doc <= 11:%{version}

%description -n texlive-amscls
This bundle contains three AMS classes, amsart (for writing articles for the
AMS), amsbook (for books) and amsproc (for proceedings), together with some
supporting material. This material forms one branch of what was originally the
AMS-LaTeX distribution. The other branch, amsmath, is now maintained and
distributed separately. The user documentation can be found in the package
amscls-doc.

%package -n texlive-amsmath
Summary:        AMS mathematical facilities for LaTeX
Version:        svn78101
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsmath-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsmath-doc <= 11:%{version}

%description -n texlive-amsmath
The package provides the principal packages in the AMS-LaTeX distribution. It
adapts for use in LaTeX most of the mathematical features found in AMS-TeX; it
is highly recommended as an adjunct to serious mathematical typesetting in
LaTeX. When amsmath is loaded, AMS-LaTeX packages amsbsy (for bold symbols),
amsopn (for operator names) and amstext (for text embedded in mathematics) are
also loaded. amsmath is part of the LaTeX required distribution; however,
several contributed packages add still further to its appeal; examples are
empheq, which provides functions for decorating and highlighting mathematics,
and ntheorem, for specifying theorem (and similar) definitions.

%package -n texlive-atbegshi
Summary:        Execute stuff at \shipout time
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)

%description -n texlive-atbegshi
This package is a modern reimplementation of package everyshi, providing
various commands to be executed before a \shipout command. It makes use of
e-TeX's facilities if they are available. The package may be used either with
LaTeX or with plain TeX.

%package -n texlive-atveryend
Summary:        Hooks at the very end of a document
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-atveryend
This LaTeX package provides some wrapper commands around LaTeX end document
hooks.

%package -n texlive-auxhook
Summary:        Hooks for auxiliary files
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-auxhook
This package auxhook provides hooks for adding stuff at the begin of .aux
files.

%package -n texlive-babel
Summary:        Multilingual support for LaTeX, LuaLaTeX, XeLaTeX, and Plain TeX
Version:        svn78713
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-babel-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-babel-doc <= 11:%{version}
Requires:       tex(fontspec.sty)
Requires:       tex(hhline.sty)

%description -n texlive-babel
Babel is the multilingual environment for LaTeX (tailored for LuaTeX, pdfTeX
and XeTeX), and sometimes Plain. Its aim is to provide a comprehensive
localization framework for different languages, scripts and cultures based on
the latest advances on international standards (Unicode, W3C, OpenType). It
supports about 300 languages (with various levels of coverage) across about 45
scripts, including complex (like CJK, Indic) and RTL ones. Besides the
traditional .ldf files, there are many locales built on a modern core that
utilizes descriptive .ini files, with tools providing precise control over
hyphenation and line breaking, captions, date formats (across various
calendars), spacing, transliteration, numbering and other locale-specific
typographical rules.

%package -n texlive-babel-english
Summary:        Babel support for English
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-babel-english-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-babel-english-doc <= 11:%{version}
Requires:       texlive-hyphen-english

%description -n texlive-babel-english
The package provides the language definition file for support of English in
babel. Care is taken to select british hyphenation patterns for British English
and Australian text, and default ('american') patterns for Canadian and USA
text.

%package -n texlive-babelbib
Summary:        Multilingual bibliographies
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-babelbib-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-babelbib-doc <= 11:%{version}
Requires:       tex(babel.sty)

%description -n texlive-babelbib
This package enables the user to generate multilingual bibliographies in
cooperation with babel. Two approaches are possible: Each citation may be
written in another language, or the whole bibliography can be typeset in a
language chosen by the user. In addition, the package supports commands to
change the typography of the bibliographies.

%package -n texlive-bigintcalc
Summary:        Integer calculations on very large numbers
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pdftexcmds.sty)

%description -n texlive-bigintcalc
This package provides expandable arithmetic operations with big integers that
can exceed TeX's number limits.

%package -n texlive-bitset
Summary:        Handle bit-vector datatype
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-bigintcalc
Requires:       tex(bigintcalc.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(intcalc.sty)

%description -n texlive-bitset
This package defines and implements the data type bit set, a vector of bits.
The size of the vector may grow dynamically. Individual bits can be
manipulated.

%package -n texlive-bookmark
Summary:        A new bookmark (outline) organization for hyperref
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)

%description -n texlive-bookmark
This package implements a new bookmark (outline) organization for package
hyperref. Bookmark properties such as style and color can now be set. Other
action types are available (URI, GoToR, Named). The bookmarks are generated in
the first compile run. Package hyperref uses two runs.

%package -n texlive-carlisle
Summary:        David Carlisle's small packages
Version:        svn59577
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-carlisle-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-carlisle-doc <= 11:%{version}
Requires:       tex(color.sty)
Requires:       tex(longtable.sty)
Requires:       tex(tabularx.sty)

%description -n texlive-carlisle
Many of David Carlisle's more substantial packages stand on their own, or as
part of the LaTeX latex-tools set; this set contains: Making dotless 'j'
characters for fonts that don't have them; A method for combining the
capabilities of longtable and tabularx; An environment for including Plain TeX
in LaTeX documents; A jiffy to remove counters from other counters' reset lists
(now obsolete as it has been incorporated into the LaTeX format); A jiffy to
create 'slashed' characters for physicists.

%package -n texlive-colortbl
Summary:        Add colour to LaTeX tables
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-colortbl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-colortbl-doc <= 11:%{version}
Requires:       tex(array.sty)
Requires:       tex(color.sty)

%description -n texlive-colortbl
The package allows rows and columns to be coloured, and even individual cells.

%package -n texlive-epstopdf-pkg
Summary:        Call epstopdf "on the fly"
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-epstopdf
Requires:       tex(grfext.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)

%description -n texlive-epstopdf-pkg
The package adds support for EPS files in the graphicx package when running
under pdfTeX. If an EPS graphic is detected, the package spawns a process to
convert the EPS to PDF, using the script epstopdf. This of course requires that
shell escape is enabled for the pdfTeX run.

%package -n texlive-etexcmds
Summary:        Avoid name clashes with e-TeX commands
Version:        svn78101
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)

%description -n texlive-etexcmds
New primitive commands are introduced in e-TeX; sometimes the names collide
with existing macros. This package solves the name clashes by adding a prefix
to e-TeX's commands. For example, eTeX's \unexpanded is provided as
\etex@unexpanded.

%package -n texlive-etoolbox
Summary:        E-TeX tools for LaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-etoolbox-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-etoolbox-doc <= 11:%{version}
Requires:       tex(etex.sty)

%description -n texlive-etoolbox
The package is a toolbox of programming facilities geared primarily towards
LaTeX class and package authors. It provides LaTeX frontends to some of the new
primitives provided by e-TeX as well as some generic tools which are not
strictly related to e-TeX but match the profile of this package. Note that the
initial versions of this package were released under the name elatex. The
package provides functions that seem to offer alternative ways of implementing
some LaTeX kernel commands; nevertheless, the package will not modify any part
of the LaTeX kernel.

%package -n texlive-fancyhdr
Summary:        Extensive control of page headers and footers in LaTeX2e
Version:        svn78348
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fancyhdr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fancyhdr-doc <= 11:%{version}
Requires:       tex(xparse.sty)

%description -n texlive-fancyhdr
The package provides extensive facilities, both for constructing headers and
footers, and for controlling their use (for example, at times when LaTeX would
automatically change the heading style in use).

%package -n texlive-firstaid
Summary:        First aid for external LaTeX files and packages that need updating
Version:        svn76740
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-firstaid
This package contains some first aid for LaTeX packages or classes that require
updates because of internal changes to the LaTeX kernel that are not yet
reflected in the package's or class's code. The file
latex2e-first-aid-for-external-files.ltx provided by this package is meant to
be loaded during format generation and not by the user.

%package -n texlive-fix2col
Summary:        Fix miscellaneous two column mode features
Version:        svn38770
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fix2col-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fix2col-doc <= 11:%{version}

%description -n texlive-fix2col
OBSOLETE: do not use in new documents. This package will do nothing in LaTeX
formats after 2015/01/01 as the fixes that it implements were incorporated into
the fixltx2e package, which is itself obsolete as since the 2015/01/01 release
these fixes are in the LaTeX format itself. Fix mark handling so that
\firstmark is taken from the first column if that column has any marks at all;
keep two column floats like figure* in sequence with single column floats like
figure.

%package -n texlive-geometry
Summary:        Flexible and complete interface to document dimensions
Version:        svn78315
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-geometry-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-geometry-doc <= 11:%{version}
Requires:       texlive-graphics
Requires:       texlive-iftex
Requires:       tex(atbegshi.sty)
Requires:       tex(ifvtex.sty)
Requires:       tex(keyval.sty)

%description -n texlive-geometry
The package provides an easy and flexible user interface to customize page
layout, implementing auto-centering and auto-balancing mechanisms so that the
users have only to give the least description for the page layout. For example,
if you want to set each margin 2cm without header space, what you need is just
\usepackage[margin=2cm,nohead]{geometry}. The package knows about all the
standard paper sizes, so that the user need not know what the nominal 'real'
dimensions of the paper are, just its standard name (such as a4, letter, etc.).
An important feature is the package's ability to communicate the paper size
it's set up to the output (whether via DVI \specials or via direct interaction
with pdf(La)TeX).

%package -n texlive-gettitlestring
Summary:        Clean up title references
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)

%description -n texlive-gettitlestring
Cleans up the title string (removing \label commands) for packages (such as
nameref) that typeset such strings.

%package -n texlive-graphics
Summary:        The LaTeX standard graphics bundle
Version:        svn78282
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-graphics-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-graphics-doc <= 11:%{version}
Requires:       texlive-epstopdf-pkg
Requires:       texlive-graphics-cfg
Requires:       texlive-graphics-def
Requires:       tex(ifthen.sty)

%description -n texlive-graphics
This is a collection of LaTeX packages for: producing colour including graphics
(eg PostScript) files rotation and scaling of text in LaTeX documents. It
comprises the packages color, graphics, graphicx, trig, epsfig, keyval, and
lscape.

%package -n texlive-graphics-cfg
Summary:        Sample configuration files for LaTeX color and graphics
Version:        svn41448
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-graphics-cfg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-graphics-cfg-doc <= 11:%{version}

%description -n texlive-graphics-cfg
This bundle includes color.cfg and graphics.cfg files that set default "driver"
options for the color and graphics packages. It contains support for defaulting
the new LuaTeX option which was added to graphics and color in the 2016-02-01
release. The LuaTeX option is only used for LuaTeX versions from 0.87, older
versions use the pdfTeX option as before.

%package -n texlive-grfext
Summary:        Manipulate the graphics package's list of extensions
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(kvdefinekeys.sty)

%description -n texlive-grfext
This package provides macros for adding to, and reordering the list of graphics
file extensions recognised by package graphics.

%package -n texlive-hopatch
Summary:        Load patches for packages
Version:        svn65491
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ltxcmds.sty)

%description -n texlive-hopatch
Hopatch provides a command with which the user may register of patch code for a
particular package. Hopatch will apply the patch immediately, if the relevant
package has already been loaded; otherwise it will store the patch until the
package appears.

%package -n texlive-hycolor
Summary:        Implements colour for packages hyperref and bookmark
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hopatch.sty)

%description -n texlive-hycolor
This package provides the code for the color option that is used by packages
hyperref and bookmark. It is not intended as package for the user.

%package -n texlive-hypcap
Summary:        Adjusting the anchors of captions
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(letltxmacro.sty)

%description -n texlive-hypcap
The package offers a solution to the problem that when you link to a float
using hyperref, the link anchors to below the float's caption, rather than the
beginning of the float. Hypcap defines a separate \capstart command, which you
put where you want links to end; you should have a \capstart command for each
\caption command. Package options can be used to auto-insert a \capstart at the
start of a float environment.

%package -n texlive-hyperref
Summary:        Extensive support for hypertext in LaTeX
Version:        svn78811
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-hyperref-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hyperref-doc <= 11:%{version}
Requires:       texlive-atbegshi
Requires:       texlive-auxhook
Requires:       texlive-bitset
Requires:       texlive-etexcmds
Requires:       texlive-gettitlestring
Requires:       texlive-hycolor
Requires:       texlive-iftex
Requires:       texlive-infwarerr
Requires:       texlive-intcalc
Requires:       texlive-kvdefinekeys
Requires:       texlive-kvoptions
Requires:       texlive-kvsetkeys
Requires:       texlive-letltxmacro
Requires:       texlive-ltxcmds
Requires:       texlive-pdfescape
Requires:       texlive-pdftexcmds
Requires:       texlive-refcount
Requires:       texlive-rerunfilecheck
Requires:       texlive-stringenc
Requires:       texlive-url
Requires:       texlive-zapfding
Requires:       tex(bitset.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(gettitlestring.sty)
Requires:       tex(hycolor.sty)
Requires:       tex(iftex.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvdefinekeys.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(minitoc.sty)
Requires:       tex(ntheorem.sty)
Requires:       tex(pdfescape.sty)
Requires:       tex(refcount.sty)
Requires:       tex(rerunfilecheck.sty)
Requires:       tex(stringenc.sty)
Requires:       tex(url.sty)

%description -n texlive-hyperref
The hyperref package is used to handle cross-referencing commands in LaTeX to
produce hypertext links in the document. The package provides backends for the
\special set defined for HyperTeX DVI processors; for embedded pdfmark commands
for processing by Acrobat Distiller (dvips and Y&Y's dvipsone); for Y&Y's
dviwindo; for PDF control within pdfTeX and dvipdfm; for TeX4ht; and for VTeX's
pdf and HTML backends. The package is distributed with the backref and nameref
packages, which make use of the facilities of hyperref. The package depends on
the author's kvoptions, ltxcmds and refcount packages.

%package -n texlive-intcalc
Summary:        Expandable arithmetic operations with integers
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-intcalc
This package provides expandable arithmetic operations with integers, using the
e-TeX extension \numexpr if it is available.

%package -n texlive-kvdefinekeys
Summary:        Define keys for use in the kvsetkeys package
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-kvdefinekeys
The package provides a macro \kv@define@key (analogous to keyval's \define@key,
to define keys for use by kvsetkeys.

%package -n texlive-kvoptions
Summary:        Key value format for package options
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etexcmds.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(ltxcmds.sty)

%description -n texlive-kvoptions
This package offers support for package authors who want to use options in
key-value format for their package options.

%package -n texlive-kvsetkeys
Summary:        Key value parser with default handler support
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-kvsetkeys
This package provides \kvsetkeys, a variant of package keyval's \setkeys. It
allows the user to specify a handler that deals with unknown options. Active
commas and equal signs may be used (e.g. see babel's shorthands) and only one
level of curly braces are removed from the values.

%package -n texlive-l3backend
Summary:        LaTeX3 backend drivers
Version:        svn78544
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-l3backend
This package forms parts of expl3, and contains the code used to interface with
backends (drivers) across the expl3 codebase. The functions here are defined
differently depending on the engine in use. As such, these are distributed
separately from l3kernel to allow this code to be updated on an independent
schedule.

%package -n texlive-l3kernel
Summary:        LaTeX3 programming conventions
Version:        svn78545
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l3kernel-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l3kernel-doc <= 11:%{version}
Requires:       texlive-l3backend
Requires:       texlive-lua-uni-algos

%description -n texlive-l3kernel
The l3kernel bundle provides an implementation of the LaTeX3 programmers'
interface, as a set of packages that run under LaTeX2e. The interface provides
the foundation on which the LaTeX3 kernel and other future code are built: it
is an API for TeX programmers. The packages are set up so that the LaTeX3
conventions can be used with regular LaTeX2e packages.

%package -n texlive-l3packages
Summary:        High-level LaTeX3 concepts
Version:        svn76637
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l3packages-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l3packages-doc <= 11:%{version}
Requires:       texlive-l3kernel

%description -n texlive-l3packages
This collection deals with higher-level ideas such as the Designer Interface,
as part of LaTeX3 developments. The packages here have over time migrated into
the LaTeX kernel: the material here is retained to support older files. The
appropriate LaTeX kernel releases incorporating the ideas from the packages
here are l3keys2e 2022-06-01 xfp 2022-06-01 xparse 2020-10-01 xtemplate
2024-06-01

%package -n texlive-latex-fonts
Summary:        A collection of fonts used in LaTeX distributions
Version:        svn28888
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-fonts-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-fonts-doc <= 11:%{version}

%description -n texlive-latex-fonts
This is a collection of fonts for use with standard LaTeX packages and classes.
It includes 'invisible' fonts (for use with the slides class), line and circle
fonts (for use in the picture environment) and 'LaTeX symbol' fonts. For full
support of a LaTeX installation, some Computer Modern font variants cmbsy(6-9),
cmcsc(8,9), cmex(7-9) and cmmib(5-9) from the amsfonts distribution, are also
necessary. The fonts are available as Metafont source, and metric (tfm) files
are also provided. Most of the fonts are also available in Adobe Type 1 format,
in the amsfonts distribution.

%package -n texlive-latex-lab
Summary:        LaTeX laboratory
Version:        svn76739
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tagpdf.sty)

%description -n texlive-latex-lab
This bundle holds optional files that are loaded in certain situations by
kernel code (if available). While this code is still in development and the use
is experimental, it is stored outside the format so that there can be
intermediate releases not affecting the production use of LaTeX. Once the code
is finalized and properly tested it will eventually move to the kernel and the
corresponding file in this bundle will vanish. Note that none of these files
are directly user accessible in documents (i.e., they aren't packages), so the
process is transparent to documents already using the new functionality.

%package -n texlive-latexconfig
Summary:        Configuration files for LaTeX-related formats
Version:        svn68923
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-latexconfig
configuration files for LaTeX-related formats

%package -n texlive-letltxmacro
Summary:        Let assignment for LaTeX macros
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-letltxmacro
TeX's \let assignment does not work for LaTeX macros with optional arguments or
for macros that are defined as robust macros by \DeclareRobustCommand. This
package defines \LetLtxMacro that also takes care of the involved internal
macros.

%package -n texlive-ltxcmds
Summary:        Some LaTeX kernel commands for general use
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ltxcmds
This package exports some utility macros from the LaTeX kernel into a separate
namespace and also makes them available for other formats such as plain TeX.

%package -n texlive-ltxmisc
Summary:        Miscellaneous LaTeX packages, etc.
Version:        svn75878
License:        GPL-2.0-or-later AND LPPL-1.3c AND LicenseRef-Public-Domain AND LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(beton.sty)
Requires:       tex(euler.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pifont.sty)
Requires:       tex(verbatim.sty)

%description -n texlive-ltxmisc
Miscellaneous LaTeX packages, etc.

%package -n texlive-lua-uni-algos
Summary:        Unicode algorithms for LuaTeX
Version:        svn76195
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lua-uni-algos
Lua code working with Unicode data has to deal with quite some challenges. For
example there are many canonically equivalent sequences which should be treated
in the same way, and even identifying a single character becomes quite
different once you have to deal with all kinds of combining characters, emoji
sequences and syllables in different scripts. Therefore lua-uni-algos wants to
build a collection of small libraries implementing algorithms to deal with lots
of the details in Unicode, such that authors of LuaTeX packages can focus on
their actual functionality instead of having to fight against the peculiarities
of Unicode. Given that this package provides Lua modules, it is only useful in
Lua(HB)TeX. Additionally, it expects an up-to-date version of the unicode-data
package to be present. This package is intended for package authors only; no
user-level functionality provided.

%package -n texlive-mfnfss
Summary:        Packages to typeset oldgerman and pandora fonts in LaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mfnfss-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mfnfss-doc <= 11:%{version}

%description -n texlive-mfnfss
This bundle contains two packages: - oldgerm, a package to typeset with old
german fonts designed by Yannis Haralambous. - pandora, a package to typeset
with Pandora fonts designed by Neena Billawala. Note that support for the
Pandora fonts is also available via the pandora-latex package.

%package -n texlive-natbib
Summary:        Flexible bibliography support
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-natbib-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-natbib-doc <= 11:%{version}
Requires:       tex(citeref.sty)

%description -n texlive-natbib
The bundle provides a package that implements both author-year and numbered
references, as well as much detailed of support for other bibliography use.
Also Provided are versions of the standard BibTeX styles that are compatible
with natbib--plainnat, unsrtnat, abbrnat. The bibliography styles produced by
custom-bib are designed from the start to be compatible with natbib.

%package -n texlive-pagesel
Summary:        Select pages of a document for output
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(everyshi.sty)

%description -n texlive-pagesel
Selects single pages, ranges of pages, odd pages or even pages for output.

%package -n texlive-pdfescape
Summary:        Implements pdfTeX's escape features using TeX or e-TeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdftexcmds.sty)

%description -n texlive-pdfescape
This package implements pdfTeX's escape features (\pdfescapehex,
\pdfunescapehex, \pdfescapename, \pdfescapestring) using TeX or e-TeX.

%package -n texlive-pdfmanagement
Summary:        LaTeX PDF management bundle
Version:        svn78778
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)
Requires:       tex(tagpdf-base.sty)

%description -n texlive-pdfmanagement
This package is used to load LaTeX's PDF management code. The PDF management
code offers backend independent interfaces to central PDF dictionaries, tools
to create annotations, outlines, form Xobjects, form fields, to embed files,
and to handle PDF standards. The code is currently provided as independent
package. It is automatically loaded if a document uses \DocumentMetadata. It
can also be loaded as a package. At a later stage it will be integrated into
the LaTeX kernel (or in parts into permanent support packages).

%package -n texlive-pdftexcmds
Summary:        LuaTeX support for pdfTeX utility functions
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)

%description -n texlive-pdftexcmds
LuaTeX provides most of the commands of pdfTeX 1.40. However, a number of
utility functions are not available. This package tries to fill the gap and
implements some of the missing primitives using Lua.

%package -n texlive-pslatex
Summary:        Use PostScript fonts by default
Version:        svn67469
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pslatex
A small package that makes LaTeX default to 'standard' PostScript fonts. It is
basically a merger of the times and the (obsolete) mathptm packages from the
psnfss suite. You must have installed standard LaTeX and the psnfss PostScript
fonts to use this package. The main novel feature is that the pslatex package
tries to compensate for the visual differences between the Adobe fonts by
scaling Helvetica by 90%, and 'condensing' Courier (i.e. scaling horizontally)
by 85%. The package is supplied with a (unix) shell file for a 'pslatex'
command that allows standard LaTeX documents to be processed, without needing
to edit the file. Note that current psnfss uses a different technique for
scaling Helvetica, and treats Courier as a lost cause (there are better free
fixed-width available now, than there were when pslatex was designed). As a
result, pslatex is widely considered obsolete.

%package -n texlive-psnfss
Summary:        Font support for common PostScript fonts
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-psnfss-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-psnfss-doc <= 11:%{version}
Requires:       texlive-graphics
Requires:       texlive-symbol
Requires:       texlive-zapfding
Requires:       tex(keyval.sty)

%description -n texlive-psnfss
Font definition files, macros and font metrics for freely-available Adobe Type
1 fonts. The font set consists of the 'LaserWriter 35' set (originally 'freely
available' because embedded in PostScript printers), and a variety of other
free fonts, together with some additions. Note that while many of the fonts are
available in PostScript (and other) printers, most publishers require fonts
embedded in documents, which requires that you have the fonts in your TeX
system. Fortunately, there are free versions of the fonts from URW (available
in the URW base5 bundle). The base set of text fonts covered by PSNFSS are:
AvantGarde, Bookman, Courier, Helvetica, New Century Schoolbook, Palatino,
Symbol, Times Roman and Zapf Dingbats. In addition, the fonts Bitstream Charter
and Adobe Utopia are covered (those fonts were contributed to the Public Domain
by their commercial foundries). Separate packages are provided to load each
font for use as main text font. The packages helvet (which allows Helvetica to
be loaded with its size scaled to something more nearly appropriate for its use
as a Sans-Serif font to match Times) and pifont (which provides the means to
select single glyphs from symbol fonts) are tailored to special requirements of
their fonts. Mathematics are covered by the mathptmx package, which constructs
passable mathematics from a combination of Times Roman, Symbol and some glyphs
from Computer Modern, and by Pazo Math (optionally extended with the fpl
small-caps and old-style figures fonts) which uses Palatino as base font, with
the mathpazo fonts. The bundle as a whole is part of the LaTeX 'required' set
of packages.

%package -n texlive-pspicture
Summary:        PostScript picture support
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pspicture-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pspicture-doc <= 11:%{version}

%description -n texlive-pspicture
A replacement for LaTeX's picture macros, that uses PostScript \special
commands. The package is now largely superseded by pict2e.

%package -n texlive-refcount
Summary:        Counter operations with label references
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)

%description -n texlive-refcount
Provides commands \setcounterref and \addtocounterref which use the section (or
whatever) number from the reference as the value to put into the counter, as
in: ...\label{sec:foo} ... \setcounterref{foonum}{sec:foo} Commands
\setcounterpageref and \addtocounterpageref do the corresponding thing with the
page reference of the label. No .ins file is distributed; process the .dtx with
plain TeX to create one.

%package -n texlive-rerunfilecheck
Summary:        Checksum based rerun checks on auxiliary files
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-atveryend
Requires:       texlive-uniquecounter
Requires:       tex(infwarerr.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(uniquecounter.sty)

%description -n texlive-rerunfilecheck
The package provides additional rerun warnings if some auxiliary files have
changed. It is based on MD5 checksum provided by pdfTeX, LuaTeX, XeTeX.

%package -n texlive-stringenc
Summary:        Converting a string between different encodings
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdfescape.sty)

%description -n texlive-stringenc
This package provides \StringEncodingConvert for converting a string between
different encodings. Both LaTeX and plain-TeX are supported.

%package -n texlive-tagpdf
Summary:        Code for PDF tagging using pdfLaTeX and LuaLaTeX
Version:        svn78799
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(xpatch.sty)

%description -n texlive-tagpdf
The package contains the core code for tagging and accessibility used by the
LaTeX kernel in the Tagged PDF project. See
https://github.com/latex3/tagging-project for more information.

%package -n texlive-tools
Summary:        The LaTeX standard tools bundle
Version:        svn76708
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tools-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tools-doc <= 11:%{version}
Requires:       tex(color.sty)

%description -n texlive-tools
A collection of (variously) simple tools provided as part of the LaTeX required
tools distribution, comprising the packages: afterpage, array, bm, calc,
dcolumn, delarray, enumerate, fileerr, fontsmpl, ftnright, hhline, indentfirst,
layout, longtable, multicol, rawfonts, shellesc, showkeys, somedefs, tabularx,
theorem, trace, varioref, verbatim, xr, and xspace.

%package -n texlive-uniquecounter
Summary:        Provides unlimited unique counter
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bigintcalc.sty)
Requires:       tex(infwarerr.sty)

%description -n texlive-uniquecounter
This package provides a kind of counter that provides unique number values.
Several counters can be created with different names. The numeric values are
not limited.

%package -n texlive-url
Summary:        Verbatim with URL-sensitive line breaks
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-url-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-url-doc <= 11:%{version}

%description -n texlive-url
The command \url is a form of verbatim command that allows linebreaks at
certain characters or combinations of characters, accepts reconfiguration, and
can usually be used in the argument to another command. (The \urldef command
provides robust commands that serve in cases when \url doesn't work in an
argument.) The command is intended for email addresses, hypertext links,
directories/paths, etc., which normally have no spaces, so by default the
package ignores spaces in its argument. However, a package option "allows
spaces", which is useful for operating systems where spaces are a common part
of file names.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/collection-latex.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1fcd5223c52f9f0823067bac1de4150386f39faefe19f6603092d084727f3cb1" || { echo "oreon: Source0 SHA256 mismatch for collection-latex.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ae.tar.xz; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "25a3ff72fb0c4e1d57cf0a6dc9c0437aca398f2a88c3bf7dbab3dc05ee6075c2" || { echo "oreon: Source2 SHA256 mismatch for ae.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ae.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "beea7aed2c4b743384051b16fb45985de2e6485a5bb26b798471c4040a892b0b" || { echo "oreon: Source3 SHA256 mismatch for ae.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/amscls.tar.xz; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6bc23a08e43f0837581486d9ceb2624598fb28f56d88333848327dbc2cf48c2d" || { echo "oreon: Source4 SHA256 mismatch for amscls.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/amscls.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "58568b86cd0d4f82a316a3663d32bd5fc0a8f0e0371048361a67cf87f9fa75e7" || { echo "oreon: Source5 SHA256 mismatch for amscls.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/amsmath.tar.xz; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2c8015242b4e7c7a7be5183ce03d8c133d2552ba186d5c0e01cb9e9599753c9e" || { echo "oreon: Source6 SHA256 mismatch for amsmath.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/amsmath.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ec1e344701f00d9aff34bbab9156f1fe2eacd0f01f3ed1316d89effc950dea43" || { echo "oreon: Source7 SHA256 mismatch for amsmath.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/atbegshi.tar.xz; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2df65cdfab8217dd87712d3e9ac3f2961d6c0275d446b705700f509f9616a9b1" || { echo "oreon: Source8 SHA256 mismatch for atbegshi.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/atbegshi.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "741b784bf46633c1622ee40ed0c030d480b8789af667b9e7cd2905a693df72c1" || { echo "oreon: Source9 SHA256 mismatch for atbegshi.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/atveryend.tar.xz; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "16e4ff5db982a6378a087c1b832794bd4cb09b14566ce0ea36a028c60d285aab" || { echo "oreon: Source10 SHA256 mismatch for atveryend.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/atveryend.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0431c9fe1ec009177b546e5fa601a2c5f3bfd57639324796b7eee2041f33b7a5" || { echo "oreon: Source11 SHA256 mismatch for atveryend.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/auxhook.tar.xz; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b131f4de33865e1463717e6631ea06e636b0884c72c9906f39c06ca267213146" || { echo "oreon: Source12 SHA256 mismatch for auxhook.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/auxhook.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4cd196e40a84a35c6d0becc760b6419ccde3f84231157ce5a4a97059a76f8739" || { echo "oreon: Source13 SHA256 mismatch for auxhook.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/babel.tar.xz; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ccd168592492a1b13aa276f0d8574a5dac3098f41ddc8d9544e683b1d37d958d" || { echo "oreon: Source14 SHA256 mismatch for babel.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/babel.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9816cdc226bdbbb3e12a47a0e8a2c08d5fb727d397a15980a3a18af6c205b398" || { echo "oreon: Source15 SHA256 mismatch for babel.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/babel-english.tar.xz; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "615f7373205ae2bd19390a0aa2859d4e7617c0a28e780ccfdcbe9053e1b8d448" || { echo "oreon: Source16 SHA256 mismatch for babel-english.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/babel-english.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dc9b15a0a243f0cd3de5adbc7c0f9ac2446982858d3d67edbb80e30f1eb3e481" || { echo "oreon: Source17 SHA256 mismatch for babel-english.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/babelbib.tar.xz; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3206b675dc96137d3245fba8e0bb79da24c26075394ffae7b7db44ba93513ab7" || { echo "oreon: Source18 SHA256 mismatch for babelbib.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/babelbib.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "515909e5a93571f4afbaa1fc9c7f815a0a476d80f1fbee99be7f0cc977886821" || { echo "oreon: Source19 SHA256 mismatch for babelbib.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bigintcalc.tar.xz; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d9b2dc626ea6f69c5450d7c56d972814ab2c2ccb57b491fd930394424a54b7d7" || { echo "oreon: Source20 SHA256 mismatch for bigintcalc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bigintcalc.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f46bfd54e8bf2f0db2c254a4cf86008cfb555ad2b5fb449aae5031d7fb12fef5" || { echo "oreon: Source21 SHA256 mismatch for bigintcalc.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bitset.tar.xz; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e653d4fbb9c65c46a4ae17efed63a08dc0498576dc4de4f470359feb5462066a" || { echo "oreon: Source22 SHA256 mismatch for bitset.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bitset.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3b9016a5c07e2fd0fc7c34e1fa8cc80752b3b2153f9e23de0056e6b127691a10" || { echo "oreon: Source23 SHA256 mismatch for bitset.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bookmark.tar.xz; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ade8a71c78233b9f4369fe49ae58037acf92c51475bc273c502bb08b2120a5de" || { echo "oreon: Source24 SHA256 mismatch for bookmark.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bookmark.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0413decdc6b3fe7ecc178bd05c039a24e32923100a49f2afd0d1b2d3d3ac731a" || { echo "oreon: Source25 SHA256 mismatch for bookmark.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/carlisle.tar.xz; test -f "$f" || { echo "oreon: missing Source26 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5b93192b5e5ca7f41e23a1ec1ff2ef59d5d54fb158201d374cbea4f46c19cc9f" || { echo "oreon: Source26 SHA256 mismatch for carlisle.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/carlisle.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source27 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9ef1e9c0dffdd947e772d97c7176a1921f81e07306776c0365cea02b500ac8dd" || { echo "oreon: Source27 SHA256 mismatch for carlisle.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/colortbl.tar.xz; test -f "$f" || { echo "oreon: missing Source28 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f4026d56c4ab20daa44720b5df96e2d8b5be6a321dbb37ae72fcb9ebba6bee0d" || { echo "oreon: Source28 SHA256 mismatch for colortbl.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/colortbl.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source29 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e4084efd03b5d59d3b30372ef6fdb40cce0999a6092a5704224bedf23fd4bae3" || { echo "oreon: Source29 SHA256 mismatch for colortbl.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/epstopdf-pkg.tar.xz; test -f "$f" || { echo "oreon: missing Source30 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8a295400882bd7ec7e3be3c426786bf970ad02a9deb60ea5f8a5ed5112ac6022" || { echo "oreon: Source30 SHA256 mismatch for epstopdf-pkg.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/epstopdf-pkg.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "688b471afd8ced0f18d558e2afc03cbbd1f2af44a31e02babc3f8b849b193e29" || { echo "oreon: Source31 SHA256 mismatch for epstopdf-pkg.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/etexcmds.tar.xz; test -f "$f" || { echo "oreon: missing Source32 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "117e4b867d9a5b08829520c0ab6153b1113e6fcdda7b50aca6eb21e2b66e3867" || { echo "oreon: Source32 SHA256 mismatch for etexcmds.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/etexcmds.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source33 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0ee7e26f7dbb2c179f9a52fdf42665289cfa6e69b948ede6bd446386a11fd8ea" || { echo "oreon: Source33 SHA256 mismatch for etexcmds.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/etoolbox.tar.xz; test -f "$f" || { echo "oreon: missing Source34 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ffb21fc7073f9cb89dbc0bd999a98b1e9b7285fc1a46056254d4a167707f0658" || { echo "oreon: Source34 SHA256 mismatch for etoolbox.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/etoolbox.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source35 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "872868e5c096fef325ecca0794e188cb6590949000bab9f66ab1f43ce96e723d" || { echo "oreon: Source35 SHA256 mismatch for etoolbox.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fancyhdr.tar.xz; test -f "$f" || { echo "oreon: missing Source36 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "08acefe6dd7d96f18d6b5f28af58f22c16801f6a031a64441f29ee0656444124" || { echo "oreon: Source36 SHA256 mismatch for fancyhdr.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fancyhdr.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source37 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "248356f3052a8168b3781e046ca6be30f7c3c219981f4c82a0c505cd74a9880a" || { echo "oreon: Source37 SHA256 mismatch for fancyhdr.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/firstaid.tar.xz; test -f "$f" || { echo "oreon: missing Source38 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a61e9c3344373e6d733821c0f3ae806b59cd1039ec2c32da6f39c7bdba7d1694" || { echo "oreon: Source38 SHA256 mismatch for firstaid.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/firstaid.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source39 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cd0cfcd57ecf6a7718732e03b221afd72924ad144b7b64018f1bdafe1d2a29b3" || { echo "oreon: Source39 SHA256 mismatch for firstaid.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fix2col.tar.xz; test -f "$f" || { echo "oreon: missing Source40 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "93f52c4685192a324f2510d23bb9ebd6ba449cded3baf39846737cb3e03dfeed" || { echo "oreon: Source40 SHA256 mismatch for fix2col.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fix2col.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source41 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4bad37d9e60839efcd669e19db0659d6ec66cec1820b4d66574f70a455a3bd84" || { echo "oreon: Source41 SHA256 mismatch for fix2col.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/geometry.tar.xz; test -f "$f" || { echo "oreon: missing Source42 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8ba10e4283961c9b0c5348351e40cd15612a7ea808e297b918528ebdfd07a50c" || { echo "oreon: Source42 SHA256 mismatch for geometry.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/geometry.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source43 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9de80856957bc6f1a944141a7a777323812bbd2324e3c7c27288708658180d61" || { echo "oreon: Source43 SHA256 mismatch for geometry.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/gettitlestring.tar.xz; test -f "$f" || { echo "oreon: missing Source44 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1bb11f84c8d3d4b703ffc89044b0c693d4b5f2e642a4c5df58a038a666281d29" || { echo "oreon: Source44 SHA256 mismatch for gettitlestring.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/gettitlestring.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source45 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "07a5d7ae8dc9bfe8285699ea0eb803b0b862e095e7dbbb48f35b630fe5a871ef" || { echo "oreon: Source45 SHA256 mismatch for gettitlestring.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/graphics.tar.xz; test -f "$f" || { echo "oreon: missing Source46 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "42f21cbf91a06079fcc5006351305e778666458536128d8b130b37433499422a" || { echo "oreon: Source46 SHA256 mismatch for graphics.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/graphics.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source47 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "51657f002ae2832e03eb311f5c38eb374acbc137ed58f17bf362870113d990ba" || { echo "oreon: Source47 SHA256 mismatch for graphics.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/graphics-cfg.tar.xz; test -f "$f" || { echo "oreon: missing Source48 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f49fd69ee7b03442e3ce16837e846d1e108e8a71db098fe8eb707c0e3d8e2c6c" || { echo "oreon: Source48 SHA256 mismatch for graphics-cfg.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/graphics-cfg.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source49 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "100d51daf649a36f0b2f4c7b505aa21501e469bda19d63cf4247e1e315a428f5" || { echo "oreon: Source49 SHA256 mismatch for graphics-cfg.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/grfext.tar.xz; test -f "$f" || { echo "oreon: missing Source50 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "54da4d608fd95ff3eb576eb65464f322b3ddf167c37147f2840deeed12c0fcc2" || { echo "oreon: Source50 SHA256 mismatch for grfext.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/grfext.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source51 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3d78f045b4ccd8040b626a0a2f8fcbb78fedebadc7853482e03f3eb7d144d9b5" || { echo "oreon: Source51 SHA256 mismatch for grfext.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/hopatch.tar.xz; test -f "$f" || { echo "oreon: missing Source52 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "63a128ddc8de740fbd2d520425128eb6bdbe115ef51d7030bf0ef406ccb1e1b1" || { echo "oreon: Source52 SHA256 mismatch for hopatch.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/hopatch.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source53 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fdb51e01d27947a6826e08788b8ae167042ed1ee500cd69a0dff4c89105f5a42" || { echo "oreon: Source53 SHA256 mismatch for hopatch.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/hycolor.tar.xz; test -f "$f" || { echo "oreon: missing Source54 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ab139b6133a062077d635a2c686f0f9b2aaa03d532ffd70e2d9896adf5f02428" || { echo "oreon: Source54 SHA256 mismatch for hycolor.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/hycolor.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source55 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "575ed201c1bc175b8ad8b83a5bca26e06031e805156bd3d4dd410d2cbbcf8888" || { echo "oreon: Source55 SHA256 mismatch for hycolor.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/hypcap.tar.xz; test -f "$f" || { echo "oreon: missing Source56 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3f316300b7c1a39b41613c6624ddbf3409757ba06a508f575e701226bad3d3a5" || { echo "oreon: Source56 SHA256 mismatch for hypcap.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/hypcap.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source57 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1f634fbd7183702865850fc9f9fd110163bd2ea0d61aae9ae51e424b02236153" || { echo "oreon: Source57 SHA256 mismatch for hypcap.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/hyperref.tar.xz; test -f "$f" || { echo "oreon: missing Source58 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1b1b844b2030db589b4aea1a2760f7e357ee47d458c4db2d60a3975e0519c732" || { echo "oreon: Source58 SHA256 mismatch for hyperref.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/hyperref.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source59 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "89f737343db72843ed1bbed99a39c6243d56ffe7f9548c76d9cb5c7c3d1327b3" || { echo "oreon: Source59 SHA256 mismatch for hyperref.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/intcalc.tar.xz; test -f "$f" || { echo "oreon: missing Source60 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a0a0a8cbd6505c96d6ad0f2158f76ae655c90e41823acb3dd5486801ced85d28" || { echo "oreon: Source60 SHA256 mismatch for intcalc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/intcalc.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source61 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "96e7dcddf7a8566eb2dcd4f2c6e1ba7d6acae148b9843bbe775b71fb9ceffadf" || { echo "oreon: Source61 SHA256 mismatch for intcalc.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/kvdefinekeys.tar.xz; test -f "$f" || { echo "oreon: missing Source62 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "236c4ffc60835277fd820ec7d8ff85d71a407732d8d4888f5432afeb8f7ef2d8" || { echo "oreon: Source62 SHA256 mismatch for kvdefinekeys.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/kvdefinekeys.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source63 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "12aade1b4ac4e120acec5a7794ea9822e736fa79e595de3d11bfe0bc0af3b20d" || { echo "oreon: Source63 SHA256 mismatch for kvdefinekeys.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/kvoptions.tar.xz; test -f "$f" || { echo "oreon: missing Source64 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4229aaf8b374dac8d7034a2381b417934243ebd3b81afc50794b17292f988957" || { echo "oreon: Source64 SHA256 mismatch for kvoptions.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/kvoptions.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source65 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "86b380b329c081a437029c652bde190e23d3012ffb9f585aa49d952f512ab78e" || { echo "oreon: Source65 SHA256 mismatch for kvoptions.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/kvsetkeys.tar.xz; test -f "$f" || { echo "oreon: missing Source66 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8b25ce85ea71f1f81008509026266071370824c2917bc4b4f3f0fe6429f369b3" || { echo "oreon: Source66 SHA256 mismatch for kvsetkeys.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/kvsetkeys.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source67 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d1dd84c69ce27bcd8fb8c64de1897167d809398cce902ec9944ef20630eb7f2d" || { echo "oreon: Source67 SHA256 mismatch for kvsetkeys.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/l3backend.tar.xz; test -f "$f" || { echo "oreon: missing Source68 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9d0081fb9fb83948f60f00b451ba17d6131e43fcc915fc9472984a3a2026b78d" || { echo "oreon: Source68 SHA256 mismatch for l3backend.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/l3backend.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source69 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3bd48bc7b874a33b02f97465523ae465ae21343ce73691a8fb0faf5f5ae5b6f5" || { echo "oreon: Source69 SHA256 mismatch for l3backend.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/l3kernel.tar.xz; test -f "$f" || { echo "oreon: missing Source70 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2b45ed0cdab7606bf5ac030db2843d00a87b57702d2aa3f0492e6c4fbcf885ea" || { echo "oreon: Source70 SHA256 mismatch for l3kernel.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/l3kernel.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source71 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f05853bbc75c11d9391942bf5d5804078244c42ad43a29375499e757df7e487e" || { echo "oreon: Source71 SHA256 mismatch for l3kernel.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/l3packages.tar.xz; test -f "$f" || { echo "oreon: missing Source72 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dbf8a6c910e8886960d735626bfc5249e08bef7eb611733b054184fe8c321091" || { echo "oreon: Source72 SHA256 mismatch for l3packages.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/l3packages.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source73 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "55b4ddcacd0bb772acbbae4b4f1451a019f51f77bc84e755303ef6249b573069" || { echo "oreon: Source73 SHA256 mismatch for l3packages.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/latex-fonts.tar.xz; test -f "$f" || { echo "oreon: missing Source74 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c542058e4dc1dfedc36bd65c44b472f69cf1d85bf271090cb10f698e901ebdbf" || { echo "oreon: Source74 SHA256 mismatch for latex-fonts.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/latex-fonts.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source75 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2ab65ef8b005d89ca4241aa49b48f8901125ca9ed8d82dc7327a31b3df32b02d" || { echo "oreon: Source75 SHA256 mismatch for latex-fonts.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/latex-lab.tar.xz; test -f "$f" || { echo "oreon: missing Source76 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8d7be55096eb2e25e53f019dc573bb21b946a1080f8feaf0310a23dcebbcce73" || { echo "oreon: Source76 SHA256 mismatch for latex-lab.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/latex-lab.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source77 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b28af19b71c479d275805fdaae1f402089935547b071860eb91f24e6bd4a0b8c" || { echo "oreon: Source77 SHA256 mismatch for latex-lab.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/latexconfig.tar.xz; test -f "$f" || { echo "oreon: missing Source78 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "731e9bbf4829b62b0331de8bec8efd22278e478ec246a5a42125db5196e9bdfc" || { echo "oreon: Source78 SHA256 mismatch for latexconfig.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/letltxmacro.tar.xz; test -f "$f" || { echo "oreon: missing Source79 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "45a6e37fb4fe964a971fa7f32407387f94f8918b1432d19e4131fddb0f27a956" || { echo "oreon: Source79 SHA256 mismatch for letltxmacro.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/letltxmacro.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source80 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d3f6f7baa0d903b385536d55856ff1d2f84bdfdd47d5da04a8517aa9acac24a6" || { echo "oreon: Source80 SHA256 mismatch for letltxmacro.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ltxcmds.tar.xz; test -f "$f" || { echo "oreon: missing Source81 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7641cdc477417f14880be88bee8bae2f49d65301e3275e2bcfa94bb3bee80182" || { echo "oreon: Source81 SHA256 mismatch for ltxcmds.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ltxcmds.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source82 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e36b940375243f570faee441a7afa96c1be95e330527e73b850a6a2e2e365dd1" || { echo "oreon: Source82 SHA256 mismatch for ltxcmds.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ltxmisc.tar.xz; test -f "$f" || { echo "oreon: missing Source83 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1f3b7b3791527ad16dbb56dc1f4984896c3aa162b99dc80b3ed8b0d80c130945" || { echo "oreon: Source83 SHA256 mismatch for ltxmisc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/lua-uni-algos.tar.xz; test -f "$f" || { echo "oreon: missing Source84 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a7f9a14f2cb5dedd3d67997d9db3de9cfdef7003a797b33892fa8728578dfb95" || { echo "oreon: Source84 SHA256 mismatch for lua-uni-algos.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/lua-uni-algos.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source85 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "583f74d7e49510b0bb6518c9b4072d760eda1b579974313facb9d8788bb2bbbd" || { echo "oreon: Source85 SHA256 mismatch for lua-uni-algos.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/mfnfss.tar.xz; test -f "$f" || { echo "oreon: missing Source86 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0e07b5f8af8cb199c8c21448a1664b69ea0c502ee091d98f4a2a272c4c5b8d83" || { echo "oreon: Source86 SHA256 mismatch for mfnfss.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/mfnfss.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source87 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6589b0be7c1a4e53de3569e4eac357c93dc04bd4d136f740eaf7f066598b2730" || { echo "oreon: Source87 SHA256 mismatch for mfnfss.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/natbib.tar.xz; test -f "$f" || { echo "oreon: missing Source88 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "38d3d95c8750a24ff36813f8616f6102d03728e87b9415708bf86be3172cdf1c" || { echo "oreon: Source88 SHA256 mismatch for natbib.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/natbib.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source89 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4af8874caa986041bb2cc7192caf29a6fac00c6eaf40ded14f0ab2180b635b2d" || { echo "oreon: Source89 SHA256 mismatch for natbib.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pagesel.tar.xz; test -f "$f" || { echo "oreon: missing Source90 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "293252b0ce2f5b442ff12a77b5e9191317f50813c7b4f4073744574c068f323a" || { echo "oreon: Source90 SHA256 mismatch for pagesel.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pagesel.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source91 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "02268229a08d07b1e692e6c6944964d11e04119a6ff33d4b884236b6fd37126a" || { echo "oreon: Source91 SHA256 mismatch for pagesel.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pdfescape.tar.xz; test -f "$f" || { echo "oreon: missing Source92 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ce556d76cdff99aa658bfbcba397347b3fc638750787931077c8c3884c1d9dae" || { echo "oreon: Source92 SHA256 mismatch for pdfescape.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pdfescape.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source93 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "13db5869796cf72f09ad50c5945b29b0dd310390ab3617468377e93ba52db61e" || { echo "oreon: Source93 SHA256 mismatch for pdfescape.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pdfmanagement.tar.xz; test -f "$f" || { echo "oreon: missing Source94 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "62d4f80ad2858badf123700a214d3fe19a955947234ddf630f9ccdf32891b6f4" || { echo "oreon: Source94 SHA256 mismatch for pdfmanagement.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pdfmanagement.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source95 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "033e4bb6c5329a1432ad7fea033de0780f7c82224f9fccd6d2a6e7412882fdf3" || { echo "oreon: Source95 SHA256 mismatch for pdfmanagement.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pdftexcmds.tar.xz; test -f "$f" || { echo "oreon: missing Source96 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "edf348a113fe792c3a4d601d637a2f6833b79bb86be895f265fa5411a5d4f69b" || { echo "oreon: Source96 SHA256 mismatch for pdftexcmds.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pdftexcmds.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source97 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "27e8c626f9163365a68bf17145937fb03e9382023be19d929a6e94246a098987" || { echo "oreon: Source97 SHA256 mismatch for pdftexcmds.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pslatex.tar.xz; test -f "$f" || { echo "oreon: missing Source98 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ec842fa032455ab21a57f3469e62adc6ac928ea969e968c1d31d07b0a1ef2c3f" || { echo "oreon: Source98 SHA256 mismatch for pslatex.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/psnfss.tar.xz; test -f "$f" || { echo "oreon: missing Source99 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "25a9a4b0eaa6c6970a9194518f0baba9574d788ed1997cd4bf507cc00ea2996c" || { echo "oreon: Source99 SHA256 mismatch for psnfss.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/psnfss.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source100 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a445acf9c8ba8b6bb78e7990bb63419d4cbdf766a74220cb483e5b116821dd4d" || { echo "oreon: Source100 SHA256 mismatch for psnfss.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pspicture.tar.xz; test -f "$f" || { echo "oreon: missing Source101 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "35cbf289734c9b647f2d8b17df23cbc077e224c6b897763072f6c0c774a1af6f" || { echo "oreon: Source101 SHA256 mismatch for pspicture.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pspicture.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source102 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "682e556e29d0048687fb4f8a0bc9e2b9cc6ded9a31f36e10db3498c1099b4df8" || { echo "oreon: Source102 SHA256 mismatch for pspicture.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/refcount.tar.xz; test -f "$f" || { echo "oreon: missing Source103 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7187382f8364172fd80b064235086b0b4076be8942d89f1c8aef2473ca938140" || { echo "oreon: Source103 SHA256 mismatch for refcount.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/refcount.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source104 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "de595ac4e61dfef95c79c9bca0b962ec718b6f4d0c9001e84f4704941d8e652e" || { echo "oreon: Source104 SHA256 mismatch for refcount.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/rerunfilecheck.tar.xz; test -f "$f" || { echo "oreon: missing Source105 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b63abce92724296bdcca429454b52ca8caaf902acc16c8c4421c286f1b5d0faf" || { echo "oreon: Source105 SHA256 mismatch for rerunfilecheck.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/rerunfilecheck.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source106 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "beef31ea6adf162d0df28b63dc3e3f55f2549a368bfb370f1985b79aca4c7bbf" || { echo "oreon: Source106 SHA256 mismatch for rerunfilecheck.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/stringenc.tar.xz; test -f "$f" || { echo "oreon: missing Source107 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "22d01de49bfbc35312b64265024332672c520ce0f33818d60d69f62869b6b348" || { echo "oreon: Source107 SHA256 mismatch for stringenc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/stringenc.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source108 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f56b6ec369ebeaff7d9164034aea49d3f07e7a5d3d13719f426b617f5950516a" || { echo "oreon: Source108 SHA256 mismatch for stringenc.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tagpdf.tar.xz; test -f "$f" || { echo "oreon: missing Source109 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0748c65d3d7154c6b46e5d8328ea2dbb02ac93301dd23e94bfc936f542e05aaa" || { echo "oreon: Source109 SHA256 mismatch for tagpdf.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tagpdf.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source110 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "746fbd2c1e1b4c97fefc0c12b54c40e070a042d6cd819afaf47d23be642441b1" || { echo "oreon: Source110 SHA256 mismatch for tagpdf.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tools.tar.xz; test -f "$f" || { echo "oreon: missing Source111 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cb3cced7a3ab923bb066ff1e0a14f79e1a02b8b248e4cfb4338079399badded2" || { echo "oreon: Source111 SHA256 mismatch for tools.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tools.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source112 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "40dcaa85bb52d417b6d5e30c5ab8c787b9d451f843d19f875d9e218323446d12" || { echo "oreon: Source112 SHA256 mismatch for tools.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/uniquecounter.tar.xz; test -f "$f" || { echo "oreon: missing Source113 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7aa4ca7c417e82c37fe2d551c10d56a59ef3bff30d5cc258f7fb067249e09f51" || { echo "oreon: Source113 SHA256 mismatch for uniquecounter.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/uniquecounter.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source114 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "72cfa78872e2759c90be9af586e718408ceb2dd8aaf081b3f2f24b3c997d223a" || { echo "oreon: Source114 SHA256 mismatch for uniquecounter.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/url.tar.xz; test -f "$f" || { echo "oreon: missing Source115 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "947284b030f06cfcbc7abb831bb5dff2b19312cf778161ee477348c2dd88fc09" || { echo "oreon: Source115 SHA256 mismatch for url.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/url.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source116 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "21a9d565c228bc8ae0a3afea4d32cd77b8627fab72f16d7ab2f11e58b3733611" || { echo "oreon: Source116 SHA256 mismatch for url.doc.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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

# Apply tools patch
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/tools-2026-02-10.patch
popd

# Rename .map files to .oldmap to avoid updmap-sys
mv %{buildroot}%{_texmf_main}/fonts/map/dvips/psnfss/psnfss.map %{buildroot}%{_texmf_main}/fonts/map/dvips/psnfss/psnfss.oldmap

# Main collection metapackage (empty)
%files

%files -n texlive-ae
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/public/ae/
%{_texmf_main}/fonts/vf/public/ae/
%{_texmf_main}/tex/latex/ae/
%doc %{_texmf_main}/doc/fonts/ae/

%files -n texlive-amscls
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/amscls/
%{_texmf_main}/tex/latex/amscls/
%doc %{_texmf_main}/doc/latex/amscls/

%files -n texlive-amsmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/amsmath/
%doc %{_texmf_main}/doc/latex/amsmath/

%files -n texlive-atbegshi
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/atbegshi/
%doc %{_texmf_main}/doc/latex/atbegshi/

%files -n texlive-atveryend
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/atveryend/
%doc %{_texmf_main}/doc/latex/atveryend/

%files -n texlive-auxhook
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/auxhook/
%doc %{_texmf_main}/doc/latex/auxhook/

%files -n texlive-babel
%license lppl1.3c.txt
%{_texmf_main}/makeindex/babel/
%{_texmf_main}/tex/generic/babel/
%doc %{_texmf_main}/doc/latex/babel/

%files -n texlive-babel-english
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-english/
%doc %{_texmf_main}/doc/generic/babel-english/

%files -n texlive-babelbib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/babelbib/
%{_texmf_main}/tex/latex/babelbib/
%doc %{_texmf_main}/doc/bibtex/babelbib/

%files -n texlive-bigintcalc
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/bigintcalc/
%doc %{_texmf_main}/doc/latex/bigintcalc/

%files -n texlive-bitset
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/bitset/
%doc %{_texmf_main}/doc/latex/bitset/

%files -n texlive-bookmark
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bookmark/
%doc %{_texmf_main}/doc/latex/bookmark/

%files -n texlive-carlisle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/carlisle/
%doc %{_texmf_main}/doc/latex/carlisle/

%files -n texlive-colortbl
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/colortbl/
%doc %{_texmf_main}/doc/latex/colortbl/

%files -n texlive-epstopdf-pkg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/epstopdf-pkg/
%doc %{_texmf_main}/doc/latex/epstopdf-pkg/

%files -n texlive-etexcmds
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/etexcmds/
%doc %{_texmf_main}/doc/latex/etexcmds/

%files -n texlive-etoolbox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/etoolbox/
%doc %{_texmf_main}/doc/latex/etoolbox/

%files -n texlive-fancyhdr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fancyhdr/
%doc %{_texmf_main}/doc/latex/fancyhdr/

%files -n texlive-firstaid
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/firstaid/
%doc %{_texmf_main}/doc/latex/firstaid/

%files -n texlive-fix2col
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fix2col/
%doc %{_texmf_main}/doc/latex/fix2col/

%files -n texlive-geometry
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/geometry/
%doc %{_texmf_main}/doc/latex/geometry/

%files -n texlive-gettitlestring
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/gettitlestring/
%doc %{_texmf_main}/doc/latex/gettitlestring/

%files -n texlive-graphics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/graphics/
%doc %{_texmf_main}/doc/latex/graphics/

%files -n texlive-graphics-cfg
%license pd.txt
%{_texmf_main}/tex/latex/graphics-cfg/
%doc %{_texmf_main}/doc/latex/graphics-cfg/

%files -n texlive-grfext
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/grfext/
%doc %{_texmf_main}/doc/latex/grfext/

%files -n texlive-hopatch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hopatch/
%doc %{_texmf_main}/doc/latex/hopatch/

%files -n texlive-hycolor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hycolor/
%doc %{_texmf_main}/doc/latex/hycolor/

%files -n texlive-hypcap
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hypcap/
%doc %{_texmf_main}/doc/latex/hypcap/

%files -n texlive-hyperref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hyperref/
%doc %{_texmf_main}/doc/latex/hyperref/

%files -n texlive-intcalc
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/intcalc/
%doc %{_texmf_main}/doc/latex/intcalc/

%files -n texlive-kvdefinekeys
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/kvdefinekeys/
%doc %{_texmf_main}/doc/latex/kvdefinekeys/

%files -n texlive-kvoptions
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kvoptions/
%doc %{_texmf_main}/doc/latex/kvoptions/

%files -n texlive-kvsetkeys
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kvsetkeys/
%doc %{_texmf_main}/doc/latex/kvsetkeys/

%files -n texlive-l3backend
%license lppl1.3c.txt
%{_texmf_main}/dvips/l3backend/
%{_texmf_main}/tex/latex/l3backend/
%doc %{_texmf_main}/doc/latex/l3backend/

%files -n texlive-l3kernel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/l3kernel/
%doc %{_texmf_main}/doc/latex/l3kernel/

%files -n texlive-l3packages
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/l3packages/
%doc %{_texmf_main}/doc/latex/l3packages/

%files -n texlive-latex-fonts
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/latex-fonts/
%{_texmf_main}/fonts/tfm/public/latex-fonts/
%doc %{_texmf_main}/doc/fonts/latex-fonts/

%files -n texlive-latex-lab
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/latex-lab/
%doc %{_texmf_main}/doc/latex/latex-lab/

%files -n texlive-latexconfig
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/latexconfig/

%files -n texlive-letltxmacro
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/letltxmacro/
%doc %{_texmf_main}/doc/latex/letltxmacro/

%files -n texlive-ltxcmds
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ltxcmds/
%doc %{_texmf_main}/doc/generic/ltxcmds/

%files -n texlive-ltxmisc
%license gpl2.txt
%license lppl1.3c.txt
%license pd.txt
%{_texmf_main}/tex/latex/ltxmisc/

%files -n texlive-lua-uni-algos
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/lua-uni-algos/
%doc %{_texmf_main}/doc/luatex/lua-uni-algos/

%files -n texlive-mfnfss
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mfnfss/
%doc %{_texmf_main}/doc/latex/mfnfss/

%files -n texlive-natbib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/natbib/
%{_texmf_main}/tex/latex/natbib/
%doc %{_texmf_main}/doc/latex/natbib/

%files -n texlive-pagesel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pagesel/
%doc %{_texmf_main}/doc/latex/pagesel/

%files -n texlive-pdfescape
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pdfescape/
%doc %{_texmf_main}/doc/latex/pdfescape/

%files -n texlive-pdfmanagement
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pdfmanagement/
%doc %{_texmf_main}/doc/latex/pdfmanagement/

%files -n texlive-pdftexcmds
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pdftexcmds/
%doc %{_texmf_main}/doc/generic/pdftexcmds/

%files -n texlive-pslatex
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/pslatex/
%{_texmf_main}/fonts/tfm/public/pslatex/
%{_texmf_main}/fonts/vf/public/pslatex/
%{_texmf_main}/tex/latex/pslatex/

%files -n texlive-psnfss
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/psnfss/
%{_texmf_main}/tex/latex/psnfss/
%doc %{_texmf_main}/doc/latex/psnfss/

%files -n texlive-pspicture
%license lppl1.3c.txt
%{_texmf_main}/dvips/pspicture/
%{_texmf_main}/tex/latex/pspicture/
%doc %{_texmf_main}/doc/latex/pspicture/

%files -n texlive-refcount
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/refcount/
%doc %{_texmf_main}/doc/latex/refcount/

%files -n texlive-rerunfilecheck
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rerunfilecheck/
%doc %{_texmf_main}/doc/latex/rerunfilecheck/

%files -n texlive-stringenc
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/stringenc/
%doc %{_texmf_main}/doc/latex/stringenc/

%files -n texlive-tagpdf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tagpdf/
%doc %{_texmf_main}/doc/latex/tagpdf/

%files -n texlive-tools
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tools/
%doc %{_texmf_main}/doc/latex/tools/

%files -n texlive-uniquecounter
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/uniquecounter/
%doc %{_texmf_main}/doc/latex/uniquecounter/

%files -n texlive-url
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/url/
%doc %{_texmf_main}/doc/latex/url/

%changelog
* Sat May 23 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12:svn77682-4
- Import TeX Live 2025 split from f44 for Oreon 11
