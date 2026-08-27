%global source0_hash 2d93df728d34137c8f9a884aa2871a2980e806672006f2c5f0c5f79412d5789c6f94958363cfc9a78b5a97a7d76bbb6cb157b2cb2a8a283f7afdfd838fa24883

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langkorean
Epoch:          12
Version:        svn54074
Release:        3%{?dist}
Summary:        Korean

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash f9270a17459444e128b5fc5d12b943043fa4ec2f87ee5996808f9dfad1c4c4146787db3ecd267767a375d1fdbd56e15850b25cd7c9c71ab270e3517b5863054a
%global source3_hash 3a3819f892bdf69afeb66b9fdfbfe1ffe06e2a488425e814cb3a1e223ec9659a71f0571dc25136e0f7afcdb616f717dcb3823b89e640b0894313683e4f79b197
%global source4_hash 4252436af26489464f4865a91902518a6af47e4d176b12e04cfbe4573ad8303df2f613920dd9bfbd0842bb13cbf847bc7ce6c274218a38cf719ba82573d6b7a6
%global source5_hash 4bc8c11c2f1240590d5576d69acc7fab41df8b75dd71448351d079d318f3e28ec9ec8f11165fad5d60d548274de7c7aaeb132a5f4e87966d5bb005fb968980ea
%global source6_hash 695176d8a718c98f749160a619dcb982474448aa53b31c08330964fd6d8ab03268ac326ef7177b05f7472c4a36482026dd9bc00598fc6973e807b7e31fed5342
%global source7_hash a4951681e018a8c327a4889cd9d158f49971160cf1ef1407203387926e59783ee40256544dc083c2f766e0808ed30e1bc4eacab3792e9eacdc7d66c0032182a9
%global source8_hash 940f6672fd2d490cae446408ed6421c77ada3ea9c0c4820b00a0b38026ed5d30fa2b0f8bf86a5904a8c04b15e561e3f146ae4f817e7e2ef8c3a9284f9c841350
%global source9_hash 34a45ea6cda9fa9b6ba453fef795740869b1cc3c3eec84b467847b7221a916f4eada3bac97b78dc6e5a545e12f87f1d56c3540fafa658535f9ca89335bc6b534
%global source10_hash be75556f3857a405d235f920866f8089f105a57f9accff07a541fe110bb8124e049ebe75368ce3282bcd329cc6a02eed0ccffdfad49020986d61221839cae4b5
%global source11_hash 7226874594b10ee48e8aea30a72e6d6f4db9f770d5d5830dc83a41f828bfe36b0b11f679aff02722e457150548860f1ad719758e6ffd239bbf9ac18d907acded
%global source12_hash 45f9671674a1e931de471c08f80a6798fc140466b8b8407cd5db98d9312d57a9433861a8c57970df9d12c2984c0a0e1c87a8b601a79ec8c9eab5d390784fdeee
%global source13_hash 09307c7c051156305af1e9d8141203ae9cd7261a619659fa27d3a0cd5cf0c93d77f6c5f0b0668d23004e5b35270a0502c6e9e0d364d7b519972c9b802d96e323
%global source14_hash fc775dae204d8f1ca7e05005ccba0bd568f00819519d34b2282028d7f2b89b9c1f9a091ed192def7281de97ea97c75b9327727489e8ff88585bb97cf5e8b8f10
%global source15_hash ff0bd0bcc32eb8166e7bff9d440692a3c21c5cc7fd7b8139b472fbc2e079cba0591d162e2a81090919990dba31d1e04b57d50c35ac1d0670ef9102c64abc88ad
%global source16_hash bec230ec4b102af07923a9892b5bbafcd04f9c34cade7d96c0f4754689ff017caeae17ef1c511b3fd4fec6c7ed047774ad55c791cb8ee7b8dfe03931884cfad2
%global source17_hash 6f4e2d8ca583b1a811ce03559dda164bca10a9fdf4f3f211e941e166d46c2327db1e3d25d15ea9e294b714d561c0d534db2bc84203a8755bc38e1e08ba3cc695
%global source18_hash b5e722e7a72d2efcd89c969c10291779a2885603817374e4318f59b4042b8890df967503016d08a91e30ba8cbbc6f1838843644f06cf44766a7096efdd3bf905
%global source19_hash c37c5041d155f9a175a6761154211a683405d094850cc829a6b942afcb93af987b4049e663d260ae2b066827007d8c6576fdcd5d14d3ff599f031b13c00e162f
%global source20_hash 5476421a802ec3daa8fcb8354924ffb090aa9ea337db315c813637fafa445ef82601edc61cb7aa424bd7e2deee7607902ed33f0cfe70c214901d4c52dfcff6c5
%global source21_hash 8f51172be1093ff9da6ebb7071f5fea435e2bdace5619faa24ebdef52b3e34197d91b8f9d302844d4e1377a2a4712247743172afcd4b01367e9f166bd76112fd
%global source22_hash 9cf9a73ba3c2190da7999c3b770e92d8afb43c640d651173c126e930155e9f87f371392accd4eadae8922ee846a5e02c0eeab845561dea943b34b185164bba3c
%global source23_hash 6173d49bb64c9b162763ff08af445e518fa650fcc13e02f5c72454d335285d9c82347cf79f945fae94429f3a9d15f9c9b58ff1d175c8f59ea7b75766cd279303

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langkorean.tar.xz#/collection-langkorean.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baekmuk.tar.xz#/baekmuk.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baekmuk.doc.tar.xz#/baekmuk.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk-ko.tar.xz#/cjk-ko.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk-ko.doc.tar.xz#/cjk-ko.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-oblivoir.tar.xz#/kotex-oblivoir.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-oblivoir.doc.tar.xz#/kotex-oblivoir.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-plain.tar.xz#/kotex-plain.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-plain.doc.tar.xz#/kotex-plain.doc.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-utf.tar.xz#/kotex-utf.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-utf.doc.tar.xz#/kotex-utf.doc.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-korean.tar.xz#/lshort-korean.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-korean.doc.tar.xz#/lshort-korean.doc.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nanumtype1.tar.xz#/nanumtype1.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nanumtype1.doc.tar.xz#/nanumtype1.doc.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmhanguljamo.tar.xz#/pmhanguljamo.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmhanguljamo.doc.tar.xz#/pmhanguljamo.doc.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uhc.tar.xz#/uhc.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uhc.doc.tar.xz#/uhc.doc.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unfonts-core.tar.xz#/unfonts-core.or11.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unfonts-core.doc.tar.xz#/unfonts-core.doc.or11.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unfonts-extra.tar.xz#/unfonts-extra.or11.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unfonts-extra.doc.tar.xz#/unfonts-extra.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-langcjk
Requires:       texlive-baekmuk
Requires:       texlive-cjk-ko
Requires:       texlive-kotex-oblivoir
Requires:       texlive-kotex-plain
Requires:       texlive-kotex-utf
Requires:       texlive-kotex-utils
Requires:       texlive-lshort-korean
Requires:       texlive-nanumtype1
Requires:       texlive-pmhanguljamo
Requires:       texlive-uhc
Requires:       texlive-unfonts-core
Requires:       texlive-unfonts-extra

%description
Support for Korean; additional packages in collection-langcjk.

%package -n texlive-baekmuk
Summary:        Baekmuk Korean TrueType fonts
Version:        svn56915
License:        Baekmuk
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-baekmuk
This bundle consists of four Korean fonts: batang.ttf: serif dotum.ttf:
sans-serif gulim.ttf: sans-serif (rounded) hline.ttf: headline These fonts were
originally retrieved from http://kldp.net/baekmuk/ and are no longer
maintained.

%package -n texlive-cjk-ko
Summary:        Extension of the CJK package for Korean typesetting
Version:        svn70300
License:        GPL-2.0-or-later AND LPPL-1.3c AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cjk
Requires:       tex(CJKfntef.sty)
# Ignoring dependency on kotex-euc.sty - not part of TeX Live
Requires:       tex(kotexutf.sty)
Requires:       tex(luatexko.sty)
Requires:       tex(ulem.sty)
Requires:       tex(xetexko.sty)
Provides:       tex(cjkutf8-josa.sty) = %{tl_version}
Provides:       tex(cjkutf8-ko.sty) = %{tl_version}
Provides:       tex(cjkutf8-nanummjhanja.sty) = %{tl_version}
Provides:       tex(kolabels-utf.sty) = %{tl_version}
Provides:       tex(konames-utf.sty) = %{tl_version}
Provides:       tex(kotex.sty) = %{tl_version}

%description -n texlive-cjk-ko
The package supports typesetting UTF-8-encoded modern Korean documents with the
help of the LaTeX2e CJK package. It provides some enhanced features focused on
Korean typesetting culture, one of them being allowing line-break between Latin
and CJK characters. The package requires nanumtype1 fonts.

%package -n texlive-kotex-oblivoir
Summary:        A LaTeX document class for typesetting Korean documents
Version:        svn76503
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-kotex-utf
Requires:       texlive-memoir
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(cjkutf8-ko.sty)
Requires:       tex(dhucs-paralist.sty)
Requires:       tex(dhucs.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kolabels-utf.sty)
Requires:       tex(kotex.sty)
Requires:       tex(luatexko.sty)
Requires:       tex(memhfixc.sty)
Requires:       tex(paralist.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(xetexko-font.sty)
Requires:       tex(xetexko-josa.sty)
Requires:       tex(xetexko-space.sty)
Requires:       tex(xetexko-vertical.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(10_5.sty) = %{tl_version}
Provides:       tex(fapapersize.sty) = %{tl_version}
Provides:       tex(hfontsel.sty) = %{tl_version}
Provides:       tex(memhangul-common.sty) = %{tl_version}
Provides:       tex(memhangul-patch.sty) = %{tl_version}
Provides:       tex(memhangul-ucs.sty) = %{tl_version}
Provides:       tex(memhangul-x.sty) = %{tl_version}
Provides:       tex(memucs-enumerate.sty) = %{tl_version}
Provides:       tex(memucs-gremph.sty) = %{tl_version}
Provides:       tex(memucs-interword-x.sty) = %{tl_version}
Provides:       tex(memucs-interword.sty) = %{tl_version}
Provides:       tex(memucs-setspace.sty) = %{tl_version}
Provides:       tex(nanumfontsel.sty) = %{tl_version}
Provides:       tex(ob-koreanappendix.sty) = %{tl_version}
Provides:       tex(ob-mathleading.sty) = %{tl_version}
Provides:       tex(ob-nokoreanappendix.sty) = %{tl_version}
Provides:       tex(ob-toclof.sty) = %{tl_version}
Provides:       tex(ob-unfontsdefault.sty) = %{tl_version}
Provides:       tex(obchapterstyles.sty) = %{tl_version}
Provides:       tex(obchaptertoc.sty) = %{tl_version}
Provides:       tex(oblivoir-misc.sty) = %{tl_version}
Provides:       tex(xetexko-var.sty) = %{tl_version}
Provides:       tex(xob-amssymb.sty) = %{tl_version}
Provides:       tex(xob-dotemph.sty) = %{tl_version}
Provides:       tex(xob-font.sty) = %{tl_version}
Provides:       tex(xob-hyper.sty) = %{tl_version}
Provides:       tex(xob-lwarp.sty) = %{tl_version}
Provides:       tex(xob-paralist.sty) = %{tl_version}

%description -n texlive-kotex-oblivoir
The class is based on memoir, and is adapted to typesetting Korean documents.
The bundle (of class and associated packages) belongs to the ko.TeX bundle. It
depends on memoir and kotex-utf to function.

%package -n texlive-kotex-plain
Summary:        Macros for typesetting Korean under Plain TeX
Version:        svn63689
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hangulcweb.tex) = %{tl_version}
Provides:       tex(kotexplain.tex) = %{tl_version}
Provides:       tex(kotexutf-core.tex) = %{tl_version}
Provides:       tex(kotexutf.tex) = %{tl_version}

%description -n texlive-kotex-plain
The package provides macros for typesetting Hangul, the native alphabet of the
Korean language, using plain *TeX. Input Korean text should be encoded in
UTF-8. The package belongs to the ko.TeX bundle.

%package -n texlive-kotex-utf
Summary:        Typeset Hangul, coded in UTF-8
Version:        svn63690
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cjk-ko
Requires:       tex(enumerate.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fnpara.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kolabels-utf.sty)
Requires:       tex(luatexko.sty)
Requires:       tex(paralist.sty)
Requires:       tex(sectsty.sty)
Requires:       tex(setspace.sty)
Requires:       tex(varioref.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xetexko.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(dhucs-cmap.sty) = %{tl_version}
Provides:       tex(dhucs-enumerate.sty) = %{tl_version}
Provides:       tex(dhucs-enumitem.sty) = %{tl_version}
Provides:       tex(dhucs-gremph.sty) = %{tl_version}
Provides:       tex(dhucs-interword.sty) = %{tl_version}
Provides:       tex(dhucs-nanumfont.sty) = %{tl_version}
Provides:       tex(dhucs-paralist.sty) = %{tl_version}
Provides:       tex(dhucs-sectsty.sty) = %{tl_version}
Provides:       tex(dhucs-setspace.sty) = %{tl_version}
Provides:       tex(dhucs-trivcj.sty) = %{tl_version}
Provides:       tex(dhucs-ucshyper.sty) = %{tl_version}
Provides:       tex(dhucs.sty) = %{tl_version}
Provides:       tex(dhucsfn.sty) = %{tl_version}
Provides:       tex(kosections-utf.sty) = %{tl_version}
Provides:       tex(kotex-logo.sty) = %{tl_version}
Provides:       tex(kotex-sections.sty) = %{tl_version}
Provides:       tex(kotex-varioref.sty) = %{tl_version}
Provides:       tex(kotexutf.sty) = %{tl_version}

%description -n texlive-kotex-utf
The package typesets Hangul, which is the native alphabet of the Korean
language; input Korean text should be encoded in UTF-8. The bundle (of class
and associated packages) belongs to the ko.TeX bundle.

%package -n texlive-lshort-korean
Summary:        Korean introduction to LaTeX
Version:        svn73814
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-korean-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-korean-doc <= 11:%{version}

%description -n texlive-lshort-korean
A translation of Oetiker's original (not so) short introduction.

%package -n texlive-nanumtype1
Summary:        Type1 subfonts of Nanum Korean fonts
Version:        svn29558
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nanumtype1
Nanum is a unicode font designed especially for Korean-language script. The
font was designed by Sandoll Communication and Fontrix; it includes the sans
serif (gothic), serif (myeongjo), pen script and brush script typefaces. The
package provides Type1 subfonts converted from Nanum Myeongjo (Regular and
ExtraBold) and Nanum Gothic (Regular and Bold) OTFs. C70, LUC, T1, and TS1 font
definition files are also provided. (The package does not include
OpenType/TrueType files, which are available from Naver)

%package -n texlive-pmhanguljamo
Summary:        Poor man's Hangul Jamo input method
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(frkjamofull.data.tex) = %{tl_version}
Provides:       tex(pmhanguljamo-frkim.code.tex) = %{tl_version}
Provides:       tex(pmhanguljamo-frkim.sty) = %{tl_version}
Provides:       tex(pmhanguljamo-rrk.sty) = %{tl_version}
Provides:       tex(pmhanguljamo.sty) = %{tl_version}

%description -n texlive-pmhanguljamo
This package provides a Hangul transliteration input method that allows to
typeset Korean letters (Hangul) using the proper fonts. The name is derived
from "Poor man's Hangul Jamo Input Method". The use of XeLaTeX is recommended.
pdfTeX is not supported.

%package -n texlive-uhc
Summary:        Fonts for the Korean language
Version:        svn16791
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uhc
Support for Korean documents written in Korean standard KSC codes for LaTeX2e.

%package -n texlive-unfonts-core
Summary:        TrueType version of Un-fonts
Version:        svn56291
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unfonts-core
The Un-fonts come from the HLaTeX as type1 fonts in 1998 by Koaunghi Un, he
made type1 fonts to use with Korean TeX (HLaTeX) in the late 1990's and
released it under the GPL license. They were converted to TrueType with the
FontForge (PfaEdit) by Won-kyu Park in 2003. Core families (9 fonts): UnBatang,
UnBatangBold: serif UnDotum, UnDotumBold: sans-serif UnGraphic, UnGraphicBold:
sans-serif style UnPilgi, UnPilgiBold: script UnGungseo: cursive, brush-stroke

%package -n texlive-unfonts-extra
Summary:        TrueType version of Un-fonts
Version:        svn56291
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unfonts-extra
The Un-fonts come from the HLaTeX as type1 fonts in 1998 by Koaunghi Un, he
made type1 fonts to use with Korean TeX (HLaTeX) in the late 1990's and
released it under the GPL license. They were converted to TrueType with the
FontForge (PfaEdit) by Won-kyu Park in 2003. Extra families (10 fonts): UnPen,
UnPenheulim: script UnTaza: typewriter style UnBom: decorative UnShinmun
UnYetgul: old Korean printing style UnJamoSora, UnJamoNovel, UnJamoDotum,
UnJamoBatang

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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-baekmuk
%license other-free.txt
%{_texmf_main}/fonts/truetype/public/baekmuk/
%doc %{_texmf_main}/doc/fonts/baekmuk/

%files -n texlive-cjk-ko
%license gpl2.txt
%license lppl1.3c.txt
%license pd.txt
%{_texmf_main}/tex/latex/cjk-ko/
%doc %{_texmf_main}/doc/latex/cjk-ko/

%files -n texlive-kotex-oblivoir
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kotex-oblivoir/
%doc %{_texmf_main}/doc/latex/kotex-oblivoir/

%files -n texlive-kotex-plain
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/kotex-plain/
%doc %{_texmf_main}/doc/plain/kotex-plain/

%files -n texlive-kotex-utf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kotex-utf/
%doc %{_texmf_main}/doc/latex/kotex-utf/

%files -n texlive-lshort-korean
%license fdl.txt
%doc %{_texmf_main}/doc/latex/lshort-korean/

%files -n texlive-nanumtype1
%license ofl.txt
%{_texmf_main}/fonts/afm/public/nanumtype1/
%{_texmf_main}/fonts/map/dvips/nanumtype1/
%{_texmf_main}/fonts/tfm/public/nanumtype1/
%{_texmf_main}/fonts/type1/public/nanumtype1/
%{_texmf_main}/fonts/vf/public/nanumtype1/
%{_texmf_main}/tex/latex/nanumtype1/
%doc %{_texmf_main}/doc/fonts/nanumtype1/

%files -n texlive-pmhanguljamo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pmhanguljamo/
%doc %{_texmf_main}/doc/latex/pmhanguljamo/

%files -n texlive-uhc
%license lppl1.3c.txt
%{_texmf_main}/dvips/uhc/
%{_texmf_main}/fonts/afm/uhc/umj/
%{_texmf_main}/fonts/map/dvips/uhc/
%{_texmf_main}/fonts/tfm/uhc/umj/
%{_texmf_main}/fonts/tfm/uhc/uwmj/
%{_texmf_main}/fonts/tfm/uhc/wmj/
%{_texmf_main}/fonts/type1/uhc/umj/
%{_texmf_main}/fonts/vf/uhc/uwmj/
%{_texmf_main}/fonts/vf/uhc/wmj/
%doc %{_texmf_main}/doc/fonts/uhc/

%files -n texlive-unfonts-core
%license gpl2.txt
%{_texmf_main}/fonts/truetype/public/unfonts-core/
%doc %{_texmf_main}/doc/fonts/unfonts-core/

%files -n texlive-unfonts-extra
%license gpl2.txt
%{_texmf_main}/fonts/truetype/public/unfonts-extra/
%doc %{_texmf_main}/doc/fonts/unfonts-extra/

%changelog
%autochangelog
