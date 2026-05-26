%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-xetex
Epoch:          12
Version:        svn78834
Release:        10%{?dist}
Summary:        XeTeX and packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-xetex.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabxetex.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabxetex.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidi-atbegshi.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidi-atbegshi.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidicontour.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidicontour.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidipagegrid.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidipagegrid.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidipresentation.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidipresentation.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidishadowtext.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidishadowtext.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/businesscard-qrcode.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/businesscard-qrcode.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cqubeamer.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cqubeamer.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex-faq.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex-faq.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixlatvian.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixlatvian.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/font-change-xetex.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/font-change-xetex.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontbook.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontbook.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontwrap.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontwrap.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interchar.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interchar.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/na-position.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/na-position.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/philokalia.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/philokalia.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptext.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptext.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shtthesis.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shtthesis.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simple-resume-cv.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simple-resume-cv.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simple-thesis-dissertation.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simple-thesis-dissertation.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tetragonos.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tetragonos.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucharclasses.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucharclasses.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-bidi.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-bidi.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unimath-plain-xetex.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unimath-plain-xetex.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unisugar.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unisugar.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xebaposter.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xebaposter.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xechangebar.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xechangebar.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecjk.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecjk.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecolor.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecolor.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecyr.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecyr.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xeindex.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xeindex.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xesearch.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xesearch.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xespotcolor.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xespotcolor.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-devanagari.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-devanagari.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-itrans.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-itrans.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-pstricks.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-pstricks.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-tibetan.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-tibetan.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexconfig.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexfontinfo.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexfontinfo.doc.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexko.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexko.doc.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexref.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexref.doc.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xevlna.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xevlna.doc.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zbmath-review-template.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zbmath-review-template.doc.tar.xz

# AppStream metadata for font components
Source89:        philokalia.metainfo.xml
# oreon url source checksums begin
%global source0_sha256 418e2de52bd2b2c83549b1fc18150d7a4d30270c9c4ff5cc5b87e98f16b7a33c
%global source0_file collection-xetex.tar.xz
%global source2_sha256 1402b5826e9805792a0d33752514822bd134d80a4ce81ac6c1bfd2f35fa1d44c
%global source2_file arabxetex.tar.xz
%global source3_sha256 573a68916ac43c498291eb809ca61e84ad5a2b09f20baa5a69a90ba046e417b2
%global source3_file arabxetex.doc.tar.xz
%global source4_sha256 1e2a310fd192e47c71574519ef571b8f3e858800dd22938e844d3ad21030d2a6
%global source4_file bidi-atbegshi.tar.xz
%global source5_sha256 4744539db60403c7314b219360d3eb7720d61ca3843e7b597eb9716fd8a243b2
%global source5_file bidi-atbegshi.doc.tar.xz
%global source6_sha256 1af1bc5dcf8ee6264d01977e3e08d10bfb6df4df9a0150c047363daf7f521bb9
%global source6_file bidicontour.tar.xz
%global source7_sha256 b71056a6081b34ee88e56bffa7a25266283578fef7ad45bdcf57208390345f5d
%global source7_file bidicontour.doc.tar.xz
%global source8_sha256 e7904ed059d624d7b7f9c6731d33d2baa8262ff127b7a695f7bb32c821d6d2a5
%global source8_file bidipagegrid.tar.xz
%global source9_sha256 b98710d64068f6307bc535f6dc1d85f8f47d4de9768d707c72afcb695d9615f6
%global source9_file bidipagegrid.doc.tar.xz
%global source10_sha256 40cdbc1824c051c7f83221e1f86b179fe3a31d2fd7e185a6a28a90635fcbd6ab
%global source10_file bidipresentation.tar.xz
%global source11_sha256 db52b97936442efc51a1b60fcebfbb575eb5da6bd3f26a7a9ce048b7f15de942
%global source11_file bidipresentation.doc.tar.xz
%global source12_sha256 4e5f17ba32775fa0347d47344beca6994e5778db30e3dd21d9a73fbdba6cb898
%global source12_file bidishadowtext.tar.xz
%global source13_sha256 6d2ca5300d76e3f12aec82221b919a41e579555d7a4d1d786039c79fd632c333
%global source13_file bidishadowtext.doc.tar.xz
%global source14_sha256 6b154dd86ee8e143bb9d674f4b09d223a95d6b4063e546c5515c9d6ba27ab2be
%global source14_file businesscard-qrcode.tar.xz
%global source15_sha256 8c91ec3a0581f8ae01e77a8dd927134173b126d5db084b5ece33e2f1881aa6b2
%global source15_file businesscard-qrcode.doc.tar.xz
%global source16_sha256 d203e73cc4b9f38ca4e8fea3c95e1791c02b07b95f240c75cf6a4405d3790211
%global source16_file cqubeamer.tar.xz
%global source17_sha256 56ea815018f2b465bb7aa3c3af2c16850f5c914289758012c91fb1409ba43d59
%global source17_file cqubeamer.doc.tar.xz
%global source18_sha256 906b771c12a53e7f770c2a4ff5ab7502a78975bd185a9aae95344473bfb90a88
%global source18_file ctex.tar.xz
%global source19_sha256 12db6b7914f4a5b53536d7d768bc52252763b7513b5c82c9c7287494ed80ac65
%global source19_file ctex.doc.tar.xz
%global source20_sha256 63e4e597b7fb7bdcbd10aaf11f706de14ad9f7de874658a3b1478ae80bc84f8f
%global source20_file ctex-faq.tar.xz
%global source21_sha256 4a130de70a5e00e30569528945c8513b6dfabc092daba4d6111061d4a2af2f7e
%global source21_file ctex-faq.doc.tar.xz
%global source22_sha256 c947331575c6a177fbaaac3e0fc6ddf38e8bf777f463b6f0bea963d97bf8b54c
%global source22_file fixlatvian.tar.xz
%global source23_sha256 1bbc85f2c63619c1e765bb1c16d42854ed1b03312af8a81baec2e6795c799976
%global source23_file fixlatvian.doc.tar.xz
%global source24_sha256 e8a254e69284b2e4f9b7167174ba856cca14dced1f56edec7838358696e03722
%global source24_file font-change-xetex.tar.xz
%global source25_sha256 f97936baf2d1a299149a116cd410412cc94a62bfd905337fc556d66da1e0f72c
%global source25_file font-change-xetex.doc.tar.xz
%global source26_sha256 43f5516f0a2d3e4da3099d40cfe1408f913041570deedf1830ae00ba8cdbd212
%global source26_file fontbook.tar.xz
%global source27_sha256 2cd8c5199f9cbf8f1f8fc9c1707646b82790821dbc2c36fd1a659072ea434559
%global source27_file fontbook.doc.tar.xz
%global source28_sha256 5746e17c35c412783de7e0cdda542594adea56603e4788d8bb080d8ea44e6616
%global source28_file fontwrap.tar.xz
%global source29_sha256 eb9c5389acbe741973783dd354642d28877544d886c3d62fc7d4818263457f2d
%global source29_file fontwrap.doc.tar.xz
%global source30_sha256 0cea538c05b04e68b79f02ed1a925cdd0b9960ed55a57ee508ba5885a265defd
%global source30_file interchar.tar.xz
%global source31_sha256 87009b419ba0f5c2c5c34499aed533311fcdc3e5490052ecb1e47b5965a8a47c
%global source31_file interchar.doc.tar.xz
%global source32_sha256 733c505cf2bf1e82e2f8543424bc147a44d1dcbaf8d246a1b1b18546f7a0b664
%global source32_file na-position.tar.xz
%global source33_sha256 b69d39825aa997e8c79110b242e1eb1853609736c36ed5785332311b9d8e4ed1
%global source33_file na-position.doc.tar.xz
%global source34_sha256 fd47b6965a373503f4592cba72790e9ff6e204f330fa89f390f0a0e146bfbddd
%global source34_file philokalia.tar.xz
%global source35_sha256 8d9495819bf6e9551ada8242663e820371fe443d0fafb05a50ec3675b5eb7f25
%global source35_file philokalia.doc.tar.xz
%global source36_sha256 d85a4f68ebacd76bbddabb530c9f029aa92e698b9fc6dec634cb4b461f00787a
%global source36_file ptext.tar.xz
%global source37_sha256 a95745ffd0fd45773adf4e4bf9588b4ca569cf3356c691b343d919018cd0d4ef
%global source37_file ptext.doc.tar.xz
%global source38_sha256 c49dd4e733944cb2dc7383b11c9c8685e124f70c66f9be97cac81659b96bf0a4
%global source38_file shtthesis.tar.xz
%global source39_sha256 dc2120790d82db827ddefa744797ba744d724d0d2da7638fbcd685b6e9ecacc4
%global source39_file shtthesis.doc.tar.xz
%global source40_sha256 a4f61a537cc686cfdf41d7dafb2841c7ee834d6a960ee99f899c6b51ed0e210d
%global source40_file simple-resume-cv.tar.xz
%global source41_sha256 0bd378cf9cfc5236f27be708b229164e26c2b8afb06eefadb6b9ad173db28cd2
%global source41_file simple-resume-cv.doc.tar.xz
%global source42_sha256 3cd3395ab2f23fa1d22589bfb448878f2a93469a34c7c1dbfe828bd5988d2c50
%global source42_file simple-thesis-dissertation.tar.xz
%global source43_sha256 b011cd1c7c9ea5f1153c693c4a1f637fa4b477a9ef040c42879e5b1396d58645
%global source43_file simple-thesis-dissertation.doc.tar.xz
%global source44_sha256 1b38f79676e1c7d06b85203c9e52aa9231b9a9110eff41309c7ee946399d0ead
%global source44_file tetragonos.tar.xz
%global source45_sha256 ecafffd4798f9c654a8aa7f6bafa39203c2ee442beb4b49528567a910d92f3fa
%global source45_file tetragonos.doc.tar.xz
%global source46_sha256 f081c0d08dffa8802f0d90bbab87d57c3b581f2a7cab540797ae5b815370c3c9
%global source46_file ucharclasses.tar.xz
%global source47_sha256 51095f75cc0b2bb2978fb0ebedf4bafffdb2f33bf8a4c1da94def4824cccd027
%global source47_file ucharclasses.doc.tar.xz
%global source48_sha256 75d3efdb248351edcc57eb55a1b478f5fc833c536d876f79dc8c4ef1a00f8956
%global source48_file unicode-bidi.tar.xz
%global source49_sha256 d96bfbc0c21ea847ab37af4e4a46fe2d597e30d62053595da32d83f57abdf57a
%global source49_file unicode-bidi.doc.tar.xz
%global source50_sha256 cf45710828f3ae50904a90bbd97f90bd9b7da490bcf537fb717f0db5875bb054
%global source50_file unimath-plain-xetex.tar.xz
%global source51_sha256 680f8fb97b57a5a6044a7ccbff512edc9123f05ebea80643066046b68547c0ba
%global source51_file unimath-plain-xetex.doc.tar.xz
%global source52_sha256 3acd0b75546976ae26b00c5af92e2b22bd33ca06c74eabca84a8d89764180a32
%global source52_file unisugar.tar.xz
%global source53_sha256 aa2b098f4920476933cb6582ef8fab163a0a663f7895ea10ff74512068cf6efe
%global source53_file unisugar.doc.tar.xz
%global source54_sha256 4da56b1ca094fbfea63d3f0b35407d107827ad1751a849f2f2231d0a9460ac37
%global source54_file xebaposter.tar.xz
%global source55_sha256 d0a6d1b181b37cd2fb7fe2303b49180fcb494082652aebb441050d2ebbe7515f
%global source55_file xebaposter.doc.tar.xz
%global source56_sha256 1bed93d19602cabecfb2ce5ce9fb7c3f94ee542c721400def05098255fe86797
%global source56_file xechangebar.tar.xz
%global source57_sha256 df9fd28e0890cb908d17ab31615d3a6ed432db8c3da868b970334976a7462274
%global source57_file xechangebar.doc.tar.xz
%global source58_sha256 f8675df08091c74a0c3e348c9da76c38f1ac561349c5dfa5b245cdc7840da399
%global source58_file xecjk.tar.xz
%global source59_sha256 c978798a1c434cb1017845cd36b9af4b565a2fd8f4d5af1aa8271f2ad3adfe19
%global source59_file xecjk.doc.tar.xz
%global source60_sha256 66d88a80b0528f57237c78e61ee67032db01fa2cffff59ad5918a2213b320311
%global source60_file xecolor.tar.xz
%global source61_sha256 09163917b3eac1118466b68681ecaf846bf46b2a5e748145e6b562e062e02994
%global source61_file xecolor.doc.tar.xz
%global source62_sha256 593896b80b3a4ac794d6364b6601a3eb709272fe46454d23e784413370339d64
%global source62_file xecyr.tar.xz
%global source63_sha256 2d9d9c2c738f0e1e3621ec401c5adf7cba1b024446966b870a04b744bb95bfef
%global source63_file xecyr.doc.tar.xz
%global source64_sha256 64847058845da0a915fcbcbb6efb212c4160ad0ace73260a4ed054dc5f97fb1c
%global source64_file xeindex.tar.xz
%global source65_sha256 51db9843e25b40f6aa1e2069a43b6b40ead1d9b0b0a29f966d8d322b39f1b984
%global source65_file xeindex.doc.tar.xz
%global source66_sha256 db9981ca6bd973df205f0c94a02f5e296b40d2f7ef4046aaa51e0bb1fb213fee
%global source66_file xesearch.tar.xz
%global source67_sha256 0ff83388fd451709806f2e46e9804aa0f46be48c097dd4291ebac828df224326
%global source67_file xesearch.doc.tar.xz
%global source68_sha256 3955c4b87241821e8c546e5a44d0576be933c64adfad445dbd53501d619683a2
%global source68_file xespotcolor.tar.xz
%global source69_sha256 ef79a5e84a6ce5599e6c9e50c8402d653fa78e6da1ff660964e8cf39d762d27f
%global source69_file xespotcolor.doc.tar.xz
%global source70_sha256 2b8ff45641f207deacaa06b1e7c0d0e025f3c8a813829c0ef330b019b35fd2b5
%global source70_file xetex-devanagari.tar.xz
%global source71_sha256 3b0a68e7575ac8c6e824707c3d9584804c6635427806a216f9c7f794e3b1ac61
%global source71_file xetex-devanagari.doc.tar.xz
%global source72_sha256 8c20f36ae226d089fee5bf8be80614cb418d8615b2900e8c742a7e3e65180523
%global source72_file xetex-itrans.tar.xz
%global source73_sha256 7e0c9709ed0bc9c4c96411b6ff119678a0fd0d0f6fa94a5d96dac13708aafd81
%global source73_file xetex-itrans.doc.tar.xz
%global source74_sha256 e7de90016a418a7ac6a6f11d2042106b1af97682c53e5bbd508f9c5ec2c72820
%global source74_file xetex-pstricks.tar.xz
%global source75_sha256 2e4f73c41088219765fd609e143ebb1e04f05be8c5cef1deb0cf137154816c9e
%global source75_file xetex-pstricks.doc.tar.xz
%global source76_sha256 b16ea132c2a42f89dd75c435e5c179cd52148dc68cff514c2be043c68f8f16fe
%global source76_file xetex-tibetan.tar.xz
%global source77_sha256 22c5f7b2913bcd12e0bc8eed327c33f665d299b1ca2219b6f0f82d39f6465532
%global source77_file xetex-tibetan.doc.tar.xz
%global source78_sha256 9a505894bdf246695cd1d7140f459f6589e36253da6cfe406c86bfadc70e104c
%global source78_file xetexconfig.tar.xz
%global source79_sha256 8208b938d8112b12c132059b287dbfa16befa1d466f6a0bb0b2668c43231bbc0
%global source79_file xetexfontinfo.tar.xz
%global source80_sha256 dba709aeb0a857ca99de94af7f02606ec4df296a4ad74485752bf262b1916e40
%global source80_file xetexfontinfo.doc.tar.xz
%global source81_sha256 c3167cf55470716b18900f08928d7e36419381b7a2511bd86f314b5defc50e30
%global source81_file xetexko.tar.xz
%global source82_sha256 a4308a671cb5cdb675375db7aac2279f2289e5179ba64f152a6fac35b5e34fd0
%global source82_file xetexko.doc.tar.xz
%global source83_sha256 1234b66aac2c5bb6c29830a29a287c6a68a172cac59e713cc374f302490fbce0
%global source83_file xetexref.tar.xz
%global source84_sha256 467461140a0b87e78eb2838d24c8f55906863b05c6ec7fd01f041288a956c9c4
%global source84_file xetexref.doc.tar.xz
%global source85_sha256 fb029d5dfbe0f3f50f2097e50efd31553d12cda6d565cf2009d7d54928ebfe31
%global source85_file xevlna.tar.xz
%global source86_sha256 0eb253eed6b9ab943fcd3982fe9c265c94d5734dbf53404e045fc611503bd84f
%global source86_file xevlna.doc.tar.xz
%global source87_sha256 41b88cd20b737535afaaf96d1daacffd301d7287f4516847f05bd5cd73c2573f
%global source87_file zbmath-review-template.tar.xz
%global source88_sha256 11337a0dd3e50540ba8752f45720a26f7af3472c3225e25d623df8d0fdd7cc88
%global source88_file zbmath-review-template.doc.tar.xz
# oreon url source checksums end
BuildRequires:  texlive-base
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-arabxetex
Requires:       texlive-bidi-atbegshi
Requires:       texlive-bidicontour
Requires:       texlive-bidipagegrid
Requires:       texlive-bidipresentation
Requires:       texlive-bidishadowtext
Requires:       texlive-businesscard-qrcode
Requires:       texlive-collection-basic
Requires:       texlive-cqubeamer
Requires:       texlive-ctex
Requires:       texlive-ctex-faq
Requires:       texlive-fixlatvian
Requires:       texlive-font-change-xetex
Requires:       texlive-fontbook
Requires:       texlive-fontwrap
Requires:       texlive-interchar
Requires:       texlive-na-position
Requires:       texlive-philokalia
Requires:       texlive-ptext
Requires:       texlive-shtthesis
Requires:       texlive-simple-resume-cv
Requires:       texlive-simple-thesis-dissertation
Requires:       texlive-tetragonos
Requires:       texlive-ucharclasses
Requires:       texlive-unicode-bidi
Requires:       texlive-unimath-plain-xetex
Requires:       texlive-unisugar
Requires:       texlive-xebaposter
Requires:       texlive-xechangebar
Requires:       texlive-xecjk
Requires:       texlive-xecolor
Requires:       texlive-xecyr
Requires:       texlive-xeindex
Requires:       texlive-xelatex-dev
Requires:       texlive-xesearch
Requires:       texlive-xespotcolor
Requires:       texlive-xetex
Requires:       texlive-xetex-devanagari
Requires:       texlive-xetex-itrans
Requires:       texlive-xetex-pstricks
Requires:       texlive-xetex-tibetan
Requires:       texlive-xetexconfig
Requires:       texlive-xetexfontinfo
Requires:       texlive-xetexko
Requires:       texlive-xetexref
Requires:       texlive-xevlna
Requires:       texlive-zbmath-review-template

%description
Packages for XeTeX, the Unicode/OpenType-enabled TeX by Jonathan Kew. See
https://tug.org/xetex.


%package -n texlive-arabxetex
Summary:        An ArabTeX-like interface for XeLaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-arabxetex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-arabxetex-doc <= 11:%{version}
Requires:       tex(amsmath.sty)
Requires:       tex(bidi.sty)
Requires:       tex(fontspec.sty)

%description -n texlive-arabxetex
ArabXeTeX provides a convenient ArabTeX-like user-interface for typesetting
languages using the Arabic script in XeLaTeX, with flexible access to font
features. Input in ArabTeX notation can be set in three different vocalization
modes or in roman transliteration. Direct UTF-8 input is also supported. The
parsing and converting of ArabTeX input to Unicode is done by means of TECkit
mappings. Version 1.0 provides support for Arabic, Maghribi Arabic, Farsi
(Persian), Urdu, Sindhi, Kashmiri, Ottoman Turkish, Kurdish, Jawi (Malay) and
Uighur. The documentation covers topics such as typesetting the Holy Quran and
typesetting bidirectional critical editions with the package ednotes.

%package -n texlive-bidi-atbegshi
Summary:        Bidi-aware shipout macros
Version:        svn62009
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-bidi-atbegshi-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-bidi-atbegshi-doc <= 11:%{version}
Requires:       tex(atbegshi-ltx.sty)

%description -n texlive-bidi-atbegshi
The package adds some commands to the atbegshi package for proper placement of
background material in the left and right corners of the output page, in both
LTR and RTL modes. The package only works with xelatex format and should be
loaded before the bidi package.

%package -n texlive-bidicontour
Summary:        Bidi-aware coloured contour around text
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-bidicontour-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-bidicontour-doc <= 11:%{version}
Requires:       tex(color.sty)
Requires:       tex(trig.sty)

%description -n texlive-bidicontour
The package is a re-implementation of the contour package, making it
bidi-aware, and adding support of the xdvipdfmx (when the outline option of the
package is used).

%package -n texlive-bidipagegrid
Summary:        Bidi-aware page grid in background
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-bidipagegrid-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-bidipagegrid-doc <= 11:%{version}
Requires:       tex(atbegshi.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)

%description -n texlive-bidipagegrid
The package is based on pagegrid.

%package -n texlive-bidipresentation
Summary:        Experimental bidi presentation
Version:        svn35267
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-bidipresentation-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-bidipresentation-doc <= 11:%{version}

%description -n texlive-bidipresentation
A great portion of the code is borrowed from the texpower bundle, with
modifications to get things working properly in both right to left and left to
right modes.

%package -n texlive-bidishadowtext
Summary:        Bidi-aware shadow text
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-bidishadowtext-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-bidishadowtext-doc <= 11:%{version}
Requires:       tex(color.sty)

%description -n texlive-bidishadowtext
This package allows you to typeset bidi-aware shadow text. It is a
re-implementation of the shadowtext package adding bidi support.

%package -n texlive-businesscard-qrcode
Summary:        Business cards with QR-Code
Version:        svn76924
License:        LGPL-2.1-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-businesscard-qrcode
What happens when you give your visiting card to someone? Either they manually
type the text into their computer or mobile phone, or it will end up in a box
and be forgotten. Nowadays data is required electronically, not on paper. Here
is the solution: A visiting card with QR-Code that contains a full vcard so
that it can be scanned with an app on the mobile phone and thereby
automatically imported into the electronic contacts. This also works well when
you are offline and bluetooth transfer fails. So here is the highly
configurable business card or visiting card with full vcard as QR-Code, ready
to send to online printers. You can specify the exact size of the paper and the
content within the paper, including generation of crop marks. The package
depends on the following other LaTeX packages: calc, crop, DejaVuSans,
etoolbox, fontawesome, fontenc, geometry, kvoptions, marvosym, qrcode,
varwidth, and wrapfig. The package needs XeLaTeX for working properly.

%package -n texlive-cqubeamer
Summary:        LaTeX Beamer Template for Chongqing University
Version:        svn54512
License:        MIT AND CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bookmark.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(perpage.sty)

%description -n texlive-cqubeamer
This package provides a LaTeX beamer template designed for researchers of
Chongqing University. It can be used for academic reports, conferences, or
thesis defense, and can be helpful for delivering a speech. It should be used
with the XeTeX engine.

%package -n texlive-ctex
Summary:        LaTeX classes and packages for Chinese typesetting
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ctex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ctex-doc <= 11:%{version}
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

%package -n texlive-fixlatvian
Summary:        Improve Latvian language support in XeLaTeX
Version:        svn21631
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fixlatvian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fixlatvian-doc <= 11:%{version}
Requires:       tex(caption.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(icomma.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(perpage.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(xstring.sty)

%description -n texlive-fixlatvian
The package offers improvement of the Latvian language support in polyglossia,
in particular in the area of the standard classes.

%package -n texlive-font-change-xetex
Summary:        Macros to change text and mathematics fonts in plain XeTeX
Version:        svn40404
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-font-change-xetex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-font-change-xetex-doc <= 11:%{version}

%description -n texlive-font-change-xetex
This package consists of macros that can be used to typeset "plain" XeTeX
documents using any OpenType or TrueType font installed on the computer system.
The macros allow the user to change the text mode fonts and some math mode
fonts. For any declared font family, various font style, weight, and size
variants like bold, italics, small caps, etc., are available through standard
and custom TeX control statements. Using the optional argument of the macros,
the available XeTeX font features and OpenType tags can be accessed. Other
features of the package include activating and deactivating hanging
punctuation, and support for special Unicode characters.

%package -n texlive-fontbook
Summary:        Generate a font book
Version:        svn23608
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fontbook-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fontbook-doc <= 11:%{version}
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xunicode.sty)

%description -n texlive-fontbook
The package provides a means of producing a 'book' of font samples (for
evaluation, etc.).

%package -n texlive-fontwrap
Summary:        Bind fonts to specific unicode blocks
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fontwrap-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fontwrap-doc <= 11:%{version}
Requires:       tex(fontspec.sty)
Requires:       tex(perltex.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)

%description -n texlive-fontwrap
The package (which runs under XeLaTeX) lets you bind fonts to specific unicode
blocks, for automatic font tagging of multilingual text. The package uses Perl
(via perltex) to construct its tables.

%package -n texlive-interchar
Summary:        Managing character class schemes in XeTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-interchar-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-interchar-doc <= 11:%{version}
Requires:       tex(xparse.sty)

%description -n texlive-interchar
The package manages character class schemes of XeTeX. Using this package, you
may switch among different character class schemes. Migration commands are
provided for make packages using this mechanism compatible with each others.

%package -n texlive-na-position
Summary:        Tables of relative positions of curves and asymptotes or tangents in Arabic documents
Version:        svn55559
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tkz-tab.sty)

%description -n texlive-na-position
This package facilitates, in most cases, the creation of tables of relative
positions of a curve and its asymptote, or a curve and a tangent in one of its
points. It depends on tkz-tab and listofitems, as well as amsmath, amsfonts,
mathrsfs, and amssymb. This package has to be used with polyglossia and XeLaTeX
to produce documents in Arabic.

%package -n texlive-philokalia
Summary:        A font to typeset the Philokalia Books
Version:        svn45356
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-philokalia-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-philokalia-doc <= 11:%{version}
Requires:       tex(lettrine.sty)
Requires:       tex(xltxtra.sty)

%description -n texlive-philokalia
The philokalia package has been designed to ease the use of the
Philokalia-Regular OpenType font with XeLaTeX. The font started as a project to
digitize the typeface used to typeset the Philokalia books.

%package -n texlive-ptext
Summary:        A 'lipsum' for Persian
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ptext-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ptext-doc <= 11:%{version}
Requires:       tex(biditools.sty)

%description -n texlive-ptext
The package provides lipsum-like facilities for the Persian language. The
source of the filling text is the Persian epic "the Shanameh" (100 paragraphs
are used.) The package needs to be run under XeLaTeX.

%package -n texlive-shtthesis
Summary:        An unofficial LaTeX thesis template for ShanghaiTech University
Version:        svn62441
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-alphalph
Requires:       biber
Requires:       texlive-biblatex
Requires:       texlive-biblatex-gb7714-2015
Requires:       texlive-booktabs
Requires:       texlive-caption
Requires:       texlive-colortbl
Requires:       texlive-ctex
Requires:       texlive-datetime
Requires:       texlive-enumitem
Requires:       texlive-fancyhdr
Requires:       texlive-fmtcount
Requires:       texlive-lastpage
Requires:       latexmk
Requires:       texlive-listings
Requires:       texlive-lua-alt-getopt
Requires:       texlive-lualatex-math
Requires:       texlive-mathtools
Requires:       texlive-ntheorem
Requires:       texlive-tex-gyre
Requires:       texlive-tocvsec2
Requires:       texlive-transparent
Requires:       texlive-undolabl
Requires:       texlive-unicode-math
Requires:       texlive-xits
Requires:       texlive-xstring

%description -n texlive-shtthesis
This package, forked from ucasthesis, is an unofficial LaTeX thesis template
for ShanghaiTech University and satisfies all format requirements of the
school. The user just needs to set \documentclass{shtthesis} and to set up
mandatory information via \shtsetup, then his or her thesis document will be
typeset properly.

%package -n texlive-simple-resume-cv
Summary:        Template for a simple resume or curriculum vitae (CV), in XeLaTeX
Version:        svn43057
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-simple-resume-cv
Template for a simple resume or curriculum vitae (CV), in XeLaTeX. Simple
template that can be further customized or extended, with numerous examples.

%package -n texlive-simple-thesis-dissertation
Summary:        Template for a simple thesis or dissertation (Ph.D. or master's degree) or technical report, in XeLaTeX
Version:        svn43058
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-simple-thesis-dissertation
Template for a simple thesis or dissertation (Ph.D. or master's degree) or
technical report, in XeLaTeX. Simple template that can be further customized or
extended, with numerous examples. Consistent style for figures, tables,
mathematical theorems, definitions, lemmas, etc.

%package -n texlive-tetragonos
Summary:        Four-Corner codes of Chinese characters
Version:        svn49732
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tetragonos
This is a XeLaTeX package for mapping Chinese characters to their codes in the
Four-Corner Method.

%package -n texlive-ucharclasses
Summary:        Font actions in XeTeX according to what is being processed
Version:        svn77682
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ucharclasses-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ucharclasses-doc <= 11:%{version}
Requires:       tex(ifxetex.sty)

%description -n texlive-ucharclasses
The package takes care of switching fonts when you switch from one Unicode
block to another in the text of a document. This way, you can write a document
with no explicit font selection, but a series of rules of the form "when
entering block ..., switch font to use ...".

%package -n texlive-unicode-bidi
Summary:        Experimental unicode bidi package for XeTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unicode-bidi
The experimental unicode-bidi package allows to mix non-RTL script with RTL
script without any markup.

%package -n texlive-unimath-plain-xetex
Summary:        OpenType math support in (plain) XeTeX
Version:        svn72498
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unimath-plain-xetex
This package provides OpenType math font support in plain TeX format. It only
works with the XeTeX engine.

%package -n texlive-unisugar
Summary:        Define syntactic sugar for Unicode LaTeX
Version:        svn22357
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-unisugar-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-unisugar-doc <= 11:%{version}
Requires:       tex(ifxetex.sty)

%description -n texlive-unisugar
The package allows the user to define shorthand aliases for single Unicode
characters, and also provides support for such aliases in RTL-text. The package
requires an TeX-alike system that uses Unicode input in a native way: current
examples are XeTeX and LuaTeX.

%package -n texlive-xebaposter
Summary:        Create beautiful scientific Persian/Latin posters using TikZ
Version:        svn75290
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xebaposter-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xebaposter-doc <= 11:%{version}

%description -n texlive-xebaposter
This package is designed for making beautiful scientific Persian/Latin posters.
It is a fork of baposter by Brian Amberg and Reinhold Kainhofer available at
LaTeX Poster Template. baposter's users should be able to compile their poster
using xebaposter (instead of baposter) without any problem.

%package -n texlive-xechangebar
Summary:        An extension of package changebar that can be used with XeLaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xechangebar
The package extends package changebar so it can be used with XeLaTeX. It
introduces the new option xetex for use with XeLaTeX. Everything else remains
the same and users should consult the original documentation for usage
information.

%package -n texlive-xecjk
Summary:        Support for CJK documents in XeLaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xecjk-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xecjk-doc <= 11:%{version}
Requires:       texlive-ctex

%description -n texlive-xecjk
A LaTeX package for typesetting CJK documents in the way users have become used
to, in the CJK package. The package requires a current version of xtemplate
(and hence of the current LaTeX3 development environment).

%package -n texlive-xecolor
Summary:        Support for color in XeLaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xecolor-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xecolor-doc <= 11:%{version}
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)

%description -n texlive-xecolor
This is a simple package which defines about 140 different colours using
XeTeX's colour feature. The colours can be used in bidirectional texts without
any problem.

%package -n texlive-xecyr
Summary:        Using Cyrillic languages in XeTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xecyr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xecyr-doc <= 11:%{version}
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(luatextra.sty)
Requires:       tex(misccorr.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)

%description -n texlive-xecyr
Helper tools for using Cyrillic languages with XeLaTeX and babel.

%package -n texlive-xeindex
Summary:        Automatic index generation for XeLaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xeindex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xeindex-doc <= 11:%{version}
Requires:       tex(makeidx.sty)
Requires:       tex(xesearch.sty)

%description -n texlive-xeindex
The package is based on XeSearch, and will automatically index words or phrases
in an XeLaTeX document. Words are declared in a list, and every occurrence then
creates an index entry whose content can be fully specified beforehand.

%package -n texlive-xesearch
Summary:        A string finder for XeTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xesearch-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xesearch-doc <= 11:%{version}

%description -n texlive-xesearch
The package finds strings (e.g. (parts of) words or phrases) and manipulates
them (apply any macro), thus turning each word or phrase into a possible
command. It is written in plain XeTeX and should thus work with any format (it
is known to work with LaTeX and ConTeXt). The main application for the moment
is XeIndex, an automatic index for XeLaTeX, but examples are given of simple
use to check spelling, count words, and highlight syntax of programming
languages.

%package -n texlive-xespotcolor
Summary:        Spot colours support for XeLaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xespotcolor-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xespotcolor-doc <= 11:%{version}
Requires:       tex(color.sty)
Requires:       tex(graphics.sty)
Requires:       tex(iftex.sty)
Requires:       tex(xcolor.sty)

%description -n texlive-xespotcolor
The package provides macros for using spot colours in LaTeX documents. The
package is a reimplementation of the spotcolor package for use with XeLaTeX. As
such, it has the same user interface and the same capabilities.

%package -n texlive-xetex-devanagari
Summary:        XeTeX input map for Unicode Devanagari
Version:        svn34296
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xetex-devanagari-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xetex-devanagari-doc <= 11:%{version}

%description -n texlive-xetex-devanagari
The package provides a map for use with Jonathan Kew's TECkit, to translate
Devanagari (encoded according to the Harvard/Kyoto convention) to Unicode
(range 0900-097F).

%package -n texlive-xetex-itrans
Summary:        Itrans input maps for use with XeLaTeX
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xetex-itrans-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xetex-itrans-doc <= 11:%{version}

%description -n texlive-xetex-itrans
The package provides maps for use with XeLaTeX with coding done using itrans.
Fontspec maps are provided for Devanagari (Sanskrit), for Sanskrit in Kannada
and for Kannada itself.

%package -n texlive-xetex-pstricks
Summary:        Running PSTricks under XeTeX
Version:        svn17055
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xetex-pstricks-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xetex-pstricks-doc <= 11:%{version}

%description -n texlive-xetex-pstricks
The package provides an indirection scheme for XeTeX to use the pstricks
xdvipdfmx.cfg configuration file, so that XeTeX documents will load it in
preference to the standard pstricks.con configuration file. With this
configuration, many PSTricks features can be used in XeLaTeX or plain XeTeX
documents.

%package -n texlive-xetex-tibetan
Summary:        XeTeX input maps for Unicode Tibetan
Version:        svn28847
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xetex-tibetan-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xetex-tibetan-doc <= 11:%{version}

%description -n texlive-xetex-tibetan
The package provides a map for use with Jonathan Kew's TECkit, to translate
Tibetan to Unicode (range 0F00-0FFF).

%package -n texlive-xetexconfig
Summary:        Crop.cfg for XeLaTeX
Version:        svn45845
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xetexconfig
crop.cfg for XeLaTeX

%package -n texlive-xetexfontinfo
Summary:        Report font features in XeTeX
Version:        svn15878
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xetexfontinfo-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xetexfontinfo-doc <= 11:%{version}

%description -n texlive-xetexfontinfo
A pair of documents to reveal the font features supported by fonts usable in
XeTeX. Use OpenType-info.tex for OpenType fonts, and AAT-info.tex for AAT fonts
(Mac OS X only).

%package -n texlive-xetexko
Summary:        Typeset Korean with Xe(La)TeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xetexko-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xetexko-doc <= 11:%{version}
Requires:       tex(fontspec.sty)
Requires:       tex(kolabels-utf.sty)

%description -n texlive-xetexko
The package supports typesetting Korean documents (including old Hangul texts),
using XeTeX. It enhances the existing support, in XeTeX, providing features
that provide quality typesetting. This package requires the cjk-ko package for
its full functionality.

%package -n texlive-xetexref
Summary:        Reference documentation of XeTeX
Version:        svn73885
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xetexref-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xetexref-doc <= 11:%{version}

%description -n texlive-xetexref
The package comprises reference documentation for XeTeX detailing its extended
features.

%package -n texlive-xevlna
Summary:        Insert non-breakable spaces using XeTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xevlna-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xevlna-doc <= 11:%{version}

%description -n texlive-xevlna
The package will directly insert nonbreakable spaces (in Czech, vlna or vlnka),
after nonsyllabic prepositions and single letter conjunctions, while the
document is being typeset. (The macros recognised maths and verbatim by TeX
means.) (Inserting nonbreakable spaces by a preprocessor will probably never be
fully reliable, because user defined macros and environments cannot reliably be
recognised.) The package works both with (Plain) XeTeX and with XeLaTeX.

%package -n texlive-zbmath-review-template
Summary:        Template for a zbMATH Open review
Version:        svn59693
License:        GPL-3.0-only AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(gensymb.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz-cd.sty)

%description -n texlive-zbmath-review-template
This package contains a template for zbMATH Open reviews. It will show what
your review will look like on zbMATH Open and you can test whether your
LaTeX-Code will compile on our system. The template has to be compiled using
XeLaTeX and relies on scrartcl, scrlayer-scrpage, amsfonts, amssymb, amsmath,
babel, enumitem, etoolbox, fontspec, gensymb, geometry, graphicx, mathrsfs,
mathtools, stmaryrd, textcomp, tikz-cd, xcolor, and xparse.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/collection-xetex.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "418e2de52bd2b2c83549b1fc18150d7a4d30270c9c4ff5cc5b87e98f16b7a33c" || { echo "oreon: Source0 SHA256 mismatch for collection-xetex.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/arabxetex.tar.xz; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1402b5826e9805792a0d33752514822bd134d80a4ce81ac6c1bfd2f35fa1d44c" || { echo "oreon: Source2 SHA256 mismatch for arabxetex.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/arabxetex.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "573a68916ac43c498291eb809ca61e84ad5a2b09f20baa5a69a90ba046e417b2" || { echo "oreon: Source3 SHA256 mismatch for arabxetex.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidi-atbegshi.tar.xz; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1e2a310fd192e47c71574519ef571b8f3e858800dd22938e844d3ad21030d2a6" || { echo "oreon: Source4 SHA256 mismatch for bidi-atbegshi.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidi-atbegshi.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4744539db60403c7314b219360d3eb7720d61ca3843e7b597eb9716fd8a243b2" || { echo "oreon: Source5 SHA256 mismatch for bidi-atbegshi.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidicontour.tar.xz; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1af1bc5dcf8ee6264d01977e3e08d10bfb6df4df9a0150c047363daf7f521bb9" || { echo "oreon: Source6 SHA256 mismatch for bidicontour.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidicontour.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b71056a6081b34ee88e56bffa7a25266283578fef7ad45bdcf57208390345f5d" || { echo "oreon: Source7 SHA256 mismatch for bidicontour.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidipagegrid.tar.xz; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e7904ed059d624d7b7f9c6731d33d2baa8262ff127b7a695f7bb32c821d6d2a5" || { echo "oreon: Source8 SHA256 mismatch for bidipagegrid.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidipagegrid.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b98710d64068f6307bc535f6dc1d85f8f47d4de9768d707c72afcb695d9615f6" || { echo "oreon: Source9 SHA256 mismatch for bidipagegrid.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidipresentation.tar.xz; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "40cdbc1824c051c7f83221e1f86b179fe3a31d2fd7e185a6a28a90635fcbd6ab" || { echo "oreon: Source10 SHA256 mismatch for bidipresentation.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidipresentation.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "db52b97936442efc51a1b60fcebfbb575eb5da6bd3f26a7a9ce048b7f15de942" || { echo "oreon: Source11 SHA256 mismatch for bidipresentation.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidishadowtext.tar.xz; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4e5f17ba32775fa0347d47344beca6994e5778db30e3dd21d9a73fbdba6cb898" || { echo "oreon: Source12 SHA256 mismatch for bidishadowtext.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bidishadowtext.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6d2ca5300d76e3f12aec82221b919a41e579555d7a4d1d786039c79fd632c333" || { echo "oreon: Source13 SHA256 mismatch for bidishadowtext.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/businesscard-qrcode.tar.xz; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6b154dd86ee8e143bb9d674f4b09d223a95d6b4063e546c5515c9d6ba27ab2be" || { echo "oreon: Source14 SHA256 mismatch for businesscard-qrcode.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/businesscard-qrcode.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8c91ec3a0581f8ae01e77a8dd927134173b126d5db084b5ece33e2f1881aa6b2" || { echo "oreon: Source15 SHA256 mismatch for businesscard-qrcode.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/cqubeamer.tar.xz; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d203e73cc4b9f38ca4e8fea3c95e1791c02b07b95f240c75cf6a4405d3790211" || { echo "oreon: Source16 SHA256 mismatch for cqubeamer.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/cqubeamer.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "56ea815018f2b465bb7aa3c3af2c16850f5c914289758012c91fb1409ba43d59" || { echo "oreon: Source17 SHA256 mismatch for cqubeamer.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ctex.tar.xz; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "906b771c12a53e7f770c2a4ff5ab7502a78975bd185a9aae95344473bfb90a88" || { echo "oreon: Source18 SHA256 mismatch for ctex.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ctex.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "12db6b7914f4a5b53536d7d768bc52252763b7513b5c82c9c7287494ed80ac65" || { echo "oreon: Source19 SHA256 mismatch for ctex.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ctex-faq.tar.xz; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "63e4e597b7fb7bdcbd10aaf11f706de14ad9f7de874658a3b1478ae80bc84f8f" || { echo "oreon: Source20 SHA256 mismatch for ctex-faq.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ctex-faq.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4a130de70a5e00e30569528945c8513b6dfabc092daba4d6111061d4a2af2f7e" || { echo "oreon: Source21 SHA256 mismatch for ctex-faq.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fixlatvian.tar.xz; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c947331575c6a177fbaaac3e0fc6ddf38e8bf777f463b6f0bea963d97bf8b54c" || { echo "oreon: Source22 SHA256 mismatch for fixlatvian.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fixlatvian.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1bbc85f2c63619c1e765bb1c16d42854ed1b03312af8a81baec2e6795c799976" || { echo "oreon: Source23 SHA256 mismatch for fixlatvian.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/font-change-xetex.tar.xz; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e8a254e69284b2e4f9b7167174ba856cca14dced1f56edec7838358696e03722" || { echo "oreon: Source24 SHA256 mismatch for font-change-xetex.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/font-change-xetex.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f97936baf2d1a299149a116cd410412cc94a62bfd905337fc556d66da1e0f72c" || { echo "oreon: Source25 SHA256 mismatch for font-change-xetex.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fontbook.tar.xz; test -f "$f" || { echo "oreon: missing Source26 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "43f5516f0a2d3e4da3099d40cfe1408f913041570deedf1830ae00ba8cdbd212" || { echo "oreon: Source26 SHA256 mismatch for fontbook.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fontbook.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source27 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2cd8c5199f9cbf8f1f8fc9c1707646b82790821dbc2c36fd1a659072ea434559" || { echo "oreon: Source27 SHA256 mismatch for fontbook.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fontwrap.tar.xz; test -f "$f" || { echo "oreon: missing Source28 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5746e17c35c412783de7e0cdda542594adea56603e4788d8bb080d8ea44e6616" || { echo "oreon: Source28 SHA256 mismatch for fontwrap.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fontwrap.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source29 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "eb9c5389acbe741973783dd354642d28877544d886c3d62fc7d4818263457f2d" || { echo "oreon: Source29 SHA256 mismatch for fontwrap.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/interchar.tar.xz; test -f "$f" || { echo "oreon: missing Source30 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0cea538c05b04e68b79f02ed1a925cdd0b9960ed55a57ee508ba5885a265defd" || { echo "oreon: Source30 SHA256 mismatch for interchar.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/interchar.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "87009b419ba0f5c2c5c34499aed533311fcdc3e5490052ecb1e47b5965a8a47c" || { echo "oreon: Source31 SHA256 mismatch for interchar.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/na-position.tar.xz; test -f "$f" || { echo "oreon: missing Source32 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "733c505cf2bf1e82e2f8543424bc147a44d1dcbaf8d246a1b1b18546f7a0b664" || { echo "oreon: Source32 SHA256 mismatch for na-position.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/na-position.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source33 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b69d39825aa997e8c79110b242e1eb1853609736c36ed5785332311b9d8e4ed1" || { echo "oreon: Source33 SHA256 mismatch for na-position.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/philokalia.tar.xz; test -f "$f" || { echo "oreon: missing Source34 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fd47b6965a373503f4592cba72790e9ff6e204f330fa89f390f0a0e146bfbddd" || { echo "oreon: Source34 SHA256 mismatch for philokalia.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/philokalia.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source35 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8d9495819bf6e9551ada8242663e820371fe443d0fafb05a50ec3675b5eb7f25" || { echo "oreon: Source35 SHA256 mismatch for philokalia.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ptext.tar.xz; test -f "$f" || { echo "oreon: missing Source36 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d85a4f68ebacd76bbddabb530c9f029aa92e698b9fc6dec634cb4b461f00787a" || { echo "oreon: Source36 SHA256 mismatch for ptext.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ptext.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source37 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a95745ffd0fd45773adf4e4bf9588b4ca569cf3356c691b343d919018cd0d4ef" || { echo "oreon: Source37 SHA256 mismatch for ptext.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/shtthesis.tar.xz; test -f "$f" || { echo "oreon: missing Source38 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c49dd4e733944cb2dc7383b11c9c8685e124f70c66f9be97cac81659b96bf0a4" || { echo "oreon: Source38 SHA256 mismatch for shtthesis.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/shtthesis.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source39 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dc2120790d82db827ddefa744797ba744d724d0d2da7638fbcd685b6e9ecacc4" || { echo "oreon: Source39 SHA256 mismatch for shtthesis.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/simple-resume-cv.tar.xz; test -f "$f" || { echo "oreon: missing Source40 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a4f61a537cc686cfdf41d7dafb2841c7ee834d6a960ee99f899c6b51ed0e210d" || { echo "oreon: Source40 SHA256 mismatch for simple-resume-cv.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/simple-resume-cv.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source41 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0bd378cf9cfc5236f27be708b229164e26c2b8afb06eefadb6b9ad173db28cd2" || { echo "oreon: Source41 SHA256 mismatch for simple-resume-cv.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/simple-thesis-dissertation.tar.xz; test -f "$f" || { echo "oreon: missing Source42 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3cd3395ab2f23fa1d22589bfb448878f2a93469a34c7c1dbfe828bd5988d2c50" || { echo "oreon: Source42 SHA256 mismatch for simple-thesis-dissertation.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/simple-thesis-dissertation.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source43 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b011cd1c7c9ea5f1153c693c4a1f637fa4b477a9ef040c42879e5b1396d58645" || { echo "oreon: Source43 SHA256 mismatch for simple-thesis-dissertation.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tetragonos.tar.xz; test -f "$f" || { echo "oreon: missing Source44 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1b38f79676e1c7d06b85203c9e52aa9231b9a9110eff41309c7ee946399d0ead" || { echo "oreon: Source44 SHA256 mismatch for tetragonos.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tetragonos.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source45 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ecafffd4798f9c654a8aa7f6bafa39203c2ee442beb4b49528567a910d92f3fa" || { echo "oreon: Source45 SHA256 mismatch for tetragonos.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ucharclasses.tar.xz; test -f "$f" || { echo "oreon: missing Source46 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f081c0d08dffa8802f0d90bbab87d57c3b581f2a7cab540797ae5b815370c3c9" || { echo "oreon: Source46 SHA256 mismatch for ucharclasses.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ucharclasses.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source47 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "51095f75cc0b2bb2978fb0ebedf4bafffdb2f33bf8a4c1da94def4824cccd027" || { echo "oreon: Source47 SHA256 mismatch for ucharclasses.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/unicode-bidi.tar.xz; test -f "$f" || { echo "oreon: missing Source48 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "75d3efdb248351edcc57eb55a1b478f5fc833c536d876f79dc8c4ef1a00f8956" || { echo "oreon: Source48 SHA256 mismatch for unicode-bidi.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/unicode-bidi.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source49 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d96bfbc0c21ea847ab37af4e4a46fe2d597e30d62053595da32d83f57abdf57a" || { echo "oreon: Source49 SHA256 mismatch for unicode-bidi.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/unimath-plain-xetex.tar.xz; test -f "$f" || { echo "oreon: missing Source50 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cf45710828f3ae50904a90bbd97f90bd9b7da490bcf537fb717f0db5875bb054" || { echo "oreon: Source50 SHA256 mismatch for unimath-plain-xetex.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/unimath-plain-xetex.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source51 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "680f8fb97b57a5a6044a7ccbff512edc9123f05ebea80643066046b68547c0ba" || { echo "oreon: Source51 SHA256 mismatch for unimath-plain-xetex.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/unisugar.tar.xz; test -f "$f" || { echo "oreon: missing Source52 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3acd0b75546976ae26b00c5af92e2b22bd33ca06c74eabca84a8d89764180a32" || { echo "oreon: Source52 SHA256 mismatch for unisugar.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/unisugar.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source53 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "aa2b098f4920476933cb6582ef8fab163a0a663f7895ea10ff74512068cf6efe" || { echo "oreon: Source53 SHA256 mismatch for unisugar.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xebaposter.tar.xz; test -f "$f" || { echo "oreon: missing Source54 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4da56b1ca094fbfea63d3f0b35407d107827ad1751a849f2f2231d0a9460ac37" || { echo "oreon: Source54 SHA256 mismatch for xebaposter.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xebaposter.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source55 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d0a6d1b181b37cd2fb7fe2303b49180fcb494082652aebb441050d2ebbe7515f" || { echo "oreon: Source55 SHA256 mismatch for xebaposter.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xechangebar.tar.xz; test -f "$f" || { echo "oreon: missing Source56 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1bed93d19602cabecfb2ce5ce9fb7c3f94ee542c721400def05098255fe86797" || { echo "oreon: Source56 SHA256 mismatch for xechangebar.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xechangebar.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source57 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "df9fd28e0890cb908d17ab31615d3a6ed432db8c3da868b970334976a7462274" || { echo "oreon: Source57 SHA256 mismatch for xechangebar.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xecjk.tar.xz; test -f "$f" || { echo "oreon: missing Source58 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f8675df08091c74a0c3e348c9da76c38f1ac561349c5dfa5b245cdc7840da399" || { echo "oreon: Source58 SHA256 mismatch for xecjk.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xecjk.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source59 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c978798a1c434cb1017845cd36b9af4b565a2fd8f4d5af1aa8271f2ad3adfe19" || { echo "oreon: Source59 SHA256 mismatch for xecjk.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xecolor.tar.xz; test -f "$f" || { echo "oreon: missing Source60 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "66d88a80b0528f57237c78e61ee67032db01fa2cffff59ad5918a2213b320311" || { echo "oreon: Source60 SHA256 mismatch for xecolor.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xecolor.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source61 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "09163917b3eac1118466b68681ecaf846bf46b2a5e748145e6b562e062e02994" || { echo "oreon: Source61 SHA256 mismatch for xecolor.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xecyr.tar.xz; test -f "$f" || { echo "oreon: missing Source62 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "593896b80b3a4ac794d6364b6601a3eb709272fe46454d23e784413370339d64" || { echo "oreon: Source62 SHA256 mismatch for xecyr.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xecyr.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source63 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2d9d9c2c738f0e1e3621ec401c5adf7cba1b024446966b870a04b744bb95bfef" || { echo "oreon: Source63 SHA256 mismatch for xecyr.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xeindex.tar.xz; test -f "$f" || { echo "oreon: missing Source64 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "64847058845da0a915fcbcbb6efb212c4160ad0ace73260a4ed054dc5f97fb1c" || { echo "oreon: Source64 SHA256 mismatch for xeindex.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xeindex.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source65 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "51db9843e25b40f6aa1e2069a43b6b40ead1d9b0b0a29f966d8d322b39f1b984" || { echo "oreon: Source65 SHA256 mismatch for xeindex.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xesearch.tar.xz; test -f "$f" || { echo "oreon: missing Source66 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "db9981ca6bd973df205f0c94a02f5e296b40d2f7ef4046aaa51e0bb1fb213fee" || { echo "oreon: Source66 SHA256 mismatch for xesearch.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xesearch.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source67 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0ff83388fd451709806f2e46e9804aa0f46be48c097dd4291ebac828df224326" || { echo "oreon: Source67 SHA256 mismatch for xesearch.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xespotcolor.tar.xz; test -f "$f" || { echo "oreon: missing Source68 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3955c4b87241821e8c546e5a44d0576be933c64adfad445dbd53501d619683a2" || { echo "oreon: Source68 SHA256 mismatch for xespotcolor.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xespotcolor.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source69 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ef79a5e84a6ce5599e6c9e50c8402d653fa78e6da1ff660964e8cf39d762d27f" || { echo "oreon: Source69 SHA256 mismatch for xespotcolor.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetex-devanagari.tar.xz; test -f "$f" || { echo "oreon: missing Source70 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2b8ff45641f207deacaa06b1e7c0d0e025f3c8a813829c0ef330b019b35fd2b5" || { echo "oreon: Source70 SHA256 mismatch for xetex-devanagari.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetex-devanagari.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source71 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3b0a68e7575ac8c6e824707c3d9584804c6635427806a216f9c7f794e3b1ac61" || { echo "oreon: Source71 SHA256 mismatch for xetex-devanagari.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetex-itrans.tar.xz; test -f "$f" || { echo "oreon: missing Source72 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8c20f36ae226d089fee5bf8be80614cb418d8615b2900e8c742a7e3e65180523" || { echo "oreon: Source72 SHA256 mismatch for xetex-itrans.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetex-itrans.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source73 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7e0c9709ed0bc9c4c96411b6ff119678a0fd0d0f6fa94a5d96dac13708aafd81" || { echo "oreon: Source73 SHA256 mismatch for xetex-itrans.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetex-pstricks.tar.xz; test -f "$f" || { echo "oreon: missing Source74 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e7de90016a418a7ac6a6f11d2042106b1af97682c53e5bbd508f9c5ec2c72820" || { echo "oreon: Source74 SHA256 mismatch for xetex-pstricks.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetex-pstricks.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source75 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2e4f73c41088219765fd609e143ebb1e04f05be8c5cef1deb0cf137154816c9e" || { echo "oreon: Source75 SHA256 mismatch for xetex-pstricks.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetex-tibetan.tar.xz; test -f "$f" || { echo "oreon: missing Source76 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b16ea132c2a42f89dd75c435e5c179cd52148dc68cff514c2be043c68f8f16fe" || { echo "oreon: Source76 SHA256 mismatch for xetex-tibetan.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetex-tibetan.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source77 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "22c5f7b2913bcd12e0bc8eed327c33f665d299b1ca2219b6f0f82d39f6465532" || { echo "oreon: Source77 SHA256 mismatch for xetex-tibetan.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetexconfig.tar.xz; test -f "$f" || { echo "oreon: missing Source78 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9a505894bdf246695cd1d7140f459f6589e36253da6cfe406c86bfadc70e104c" || { echo "oreon: Source78 SHA256 mismatch for xetexconfig.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetexfontinfo.tar.xz; test -f "$f" || { echo "oreon: missing Source79 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8208b938d8112b12c132059b287dbfa16befa1d466f6a0bb0b2668c43231bbc0" || { echo "oreon: Source79 SHA256 mismatch for xetexfontinfo.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetexfontinfo.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source80 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dba709aeb0a857ca99de94af7f02606ec4df296a4ad74485752bf262b1916e40" || { echo "oreon: Source80 SHA256 mismatch for xetexfontinfo.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetexko.tar.xz; test -f "$f" || { echo "oreon: missing Source81 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c3167cf55470716b18900f08928d7e36419381b7a2511bd86f314b5defc50e30" || { echo "oreon: Source81 SHA256 mismatch for xetexko.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetexko.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source82 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a4308a671cb5cdb675375db7aac2279f2289e5179ba64f152a6fac35b5e34fd0" || { echo "oreon: Source82 SHA256 mismatch for xetexko.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetexref.tar.xz; test -f "$f" || { echo "oreon: missing Source83 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1234b66aac2c5bb6c29830a29a287c6a68a172cac59e713cc374f302490fbce0" || { echo "oreon: Source83 SHA256 mismatch for xetexref.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xetexref.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source84 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "467461140a0b87e78eb2838d24c8f55906863b05c6ec7fd01f041288a956c9c4" || { echo "oreon: Source84 SHA256 mismatch for xetexref.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xevlna.tar.xz; test -f "$f" || { echo "oreon: missing Source85 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fb029d5dfbe0f3f50f2097e50efd31553d12cda6d565cf2009d7d54928ebfe31" || { echo "oreon: Source85 SHA256 mismatch for xevlna.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/xevlna.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source86 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0eb253eed6b9ab943fcd3982fe9c265c94d5734dbf53404e045fc611503bd84f" || { echo "oreon: Source86 SHA256 mismatch for xevlna.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/zbmath-review-template.tar.xz; test -f "$f" || { echo "oreon: missing Source87 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "41b88cd20b737535afaaf96d1daacffd301d7287f4516847f05bd5cd73c2573f" || { echo "oreon: Source87 SHA256 mismatch for zbmath-review-template.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/zbmath-review-template.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source88 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "11337a0dd3e50540ba8752f45720a26f7af3472c3225e25d623df8d0fdd7cc88" || { echo "oreon: Source88 SHA256 mismatch for zbmath-review-template.doc.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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

# Install AppStream metadata for font components
cp %{SOURCE89} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/philokalia %{buildroot}%{_datadir}/fonts/philokalia

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-arabxetex
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/xelatex/arabxetex/
%doc %{_texmf_main}/doc/xelatex/arabxetex/

%files -n texlive-bidi-atbegshi
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidi-atbegshi/
%doc %{_texmf_main}/doc/xelatex/bidi-atbegshi/

%files -n texlive-bidicontour
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidicontour/
%doc %{_texmf_main}/doc/xelatex/bidicontour/

%files -n texlive-bidipagegrid
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidipagegrid/
%doc %{_texmf_main}/doc/xelatex/bidipagegrid/

%files -n texlive-bidipresentation
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidipresentation/
%doc %{_texmf_main}/doc/xelatex/bidipresentation/

%files -n texlive-bidishadowtext
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidishadowtext/
%doc %{_texmf_main}/doc/xelatex/bidishadowtext/

%files -n texlive-businesscard-qrcode
%license lgpl2.1.txt
%{_texmf_main}/tex/xelatex/businesscard-qrcode/
%doc %{_texmf_main}/doc/xelatex/businesscard-qrcode/

%files -n texlive-cqubeamer
%license mit.txt
%license cc-by-4.txt
%{_texmf_main}/tex/xelatex/cqubeamer/
%doc %{_texmf_main}/doc/xelatex/cqubeamer/

%files -n texlive-ctex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ctex/
%{_texmf_main}/tex/latex/ctex/
%{_texmf_main}/tex/luatex/ctex/
%doc %{_texmf_main}/doc/latex/ctex/

%files -n texlive-ctex-faq
%license fdl.txt
%doc %{_texmf_main}/doc/latex/ctex-faq/

%files -n texlive-fixlatvian
%license lppl1.3c.txt
%{_texmf_main}/makeindex/fixlatvian/
%{_texmf_main}/tex/xelatex/fixlatvian/
%doc %{_texmf_main}/doc/xelatex/fixlatvian/

%files -n texlive-font-change-xetex
%license cc-by-sa-4.txt
%{_texmf_main}/tex/xetex/font-change-xetex/
%doc %{_texmf_main}/doc/xetex/font-change-xetex/

%files -n texlive-fontbook
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/fontbook/
%doc %{_texmf_main}/doc/xelatex/fontbook/

%files -n texlive-fontwrap
%license gpl2.txt
%{_texmf_main}/tex/xelatex/fontwrap/
%doc %{_texmf_main}/doc/xelatex/fontwrap/

%files -n texlive-interchar
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/interchar/
%doc %{_texmf_main}/doc/xelatex/interchar/

%files -n texlive-na-position
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/na-position/
%doc %{_texmf_main}/doc/xelatex/na-position/

%files -n texlive-philokalia
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/philokalia/
%{_texmf_main}/tex/xelatex/philokalia/
%doc %{_texmf_main}/doc/xelatex/philokalia/
%{_datadir}/fonts/philokalia
%{_datadir}/appdata/philokalia.metainfo.xml

%files -n texlive-ptext
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/ptext/
%doc %{_texmf_main}/doc/xelatex/ptext/

%files -n texlive-shtthesis
%license gpl3.txt
%{_texmf_main}/tex/latex/shtthesis/
%doc %{_texmf_main}/doc/latex/shtthesis/

%files -n texlive-simple-resume-cv
%license pd.txt
%{_texmf_main}/tex/xelatex/simple-resume-cv/
%doc %{_texmf_main}/doc/xelatex/simple-resume-cv/

%files -n texlive-simple-thesis-dissertation
%license pd.txt
%{_texmf_main}/tex/xelatex/simple-thesis-dissertation/
%doc %{_texmf_main}/doc/xelatex/simple-thesis-dissertation/

%files -n texlive-tetragonos
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/tetragonos/
%doc %{_texmf_main}/doc/xelatex/tetragonos/

%files -n texlive-ucharclasses
%license pd.txt
%{_texmf_main}/tex/xelatex/ucharclasses/
%doc %{_texmf_main}/doc/xelatex/ucharclasses/

%files -n texlive-unicode-bidi
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/unicode-bidi/
%doc %{_texmf_main}/doc/xelatex/unicode-bidi/

%files -n texlive-unimath-plain-xetex
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/xetex/unimath-plain-xetex/
%doc %{_texmf_main}/doc/xetex/unimath-plain-xetex/

%files -n texlive-unisugar
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/unisugar/
%doc %{_texmf_main}/doc/xelatex/unisugar/

%files -n texlive-xebaposter
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xebaposter/
%doc %{_texmf_main}/doc/latex/xebaposter/

%files -n texlive-xechangebar
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xechangebar/
%doc %{_texmf_main}/doc/xelatex/xechangebar/

%files -n texlive-xecjk
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/xelatex/xecjk/
%doc %{_texmf_main}/doc/xelatex/xecjk/

%files -n texlive-xecolor
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xecolor/
%doc %{_texmf_main}/doc/xelatex/xecolor/

%files -n texlive-xecyr
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xecyr/
%doc %{_texmf_main}/doc/xelatex/xecyr/

%files -n texlive-xeindex
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xeindex/
%doc %{_texmf_main}/doc/xelatex/xeindex/

%files -n texlive-xesearch
%license lppl1.3c.txt
%{_texmf_main}/tex/xetex/xesearch/
%doc %{_texmf_main}/doc/xetex/xesearch/

%files -n texlive-xespotcolor
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xespotcolor/
%doc %{_texmf_main}/doc/xelatex/xespotcolor/

%files -n texlive-xetex-devanagari
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%doc %{_texmf_main}/doc/xetex/xetex-devanagari/

%files -n texlive-xetex-itrans
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%doc %{_texmf_main}/doc/xelatex/xetex-itrans/

%files -n texlive-xetex-pstricks
%license pd.txt
%{_texmf_main}/tex/xelatex/xetex-pstricks/
%{_texmf_main}/tex/xetex/xetex-pstricks/
%doc %{_texmf_main}/doc/xetex/xetex-pstricks/

%files -n texlive-xetex-tibetan
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%doc %{_texmf_main}/doc/xetex/xetex-tibetan/

%files -n texlive-xetexconfig
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xetexconfig/

%files -n texlive-xetexfontinfo
%license apache2.txt
%{_texmf_main}/tex/xetex/xetexfontinfo/
%doc %{_texmf_main}/doc/xetex/xetexfontinfo/

%files -n texlive-xetexko
%license lppl1.3c.txt
%{_texmf_main}/tex/xetex/xetexko/
%doc %{_texmf_main}/doc/xetex/xetexko/

%files -n texlive-xetexref
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/xetex/xetexref/

%files -n texlive-xevlna
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xevlna/
%doc %{_texmf_main}/doc/xelatex/xevlna/

%files -n texlive-zbmath-review-template
%license gpl3.txt
%license cc-by-sa-4.txt
%{_texmf_main}/tex/xelatex/zbmath-review-template/
%doc %{_texmf_main}/doc/xelatex/zbmath-review-template/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12:svn78834-10
- Import
