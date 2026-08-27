%global source0_hash 719c321173ca12660891080dae509080934f72d13a9417b2c40a22add963c7c5a1ee95d3b306f0d6c26b0db97d69979c27fbb15d1690849aa03b06d4b0193a67

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langczechslovak
Epoch:          12
Version:        svn54074
Release:        5%{?dist}
Summary:        Czech/Slovak

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 0cc0f07fafefa6d7ea1ae1b2ce143dbec124fe96b36221f1b5a847fd0b789d1974b5990ebd93b8ac0607f63956948bede25c7e690784ca7e9638f48139585a32
%global source3_hash 1575fbe0d70725e975cdb0c1c5ca685985d91f23e4a997af4a0db21905ac34962f69653ffe4084065bda70cfbba0f0a1f0885d3afc19e98d0045ebb68cb545c3
%global source4_hash b14b98d2cb66a3f8f5d8a313d9208a700d1c3664a5bd23f5baf0d9aa2e3acf3891a0536871988e7579020570999ea05a9dcd60a404cd6670e3c1cf8110d9094e
%global source5_hash da1d663125b913e3480ad147ac1f5c1befa00110e71bbd2d42384db03fe0f0db3133b49e26d1a336b49c10018990763d42ef49b64440c9138d9d938057ac90e0
%global source6_hash c5f35424e63c3cf16eb2a71380917e1e8e33d1ebf62a4472b989c4e4df8b9f84d45bb6220e92eeb614aa40d0bdf977a47a905389072d066dc93b009856deff17
%global source7_hash 300c9fa3a5b23001c03c2bd2e0db994e2f9168068afb39185064a70b85d5da9a62ca652959b2dc8a71735cbbe96d029b10fed51bb22ba6a386d9b555905925e4
%global source8_hash 2b1769ccc09de03c868bde8246c0d90a4e799e45d15c183fab121fa4356cbda85251e422e5d7ba6914027e640259d4a9acd55ada2689fe04935901ce86b3d10d
%global source9_hash 41e82154a95a69cf29d6a55faebeae61a02a558cb8b4a906ca4931f446fbb5741e85cb72b5c89302d518d0b27520f1efb2ae61147846ead5fb150ece6dd98a13
%global source10_hash bb2ff88687d3a87d6f2c9679738deed9c4a207b3ccfc246f6d1e88ac8a5b29129db7a5804efdd6d4eb81c21b113a24c8bb7c776ccf568e7a9bb1800d9c42a4f2
%global source11_hash cc0f0d0e2af2c210cb7888e90d668016dba4cfce3ae90faf0597a7f8c2058dfe56b92b71d185705c7d3b19d53b989724a9106ab56664fd2e6f4e95da5c0a48b8
%global source12_hash e84c12eed94f459a7769527197f8b4b2f638297eec5d41bc7e4e3cc86c593cf957158946eb495947ff557ff323a085212b61cb3233972238d3afa2fff54e367b
%global source13_hash d6b32a80d6f70c3490d6c0dbd4f52cb9e2bb17ea9d15340e0b0f829d4eeb7317dccc22cfa79af70c4f6862b58f182cad9a136800375708774620aee4cfafbfa2
%global source14_hash a25bd09502b1a0b9699ea5f9a0e8b3a0d3405de49d27502a7020cd62fdd33b06ff0ba4fe50e2e56244862f07ce4b70162a5d8ee7c20f49e503590a9941721c3e
%global source15_hash dc967aae970e535c5dea48264c30f01d5ff3521851abd718905b78497c3d95d403c4f1ec8633cd2a7a55fe0a6bc1e1523391b214fbb8a0e2ed03737b09080e40
%global source16_hash 10de238b8152907ec04834d6b4737cebb13bd6567c9867e19e2003d123299c733012569cd64a66d31a79894f9b37c1fc409cd5b76ed10832762988fc318875e5
%global source17_hash 228d83ed83c79cec5356964bbe47cd589ee1e2a418c7110c3487bf91f8e340be979d067358168b523d5a8b9750f1430ba2ca1450c9c604a2de27067f48bf5293
%global source18_hash cf07c907cc07b76d8c6872852791e260fa6c2ff83186cb19886bc74408773d24d3961ab6087780dddaec91d982548bd04ce987a8908d939eff6ef4d198639b55
%global source19_hash 6ea6d73a840dadc62897a21bb5c68ac2b18c40168a65fd48aaa3c6cb381b6ce57bba7f9392896c5e23b65cc0f453838b8d764cdefea3778b769124ad97cf1844
%global source20_hash fcfdf84d0d565511b8db4be1d73cef719364f842031d48cbd947117c7bb953f7b2a049849223540a4b2c512a6910635c540b9a629d4769cc43ff99b0ab04d1bf

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langczechslovak.tar.xz#/collection-langczechslovak.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-czech.tar.xz#/babel-czech.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-czech.doc.tar.xz#/babel-czech.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-slovak.tar.xz#/babel-slovak.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-slovak.doc.tar.xz#/babel-slovak.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cnbwp.tar.xz#/cnbwp.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cnbwp.doc.tar.xz#/cnbwp.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cs.tar.xz#/cs.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csbulletin.tar.xz#/csbulletin.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csbulletin.doc.tar.xz#/csbulletin.doc.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cstex.tar.xz#/cstex.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cstex.doc.tar.xz#/cstex.doc.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-czech.tar.xz#/hyphen-czech.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-slovak.tar.xz#/hyphen-slovak.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-czech.tar.xz#/lshort-czech.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-czech.doc.tar.xz#/lshort-czech.doc.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-slovak.tar.xz#/lshort-slovak.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-slovak.doc.tar.xz#/lshort-slovak.doc.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-cz.tar.xz#/texlive-cz.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-cz.doc.tar.xz#/texlive-cz.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-babel-czech
Requires:       texlive-babel-slovak
Requires:       texlive-cnbwp
Requires:       texlive-cs
Requires:       texlive-csbulletin
Requires:       texlive-cslatex
Requires:       texlive-csplain
Requires:       texlive-cstex
Requires:       texlive-hyphen-czech
Requires:       texlive-hyphen-slovak
Requires:       texlive-vlna
Requires:       texlive-lshort-czech
Requires:       texlive-lshort-slovak
Requires:       texlive-texlive-cz

%description
Support for Czech/Slovak.

%package -n texlive-babel-czech
Summary:        Babel support for Czech
Version:        svn30261
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(czech.ldf) = %{tl_version}

%description -n texlive-babel-czech
The package provides the language definition file for support of Czech in
babel. Some shortcuts are defined, as well as translations to Czech of standard
"LaTeX names".

%package -n texlive-babel-slovak
Summary:        Babel support for typesetting Slovak
Version:        svn30292
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(slovak.ldf) = %{tl_version}

%description -n texlive-babel-slovak
The package provides the language definition file for support of Slovak in
babel, including Slovak variants of LaTeX built-in-names. Shortcuts are also
defined.

%package -n texlive-cnbwp
Summary:        Typeset working papers of the Czech National Bank
Version:        svn69910
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(dcolumn.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(multicol.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(rotating.sty)
Requires:       tex(url.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xevlna.sty)
Requires:       tex(zwpagelayout.sty)
Provides:       tex(cnbwp-manual.sty) = %{tl_version}
Provides:       tex(cnbwp.cls) = %{tl_version}

%description -n texlive-cnbwp
The package supports proper formatting of Working Papers of the Czech National
Bank (WP CNB). The package was developed for CNB but it is also intended for
authors from outside CNB.

%package -n texlive-cs
Summary:        Czech/Slovak-tuned Computer Modern fonts
Version:        svn41553
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cmexb

%description -n texlive-cs
The fonts are provided as Metafont source; Type 1 format versions (csfonts-t1)
are also available.

%package -n texlive-csbulletin
Summary:        LaTeX class for articles submitted to the CSTUG Bulletin (Zpravodaj)
Version:        svn77112
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(csbulacronym.sty) = %{tl_version}
Provides:       tex(csbulletin.cls) = %{tl_version}
Provides:       tex(csbulobalka.cls) = %{tl_version}
Provides:       tex(csbulobalka.sty) = %{tl_version}
Provides:       tex(csbulv1.cls) = %{tl_version}

%description -n texlive-csbulletin
The package provides the class for articles for the CSTUG Bulletin (Zpravodaj
Ceskoslovenskeho sdruzeni uzivatelu TeXu). You can see the structure of a
document by looking at the source file of the manual.

%package -n texlive-cstex
Summary:        Support for Czech/Slovak languages
Version:        svn64149
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-cstex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cstex-doc <= 11:%{version}

%description -n texlive-cstex
This package mirrors the macros part of the home site's distribution of CSTeX.
The licence (modified GPL) applies to some of the additions that make it a
Czech/Slovak language distribution, rather than the distribution of a basic
Plain/LaTeX distribution.

%package -n texlive-hyphen-czech
Summary:        Czech hyphenation patterns.
Version:        svn73410
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-cs.ec.tex) = %{tl_version}
Provides:       tex(hyph-cs.tex) = %{tl_version}
Provides:       tex(loadhyph-cs.tex) = %{tl_version}

%description -n texlive-hyphen-czech
Hyphenation patterns for Czech in T1/EC and UTF-8 encodings. Original patterns
'czhyphen' are still distributed in the 'csplain' package and loaded with ISO
Latin 2 encoding (IL2).

%package -n texlive-hyphen-slovak
Summary:        Slovak hyphenation patterns.
Version:        svn73410
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sk.ec.tex) = %{tl_version}
Provides:       tex(hyph-sk.tex) = %{tl_version}
Provides:       tex(loadhyph-sk.tex) = %{tl_version}

%description -n texlive-hyphen-slovak
Hyphenation patterns for Slovak in T1/EC and UTF-8 encodings. Original patterns
'skhyphen' are still distributed in the 'csplain' package and loaded with ISO
Latin 2 encoding (IL2).

%package -n texlive-lshort-czech
Summary:        Czech translation of the "Short Introduction to LaTeX2e"
Version:        svn55643
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-czech-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-czech-doc <= 11:%{version}

%description -n texlive-lshort-czech
This is the Czech translation of "A Short Introduction to LaTeX2e".

%package -n texlive-lshort-slovak
Summary:        Slovak introduction to LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-slovak-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-slovak-doc <= 11:%{version}

%description -n texlive-lshort-slovak
A Slovak translation of Oetiker's (not so) short introduction.

%package -n texlive-texlive-cz
Summary:        TeX Live manual (Czech/Slovak)
Version:        svn77067
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-cz-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-cz-doc <= 11:%{version}

%description -n texlive-texlive-cz
TeX Live manual (Czech/Slovak)

%post -n texlive-hyphen-czech
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/czech.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "czech loadhyph-cs.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{czech}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{czech}{loadhyph-cs.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-czech
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/czech.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{czech}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-slovak
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/slovak.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "slovak loadhyph-sk.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{slovak}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{slovak}{loadhyph-sk.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-slovak
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/slovak.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{slovak}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-czech
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-czech/
%doc %{_texmf_main}/doc/generic/babel-czech/

%files -n texlive-babel-slovak
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-slovak/
%doc %{_texmf_main}/doc/generic/babel-slovak/

%files -n texlive-cnbwp
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/cnbwp/
%{_texmf_main}/makeindex/cnbwp/
%{_texmf_main}/tex/latex/cnbwp/
%doc %{_texmf_main}/doc/latex/cnbwp/

%files -n texlive-cs
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/cs/
%{_texmf_main}/fonts/map/dvips/cs/
%{_texmf_main}/fonts/source/public/cs/
%{_texmf_main}/fonts/tfm/cs/cs-a35/
%{_texmf_main}/fonts/tfm/cs/cs-charter/
%{_texmf_main}/fonts/tfm/public/cs/
%{_texmf_main}/fonts/type1/public/cs/
%{_texmf_main}/fonts/vf/cs/cs-a35/
%{_texmf_main}/fonts/vf/cs/cs-charter/

%files -n texlive-csbulletin
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/csbulletin/
%doc %{_texmf_main}/doc/latex/csbulletin/

%files -n texlive-cstex
%license pd.txt
%doc %{_texmf_main}/doc/cstex/

%files -n texlive-hyphen-czech
%license gpl2.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-slovak
%license gpl2.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-lshort-czech
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-czech/

%files -n texlive-lshort-slovak
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/lshort-slovak/

%files -n texlive-texlive-cz
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-cz/

%changelog
%autochangelog
