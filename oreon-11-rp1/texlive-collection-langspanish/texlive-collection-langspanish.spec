%global source0_hash 9832d0e4f367ae73c292fd9d8894527c373c0db762ebf683667bee96f3431f1b6b70e3b2425bf6bbd8ca0a1f9e633ce8022b8747465e670523aecc607f7577ca

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langspanish
Epoch:          12
Version:        svn72203
Release:        3%{?dist}
Summary:        Spanish

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash a1203a09f77e3753fc28d632abc1c7d686085cd016acbab38a767b85a815d0dd05006e49b11524deb85bb8a20a3a8f413917529842f850d4efbe80b38c216ee2
%global source3_hash 4c4cd96889c2f1db9766099de6d149963579d27256f44d555023e205ca09617b570237e7eec2b5523c61af4d1124683ade9eeed4a5fb96f140423176ef163cad
%global source4_hash 728d847331f1a00766cfc2818691516234b153182f31ad2da024ec3194cc384a41ca89cc67ce66447191188dfe088d1dc4c8af3b2e6952931ec7eb58737c4bca
%global source5_hash 3184373d85b1e9bd76588318372ced328d2ce7f6d4f45bc5634671a88314d1ed18cedd968e59dd5203b4d77e6d3576f36a654b1a8bbdaa106d47cbdfb825e452
%global source6_hash 1c8aef52e0eaba8a55e6c0bdaca4ef47012012a85d38ed268207227063d042f2f0b2cbafa3d1e4d71432e3ea6effd2a781ab0aefc536276de36a95d0dc834b68
%global source7_hash a60ed8ffc43cb56aeafab8d09e8235eea9482ff8cdabc00da68938d980b20a7067da3286fa8ce19eddf9276b51e78dd944545cb8bb891bc13c31cffbab39544e
%global source8_hash bfdad727600b708fbcd643f9a78f256252cf54d3addb9d94744cd390950cbec7fb5a87c04b80b7e1863a49e4933eb1411fc00374737c600481f48296f0b06e3e
%global source9_hash 913182c436b45fde4fe288260325e0d7173773c0bab06f370ab47c1eb483ff50d29539b084de137a34395dd85663217e17b088648d512b2fc3d76644f9cb5561
%global source10_hash 33f66e4f928591188289f07e003cac10229735e69ee7390020748e119930ea7b74ad69e5eea991d8e34325ac4d548ce0b843a00b3ca50b9e6fae3e96526a4ad8
%global source11_hash 5b5d0ebda1bde2c1c67fd4853a41bb10956487fa5ad2686d6814dbdd51f68dde2a3d294797b7b1602d587a44ea6acbd8260ab9965efab81d91eb9d9fdb93da69
%global source12_hash aa81a1a75029fe02ba5b5e44d9092721686626757c18793147d221e6909a298feb25568db22684dff0f012b1e9b1a13773029b7bf57f322c9f3a589f9b4429da
%global source13_hash 57489ea5726a482cadd57ee3d77bc758b976acb0ceb28bf959921d1d64ef1ebd44ef9ef5db175be41e7bfaf755aa83f0c48aa501d7d0bd7e126e68f884347218
%global source14_hash 0fbd0bbba635dd482d844e2987e997b6c3c170527645bd1932548701f998e74e6d863285c226b5040e560eb0b28066b797c37617da6939633e9f9830347c53a7
%global source15_hash bb0eb72cd85cd0c6201bf327ddd0afc8af85542943f9ad4d2d6decb7f7a297935a2f399316d5244df2a66700694d2bee470e8d00afab25fd3e629a2037478338
%global source16_hash 73cecbb031be2d421c25a7d6a5c04d08e30d83a88b4132682d434a879da915f1d4af56980f1bf04f7df5a3e881ecdd940a058a2dcf89b5e9f48c378eb322da06
%global source17_hash a6886d54c0f5e1915ff9efbc4974ab1ef7f6dc026d67a0596ed47ac9e94da098e690bc70d5ed3e45a4d8cbd0f877f0cd6cd3a3757288dfc2df284e9c040b7c1e
%global source18_hash b1546b0864e8ec408c48d88edab390d1343f91ec5a0dcb53eb924684ffbd39936913b9f6b8aec2182d7b6137a1ae2a31bbd7e4ba525bc577396676f4af725752
%global source19_hash b71748fb67ea3bbf60102bcaa6990c9fbc024bbb1a7031dce7f91bf7764b9a589dc694fedeb884318781a9cbdc571f9080ab60b68022d2641c4308b46cf3e22f
%global source20_hash ab9965189096647e8af9aa58a937fa15595bed32055b3819bfd12334cf60e01d18b12563de8169ea28e3c0a7768864e51631c29bbbe47d45e09ffb2b87c5d524
%global source21_hash a45f2db2445e2daec8b31e995669a189c1d201f457e06de7fc2a85ad85686b31fcf70040e7840e1168e29b2e5caf796c45b6ce934780fa5982d0750438263606
%global source22_hash 71cb48ffcd2d87148ca3acec4dd2bcbb0c9278c1fce9eced94d50d719eedc851418737db4288678e4958955b38fae3a9b75ff292d57b9522f657774700c0c9fc
%global source23_hash 8f8f4c094cd2fb2938b3b83f54cd921f8eb40bad9f4e98b804533a885bd331ec4ac13231a1a6dba317fd8eef8d208e32aca749b341ddbcf166bee30858052571
%global source24_hash e6e227782f6703c47fa4e0a3747e9bc2f7031f172cc50ff1b14ca718161d347d4796d2690ee45abde3c7a93a27cea230e8d18e7995aab235f1614fcc9f4c0e49
%global source25_hash 9028d94dfc187fed4b2edd47dc154d8d00bb4248cc7462a8f4681988d00fcd8f15ffcc39188c681f18dfd66fda264407e0ad957ba3287f5fd81eb8da670b7576
%global source26_hash 0f7e36cff9bcadf07f3adb084ed2e4c4346dc49b738553f6a0c4dd470f5979aa3d1eb307fd90e5da1638ed65ea6413dd0a5c0b21e2965a6269477d6f772618a1
%global source27_hash 3525bb6835d5f68a8f4ff9edd2e745e8d1a5f3db64245511077ff25c54da1dccc9ffa35522c3677ae330a84b69763e1c61c300774d688c2911021287ab3ae1ea

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langspanish.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antique-spanish-units.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antique-spanish-units.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-catalan.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-catalan.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-galician.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-galician.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-spanish.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-spanish.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/es-tex-faq.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/es-tex-faq.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-catalan.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-galician.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-spanish.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-spanish.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2tabu-spanish.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2tabu-spanish.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2e-help-texinfo-spanish.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2e-help-texinfo-spanish.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-esmx.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-esmx.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-spanish.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-spanish.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-es.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-es.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-es.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-es.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-antique-spanish-units
Requires:       texlive-babel-catalan
Requires:       texlive-babel-galician
Requires:       texlive-babel-spanish
Requires:       texlive-collection-basic
Requires:       texlive-es-tex-faq
Requires:       texlive-hyphen-catalan
Requires:       texlive-hyphen-galician
Requires:       texlive-hyphen-spanish
Requires:       texlive-l2tabu-spanish
Requires:       texlive-latex2e-help-texinfo-spanish
Requires:       texlive-latexcheat-esmx
Requires:       texlive-lshort-spanish
Requires:       texlive-quran-es
Requires:       texlive-texlive-es

%description
Support for Spanish.

%package -n texlive-antique-spanish-units
Summary:        A short document about antique spanish units
Version:        svn69568
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-antique-spanish-units-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-antique-spanish-units-doc <= 11:%{version}

%description -n texlive-antique-spanish-units
This short document is about antique spanish units used in Spain and their
colonies between the sixteenth and nineteenth centuries. The next step will be
to develop a LaTeX package similar to siunitx. The document could be
interesting for historians, economists, metrologists and others, as a reference
and detailed compendium about this old system of units.

%package -n texlive-babel-catalan
Summary:        Babel contributed support for Catalan
Version:        svn30259
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(catalan.ldf) = %{tl_version}

%description -n texlive-babel-catalan
The package establishes Catalan conventions in a document (or a subset of the
conventions, if Catalan is not the main language of the document).

%package -n texlive-babel-galician
Summary:        Babel/Polyglossia support for Galician
Version:        svn30270
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(galician.ldf) = %{tl_version}

%description -n texlive-babel-galician
The package provides a language description file that enables support of
Galician either with babel or with polyglossia.

%package -n texlive-babel-spanish
Summary:        Babel support for Spanish
Version:        svn59367
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(romanidx.sty) = %{tl_version}
Provides:       tex(spanish.ldf) = %{tl_version}

%description -n texlive-babel-spanish
This bundle provides the means to typeset Spanish text, with the support
provided by the LaTeX standard package babel. Note that separate support is
provided for those who wish to typeset Spanish as written in Mexico.

%package -n texlive-es-tex-faq
Summary:        CervanTeX (Spanish TeX Group) FAQ
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-es-tex-faq-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-es-tex-faq-doc <= 11:%{version}

%description -n texlive-es-tex-faq
SGML source, converted LaTeX version, and readable copies of the FAQ from the
Spanish TeX users group.

%package -n texlive-hyphen-catalan
Summary:        Catalan hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ca.ec.tex) = %{tl_version}
Provides:       tex(hyph-ca.tex) = %{tl_version}
Provides:       tex(loadhyph-ca.tex) = %{tl_version}

%description -n texlive-hyphen-catalan
Hyphenation patterns for Catalan in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-galician
Summary:        Galician hyphenation patterns.
Version:        svn73410
License:        Unlicense
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-gl.ec.tex) = %{tl_version}
Provides:       tex(hyph-gl.tex) = %{tl_version}
Provides:       tex(loadhyph-gl.tex) = %{tl_version}

%description -n texlive-hyphen-galician
Hyphenation patterns for Galician in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-spanish
Summary:        Spanish hyphenation patterns.
Version:        svn75447
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-es.ec.tex) = %{tl_version}
Provides:       tex(hyph-es.tex) = %{tl_version}
Provides:       tex(loadhyph-es.tex) = %{tl_version}

%description -n texlive-hyphen-spanish
Hyphenation patterns for Spanish in T1/EC and UTF-8 encodings.

%package -n texlive-l2tabu-spanish
Summary:        Spanish translation of "Obsolete packages and commands"
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l2tabu-spanish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l2tabu-spanish-doc <= 11:%{version}

%description -n texlive-l2tabu-spanish
A Spanish translation of the l2tabu practical guide to LaTeX2e by Mark Trettin.
A list of obsolete packages, commands and usages.

%package -n texlive-latex2e-help-texinfo-spanish
Summary:        Unofficial reference manual covering LaTeX2e
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex2e-help-texinfo-spanish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex2e-help-texinfo-spanish-doc <= 11:%{version}

%description -n texlive-latex2e-help-texinfo-spanish
The manual is provided as Texinfo source (which was originally derived from the
VMS help file in the DECUS TeX distribution of 1990, with many subsequent
changes). This is a collaborative development, and details of getting involved
are to be found on the package home page. A Spanish translation is included
here, and a French translation is available as a separate package. All the
other formats in the distribution are derived from the Texinfo source, as
usual.

%package -n texlive-latexcheat-esmx
Summary:        A LaTeX cheat sheet, in Spanish
Version:        svn36866
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latexcheat-esmx-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latexcheat-esmx-doc <= 11:%{version}

%description -n texlive-latexcheat-esmx
This is a translation to Spanish (Castellano) of Winston Chang's LaTeX cheat
sheet (a reference sheet for writing scientific papers).

%package -n texlive-lshort-spanish
Summary:        Short introduction to LaTeX, Spanish translation
Version:        svn35050
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-spanish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-spanish-doc <= 11:%{version}

%description -n texlive-lshort-spanish
A Spanish translation of the Short Introduction to LaTeX2e, version 20.

%package -n texlive-quran-es
Summary:        Spanish Translations for the quran package
Version:        svn74874
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-es.sty) = %{tl_version}
Provides:       tex(qurantext-esi.translation.def) = %{tl_version}
Provides:       tex(qurantext-esii.translation.def) = %{tl_version}
Provides:       tex(qurantext-esiii.translation.def) = %{tl_version}

%description -n texlive-quran-es
The package is designed for typesetting several Spanish translations of the
Holy Quran. It extends the quran package by adding three additional Spanish
translations.

%package -n texlive-texlive-es
Summary:        TeX Live manual (Spanish)
Version:        svn74997
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-es-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-es-doc <= 11:%{version}

%description -n texlive-texlive-es
TeX Live manual (Spanish)

%post -n texlive-hyphen-catalan
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/catalan.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "catalan loadhyph-ca.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{catalan}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{catalan}{loadhyph-ca.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-catalan
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/catalan.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{catalan}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-galician
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/galician.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "galician loadhyph-gl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{galician}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{galician}{loadhyph-gl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-galician
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/galician.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{galician}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-spanish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/spanish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "spanish loadhyph-es.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=espanol.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=espanol" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{spanish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{spanish}{loadhyph-es.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{espanol}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{espanol}{loadhyph-es.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-spanish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/spanish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=espanol.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{spanish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{espanol}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-antique-spanish-units
%license cc-by-4.txt
%doc %{_texmf_main}/doc/generic/antique-spanish-units/

%files -n texlive-babel-catalan
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-catalan/
%doc %{_texmf_main}/doc/generic/babel-catalan/

%files -n texlive-babel-galician
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-galician/
%doc %{_texmf_main}/doc/generic/babel-galician/

%files -n texlive-babel-spanish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-spanish/
%doc %{_texmf_main}/doc/generic/babel-spanish/

%files -n texlive-es-tex-faq
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/generic/es-tex-faq/

%files -n texlive-hyphen-catalan
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-galician
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-spanish
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%doc %{_texmf_main}/doc/generic/hyph-utf8/

%files -n texlive-l2tabu-spanish
%license pd.txt
%doc %{_texmf_main}/doc/latex/l2tabu-spanish/

%files -n texlive-latex2e-help-texinfo-spanish
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/info/
%doc %{_texmf_main}/doc/latex/latex2e-help-texinfo-spanish/

%files -n texlive-latexcheat-esmx
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latexcheat-esmx/

%files -n texlive-lshort-spanish
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-spanish/

%files -n texlive-quran-es
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/quran-es/
%doc %{_texmf_main}/doc/xelatex/quran-es/

%files -n texlive-texlive-es
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-es/

%changelog
%autochangelog
