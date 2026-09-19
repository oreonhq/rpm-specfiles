%global source0_hash fc0d08f70aeb83869109290e6d1585d513097dcd4e17791752ecd3d26ac202838afb5931f78ceaeeaf72c63b18fe9183edd650c075d03188f24cb2caded178de

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langpolish
Epoch:          12
Version:        svn54074
Release:        3%{?dist}
Summary:        Polish

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 6c5bdaa1aeddea30a828d1b4dacfc3730b864b81089643c69de9fdb6dc1583b5b21aca5dfa4ecec57555a3e81e670db600572a94af7a37918ccb9efecd3eb7be
%global source3_hash 36f9e8c91120da8a100597e5869fa5559a8f93ed95ac987b916257c64af5d3e1a4429a0173e53dae96579f148697e095999ab41b2ac8fe0a75a5e13073a1f0ad
%global source4_hash 1e5629a2e6e6099a319d8b8a1efec83262780c70a57c482f66a33a48722bcdb18fb891a96b6b6f29c54d71ce581dd1c82decdd22ad74d6ef61765fec3f8c3614
%global source5_hash 29fba5bb48aeb2353616cfe9a8dd4fff90c164c10779b8115958733470fd47dc40a567212c62315110a5a7a51363c9f917c4984583d40177037d6b0803ce66fe
%global source6_hash 3d0bef5ca5c37f1cae98bd0555d714ed4408b6fde4ffcfa78cf2512114c9aa09b81b23bc6d76705f64dd08ea493add2027e7af997357ff5c4cc360deae11ba92
%global source7_hash f5503008430e969a604973e4481f8ab51269a2c3570f757787eb7a1a9d11b8508ec7ca1709a21b9e2299059a9c8ca20e5806093bd24166eb44e167c06e4fd0ee
%global source8_hash e752e4b53191a9c5b46d1aa5797d491b98ab2585873e9a9a1471aa89accd898cadc5a9332ab36828b4baa6a3d3d69b311794e1948b788db755dc8f066a68550b
%global source9_hash 9c1c0279f18a37b2a500e415364dd4404a7dca8b6e0f85b053db5511826eb401865984ee3471fbe607e4cfa605ab50c08e6c11b166dd629e84d9f07db4af7114
%global source10_hash d7265e7c76e29763641a5cd208427902fdb2c347f09578f199d403795210a173301a2a069921302a0ac1c124c618defadaced5c1cf96e001def8185a21b297aa
%global source11_hash c61289a35103ecfab025169d432be2b3c7f2fd4ff1eb094b345feae6c9a30bd2cee70e0402eb6c2ea330254cf00d04c02649a40d6bd011f9cc612521c88b94a6
%global source12_hash abc5162a490b9646649dfdf50779ab12632eb3ddc6d1c2bae93a4bb00ef1f9387bc8d873a7b5c062b92a999c9d62b74e64b1688dd3582255f7386958649ee009
%global source13_hash dfcd842a6ca4d628848b1c705f6f0cf21f3358d303eef745ef822bb3f4d3c402a5477242483f938a3e9e1ed004346dcfc95cb262c5d32af1f2f5d3e174f1c8fc
%global source14_hash b8c6455556eb60c3b8e6b9f79663ab315f22fa7dec10894577003bef994939095401736a134e8a6b06798b451d7f6be60fc782e0b92b9152c3fcc4fa0e9c37c3
%global source15_hash bb0d16d92272c6233284fbcd94864c381ce60343e5b9ac23a04871a515f36c18d5eca92e7ad4f80b1335348f62baa703671984db2c85d5a35d84f725f699db9a
%global source16_hash efde952f17a904492b2c36e49801514b97ac5302b406beca7680a893051bc3821e70cdaad8d01dab479476298154c5ce2db99d43b04cf51cbcc5e16358c9b9f0
%global source17_hash 91ec6d489652477c1ac1f21baa2879814b9081e67dff6c770df1601c5113ad333b003cb2ecb9ceaf2b30398f4b8d2ea57b61f7d872159eaa22137bebcdaefb5b
%global source18_hash 2001e894d897357e8a214634328497e4aa7a80cdc6fb39ea16cce31a94898c3753ff380f04a12f2450dc46067f851c40d4bb33e8e3f00aaccf5cac72aa5b085d
%global source19_hash 18b9546576957553b477a1c5a90e6780770f18d6aced92b17017c44770b6bfa9c3cf928500a9e56c6c67f45d375bc12ad8ebc97eb1589f3cf7b5b3ed2f7b55c6
%global source20_hash 0441621561c2c4208d083f84eaf47573de94248cc1aaf027061de636c1a65f35a307260eaf390257bd02acac34b42963f96030ee27c83650deb11234edec89bf
%global source21_hash 7387592a338e7ba10942e4ed96364e36ca325040bff02cd69bf0f98d471775d38bd63e54bad494f64874e2fd0462762595c5796d7453aa6909fccc2d9d6bd27c
%global source22_hash 6b6fc20f5ec1269d318813b1ad34020e2b5341ed8891c11d2eda6b84884b3782e992dd9dde16d14b2030f2b57e1146fb6da6e761a35b12a3d88e8d865285668d
%global source23_hash 07ca34ae47976c65deba5443052001406390befb6dc675af7651141505f088e2f67f39648f14a94f70788eda79221efb05c2246d1991811e697e88c7408f6cf6
%global source24_hash a61b861cdac25c0d8c7d48f67abb9eed88458d0d55e8afb706adabfbed0d1e7c7159fcf000b8012885f82f849ee965bf6a2607f1b67f2d9191f59f8538147230
%global source25_hash 23005895f708b07162b2b251be125b70dfa8ef6add8ef7c5dbab2c5a2e211f65fce8432cbf3ee324a9b72c2296d5dfffaaf5a52d77425e4d6fc3c042397d6bec
%global source26_hash fd22d5a6c34e5ab7859bbb515d54e822eb5167853abba3e25d5137df1bc34f0bad9892c16f7ed5dfded8b90651551e1ed84a00d561c561ba18f50fa04e7bc7af
%global source27_hash eb14d312f74c46b46a4b2b0cd142492d3b549d3f58db2908301a5d43a001f4d5cd6d252881ac1ed4f56606289d3e8b17dfc3e3fb2c66b2b69c68b1db7e652df1
%global source28_hash 1f76e8b6790c7474df16ad5d35d16a6706a4f53fab0c551da1bbc910d83015fc2c7866c73f2dfb73dcb1d13a612515672e26a8687901bb6c20efa27609e7b939
%global source29_hash 0cd4c549c7b00939dec5055705658f76f6ebbe5de70e082652b761673ba5a249924fb862a319512a9a124b9cdaae8906c74439bba97be8825d4d1ffc70642c8f
%global source30_hash cd438089d90faa0e9144d23adb78ce91d85b80ce084cb92511cc23882c675cb654cb704aebeb623bb29c70b764c8a0ab19915607664895c457c583f376c1088e

Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/collection-langpolish.tar.xz#/collection-langpolish.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-polish.tar.xz#/babel-polish.or11.tar.xz
Source3:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-polish.doc.tar.xz#/babel-polish.doc.or11.tar.xz
Source4:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bredzenie.tar.xz#/bredzenie.or11.tar.xz
Source5:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/bredzenie.doc.tar.xz#/bredzenie.doc.or11.tar.xz
Source6:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/cc-pl.tar.xz#/cc-pl.or11.tar.xz
Source7:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/cc-pl.doc.tar.xz#/cc-pl.doc.or11.tar.xz
Source8:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/gustlib.tar.xz#/gustlib.or11.tar.xz
Source9:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/gustlib.doc.tar.xz#/gustlib.doc.or11.tar.xz
Source10:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/hyphen-polish.tar.xz#/hyphen-polish.or11.tar.xz
Source11:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/lshort-polish.tar.xz#/lshort-polish.or11.tar.xz
Source12:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/lshort-polish.doc.tar.xz#/lshort-polish.doc.or11.tar.xz
Source13:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/mwcls.tar.xz#/mwcls.or11.tar.xz
Source14:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/mwcls.doc.tar.xz#/mwcls.doc.or11.tar.xz
Source15:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pl.tar.xz#/pl.or11.tar.xz
Source16:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pl.doc.tar.xz#/pl.doc.or11.tar.xz
Source17:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/polski.tar.xz#/polski.or11.tar.xz
Source18:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/polski.doc.tar.xz#/polski.doc.or11.tar.xz
Source19:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/przechlewski-book.tar.xz#/przechlewski-book.or11.tar.xz
Source20:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/przechlewski-book.doc.tar.xz#/przechlewski-book.doc.or11.tar.xz
Source21:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/qpxqtx.tar.xz#/qpxqtx.or11.tar.xz
Source22:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/qpxqtx.doc.tar.xz#/qpxqtx.doc.or11.tar.xz
Source23:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tap.tar.xz#/tap.or11.tar.xz
Source24:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tap.doc.tar.xz#/tap.doc.or11.tar.xz
Source25:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tex-virtual-academy-pl.tar.xz#/tex-virtual-academy-pl.or11.tar.xz
Source26:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/tex-virtual-academy-pl.doc.tar.xz#/tex-virtual-academy-pl.doc.or11.tar.xz
Source27:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-pl.tar.xz#/texlive-pl.or11.tar.xz
Source28:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-pl.doc.tar.xz#/texlive-pl.doc.or11.tar.xz
Source29:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/utf8mex.tar.xz#/utf8mex.or11.tar.xz
Source30:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/utf8mex.doc.tar.xz#/utf8mex.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-latex
Requires:       texlive-collection-basic
Requires:       texlive-babel-polish
Requires:       texlive-bredzenie
Requires:       texlive-cc-pl
Requires:       texlive-gustlib
Requires:       texlive-hyphen-polish
Requires:       texlive-lshort-polish
Requires:       texlive-mex
Requires:       texlive-mwcls
Requires:       texlive-pl
Requires:       texlive-polski
Requires:       texlive-przechlewski-book
Requires:       texlive-qpxqtx
Requires:       texlive-tap
Requires:       texlive-tex-virtual-academy-pl
Requires:       texlive-texlive-pl
Requires:       texlive-utf8mex

%description
Support for Polish.

%package -n texlive-babel-polish
Summary:        Babel support for Polish
Version:        svn62680
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(polish-compat.ldf) = %{tl_version}
Provides:       tex(polish.ldf) = %{tl_version}

%description -n texlive-babel-polish
The package provides the language definition file for support of Polish in
babel. Some shortcuts are defined, as well as translations to Polish of
standard "LaTeX names".

%package -n texlive-bredzenie
Summary:        A Polish version of "lorem ipsum..." in the form of a LaTeX package
Version:        svn44371
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bredzenie.sty) = %{tl_version}

%description -n texlive-bredzenie
This is a polish version of the classic pseudo-Latin "lorem ipsum dolor sit
amet...". It provides access to several paragraphs of pseudo-Polish generated
with Hidden Markov Models and Recurrent Neural Networks trained on a corpus of
Polish.

%package -n texlive-cc-pl
Summary:        Polish extension of Computer Concrete fonts
Version:        svn58602
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cc-pl
These Metafont sources rely on the availability of the Metafont 'Polish' fonts
and of the Metafont sources of the original Concrete fonts. Adobe Type 1
versions of the fonts are included.

%package -n texlive-gustlib
Summary:        Plain macros for much core and extra functionality, from GUST
Version:        svn54074
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(biblotex.tex) = %{tl_version}
Provides:       tex(infr-ex.tex) = %{tl_version}
Provides:       tex(infram.tex) = %{tl_version}
Provides:       tex(map.tex) = %{tl_version}
Provides:       tex(mcol-ex.tex) = %{tl_version}
Provides:       tex(meashor.tex) = %{tl_version}
Provides:       tex(mimulcol.tex) = %{tl_version}
Provides:       tex(plidxmac.tex) = %{tl_version}
Provides:       tex(przyklad.tex) = %{tl_version}
Provides:       tex(rbox-ex.tex) = %{tl_version}
Provides:       tex(roundbox.tex) = %{tl_version}
Provides:       tex(split.tex) = %{tl_version}
Provides:       tex(tp-crf.tex) = %{tl_version}
Provides:       tex(tsp.tex) = %{tl_version}
Provides:       tex(tun.tex) = %{tl_version}
Provides:       tex(verbatim-dek.tex) = %{tl_version}

%description -n texlive-gustlib
Includes bibliography support, token manipulation, cross-references, verbatim,
determining length of a paragraph's last line, multicolumn output, Polish
bibliography and index styles, prepress and color separation, graphics
manipulation, tables.

%package -n texlive-hyphen-polish
Summary:        Polish hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-pl.qx.tex) = %{tl_version}
Provides:       tex(hyph-pl.tex) = %{tl_version}
Provides:       tex(loadhyph-pl.tex) = %{tl_version}

%description -n texlive-hyphen-polish
Hyphenation patterns for Polish in QX and UTF-8 encodings. These patterns are
also used by Polish TeX formats MeX and LaMeX.

%package -n texlive-lshort-polish
Summary:        Introduction to LaTeX in Polish
Version:        svn63289
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-polish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-polish-doc <= 11:%{version}

%description -n texlive-lshort-polish
This is the Polish translation of A Short Introduction to LaTeX2e.

%package -n texlive-mwcls
Summary:        Polish-oriented document classes
Version:        svn77050
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mwcls
mwcls is a set of document classes for LaTeX2e designed with Polish
typographical tradition in mind. Classes include: 'mwart' (which is a
replacement for 'article'), 'mwrep' (replacing 'report'), and 'mwbk' (replacing
'book'). Most features present in standard classes work with mwcls classes.
Some extensions/exceptions include: sectioning commands allow for second
optional argument (it is possible to state different texts for running head and
for TOC), new environments 'itemize*' and 'enumerate*' for lists with long
items, page styles have variants for normal, opening, closing, and blank pages.

%package -n texlive-pl
Summary:        Polish extension of Computer Modern fonts
Version:        svn58661
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pl
The Polish extension of the Computer Modern fonts (compatible with CM itself)
for use with Polish TeX formats. The fonts were originally a part of the MeX
distribution (and they are still available that way).

%package -n texlive-polski
Summary:        Typeset Polish documents with LaTeX and Polish fonts
Version:        svn60322
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyphen-polish
Requires:       texlive-pl
Provides:       tex(amigapl.def) = %{tl_version}
Provides:       tex(mazovia.def) = %{tl_version}
Provides:       tex(ot1patch.sty) = %{tl_version}
Provides:       tex(plprefix.sty) = %{tl_version}
Provides:       tex(polski.sty) = %{tl_version}
Provides:       tex(qxenc.def) = %{tl_version}

%description -n texlive-polski
Tools to typeset monolingual Polish documents in LaTeX2e without babel or
polyglossia. The package loads Polish hyphenation patterns, ensures that a font
encoding suitable for Polish is used; in particular it enables Polish
adaptation of Computer Modern fonts (the so-called PL fonts), provides
translations of \today and names like "Bibliography" or "Chapter", redefines
math symbols according to Polish typographical tradition, provides macros for
dashes according to Polish orthography, provides a historical input method for
"Polish characters", works with traditional TeX as well as with Unicode aware
variants. (This package was previously known as platex, but has been renamed to
resolve a name clash.)

%package -n texlive-przechlewski-book
Summary:        Examples from Przechlewski's LaTeX book
Version:        svn23552
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-przechlewski-book
The bundle provides machine-readable copies of the examples from the book
"Praca magisterska i dyplomowa z programem LaTeX".

%package -n texlive-qpxqtx
Summary:        Polish macros and fonts supporting Pagella/pxfonts and Termes/txfonts
Version:        svn45797
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(amspbold.tex) = %{tl_version}
Provides:       tex(amsqpx.def) = %{tl_version}
Provides:       tex(amsqpx.tex) = %{tl_version}
Provides:       tex(amsqtx.def) = %{tl_version}
Provides:       tex(amsqtx.tex) = %{tl_version}
Provides:       tex(amstbold.tex) = %{tl_version}
Provides:       tex(qpxmath.sty) = %{tl_version}
Provides:       tex(qpxmath.tex) = %{tl_version}
Provides:       tex(qtxmath.sty) = %{tl_version}
Provides:       tex(qtxmath.tex) = %{tl_version}

%description -n texlive-qpxqtx
Polish macros and fonts supporting Pagella/pxfonts and Termes/txfonts

%package -n texlive-tap
Summary:        TeX macros for typesetting complex tables
Version:        svn31731
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tap.tex) = %{tl_version}

%description -n texlive-tap
The package offers a simple notation for pretty complex tables (to Michael J.
Ferguson's credit). With PostScript, the package allows shaded/coloured tables,
diagonal rules, etc. The package is supposed to work with both Plain and LaTeX.
An AWK converter from ASCII semigraphic tables to TAP notation is included.

%package -n texlive-tex-virtual-academy-pl
Summary:        TeX usage web pages, in Polish
Version:        svn67718
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-virtual-academy-pl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-virtual-academy-pl-doc <= 11:%{version}

%description -n texlive-tex-virtual-academy-pl
TeX Virtual Academy is a bundle of Polish documentation in HTML format about
TeX and Co. It contains information for beginners, LaTeX packages,
descriptions, etc.

%package -n texlive-texlive-pl
Summary:        TeX Live manual (Polish)
Version:        svn74803
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-pl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-pl-doc <= 11:%{version}

%description -n texlive-texlive-pl
TeX Live manual (Polish)

%package -n texlive-utf8mex
Summary:        Tools to produce formats that read Polish language input
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(utf8-pl.tex) = %{tl_version}
Provides:       tex(utf8plsq.tex) = %{tl_version}

%description -n texlive-utf8mex
The bundle provides files for building formats to read input in Polish
encodings.

%post -n texlive-hyphen-polish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/polish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "polish loadhyph-pl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{polish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{polish}{loadhyph-pl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-polish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/polish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{polish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-polish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-polish/
%doc %{_texmf_main}/doc/generic/babel-polish/

%files -n texlive-bredzenie
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bredzenie/
%doc %{_texmf_main}/doc/latex/bredzenie/

%files -n texlive-cc-pl
%license pd.txt
%{_texmf_main}/fonts/map/dvips/cc-pl/
%{_texmf_main}/fonts/source/public/cc-pl/
%{_texmf_main}/fonts/tfm/public/cc-pl/
%{_texmf_main}/fonts/type1/public/cc-pl/
%doc %{_texmf_main}/doc/fonts/cc-pl/

%files -n texlive-gustlib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/gustlib/
%{_texmf_main}/bibtex/bst/gustlib/
%{_texmf_main}/tex/plain/gustlib/
%doc %{_texmf_main}/doc/plain/gustlib/

%files -n texlive-hyphen-polish
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-lshort-polish
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-polish/

%files -n texlive-mwcls
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mwcls/
%doc %{_texmf_main}/doc/latex/mwcls/

%files -n texlive-pl
%license pd.txt
%{_texmf_main}/dvips/pl/
%{_texmf_main}/fonts/afm/public/pl/
%{_texmf_main}/fonts/enc/dvips/pl/
%{_texmf_main}/fonts/map/dvips/pl/
%{_texmf_main}/fonts/source/public/pl/
%{_texmf_main}/fonts/tfm/public/pl/
%{_texmf_main}/fonts/type1/public/pl/
%doc %{_texmf_main}/doc/fonts/pl/

%files -n texlive-polski
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/polski/
%doc %{_texmf_main}/doc/latex/polski/

%files -n texlive-przechlewski-book
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/przechlewski-book/
%{_texmf_main}/tex/latex/przechlewski-book/
%doc %{_texmf_main}/doc/latex/przechlewski-book/

%files -n texlive-qpxqtx
%license pd.txt
%{_texmf_main}/fonts/tfm/public/qpxqtx/
%{_texmf_main}/fonts/vf/public/qpxqtx/
%{_texmf_main}/tex/generic/qpxqtx/
%doc %{_texmf_main}/doc/fonts/qpxqtx/

%files -n texlive-tap
%license pd.txt
%{_texmf_main}/tex/generic/tap/
%doc %{_texmf_main}/doc/generic/tap/

%files -n texlive-tex-virtual-academy-pl
%license fdl.txt
%doc %{_texmf_main}/doc/generic/tex-virtual-academy-pl/

%files -n texlive-texlive-pl
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-pl/

%files -n texlive-utf8mex
%license pd.txt
%{_texmf_main}/tex/mex/utf8mex/
%doc %{_texmf_main}/doc/mex/utf8mex/

%changelog
%autochangelog
