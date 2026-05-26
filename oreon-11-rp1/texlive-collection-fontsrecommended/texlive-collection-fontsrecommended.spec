%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-fontsrecommended
Epoch:          12
Version:        svn54074
Release:        8%{?dist}
Summary:        Recommended fonts

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-fontsrecommended.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/avantgar.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookman.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/charter.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/charter.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-super.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-super.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmextra.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/courier.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euro.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euro.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euro-ce.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euro-ce.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eurosym.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eurosym.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fpl.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fpl.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/helvetic.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lm.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lm.doc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lm-math.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lm-math.doc.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/marvosym.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/marvosym.doc.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathpazo.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathpazo.doc.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/manfnt-font.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mflogo-font.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mflogo-font.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ncntrsbk.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/palatino.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxfonts.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxfonts.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rsfs.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rsfs.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/symbol.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre-math.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre-math.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/times.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tipa.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tipa.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/txfonts.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/txfonts.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utopia.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utopia.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasy.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasy.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasy-type1.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasy-type1.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasysym.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasysym.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zapfchan.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zapfding.tar.xz

# AppStream metadata for font components
Source56:        lm.metainfo.xml
Source57:        lm-math.metainfo.xml
Source58:        tex-gyre.metainfo.xml
Source59:        tex-gyre-math.metainfo.xml
# oreon url source checksums begin
%global source0_sha256 a4de421c3ff528ab4e7dd91437b33418f8298027341cec856ede8d31d9e409de
%global source0_file collection-fontsrecommended.tar.xz
%global source2_sha256 4200ef68e6a3564eb6dd3bbad9f760e70c10a81d7ad3a81b93988800dbd50141
%global source2_file avantgar.tar.xz
%global source3_sha256 ec4736522d6749513268a83502febc4dcb73346f8e0b70dafaa76a74ae8998ca
%global source3_file bookman.tar.xz
%global source4_sha256 34a08f3370093966207b4a3fed029c215882c89658925624362a877f927c9bd0
%global source4_file charter.tar.xz
%global source5_sha256 734c4ce42bbee7206f1f5079b4d07faeb5bd129a6a3f1b9cd331b587b5567573
%global source5_file charter.doc.tar.xz
%global source6_sha256 70867904e38451ab1a11ba4677dd5891914f128170b53fac26d3e9dca9d326e4
%global source6_file cm-super.tar.xz
%global source7_sha256 73964d63f70963a6c7afeb45d133fb1ffb740e65aef266c9c576e80445b03698
%global source7_file cm-super.doc.tar.xz
%global source8_sha256 b07224532bb16bba4e0720a7f762acbab6a822f0c7cd463d85f3b36fc2ac3f8c
%global source8_file cmextra.tar.xz
%global source9_sha256 eaecb5bcd119e6409ac549fdffbe73a6bf7087daef43085104a1ba03787ec989
%global source9_file courier.tar.xz
%global source10_sha256 971e545295d359bc67244d6cfd19b422dc866040247562946bb1ee80080b2241
%global source10_file euro.tar.xz
%global source11_sha256 db05760a9a98a332d1705fd6b51e51ad3865f63c6c46e230091e56b17b5e4e31
%global source11_file euro.doc.tar.xz
%global source12_sha256 0756c928792e4678b0533e650074426c2709fb28fb8d7fb26fc962a815180a6b
%global source12_file euro-ce.tar.xz
%global source13_sha256 7c532a90770f32b89acdff14343dbd68da3609d4d446e09b34a2a2a91aafc5ca
%global source13_file euro-ce.doc.tar.xz
%global source14_sha256 db2f7325383f6fa4ed2dc805c432da40fa1ecc742026928001b0cded9b3de07f
%global source14_file eurosym.tar.xz
%global source15_sha256 eebacc24983585ac07f4cdc1417c713d2b52089ee9b04f3559162dc0c30c909f
%global source15_file eurosym.doc.tar.xz
%global source16_sha256 f12f95c8bd681618311dff369a5a4453478be9bef1a9054f647edbec99b306ed
%global source16_file fpl.tar.xz
%global source17_sha256 1170e2fa4668feaebd358f33fd6ca11e2a0b2189fd48e9f323a445a788bf4e6d
%global source17_file fpl.doc.tar.xz
%global source18_sha256 155b23ee6096e32fe7a481500a75269027042abebc3955e7966327c1d1f41db4
%global source18_file helvetic.tar.xz
%global source19_sha256 6ecafd1f066d189a0688c10572a01d45c231fa236d6ec1cca726ca4eef41e57c
%global source19_file lm.tar.xz
%global source20_sha256 23a71d500b3d8e1fc8bb9b2a6ffc2c8c48a66dfd99fffe18a42616afc6ee175b
%global source20_file lm.doc.tar.xz
%global source21_sha256 876211c73c151423bb4d1fc17064847e09436ffbfd183d7f0078a1fa8ba9c387
%global source21_file lm-math.tar.xz
%global source22_sha256 8f748f31882efdd13370fdb9c708bc4bb6202647b21af140d3a86b47acd0bf9b
%global source22_file lm-math.doc.tar.xz
%global source23_sha256 4ade7bea5482086218a6047109fecae8055bc22bf479cbb437b4ef3bd85977fc
%global source23_file marvosym.tar.xz
%global source24_sha256 2e2ed45595e417c9ffad852c1576a21a04041f49789b8ec133c63f23d8873417
%global source24_file marvosym.doc.tar.xz
%global source25_sha256 b42822082e609bc2c707bb2657ff5bf6f491718ab391d2c884f7dfed0d51ec15
%global source25_file mathpazo.tar.xz
%global source26_sha256 2577ad02cb00a43c8602cc4815b665b1467735b941c6c80e3e0e6d5c5a18ecc0
%global source26_file mathpazo.doc.tar.xz
%global source27_sha256 f1bbb929781f5a5f524ec7f1a4871a58259c2b22eb637872f71264a5dcdc26d4
%global source27_file manfnt-font.tar.xz
%global source28_sha256 872232b0651640e772d8d2366e2074b7c8e5dabd53617280c587ed210a2b0d42
%global source28_file mflogo-font.tar.xz
%global source29_sha256 cf59b4f297c17a03b32d74f4d04276d1c42a84ceb3d4e21a41fbbbb4e9e0bc34
%global source29_file mflogo-font.doc.tar.xz
%global source30_sha256 4976f1859fb159505e60f1a21274b6b63c5af88f2e03cd0ea6a7e3c84512f4b7
%global source30_file ncntrsbk.tar.xz
%global source31_sha256 a5950b7ce364231aace8830cdedbe6ab511bfe663a2f1ba0bd270e618463b6f1
%global source31_file palatino.tar.xz
%global source32_sha256 bdddf89946b2a237a75d8d9ee9f2bc6597c868ba2eb73c0a4925a1e631aecd60
%global source32_file pxfonts.tar.xz
%global source33_sha256 61e343867a2afa56cee8173f67e744738b5fe276e7f58a9f06748b39d3695ba9
%global source33_file pxfonts.doc.tar.xz
%global source34_sha256 1afec0c5e9711f652675e38b7cd7e88101c44aa0d0ff317ad6ac06f1d2cc7043
%global source34_file rsfs.tar.xz
%global source35_sha256 a152acc91945bd8e115789ae0b0be5f60672b99938b4798c772b42ca58976a72
%global source35_file rsfs.doc.tar.xz
%global source36_sha256 c6b615bf830b8260a18f26a2aedd406c0e3aa9a24831cc1b2bc73be1774a669b
%global source36_file symbol.tar.xz
%global source37_sha256 dfb4f55c4b02993003777a48663987bd102a3c5a2913172571e05fe2eb18407d
%global source37_file tex-gyre.tar.xz
%global source38_sha256 c81a8ac0381e34c55b0075aec75e6646b69bb7b428ebb7d1eca337001f1ef08c
%global source38_file tex-gyre.doc.tar.xz
%global source39_sha256 8972d19fec5a701499fb6edc86f3ac4266343d42140cf6ae27edd44c2e916da3
%global source39_file tex-gyre-math.tar.xz
%global source40_sha256 8c06fd0df3b1ad8fbcbc1b025f3ab086e1c0bb7260f2d4e21609140cdb569076
%global source40_file tex-gyre-math.doc.tar.xz
%global source41_sha256 55f6097b5685a22a3ec1db61ae372ffe00b25d622ed4ee3d010cd8a037e48a00
%global source41_file times.tar.xz
%global source42_sha256 07f7c0994c3e37ab2de47fe22c3046229de7138e800d4e67f6d1ad39d7066f9d
%global source42_file tipa.tar.xz
%global source43_sha256 9b854ecf441a08c0c616b3811076c27803d9bdf153075bb3968e65450d135c7c
%global source43_file tipa.doc.tar.xz
%global source44_sha256 03189f5a8b40535a5ca705aabb80aa9e9c9b9c993ba5885f891a3cdfc80afb1d
%global source44_file txfonts.tar.xz
%global source45_sha256 abc1bc408dd6f4563f116f9da4d4d07a02360210655a89958c1acf11f0d8f856
%global source45_file txfonts.doc.tar.xz
%global source46_sha256 d8148e06274d9f3eca68d90586ee4f5797068ce8bb9ff93a7cb24872f520a643
%global source46_file utopia.tar.xz
%global source47_sha256 a068f320e6c217355a73d7e91661dcae16cfbb91dd048bc691949cadc1304df7
%global source47_file utopia.doc.tar.xz
%global source48_sha256 9fc877454fef9746c8c85e5282caf349d7e67ed44ba2ee18202d76862e054d13
%global source48_file wasy.tar.xz
%global source49_sha256 6d078bbf6d64d342726c42d14d81386fde079c8952f9645c19f65085da0a94d6
%global source49_file wasy.doc.tar.xz
%global source50_sha256 1bd86eff809059e4a7c009d8fbe2dd756e568de1d91d6489d82766a1b6f60129
%global source50_file wasy-type1.tar.xz
%global source51_sha256 6613f94af665385aa4516468858899f250f2fd5e1748d86db7da8a277b43a689
%global source51_file wasy-type1.doc.tar.xz
%global source52_sha256 6f574fd99a7304f0759aacc62a60747f4c8ef7922f53be6aa5ab168d78c45ef3
%global source52_file wasysym.tar.xz
%global source53_sha256 76580fff1ccd6f6e8d7331b9aeaeeb2addc3fc6242f000169996c85d0178d6ea
%global source53_file wasysym.doc.tar.xz
%global source54_sha256 b1af3ec046fc3bdc9c1f35586a523cfd1393d02fd28e146b3efd2260d3311214
%global source54_file zapfchan.tar.xz
%global source55_sha256 7c95b0011067228c4395aef990d92e190a66f825f6f3fb5bf09a738893b47ece
%global source55_file zapfding.tar.xz
# oreon url source checksums end
BuildRequires:  texlive-base
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-avantgar
Requires:       texlive-bookman
Requires:       texlive-charter
Requires:       texlive-cm-super
Requires:       texlive-cmextra
Requires:       texlive-courier
Requires:       texlive-euro
Requires:       texlive-euro-ce
Requires:       texlive-eurosym
Requires:       texlive-fpl
Requires:       texlive-helvetic
Requires:       texlive-lm
Requires:       texlive-lm-math
Requires:       texlive-marvosym
Requires:       texlive-mathpazo
Requires:       texlive-manfnt-font
Requires:       texlive-mflogo-font
Requires:       texlive-ncntrsbk
Requires:       texlive-palatino
Requires:       texlive-pxfonts
Requires:       texlive-rsfs
Requires:       texlive-symbol
Requires:       texlive-tex-gyre
Requires:       texlive-tex-gyre-math
Requires:       texlive-times
Requires:       texlive-tipa
Requires:       texlive-txfonts
Requires:       texlive-utopia
Requires:       texlive-wasy
Requires:       texlive-wasy-type1
Requires:       texlive-wasysym
Requires:       texlive-zapfchan
Requires:       texlive-zapfding

%description
Recommended fonts, including the base 35 PostScript fonts, Latin Modern, TeX
Gyre, and T1 and other encoding support for Computer Modern, in outline form.


%package -n texlive-avantgar
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-avantgar
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-bookman
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bookman
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-charter
Summary:        Charter fonts
Version:        svn15878
License:        LicenseRef-Charter
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-charter-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-charter-doc <= 11:%{version}

%description -n texlive-charter
A commercial text font donated for the common good. Support for use with LaTeX
is available in freenfss, part of psnfss.

%package -n texlive-cm-super
Summary:        CM-Super family of fonts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-cm-super-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cm-super-doc <= 11:%{version}

%description -n texlive-cm-super
The CM-Super family provides Adobe Type 1 fonts that replace the T1/TS1-encoded
Computer Modern (EC/TC), T1/TS1-encoded Concrete, T1/TS1-encoded CM bright and
LH Cyrillic fonts (thus supporting all European languages except Greek), and
bringing many ameliorations in typesetting quality. The fonts exhibit the same
metrics as the Metafont-encoded originals.

%package -n texlive-cmextra
Summary:        Knuth's local information
Version:        svn57866
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cmextra
A collection of experimental programs and developments based on, or
complementary to, the matter in his distribution directories.

%package -n texlive-courier
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-courier
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-euro
Summary:        Provide Euro values for national currency amounts
Version:        svn22191
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-euro-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-euro-doc <= 11:%{version}
Requires:       tex(fp-basic.sty)
Requires:       tex(fp-snap.sty)

%description -n texlive-euro
Converts arbitrary national currency amounts using the Euro as base unit, and
typesets monetary amounts in almost any desired way. Write, e.g., \ATS{17.6} to
get something like '17,60 oS (1,28 Euro)' automatically. Conversion rates for
the initial Euro-zone countries are already built-in. Further rates can be
added easily. The package uses the fp package to do its sums.

%package -n texlive-euro-ce
Summary:        Euro and CE sign font
Version:        svn25714
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-euro-ce
Metafont source for the symbols in several variants, designed to fit with the
Computer Modern-set text.

%package -n texlive-eurosym
Summary:        Metafont and macros for Euro sign
Version:        svn78101
License:        Eurosym
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-eurosym-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-eurosym-doc <= 11:%{version}

%description -n texlive-eurosym
The European currency symbol for the Euro implemented in Metafont, using the
official European Commission dimensions, and providing several shapes (normal,
slanted, bold, outline). The package also includes a LaTeX package which
defines the macro, pre-compiled tfm files, and documentation.

%package -n texlive-fpl
Summary:        SC and OsF fonts for URW Palladio L
Version:        svn54512
License:        GPL-2.0-only AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fpl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fpl-doc <= 11:%{version}

%description -n texlive-fpl
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L which are
compatible with respect to metrics with the Palatino SC/OsF fonts from Adobe.
Note that it is not my aim to exactly reproduce the outlines of the original
Adobe fonts. The SC and OsF in the FPL Fonts were designed with the glyphs from
URW Palladio L as starting point. For some glyphs (e.g. 'o') I got the best
result by scaling and boldening. For others (e.g. 'h') shifting selected
portions of the character gave more satisfying results. All this was done using
the free font editor FontForge. The kerning data in these fonts comes from
Walter Schmidt's improved Palatino metrics. LaTeX use is enabled by the
mathpazo package, which is part of the psnfss distribution.

%package -n texlive-helvetic
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-helvetic
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-lm
Summary:        Latin modern fonts in outline formats
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lm-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lm-doc <= 11:%{version}

%description -n texlive-lm
The Latin Modern family of fonts consists of 72 text fonts and 20 mathematics
fonts, and is based on the Computer Modern fonts released into public domain by
AMS (copyright (c) 1997 AMS). The lm font set contains a lot of additional
characters, mainly accented ones, but not exclusively. There is one set of
fonts, available both in Adobe Type 1 format (*.pfb) and in OpenType format
(*.otf). There are five sets of TeX Font Metric files, corresponding to: Cork
encoding (cork-*.tfm); QX encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding
(texnansi-*.tfm); T5 (Vietnamese) encoding (t5-*.tfm); and Text Companion for
EC fonts aka TS1 (ts1-*.tfm).

%package -n texlive-lm-math
Summary:        OpenType maths fonts for Latin Modern
Version:        svn67718
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lm-math-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lm-math-doc <= 11:%{version}

%description -n texlive-lm-math
Latin Modern Math is a maths companion for the Latin Modern family of fonts, in
OpenType format. For use with LuaLaTeX or XeLaTeX, support is available from
the unicode-math package.

%package -n texlive-manfnt-font
Summary:        Knuth's "manual" fonts
Version:        svn45777
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-manfnt-font
Metafont (by Donald Knuth) and Adobe Type 1 (by Taco Hoekwater) versions of the
font containing the odd symbols Knuth uses in his books. LaTeX support is
available using the manfnt package

%package -n texlive-marvosym
Summary:        Martin Vogel's Symbols (marvosym) font
Version:        svn77682
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-marvosym-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-marvosym-doc <= 11:%{version}

%description -n texlive-marvosym
Martin Vogel's Symbol font (marvosym) contains the Euro currency symbol as
defined by the European commission, along with symbols for structural
engineering; symbols for steel cross-sections; astronomy signs (sun, moon,
planets); the 12 signs of the zodiac; scissor symbols; CE sign and others. The
package contains both the original TrueType font and the derived Type 1 font,
together with support files for TeX (LaTeX).

%package -n texlive-mathpazo
Summary:        Fonts to typeset mathematics to match Palatino
Version:        svn77682
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mathpazo-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mathpazo-doc <= 11:%{version}
Requires:       texlive-fpl
Requires:       texlive-palatino

%description -n texlive-mathpazo
The Pazo Math fonts are a family of PostScript fonts suitable for typesetting
mathematics in combination with the Palatino family of text fonts. The Pazo
Math family is made up of five fonts provided in Adobe Type 1 format (PazoMath,
PazoMath-Italic, PazoMath-Bold, PazoMath-BoldItalic, and
PazoMathBlackboardBold). These contain, in designs that match Palatino, glyphs
that are usually not available in Palatino and for which Computer Modern looks
odd when combined with Palatino. These glyphs include the uppercase Greek
alphabet in upright and slanted shapes in regular and bold weights, the
lowercase Greek alphabet in slanted shape in regular and bold weights, several
mathematical glyphs (partialdiff, summation, product, coproduct, emptyset,
infinity, and proportional) in regular and bold weights, other glyphs (Euro and
dotlessj) in upright and slanted shapes in regular and bold weights, and the
uppercase letters commonly used to represent various number sets (C, I, N, Q,
R, and Z) in blackboard bold. LaTeX macro support (using package mathpazo.sty)
is provided in psnfss (a required part of any LaTeX distribution).

%package -n texlive-mflogo-font
Summary:        Metafont logo font
Version:        svn54512
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mflogo-font-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mflogo-font-doc <= 11:%{version}

%description -n texlive-mflogo-font
These fonts were created in Metafont by Knuth, for his own publications. At
some stage, the letters 'P' and 'S' were added, so that the MetaPost logo could
also be expressed. The fonts were originally issued (of course) as Metafont
source; they have since been autotraced and reissued in Adobe Type 1 format by
Taco Hoekwater.

%package -n texlive-ncntrsbk
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ncntrsbk
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-palatino
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-palatino
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-pxfonts
Summary:        Palatino-like fonts in support of mathematics
Version:        svn77682
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pxfonts-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pxfonts-doc <= 11:%{version}

%description -n texlive-pxfonts
Pxfonts supplies virtual text roman fonts using Adobe Palatino (or
URWPalladioL) with some modified and additional text symbols in the OT1, T1,
and TS1 encodings; maths alphabets using Palatino/Palladio; maths fonts
providing all the symbols of the Computer Modern and AMS fonts, including all
the Greek capital letters from CMR; and additional maths fonts of various other
symbols. The set is complemented by a sans-serif set of text fonts, based on
Helvetica/NimbusSanL, and a monospace set derived from the parallel TX font
set. All the fonts are in Type 1 format (AFM and PFB files), and are supported
by TeX metrics (VF and TFM files) and macros for use with LaTeX.

%package -n texlive-rsfs
Summary:        Ralph Smith's Formal Script font
Version:        svn15878
License:        LicenseRef-Rsfs
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-rsfs-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-rsfs-doc <= 11:%{version}

%description -n texlive-rsfs
The fonts provide uppercase 'formal' script letters for use as symbols in
scientific and mathematical typesetting (in contrast to the informal script
fonts such as that used for the 'calligraphic' symbols in the TeX maths symbol
font). The fonts are provided as Metafont source, and as derived Adobe Type 1
format. LaTeX support, for using these fonts in mathematics, is available via
one of the packages calrsfs and mathrsfs.

%package -n texlive-symbol
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-symbol
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-tex-gyre
Summary:        TeX Fonts extending freely available URW fonts
Version:        svn68624
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-gyre-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-gyre-doc <= 11:%{version}
Requires:       tex(kvoptions.sty)

%description -n texlive-tex-gyre
The TeX-GYRE bundle consists of six font families: TeX Gyre Adventor is based
on the URW Gothic L family of fonts (which is derived from ITC Avant Garde
Gothic, designed by Herb Lubalin and Tom Carnase). TeX Gyre Bonum is based on
the URW Bookman L family (from Bookman Old Style, designed by Alexander
Phemister). TeX Gyre Chorus is based on URW Chancery L Medium Italic (from ITC
Zapf Chancery, designed by Hermann Zapf in 1979). TeX-Gyre Cursor is based on
URW Nimbus Mono L (based on Courier, designed by Howard G. Kettler in 1955, for
IBM). TeX Gyre Heros is based on URW Nimbus Sans L (from Helvetica, prepared by
Max Miedinger, with Eduard Hoffmann in 1957). TeX Gyre Pagella is based on URW
Palladio L (from Palatino, designed by Hermann Zapf in the 1940s). TeX Gyre
Schola is based on the URW Century Schoolbook L family (from Century
Schoolbook, designed by Morris Fuller Benton for the American Type Founders).
TeX Gyre Termes is based on the URW Nimbus Roman No9 L family of fonts (from
Times New Roman, designed by Stanley Morison together with Starling Burgess and
Victor Lardent and first offered by Monotype). The constituent standard faces
of each family have been greatly extended (though Chorus omits Greek support
and has no small-caps family). Each family is available in Adobe Type 1 and
Open Type formats, and LaTeX support (for use with a variety of encodings) is
provided. Vietnamese characters were added by Han The Thanh. There are
companion maths fonts for several of these designs, listed in the TeX Gyre Math
package.

%package -n texlive-tex-gyre-math
Summary:        Maths fonts to match tex-gyre text fonts
Version:        svn41264
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-gyre-math-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-gyre-math-doc <= 11:%{version}

%description -n texlive-tex-gyre-math
TeX-Gyre-Math is a collection of maths fonts to match the text fonts of the
TeX-Gyre collection. The collection is available in OpenType format, only;
fonts conform to the developing standards for OpenType maths fonts.
TeX-Gyre-Math-Bonum (to match TeX-Gyre-Bonum), TeX-Gyre-Math-Pagella (to match
TeX-Gyre-Pagella), TeX-Gyre-Math-Schola (to match TeX-Gyre-Schola) and
TeX-Gyre-Math-Termes (to match TeX-Gyre-Termes) fonts are provided.

%package -n texlive-times
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-times
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-tipa
Summary:        Fonts and macros for IPA phonetics characters
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tipa-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tipa-doc <= 11:%{version}
Requires:       tex(fontenc.sty)

%description -n texlive-tipa
These fonts are considered the 'ultimate answer' to IPA typesetting. The
encoding of these 8-bit fonts has been registered as LaTeX standard encoding
T3, and the set of addendum symbols as encoding TS3. 'Times-like' Adobe Type 1
versions are provided for both the T3 and the TS3 fonts.

%package -n texlive-txfonts
Summary:        Times-like fonts in support of mathematics
Version:        svn77682
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-txfonts-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-txfonts-doc <= 11:%{version}

%description -n texlive-txfonts
Txfonts supplies virtual text roman fonts using Adobe Times (or URW
NimbusRomNo9L) with some modified and additional text symbols in the OT1, T1,
and TS1 encodings; maths alphabets using Times/URW Nimbus; maths fonts
providing all the symbols of the Computer Modern and AMS fonts, including all
the Greek capital letters from CMR; and additional maths fonts of various other
symbols. The set is complemented by a sans-serif set of text fonts, based on
Helvetica/NimbusSanL, and a monospace set. All the fonts are in Type 1 format
(AFM and PFB files), and are supported by TeX metrics (VF and TFM files) and
macros for use with LaTeX.

%package -n texlive-utopia
Summary:        Adobe Utopia fonts
Version:        svn77682
License:        LicenseRef-Utopia
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-utopia-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-utopia-doc <= 11:%{version}

%description -n texlive-utopia
The Adobe Standard Encoding set (upright and italic shapes, medium and bold
weights) of the Utopia font family, which Adobe donated to the X Consortium.
Macro support, and maths fonts that match the Utopia family, are provided by
the Fourier and the Mathdesign font packages.

%package -n texlive-wasy
Summary:        The wasy fonts (Waldi symbol fonts)
Version:        svn53533
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-wasy-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-wasy-doc <= 11:%{version}

%description -n texlive-wasy
This font contains all lasy characters (by L.Lamport, copyright notice in
lasychr.mf), and a lot more symbols. Provided are the Metafont files for
5-10pt, and bold and slanted 10pt fonts, together with a .tex and .pdf
documentation, and a file for using the fonts in a PLAIN-TeX document. Type-1
fonts by Michael Sharpe and Taco Hoekwater are available as separate package
wasy-type1. Support under LaTeX is provided by Axel Kielhorn's wasysym package.

%package -n texlive-wasy-type1
Summary:        Type 1 versions of wasy fonts
Version:        svn53534
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-wasy

%description -n texlive-wasy-type1
Converted (Adobe Type 1) outlines of the wasy fonts.

%package -n texlive-wasysym
Summary:        LaTeX support for the wasy fonts
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-wasysym-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-wasysym-doc <= 11:%{version}

%description -n texlive-wasysym
The wasy (Waldi Symbol) font by Roland Waldi provides many glyphs like male and
female symbols and astronomical symbols, as well as the complete lasy font set
and other odds and ends. This package implements an easy to use interface for
these symbols.

%package -n texlive-zapfchan
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-zapfchan
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-zapfding
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-zapfding
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/collection-fontsrecommended.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a4de421c3ff528ab4e7dd91437b33418f8298027341cec856ede8d31d9e409de" || { echo "oreon: Source0 SHA256 mismatch for collection-fontsrecommended.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/avantgar.tar.xz; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4200ef68e6a3564eb6dd3bbad9f760e70c10a81d7ad3a81b93988800dbd50141" || { echo "oreon: Source2 SHA256 mismatch for avantgar.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/bookman.tar.xz; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ec4736522d6749513268a83502febc4dcb73346f8e0b70dafaa76a74ae8998ca" || { echo "oreon: Source3 SHA256 mismatch for bookman.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/charter.tar.xz; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "34a08f3370093966207b4a3fed029c215882c89658925624362a877f927c9bd0" || { echo "oreon: Source4 SHA256 mismatch for charter.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/charter.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "734c4ce42bbee7206f1f5079b4d07faeb5bd129a6a3f1b9cd331b587b5567573" || { echo "oreon: Source5 SHA256 mismatch for charter.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/cm-super.tar.xz; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "70867904e38451ab1a11ba4677dd5891914f128170b53fac26d3e9dca9d326e4" || { echo "oreon: Source6 SHA256 mismatch for cm-super.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/cm-super.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "73964d63f70963a6c7afeb45d133fb1ffb740e65aef266c9c576e80445b03698" || { echo "oreon: Source7 SHA256 mismatch for cm-super.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/cmextra.tar.xz; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b07224532bb16bba4e0720a7f762acbab6a822f0c7cd463d85f3b36fc2ac3f8c" || { echo "oreon: Source8 SHA256 mismatch for cmextra.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/courier.tar.xz; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "eaecb5bcd119e6409ac549fdffbe73a6bf7087daef43085104a1ba03787ec989" || { echo "oreon: Source9 SHA256 mismatch for courier.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/euro.tar.xz; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "971e545295d359bc67244d6cfd19b422dc866040247562946bb1ee80080b2241" || { echo "oreon: Source10 SHA256 mismatch for euro.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/euro.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "db05760a9a98a332d1705fd6b51e51ad3865f63c6c46e230091e56b17b5e4e31" || { echo "oreon: Source11 SHA256 mismatch for euro.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/euro-ce.tar.xz; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0756c928792e4678b0533e650074426c2709fb28fb8d7fb26fc962a815180a6b" || { echo "oreon: Source12 SHA256 mismatch for euro-ce.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/euro-ce.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7c532a90770f32b89acdff14343dbd68da3609d4d446e09b34a2a2a91aafc5ca" || { echo "oreon: Source13 SHA256 mismatch for euro-ce.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/eurosym.tar.xz; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "db2f7325383f6fa4ed2dc805c432da40fa1ecc742026928001b0cded9b3de07f" || { echo "oreon: Source14 SHA256 mismatch for eurosym.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/eurosym.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "eebacc24983585ac07f4cdc1417c713d2b52089ee9b04f3559162dc0c30c909f" || { echo "oreon: Source15 SHA256 mismatch for eurosym.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fpl.tar.xz; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f12f95c8bd681618311dff369a5a4453478be9bef1a9054f647edbec99b306ed" || { echo "oreon: Source16 SHA256 mismatch for fpl.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/fpl.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1170e2fa4668feaebd358f33fd6ca11e2a0b2189fd48e9f323a445a788bf4e6d" || { echo "oreon: Source17 SHA256 mismatch for fpl.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/helvetic.tar.xz; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "155b23ee6096e32fe7a481500a75269027042abebc3955e7966327c1d1f41db4" || { echo "oreon: Source18 SHA256 mismatch for helvetic.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/lm.tar.xz; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6ecafd1f066d189a0688c10572a01d45c231fa236d6ec1cca726ca4eef41e57c" || { echo "oreon: Source19 SHA256 mismatch for lm.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/lm.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "23a71d500b3d8e1fc8bb9b2a6ffc2c8c48a66dfd99fffe18a42616afc6ee175b" || { echo "oreon: Source20 SHA256 mismatch for lm.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/lm-math.tar.xz; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "876211c73c151423bb4d1fc17064847e09436ffbfd183d7f0078a1fa8ba9c387" || { echo "oreon: Source21 SHA256 mismatch for lm-math.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/lm-math.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8f748f31882efdd13370fdb9c708bc4bb6202647b21af140d3a86b47acd0bf9b" || { echo "oreon: Source22 SHA256 mismatch for lm-math.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/marvosym.tar.xz; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4ade7bea5482086218a6047109fecae8055bc22bf479cbb437b4ef3bd85977fc" || { echo "oreon: Source23 SHA256 mismatch for marvosym.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/marvosym.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2e2ed45595e417c9ffad852c1576a21a04041f49789b8ec133c63f23d8873417" || { echo "oreon: Source24 SHA256 mismatch for marvosym.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/mathpazo.tar.xz; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b42822082e609bc2c707bb2657ff5bf6f491718ab391d2c884f7dfed0d51ec15" || { echo "oreon: Source25 SHA256 mismatch for mathpazo.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/mathpazo.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source26 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2577ad02cb00a43c8602cc4815b665b1467735b941c6c80e3e0e6d5c5a18ecc0" || { echo "oreon: Source26 SHA256 mismatch for mathpazo.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/manfnt-font.tar.xz; test -f "$f" || { echo "oreon: missing Source27 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f1bbb929781f5a5f524ec7f1a4871a58259c2b22eb637872f71264a5dcdc26d4" || { echo "oreon: Source27 SHA256 mismatch for manfnt-font.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/mflogo-font.tar.xz; test -f "$f" || { echo "oreon: missing Source28 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "872232b0651640e772d8d2366e2074b7c8e5dabd53617280c587ed210a2b0d42" || { echo "oreon: Source28 SHA256 mismatch for mflogo-font.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/mflogo-font.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source29 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cf59b4f297c17a03b32d74f4d04276d1c42a84ceb3d4e21a41fbbbb4e9e0bc34" || { echo "oreon: Source29 SHA256 mismatch for mflogo-font.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/ncntrsbk.tar.xz; test -f "$f" || { echo "oreon: missing Source30 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4976f1859fb159505e60f1a21274b6b63c5af88f2e03cd0ea6a7e3c84512f4b7" || { echo "oreon: Source30 SHA256 mismatch for ncntrsbk.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/palatino.tar.xz; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a5950b7ce364231aace8830cdedbe6ab511bfe663a2f1ba0bd270e618463b6f1" || { echo "oreon: Source31 SHA256 mismatch for palatino.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pxfonts.tar.xz; test -f "$f" || { echo "oreon: missing Source32 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bdddf89946b2a237a75d8d9ee9f2bc6597c868ba2eb73c0a4925a1e631aecd60" || { echo "oreon: Source32 SHA256 mismatch for pxfonts.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/pxfonts.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source33 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "61e343867a2afa56cee8173f67e744738b5fe276e7f58a9f06748b39d3695ba9" || { echo "oreon: Source33 SHA256 mismatch for pxfonts.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/rsfs.tar.xz; test -f "$f" || { echo "oreon: missing Source34 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1afec0c5e9711f652675e38b7cd7e88101c44aa0d0ff317ad6ac06f1d2cc7043" || { echo "oreon: Source34 SHA256 mismatch for rsfs.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/rsfs.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source35 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a152acc91945bd8e115789ae0b0be5f60672b99938b4798c772b42ca58976a72" || { echo "oreon: Source35 SHA256 mismatch for rsfs.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/symbol.tar.xz; test -f "$f" || { echo "oreon: missing Source36 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c6b615bf830b8260a18f26a2aedd406c0e3aa9a24831cc1b2bc73be1774a669b" || { echo "oreon: Source36 SHA256 mismatch for symbol.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tex-gyre.tar.xz; test -f "$f" || { echo "oreon: missing Source37 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dfb4f55c4b02993003777a48663987bd102a3c5a2913172571e05fe2eb18407d" || { echo "oreon: Source37 SHA256 mismatch for tex-gyre.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tex-gyre.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source38 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c81a8ac0381e34c55b0075aec75e6646b69bb7b428ebb7d1eca337001f1ef08c" || { echo "oreon: Source38 SHA256 mismatch for tex-gyre.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tex-gyre-math.tar.xz; test -f "$f" || { echo "oreon: missing Source39 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8972d19fec5a701499fb6edc86f3ac4266343d42140cf6ae27edd44c2e916da3" || { echo "oreon: Source39 SHA256 mismatch for tex-gyre-math.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tex-gyre-math.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source40 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8c06fd0df3b1ad8fbcbc1b025f3ab086e1c0bb7260f2d4e21609140cdb569076" || { echo "oreon: Source40 SHA256 mismatch for tex-gyre-math.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/times.tar.xz; test -f "$f" || { echo "oreon: missing Source41 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "55f6097b5685a22a3ec1db61ae372ffe00b25d622ed4ee3d010cd8a037e48a00" || { echo "oreon: Source41 SHA256 mismatch for times.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tipa.tar.xz; test -f "$f" || { echo "oreon: missing Source42 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "07f7c0994c3e37ab2de47fe22c3046229de7138e800d4e67f6d1ad39d7066f9d" || { echo "oreon: Source42 SHA256 mismatch for tipa.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tipa.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source43 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9b854ecf441a08c0c616b3811076c27803d9bdf153075bb3968e65450d135c7c" || { echo "oreon: Source43 SHA256 mismatch for tipa.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/txfonts.tar.xz; test -f "$f" || { echo "oreon: missing Source44 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "03189f5a8b40535a5ca705aabb80aa9e9c9b9c993ba5885f891a3cdfc80afb1d" || { echo "oreon: Source44 SHA256 mismatch for txfonts.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/txfonts.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source45 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "abc1bc408dd6f4563f116f9da4d4d07a02360210655a89958c1acf11f0d8f856" || { echo "oreon: Source45 SHA256 mismatch for txfonts.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/utopia.tar.xz; test -f "$f" || { echo "oreon: missing Source46 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d8148e06274d9f3eca68d90586ee4f5797068ce8bb9ff93a7cb24872f520a643" || { echo "oreon: Source46 SHA256 mismatch for utopia.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/utopia.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source47 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a068f320e6c217355a73d7e91661dcae16cfbb91dd048bc691949cadc1304df7" || { echo "oreon: Source47 SHA256 mismatch for utopia.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/wasy.tar.xz; test -f "$f" || { echo "oreon: missing Source48 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9fc877454fef9746c8c85e5282caf349d7e67ed44ba2ee18202d76862e054d13" || { echo "oreon: Source48 SHA256 mismatch for wasy.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/wasy.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source49 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6d078bbf6d64d342726c42d14d81386fde079c8952f9645c19f65085da0a94d6" || { echo "oreon: Source49 SHA256 mismatch for wasy.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/wasy-type1.tar.xz; test -f "$f" || { echo "oreon: missing Source50 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1bd86eff809059e4a7c009d8fbe2dd756e568de1d91d6489d82766a1b6f60129" || { echo "oreon: Source50 SHA256 mismatch for wasy-type1.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/wasy-type1.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source51 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6613f94af665385aa4516468858899f250f2fd5e1748d86db7da8a277b43a689" || { echo "oreon: Source51 SHA256 mismatch for wasy-type1.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/wasysym.tar.xz; test -f "$f" || { echo "oreon: missing Source52 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6f574fd99a7304f0759aacc62a60747f4c8ef7922f53be6aa5ab168d78c45ef3" || { echo "oreon: Source52 SHA256 mismatch for wasysym.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/wasysym.doc.tar.xz; test -f "$f" || { echo "oreon: missing Source53 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "76580fff1ccd6f6e8d7331b9aeaeeb2addc3fc6242f000169996c85d0178d6ea" || { echo "oreon: Source53 SHA256 mismatch for wasysym.doc.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/zapfchan.tar.xz; test -f "$f" || { echo "oreon: missing Source54 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b1af3ec046fc3bdc9c1f35586a523cfd1393d02fd28e146b3efd2260d3311214" || { echo "oreon: Source54 SHA256 mismatch for zapfchan.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/zapfding.tar.xz; test -f "$f" || { echo "oreon: missing Source55 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7c95b0011067228c4395aef990d92e190a66f825f6f3fb5bf09a738893b47ece" || { echo "oreon: Source55 SHA256 mismatch for zapfding.tar.xz" >&2; exit 1; })
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

# Install AppStream metadata for font components
cp %{SOURCE56} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE57} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE58} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE59} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/lm %{buildroot}%{_datadir}/fonts/lm
ln -sf %{_texmf_main}/fonts/opentype/public/lm-math %{buildroot}%{_datadir}/fonts/lm-math
ln -sf %{_texmf_main}/fonts/opentype/public/tex-gyre %{buildroot}%{_datadir}/fonts/tex-gyre
ln -sf %{_texmf_main}/fonts/opentype/public/tex-gyre-math %{buildroot}%{_datadir}/fonts/tex-gyre-math

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-avantgar
%license gpl2.txt
%{_texmf_main}/dvips/avantgar/
%{_texmf_main}/fonts/afm/adobe/avantgar/
%{_texmf_main}/fonts/afm/urw/avantgar/
%{_texmf_main}/fonts/map/dvips/avantgar/
%{_texmf_main}/fonts/tfm/adobe/avantgar/
%{_texmf_main}/fonts/tfm/urw35vf/avantgar/
%{_texmf_main}/fonts/type1/urw/avantgar/
%{_texmf_main}/fonts/vf/adobe/avantgar/
%{_texmf_main}/fonts/vf/urw35vf/avantgar/
%{_texmf_main}/tex/latex/avantgar/

%files -n texlive-bookman
%license gpl2.txt
%{_texmf_main}/dvips/bookman/
%{_texmf_main}/fonts/afm/adobe/bookman/
%{_texmf_main}/fonts/afm/urw/bookman/
%{_texmf_main}/fonts/map/dvips/bookman/
%{_texmf_main}/fonts/tfm/adobe/bookman/
%{_texmf_main}/fonts/tfm/urw35vf/bookman/
%{_texmf_main}/fonts/type1/urw/bookman/
%{_texmf_main}/fonts/vf/adobe/bookman/
%{_texmf_main}/fonts/vf/urw35vf/bookman/
%{_texmf_main}/tex/latex/bookman/

%files -n texlive-charter
%license other-free.txt
%{_texmf_main}/fonts/afm/bitstrea/charter/
%{_texmf_main}/fonts/tfm/bitstrea/charter/
%{_texmf_main}/fonts/type1/bitstrea/charter/
%{_texmf_main}/fonts/vf/bitstrea/charter/
%doc %{_texmf_main}/doc/fonts/charter/

%files -n texlive-cm-super
%license gpl2.txt
%{_texmf_main}/dvips/cm-super/
%{_texmf_main}/fonts/afm/public/cm-super/
%{_texmf_main}/fonts/enc/dvips/cm-super/
%{_texmf_main}/fonts/map/dvips/cm-super/
%{_texmf_main}/fonts/map/vtex/cm-super/
%{_texmf_main}/fonts/type1/public/cm-super/
%{_texmf_main}/tex/latex/cm-super/
%doc %{_texmf_main}/doc/fonts/cm-super/

%files -n texlive-cmextra
%license pd.txt
%{_texmf_main}/fonts/source/public/cmextra/
%{_texmf_main}/fonts/tfm/public/cmextra/

%files -n texlive-courier
%license gpl2.txt
%{_texmf_main}/dvips/courier/
%{_texmf_main}/fonts/afm/adobe/courier/
%{_texmf_main}/fonts/afm/urw/courier/
%{_texmf_main}/fonts/map/dvips/courier/
%{_texmf_main}/fonts/tfm/adobe/courier/
%{_texmf_main}/fonts/tfm/urw35vf/courier/
%{_texmf_main}/fonts/type1/adobe/courier/
%{_texmf_main}/fonts/type1/urw/courier/
%{_texmf_main}/fonts/vf/adobe/courier/
%{_texmf_main}/fonts/vf/urw35vf/courier/
%{_texmf_main}/tex/latex/courier/

%files -n texlive-euro
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/euro/
%doc %{_texmf_main}/doc/latex/euro/

%files -n texlive-euro-ce
%license bsd.txt
%{_texmf_main}/fonts/source/public/euro-ce/
%{_texmf_main}/fonts/tfm/public/euro-ce/
%doc %{_texmf_main}/doc/fonts/euro-ce/

%files -n texlive-eurosym
%license other-free.txt
%{_texmf_main}/fonts/map/dvips/eurosym/
%{_texmf_main}/fonts/source/public/eurosym/
%{_texmf_main}/fonts/tfm/public/eurosym/
%{_texmf_main}/fonts/type1/public/eurosym/
%{_texmf_main}/tex/latex/eurosym/
%doc %{_texmf_main}/doc/fonts/eurosym/

%files -n texlive-fpl
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/fpl/
%{_texmf_main}/fonts/type1/public/fpl/
%doc %{_texmf_main}/doc/fonts/fpl/

%files -n texlive-helvetic
%license gpl2.txt
%{_texmf_main}/dvips/helvetic/
%{_texmf_main}/fonts/afm/adobe/helvetic/
%{_texmf_main}/fonts/afm/urw/helvetic/
%{_texmf_main}/fonts/map/dvips/helvetic/
%{_texmf_main}/fonts/tfm/adobe/helvetic/
%{_texmf_main}/fonts/tfm/monotype/helvetic/
%{_texmf_main}/fonts/tfm/urw35vf/helvetic/
%{_texmf_main}/fonts/type1/urw/helvetic/
%{_texmf_main}/fonts/vf/adobe/helvetic/
%{_texmf_main}/fonts/vf/monotype/helvetic/
%{_texmf_main}/fonts/vf/urw35vf/helvetic/
%{_texmf_main}/tex/latex/helvetic/

%files -n texlive-lm
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/lm/
%{_texmf_main}/fonts/enc/dvips/lm/
%{_texmf_main}/fonts/map/dvipdfm/lm/
%{_texmf_main}/fonts/map/dvips/lm/
%{_texmf_main}/fonts/opentype/public/lm/
%{_texmf_main}/fonts/tfm/public/lm/
%{_texmf_main}/fonts/type1/public/lm/
%{_texmf_main}/tex/latex/lm/
%doc %{_texmf_main}/doc/fonts/lm/
%{_datadir}/fonts/lm
%{_datadir}/appdata/lm.metainfo.xml

%files -n texlive-lm-math
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/lm-math/
%doc %{_texmf_main}/doc/fonts/lm-math/
%{_datadir}/fonts/lm-math
%{_datadir}/appdata/lm-math.metainfo.xml

%files -n texlive-manfnt-font
%license knuth.txt
%{_texmf_main}/fonts/afm/hoekwater/manfnt-font/
%{_texmf_main}/fonts/map/dvips/manfnt-font/
%{_texmf_main}/fonts/type1/hoekwater/manfnt-font/

%files -n texlive-marvosym
%license ofl.txt
%{_texmf_main}/fonts/afm/public/marvosym/
%{_texmf_main}/fonts/map/dvips/marvosym/
%{_texmf_main}/fonts/tfm/public/marvosym/
%{_texmf_main}/fonts/truetype/public/marvosym/
%{_texmf_main}/fonts/type1/public/marvosym/
%{_texmf_main}/tex/latex/marvosym/
%doc %{_texmf_main}/doc/fonts/marvosym/

%files -n texlive-mathpazo
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/mathpazo/
%{_texmf_main}/fonts/tfm/public/mathpazo/
%{_texmf_main}/fonts/type1/public/mathpazo/
%{_texmf_main}/fonts/vf/public/mathpazo/
%doc %{_texmf_main}/doc/latex/mathpazo/

%files -n texlive-mflogo-font
%license knuth.txt
%{_texmf_main}/fonts/afm/hoekwater/mflogo-font/
%{_texmf_main}/fonts/map/dvips/mflogo-font/
%{_texmf_main}/fonts/type1/hoekwater/mflogo-font/
%doc %{_texmf_main}/doc/fonts/mflogo-font/

%files -n texlive-ncntrsbk
%license gpl2.txt
%{_texmf_main}/dvips/ncntrsbk/
%{_texmf_main}/fonts/afm/adobe/ncntrsbk/
%{_texmf_main}/fonts/afm/urw/ncntrsbk/
%{_texmf_main}/fonts/map/dvips/ncntrsbk/
%{_texmf_main}/fonts/tfm/adobe/ncntrsbk/
%{_texmf_main}/fonts/tfm/urw35vf/ncntrsbk/
%{_texmf_main}/fonts/type1/urw/ncntrsbk/
%{_texmf_main}/fonts/vf/adobe/ncntrsbk/
%{_texmf_main}/fonts/vf/urw35vf/ncntrsbk/
%{_texmf_main}/tex/latex/ncntrsbk/

%files -n texlive-palatino
%license gpl2.txt
%{_texmf_main}/dvips/palatino/
%{_texmf_main}/fonts/afm/adobe/palatino/
%{_texmf_main}/fonts/afm/urw/palatino/
%{_texmf_main}/fonts/map/dvips/palatino/
%{_texmf_main}/fonts/tfm/adobe/palatino/
%{_texmf_main}/fonts/tfm/urw35vf/palatino/
%{_texmf_main}/fonts/type1/urw/palatino/
%{_texmf_main}/fonts/vf/adobe/palatino/
%{_texmf_main}/fonts/vf/urw35vf/palatino/
%{_texmf_main}/tex/latex/palatino/

%files -n texlive-pxfonts
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/pxfonts/
%{_texmf_main}/fonts/map/dvips/pxfonts/
%{_texmf_main}/fonts/tfm/public/pxfonts/
%{_texmf_main}/fonts/type1/public/pxfonts/
%{_texmf_main}/fonts/vf/public/pxfonts/
%{_texmf_main}/tex/latex/pxfonts/
%doc %{_texmf_main}/doc/fonts/pxfonts/

%files -n texlive-rsfs
%license other-free.txt
%{_texmf_main}/fonts/afm/public/rsfs/
%{_texmf_main}/fonts/map/dvips/rsfs/
%{_texmf_main}/fonts/source/public/rsfs/
%{_texmf_main}/fonts/tfm/public/rsfs/
%{_texmf_main}/fonts/type1/public/rsfs/
%{_texmf_main}/tex/plain/rsfs/
%doc %{_texmf_main}/doc/fonts/rsfs/

%files -n texlive-symbol
%license gpl2.txt
%{_texmf_main}/dvips/symbol/
%{_texmf_main}/fonts/afm/adobe/symbol/
%{_texmf_main}/fonts/afm/urw/symbol/
%{_texmf_main}/fonts/map/dvips/symbol/
%{_texmf_main}/fonts/tfm/adobe/symbol/
%{_texmf_main}/fonts/tfm/monotype/symbol/
%{_texmf_main}/fonts/tfm/urw35vf/symbol/
%{_texmf_main}/fonts/type1/urw/symbol/
%{_texmf_main}/tex/latex/symbol/

%files -n texlive-tex-gyre
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/tex-gyre/
%{_texmf_main}/fonts/enc/dvips/tex-gyre/
%{_texmf_main}/fonts/map/dvips/tex-gyre/
%{_texmf_main}/fonts/opentype/public/tex-gyre/
%{_texmf_main}/fonts/tfm/public/tex-gyre/
%{_texmf_main}/fonts/type1/public/tex-gyre/
%{_texmf_main}/tex/latex/tex-gyre/
%doc %{_texmf_main}/doc/fonts/tex-gyre/
%{_datadir}/fonts/tex-gyre
%{_datadir}/appdata/tex-gyre.metainfo.xml

%files -n texlive-tex-gyre-math
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/tex-gyre-math/
%doc %{_texmf_main}/doc/fonts/tex-gyre-math/
%{_datadir}/fonts/tex-gyre-math
%{_datadir}/appdata/tex-gyre-math.metainfo.xml

%files -n texlive-times
%license gpl2.txt
%{_texmf_main}/dvips/times/
%{_texmf_main}/fonts/afm/adobe/times/
%{_texmf_main}/fonts/afm/urw/times/
%{_texmf_main}/fonts/map/dvips/times/
%{_texmf_main}/fonts/tfm/adobe/times/
%{_texmf_main}/fonts/tfm/urw35vf/times/
%{_texmf_main}/fonts/type1/urw/times/
%{_texmf_main}/fonts/vf/adobe/times/
%{_texmf_main}/fonts/vf/urw35vf/times/
%{_texmf_main}/tex/latex/times/

%files -n texlive-tipa
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/tipa/
%{_texmf_main}/fonts/source/public/tipa/
%{_texmf_main}/fonts/tfm/public/tipa/
%{_texmf_main}/fonts/type1/public/tipa/
%{_texmf_main}/tex/latex/tipa/
%doc %{_texmf_main}/doc/fonts/tipa/

%files -n texlive-txfonts
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/txfonts/
%{_texmf_main}/fonts/enc/dvips/txfonts/
%{_texmf_main}/fonts/map/dvips/txfonts/
%{_texmf_main}/fonts/tfm/public/txfonts/
%{_texmf_main}/fonts/type1/public/txfonts/
%{_texmf_main}/fonts/vf/public/txfonts/
%{_texmf_main}/tex/latex/txfonts/
%doc %{_texmf_main}/doc/fonts/txfonts/

%files -n texlive-utopia
%{_texmf_main}/fonts/afm/adobe/utopia/
%{_texmf_main}/fonts/tfm/adobe/utopia/
%{_texmf_main}/fonts/type1/adobe/utopia/
%{_texmf_main}/fonts/vf/adobe/utopia/
%doc %{_texmf_main}/doc/fonts/utopia/

%files -n texlive-wasy
%license pd.txt
%{_texmf_main}/fonts/source/public/wasy/
%{_texmf_main}/fonts/tfm/public/wasy/
%{_texmf_main}/tex/plain/wasy/
%doc %{_texmf_main}/doc/fonts/wasy/

%files -n texlive-wasy-type1
%license pd.txt
%{_texmf_main}/fonts/afm/public/wasy-type1/
%{_texmf_main}/fonts/map/dvips/wasy-type1/
%{_texmf_main}/fonts/type1/public/wasy-type1/
%doc %{_texmf_main}/doc/fonts/wasy-type1/

%files -n texlive-wasysym
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/wasysym/
%doc %{_texmf_main}/doc/latex/wasysym/

%files -n texlive-zapfchan
%license gpl2.txt
%{_texmf_main}/dvips/zapfchan/
%{_texmf_main}/fonts/afm/adobe/zapfchan/
%{_texmf_main}/fonts/afm/urw/zapfchan/
%{_texmf_main}/fonts/map/dvips/zapfchan/
%{_texmf_main}/fonts/tfm/adobe/zapfchan/
%{_texmf_main}/fonts/tfm/urw35vf/zapfchan/
%{_texmf_main}/fonts/type1/urw/zapfchan/
%{_texmf_main}/fonts/vf/adobe/zapfchan/
%{_texmf_main}/fonts/vf/urw35vf/zapfchan/
%{_texmf_main}/tex/latex/zapfchan/

%files -n texlive-zapfding
%license gpl2.txt
%{_texmf_main}/dvips/zapfding/
%{_texmf_main}/fonts/afm/adobe/zapfding/
%{_texmf_main}/fonts/afm/urw/zapfding/
%{_texmf_main}/fonts/map/dvips/zapfding/
%{_texmf_main}/fonts/tfm/adobe/zapfding/
%{_texmf_main}/fonts/tfm/urw35vf/zapfding/
%{_texmf_main}/fonts/type1/urw/zapfding/
%{_texmf_main}/tex/latex/zapfding/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12:svn54074-8
- Import
