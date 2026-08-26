%global source0_hash 800991b6bb8ac7772ad030ad665b812abd9b294498f7b7678be721ccc87d54607e267bd189a0591ebead2c6ecb64047e5b5581c374f067c3b1575b6d442cc6c9
%global source1_hash 900a9d4fb8f2318866d55ae1b18f26cb7ae52cf2450bf0765639d68e4d00dc6e

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langgreek
Epoch:          12
Version:        svn65038
Release:        4%{?dist}
Summary:        Greek

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash c30761113caabce53316cebc4d8db52abc6dc12eac8699402dce1d1095c558f0b3e66c57b5feb2bd0a320c415c80405c12b815d99f55cdc20ef130d07424aab6
%global source3_hash 647dc3e327422294c78bbf207859197914c214d032d1d676eecb085f30958eea33d464d84f5472af1eed6c05d23b02a6b10b1f62fd38c1056249fe1c83e3a99d
%global source4_hash c6e8493a80e328a10208088f7490a14bbec76fc8d969b85c6505d655840d9e4d8e05da3a1a3b17d76fcc0ad26df7251765d7d4e812000cd3fb9101ad5a46c3a9
%global source5_hash 3143cf03735fc6e5b3a77f17b6099f139d6a1cfcaecf140dab6eb4c72398742719956bc03052e539eefa9acbebd00ab14f7b0be829ece74b8a66dd227580542b
%global source6_hash 7dc4d59d4cd895997c89016f944056202e9b086ae39f3e6c26558de17da6e87849eeeed0c2c0c0842ebb4df4142a8a5635f25ca55ca5b50b6cb089241ed4373f
%global source7_hash b94b10d44c274187bf5195e5c1897417ee992cc4b23d991c460ac1c27aef4242cdd237ceb91bb7ba1f640110dfb1f8b75d24bd76bd3ab8489ee95e9244debf60
%global source8_hash 0e7cecfdfa102113f75f46f9c8bc76f578fca6c967128bb8b203af76cc64cbefd123ae87a8b04a9780f498517bd9f660d12e2dc586220f2c12cc8aa76f1aa40a
%global source9_hash a069b7ca1b46e5656a05a5e38a0f9ea5c3ab1e5301edc47d7fdd43817a8f5d641980c2e54b7731dcbcf16e12f0dff17df5a816d66f7bd2b613232788815bb8e0
%global source10_hash af6f11a601f2ea3fd38d639beb3f836becb71aca7d282f5d0c7e020e9f73269c560ae3ac08d93706731872bd1a271c75724e1049c2dbf65e9ac0ea8f6c9b4724
%global source11_hash 8fb94b444966e6e3bd63b5b3ea62f661c038767222b08df2bd288965902cf152e1af4ad4b9d69859d11b1b558f4015b2f304afb0a43c356ff663498d830e1554
%global source12_hash 9d5a094da8465a6b0fd423eab822910023ee2012ccdeeca485eb2bc23deae1ad27e31d409db978b2346f20df92ee6f0a556e6a5e85da28d2bc5bdb78a8cb50a5
%global source13_hash d217e5daa729f92b48ca3edd44f242f98d181a45c41022eda9ae13a810c5d77844da2f08e868a9fb3955eab1c0120636eb149ac7c3aea8a5b0ff053fd3c03273
%global source14_hash 4c03a857a77bb4c10b1fb7e3e5c5fc8106326bd1fb5ac44a51a135e6893bafdb739f6fc71c87223da7421a1ed22d421a805b46dc96f03116cf17ead0b6efd791
%global source15_hash 57f31a086773c1cddc17d7f911b5a0c6718f07fdca723f39e7fd2c0b993c9d8cdb42d0de71857a63d0860beec9f8c7a5e3253e49e1b6140ddbfbcf3a88832c63
%global source16_hash 000f35ab32421138b65de373c892c6727f8747d10f3bc9c33f66b53e28667cd82814917103e600b3bd5bb94f70e978ce84fa1cb982095ae54a40c53f9d0a9f65
%global source17_hash f2473f98b55b2bbf3f1a7a364fc22e6915eb437c2f36d39154bf586403392ba6b7a7da4593e9acf33b6460c2ca9073272294e70d8a5f6c6c2a3c017970d10762
%global source18_hash 47dbf3388943440918879234037ddb08a8ea7f2851945273af2a01b032484e849af3898860f1daced148b770c4146701a987afe3ba3b8b66dd030bce36c4006d
%global source19_hash 2f85fc72c0415b48fd74ebe9d19e5ce86440c57c08038e96a2d99673143f2848bc347e95f7beab7753d0921414fc635aa9b4f98eafc91fabf64155a55a407bee
%global source20_hash 376a859b539d64fe3b227a91e6f5b3f9c7ad60f2a7c9a7862e6445e8d8299e192add9afa5c4f260e1080076e9a7345ddce3c83c99cf7f43de7574fe4b8d3caf2
%global source21_hash 5e9f2bc1702a5e4001685552e385e090434e9fc98a2c3fae7dc427e23a5fe38def9a6ab2b0efddf64874b5f1e3cc027d7954bb841a2cf2697170f9a59e486d47
%global source22_hash d7aeb9640061341ed39a71f7f69036f892bbe60b9db2236660e163b42fede81d6be58627b0163d3a183c120c9c8fa54f91a1a036ed9e50d2a72d5eac7f8a79a5
%global source23_hash b58305d403a58a60ac0cd6ebb60afe3058430eae15774895e03e41b331824673c128c5f06b583525e2311dd8ee5166549ea831e756e8c934c73ae911a0adbaa7
%global source24_hash 5564a68c8148e16b688f87b5e72f774751adc3a6831885bc3adbb41a46ec052c06ebc1fa55e5da54dfaf12e95097b022489626812c1dde3557639ecad55f2a63
%global source25_hash 71a489b323db46e5c06993e62567d7166046d3e0abc2d93c50e8c14a912b6ac20f1c51b6a1816e284d53f7a0be71bd8082c1a0cb27c7b1f47cc88d481d107bf1
%global source26_hash a473f01224a3c6a2823cb66b23e101dc963c295dacc364c5b7efce2924c89b9042294565ee31960743d1902da75dde0752ba45386026fbe7465034842364f093
%global source27_hash 284b572141afbf06496e0ff27b2b2a25f7ad13bdf2f3d187bf4b1daa83366c52f82e44ca53460c7bf61a033fed44829c635ad42e3a48df13220ac6f198061f21
%global source28_hash cb9101cde0b3709e0f63cbacf2344e5b81af9b2518c4190b6c66160670fee99d70a2c606b2760d7b1ecde0d132de6d0839fee23779549516c7d1b5fdbbd8622a
%global source29_hash 80067d5960e78ac6f0685ddfbe4d0a0dc7f6fdd3df663539fcb55df3fb8158621e6426dc939bebc7307b78c588ffcfe4e06c0a43e9cee3664494b794850ccdfd
%global source30_hash e0260b4d74269524d39cb3d8999cc07f5fd6288e0e26a557cd2dc7bec0ae38baf8b3bb41da2bbee96477fd2eccd106335dd5b6b406ef0f2b3f632f57dc58dde9
%global source31_hash 89002af0024ec804ebffcc45f3a33337ffdb66f71e1ca70224b0936388892dadf99605a8ca3f59a2b879e76e24acc91b1da92622d602f49b236aecb8aafe64b9
%global source32_hash 9dd3bd7a8ef3267965f30048e4a71314b6a9813cb400b7a94dfe285606d7554cde80aa429603d0fb1f587935e193e5ece5ed67870fc4e0c66eb5152c392a9cdc
%global source33_hash b4a8465264a174320180ac5f9bd89900f7a3b351af21d3a138db40b0781228bac8f8e9ea66a54a1910b3750d65eed17f74880f1c7396780dcd631eda164aff58
%global source34_hash b9c57f71b2c5e48ab3b96984b231f5ad418d884caad0a3747c78bdf0a5688c4ac05993e43707236b02650750d5b7507d39e50668b7cc16e00a35547d63d0bbb3
%global source35_hash b341d12068f112e2a9999f9907e095bead013a425a1efed1078ff03920163bc8a4e5d564fca197e9b9a3056f65cfd8e40fed66dd5aadd2408ebdeb94be863e69
%global source36_hash f26fc31b9b9b8299d4a64918f0d94274a9eefc9218c0b827bdf344a66323b4c514e28a0fdca378566b0cc91d97c954da4e8015f2f3b6b1c4d591afd2f583ad92
%global source37_hash f0b5cc9b7267aa07dc0b0f8c6d23a164bc239591fd13b5d77c5c840d33e131546c63c63a3bbbee2851000bda2e8593e7617f8a7ae381e7cd0561302a667acac1
%global source38_hash 915df985f4766f492a70a35342e086567d17c155ea0dfce5514c6edebaf1dacb78998dc4bf5cc44415fef580a7779083bc2261a22dfd668e8f2023f1f15bff35
%global source39_hash 415c04ea9add325ad71e678cafa99fe896d02c8b16facb0c4f69d656f0621e131c79be9470d15c755bfc4f63d9b6611e58829281c0e5c7209ac7c10ecc456b0a
%global source40_hash c68c01069ef48b668f471c86d0b562f2455e9bf022ee7a9d9a9b2c6475b9fd04b4e1b9b0eb7cac215f51ca965d35a1cc80102a6d862b2d72f9d9c72f07fd5900
%global source41_hash 50a35159c65afa43900ee8633d2b86effa5aec6a430f2e8fa85f77442da35b140012b27959155564e29286aba465d9bab17c9f5ce5ec0a889ec4ed5dff1b4dcb
%global source42_hash 9bdbd72f86e0b957580bb008ba349eb428721913010e9fe2cd9ee9b01733d6259914712b60a4a7f0f5804041e6cf876d8bdda2910de1b191715c1d9c8d8fbf77
%global source43_hash c5f03b824d75099a38f8d203722d0edc4136392ff282489f6473a83dc178f536eb972ede3bd9371f47f39dfc2dbda6b4db78d282642889b4036dbbdb8e49a473
%global source44_hash f1d7123e4438f781f6f4f7448119c7dc968be54888c027f8a7c95e5c70f06adcb58d127de21679bc125355f85f82ec94d2537cb0467f7c285427fba6b8f50775
%global source45_hash 8551d00c2bf130522b1403c9eb9ebb9865207d71c41286ca1f06c7ffbb727e0b90482f8668bd1de3103bec99029ac13a724cc9b00937cc2f4a31b6db69bb987d
%global source46_hash baf4203ce3dcebaa8ebda98220a1fce3513e4b9325a23b76f5beb902c44c544403f3bba42a4114e01913cfcfc393e35489330839b8c1a7a8d8fa9d47cf7be5fb
%global source47_hash 509e69acdef68eadc65fef6980e9166c6327e8927fb9cdf6a7a33786a8668ac9b900954a4bb661f223967b26dd240d5ebd91683658b324be284e46876c39061d
%global source48_hash 40ecdfe71670357e8ec84fd262015b5b5d0b8e486ab80c05d0863a335649501e9548d785cc2b2374f989b820dadd9a074cc229674dd1ae9a6252d4a0ebeb4191

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langgreek.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-greek.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-greek.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/begingreek.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/begingreek.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/betababel.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/betababel.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cbfonts.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cbfonts.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cbfonts-fd.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cbfonts-fd.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsbaskerville.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsbaskerville.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsporson.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsporson.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greek-fontenc.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greek-fontenc.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greek-inputenc.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greek-inputenc.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greekdates.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greekdates.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greektex.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greektex.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greektonoi.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greektonoi.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-ancientgreek.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-greek.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-greek.doc.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibycus-babel.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibycus-babel.doc.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibygrk.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibygrk.doc.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kerkis.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kerkis.doc.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/levy.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/levy.doc.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lgreek.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lgreek.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lgrmath.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lgrmath.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/talos.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/talos.doc.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/teubner.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/teubner.doc.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xgreek.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xgreek.doc.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yannisgr.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yannisgr.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-babel-greek
Requires:       texlive-begingreek
Requires:       texlive-betababel
Requires:       texlive-cbfonts
Requires:       texlive-cbfonts-fd
Requires:       texlive-collection-basic
Requires:       texlive-gfsbaskerville
Requires:       texlive-gfsporson
Requires:       texlive-greek-fontenc
Requires:       texlive-greek-inputenc
Requires:       texlive-greekdates
Requires:       texlive-greektex
Requires:       texlive-greektonoi
Requires:       texlive-hyphen-ancientgreek
Requires:       texlive-hyphen-greek
Requires:       texlive-ibycus-babel
Requires:       texlive-ibygrk
Requires:       texlive-kerkis
Requires:       texlive-levy
Requires:       texlive-lgreek
Requires:       texlive-lgrmath
Requires:       texlive-mkgrkindex
Requires:       texlive-talos
Requires:       texlive-teubner
Requires:       texlive-xgreek
Requires:       texlive-yannisgr

%description
Support for Greek.

%package -n texlive-babel-greek
Summary:        Babel support for the Greek language and script
Version:        svn68532
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(athnum.sty) = %{tl_version}
Provides:       tex(greek.ldf) = %{tl_version}
Provides:       tex(grmath.sty) = %{tl_version}

%description -n texlive-babel-greek
The bundle provides comprehensive support for the Greek language and script via
the Babel system. Document authors can select between the monotonic
(single-diacritic), polytonic (multiple-diacritic), and ancient orthography of
the Greek language. Included are the packages grmath for Greek function names
in mathematics, and athnum for Attic numerals.

%package -n texlive-begingreek
Summary:        Greek environment to be used with pdfLaTeX only
Version:        svn63255
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Provides:       tex(begingreek.sty) = %{tl_version}

%description -n texlive-begingreek
This simple package defines a greek environment to be used with pdfLaTeX only,
that accepts an optional Greek font family name to type its contents with. A
similar \greektxt command does a similar action for shorter texts.

%package -n texlive-betababel
Summary:        Insert ancient greek text coded in Beta Code
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(teubner.sty)
Provides:       tex(betababel.sty) = %{tl_version}

%description -n texlive-betababel
The betababel package extends the babel polutonikogreek option to provide a
simple way to insert ancient Greek texts with diacritical characters into your
document using the commonly used Beta Code transliteration. You can directly
insert Beta Code texts -- as they can be found at the Perseus project, for
example -- without modification.

%package -n texlive-cbfonts
Summary:        Complete set of Greek fonts
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cbfonts-fd

%description -n texlive-cbfonts
This bundle presents the whole of Beccari's original Greek font set, which use
the 'Lispiakos' font shape derived from the shape of the fonts used in
printers' shops in Lispia. The fonts are available both as Metafont source and
in Adobe Type 1 format, and at the same wide set of design sizes as are such
font sets as the EC fonts. Please note that this package needs the
complementary cbfonts-fd package to work properly.

%package -n texlive-cbfonts-fd
Summary:        LaTeX font description files for the CB Greek fonts
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cbfonts-fd
The package provides font description files for all the many shapes available
from the cbfonts collection. The files provide the means whereby the NFSS knows
which fonts a LaTeX user is requesting. The package depends on
cbgreek-complete.

%package -n texlive-gfsbaskerville
Summary:        A Greek font, from one such by Baskerville
Version:        svn19440
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gfsbaskerville.sty) = %{tl_version}

%description -n texlive-gfsbaskerville
The font is a digital implementation of Baskerville's classic Greek font,
provided by the Greek Font Society. The font covers Greek only, and LaTeX
support provides for the use of LGR encoding.

%package -n texlive-gfsporson
Summary:        A Greek font, originally from Porson
Version:        svn18651
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gfsporson.sty) = %{tl_version}

%description -n texlive-gfsporson
Porson is an elegant Greek font, originally cut at the turn of the 19th Century
in England. The present version has been provided by the Greek Font Society.
The font supports the Greek alphabet only. LaTeX support is provided, using the
LGR encoding.

%package -n texlive-greek-fontenc
Summary:        LICR macros and encoding definition files for Greek
Version:        svn68877
License:        LPPL-1.3c AND BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(alphabeta.sty) = %{tl_version}
Provides:       tex(greek-euenc.def) = %{tl_version}
Provides:       tex(greek-fontenc.def) = %{tl_version}
Provides:       tex(lgrenc.def) = %{tl_version}
Provides:       tex(puenc-greek.def) = %{tl_version}
Provides:       tex(textalpha.sty) = %{tl_version}
Provides:       tex(tuenc-greek.def) = %{tl_version}

%description -n texlive-greek-fontenc
LICR macros for characters from the Greek script and encoding definition files
for Greek text font encodings.

%package -n texlive-greek-inputenc
Summary:        Greek encoding support for inputenc
Version:        svn66634
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(iso-8859-7.def) = %{tl_version}
Provides:       tex(macgreek.def) = %{tl_version}

%description -n texlive-greek-inputenc
Input encoding definition files for UTF-8, Macintosh Greek, and ISO 8859-7
enabling the use of literal characters for Greek letters and symbols with 8-bit
TeX engines (pdfLaTeX).

%package -n texlive-greekdates
Summary:        Provides ancient Greek day and month names, dates, etc.
Version:        svn75878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Provides:       tex(greekdates.sty) = %{tl_version}

%description -n texlive-greekdates
The package provides easy access to ancient Greek names of days and months of
various regions of Greece. In case the historical information about a region is
not complete, we use the Athenian name of the month. Moreover commands and
options are provided, in order to completely switch to the "ancient way",
commands such as \today.

%package -n texlive-greektex
Summary:        Fonts for typesetting Greek/English documents
Version:        svn28327
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(greektex.sty) = %{tl_version}

%description -n texlive-greektex
The fonts are based on Silvio Levy's classical Greek fonts; macros and Greek
hyphenation patterns for the fonts' encoding are also provided.

%package -n texlive-greektonoi
Summary:        Facilitates writing/editing of multiaccented greek
Version:        svn39419
License:        LGPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(greektonoi.sty) = %{tl_version}

%description -n texlive-greektonoi
The greektonoi mapping extends the betababel package or the babel
polutonikogreek option to provide a simple way to insert ancient Greek texts
with diacritical characters into your document using a similar method to the
commonly used Beta Code transliteration, but with much more freedom. It is
designed especially for the XeTeX engine and it could also be used for fast and
easy modification of monotonic greek texts to polytonic. The output text is
natively encoded in Unicode, so it can be reused in any possible way. The
greektonoi package provides, in addition to inserting greek accents and
breathings, many other symbols used in greek numbers and arithmetic or in the
greek archaic period. It could be used with greektonoi mapping or indepedently.

%package -n texlive-hyphen-ancientgreek
Summary:        Ancient Greek hyphenation patterns.
Version:        svn74823
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(grahyph5.tex) = %{tl_version}
Provides:       tex(hyph-grc.tex) = %{tl_version}
Provides:       tex(ibyhyph.tex) = %{tl_version}
Provides:       tex(loadhyph-grc.tex) = %{tl_version}

%description -n texlive-hyphen-ancientgreek
Hyphenation patterns for Ancient Greek in LGR and UTF-8 encodings, including
support for (obsolete) Ibycus font encoding. Patterns in UTF-8 use two code
positions for each of the vowels with acute accent (a.k.a tonos, oxia), e.g.,
U+03AE, U+1F75 for eta.

%package -n texlive-hyphen-greek
Summary:        Modern Greek hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(grmhyph5.tex) = %{tl_version}
Provides:       tex(grphyph5.tex) = %{tl_version}
Provides:       tex(hyph-el-monoton.tex) = %{tl_version}
Provides:       tex(hyph-el-polyton.tex) = %{tl_version}
Provides:       tex(loadhyph-el-monoton.tex) = %{tl_version}
Provides:       tex(loadhyph-el-polyton.tex) = %{tl_version}

%description -n texlive-hyphen-greek
Hyphenation patterns for Modern Greek in monotonic and polytonic spelling in
LGR and UTF-8 encodings. Patterns in UTF-8 use two code positions for each of
the vowels with acute accent (a.k.a tonos, oxia), e.g., U+03AC, U+1F71 for
alpha.

%package -n texlive-ibycus-babel
Summary:        Use the Ibycus 4 Greek font with Babel
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ibycus.ldf) = %{tl_version}
Provides:       tex(lgienc.def) = %{tl_version}

%description -n texlive-ibycus-babel
The package allows you to use the Ibycus 4 font for ancient Greek with Babel.
It uses a Perl script to generate hyphenation patterns for Ibycus from those
for the ordinary Babel encoding, cbgreek. It sets up ibycus as a
pseudo-language you can specify in the normal Babel manner. For proper
hyphenation of Greek quoted in mid-paragraph, you should use it with elatex
(all current distributions of LaTeX are built with e-TeX, so the constraint
should not be onerous).

%package -n texlive-ibygrk
Summary:        Fonts and macros to typeset ancient Greek
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(iby4extr.tex) = %{tl_version}
Provides:       tex(ibycus4.sty) = %{tl_version}
Provides:       tex(ibycus4.tex) = %{tl_version}
Provides:       tex(ibycusps.tex) = %{tl_version}
Provides:       tex(psibycus.sty) = %{tl_version}
Provides:       tex(pssetiby.tex) = %{tl_version}
Provides:       tex(setiby4.tex) = %{tl_version}
Provides:       tex(tlgsqq.tex) = %{tl_version}
Provides:       tex(version4.tex) = %{tl_version}

%description -n texlive-ibygrk
Ibycus is a Greek typeface, based on Silvio Levy's realisation of a classic
Didot cut of Greek type from around 1800. The fonts are available both as
Metafont source and in Adobe Type 1 format. This distribution of ibycus is
accompanied by a set of macro packages to use it with Plain TeX or LaTeX, but
for use with Babel, see the ibycus-babel package.

%package -n texlive-kerkis
Summary:        Kerkis (Greek) font family
Version:        svn56271
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(txfonts.sty)
Provides:       tex(kerkis.sty) = %{tl_version}
Provides:       tex(kmath.sty) = %{tl_version}

%description -n texlive-kerkis
Sans-serif Greek fonts to match the URW Bookman set (which are distributed with
Kerkis). The Kerkis font set has some support for mathematics as well as other
glyphs missing from the base URW Bookman fonts. Macros are provided to use the
fonts in OT1, T1 (only NG/ng glyphs missing) and LGR encodings, as well as in
mathematics; small caps and old-style number glyphs are also available. The
philosophy, and the design process, of the Kerkis fonts is discussed in a paper
in TUGboat 23(3/4), 2002.

%package -n texlive-levy
Summary:        Fonts for typesetting classical greek
Version:        svn76924
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(greekmacros.tex) = %{tl_version}
Provides:       tex(slgreek.sty) = %{tl_version}

%description -n texlive-levy
These fonts are derivatives of Knuth's CM fonts. Macros for use with Plain TeX
are included in the package; for use with LaTeX, see lgreek (with English
documentation) or levy (with German documentation).

%package -n texlive-lgreek
Summary:        LaTeX macros for using Silvio Levy's Greek fonts
Version:        svn21818
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(LGenc.def) = %{tl_version}
Provides:       tex(lgreek.sty) = %{tl_version}

%description -n texlive-lgreek
A conversion of Silvio Levy's Plain TeX macros for use with LaTeX.

%package -n texlive-lgrmath
Summary:        Use LGR-encoded fonts in math mode
Version:        svn65038
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(lgrmath.sty) = %{tl_version}

%description -n texlive-lgrmath
The lgrmath package is a LaTeX package which sets the Greek letters in math
mode to use glyphs from the LGR-encoded font of one's choice. The documentation
includes a rather extensive list of the available font family names on typical
LaTeX installations.

%package -n texlive-talos
Summary:        A Greek cult font from the eighties
Version:        svn61820
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-talos
A cult Greek font from the eighties, used at the University of Crete, Greece.
It belonged to the first TeX installation in a Greek University and most
probably the first TeX installation that supported the Greek language.

%package -n texlive-teubner
Summary:        Philological typesetting of classical Greek
Version:        svn68074
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(exscale.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(trace.sty)
Provides:       tex(teubner.sty) = %{tl_version}
Provides:       tex(teubnertx.sty) = %{tl_version}

%description -n texlive-teubner
An extension to babel greek option for typesetting classical Greek with a
philological approach. The package works with the author's greek fonts using
the 'Lispiakos' font shape derived from that of the fonts used in printers'
shops in Lispia. The package name honours the publisher B.G. Teubner
Verlaggesellschaft whose Greek text publications are of high quality.

%package -n texlive-xgreek
Summary:        Greek Language Support for XeLaTeX and LuaLaTeX
Version:        svn73620
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listings.sty)
Requires:       tex(luahyphenrules.sty)
Provides:       tex(xelistings.sty) = %{tl_version}
Provides:       tex(xgreek.sty) = %{tl_version}

%description -n texlive-xgreek
This package has been designed so to allow people to typeset Greek language
documents using XeLaTeX or LuaLaTeX. It is released in the hope that people
will use it and spot errors, bugs, features so to improve it. Practically, it
provides all the capabilities of the greek option of the babel package. The
package can be invoked with any of the following options: monotonic (for
typesetting modern monotonic Greek), polytonic (for typesetting modern
polytonic Greek), and ancient (for typesetting ancient texts). The default
option is monotonic. The command \setlanguage{<lang>} activates the hyphenation
patterns of the language <lang>. This, however, can only be done if the format
file has not been built with the babel mechanism.

%package -n texlive-yannisgr
Summary:        Greek fonts by Yannis Haralambous
Version:        svn22613
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-yannisgr
A family of 7-bit fonts with a code table designed for setting modern polytonic
Greek. The fonts are provided as Metafont source; macros to produce a Greek
variant of Plain TeX (including a hyphenation table adapted to the fonts' code
table) are provided.

%post -n texlive-hyphen-ancientgreek
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/ancientgreek.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ancientgreek loadhyph-grc.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ancientgreek}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ancientgreek}{loadhyph-grc.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/ibycus.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ibycus ibyhyph.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ibycus}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ibycus}{ibyhyph.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ancientgreek
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/ancientgreek.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ancientgreek}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/ibycus.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ibycus}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-greek
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/greek.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "greek loadhyph-el-polyton.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=polygreek.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=polygreek" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{greek}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{greek}{loadhyph-el-polyton.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{polygreek}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{polygreek}{loadhyph-el-polyton.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/monogreek.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "monogreek loadhyph-el-monoton.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{monogreek}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{monogreek}{loadhyph-el-monoton.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-greek
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/greek.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=polygreek.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{greek}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{polygreek}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/monogreek.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{monogreek}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-greek
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-greek/
%doc %{_texmf_main}/doc/generic/babel-greek/

%files -n texlive-begingreek
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/begingreek/
%doc %{_texmf_main}/doc/latex/begingreek/

%files -n texlive-betababel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/betababel/
%doc %{_texmf_main}/doc/latex/betababel/

%files -n texlive-cbfonts
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/cbfonts/
%{_texmf_main}/fonts/map/dvips/cbfonts/
%{_texmf_main}/fonts/source/public/cbfonts/
%{_texmf_main}/fonts/tfm/public/cbfonts/
%{_texmf_main}/fonts/type1/public/cbfonts/
%doc %{_texmf_main}/doc/fonts/cbfonts/

%files -n texlive-cbfonts-fd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cbfonts-fd/
%doc %{_texmf_main}/doc/fonts/cbfonts-fd/

%files -n texlive-gfsbaskerville
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/gfsbaskerville/
%{_texmf_main}/fonts/enc/dvips/gfsbaskerville/
%{_texmf_main}/fonts/map/dvips/gfsbaskerville/
%{_texmf_main}/fonts/opentype/public/gfsbaskerville/
%{_texmf_main}/fonts/tfm/public/gfsbaskerville/
%{_texmf_main}/fonts/type1/public/gfsbaskerville/
%{_texmf_main}/fonts/vf/public/gfsbaskerville/
%{_texmf_main}/tex/latex/gfsbaskerville/
%doc %{_texmf_main}/doc/fonts/gfsbaskerville/

%files -n texlive-gfsporson
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/gfsporson/
%{_texmf_main}/fonts/enc/dvips/gfsporson/
%{_texmf_main}/fonts/map/dvips/gfsporson/
%{_texmf_main}/fonts/opentype/public/gfsporson/
%{_texmf_main}/fonts/tfm/public/gfsporson/
%{_texmf_main}/fonts/type1/public/gfsporson/
%{_texmf_main}/fonts/vf/public/gfsporson/
%{_texmf_main}/tex/latex/gfsporson/
%doc %{_texmf_main}/doc/fonts/gfsporson/

%files -n texlive-greek-fontenc
%license lppl1.3c.txt
%license bsd2.txt
%{_texmf_main}/tex/latex/greek-fontenc/
%doc %{_texmf_main}/doc/latex/greek-fontenc/

%files -n texlive-greek-inputenc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/greek-inputenc/
%doc %{_texmf_main}/doc/latex/greek-inputenc/

%files -n texlive-greekdates
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/greekdates/
%doc %{_texmf_main}/doc/latex/greekdates/

%files -n texlive-greektex
%license pd.txt
%{_texmf_main}/tex/latex/greektex/
%doc %{_texmf_main}/doc/fonts/greektex/

%files -n texlive-greektonoi
%license lgpl.txt
%{_texmf_main}/fonts/map/dvips/greektonoi/
%{_texmf_main}/tex/latex/greektonoi/
%doc %{_texmf_main}/doc/latex/greektonoi/

%files -n texlive-hyphen-ancientgreek
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%{_texmf_main}/tex/generic/hyphen/

%files -n texlive-hyphen-greek
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%{_texmf_main}/tex/generic/hyphen/
%doc %{_texmf_main}/doc/generic/elhyphen/

%files -n texlive-ibycus-babel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ibycus-babel/
%doc %{_texmf_main}/doc/latex/ibycus-babel/

%files -n texlive-ibygrk
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/ibygrk/
%{_texmf_main}/fonts/enc/dvips/ibygrk/
%{_texmf_main}/fonts/map/dvips/ibygrk/
%{_texmf_main}/fonts/source/public/ibygrk/
%{_texmf_main}/fonts/tfm/public/ibygrk/
%{_texmf_main}/fonts/type1/public/ibygrk/
%{_texmf_main}/tex/generic/ibygrk/
%doc %{_texmf_main}/doc/fonts/ibygrk/

%files -n texlive-kerkis
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/kerkis/
%{_texmf_main}/fonts/enc/dvips/kerkis/
%{_texmf_main}/fonts/map/dvips/kerkis/
%{_texmf_main}/fonts/opentype/public/kerkis/
%{_texmf_main}/fonts/tfm/public/kerkis/
%{_texmf_main}/fonts/type1/public/kerkis/
%{_texmf_main}/fonts/vf/public/kerkis/
%{_texmf_main}/tex/latex/kerkis/
%doc %{_texmf_main}/doc/fonts/kerkis/

%files -n texlive-levy
%license gpl2.txt
%{_texmf_main}/fonts/source/public/levy/
%{_texmf_main}/fonts/tfm/public/levy/
%{_texmf_main}/tex/generic/levy/
%doc %{_texmf_main}/doc/fonts/levy/

%files -n texlive-lgreek
%license gpl2.txt
%{_texmf_main}/tex/latex/lgreek/
%doc %{_texmf_main}/doc/latex/lgreek/

%files -n texlive-lgrmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lgrmath/
%doc %{_texmf_main}/doc/latex/lgrmath/

%files -n texlive-talos
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/talos/
%doc %{_texmf_main}/doc/fonts/talos/

%files -n texlive-teubner
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/teubner/
%doc %{_texmf_main}/doc/latex/teubner/

%files -n texlive-xgreek
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xgreek/
%doc %{_texmf_main}/doc/latex/xgreek/

%files -n texlive-yannisgr
%license gpl2.txt
%{_texmf_main}/fonts/source/public/yannisgr/
%{_texmf_main}/fonts/tfm/public/yannisgr/
%doc %{_texmf_main}/doc/fonts/yannisgr/

%changelog
%autochangelog
