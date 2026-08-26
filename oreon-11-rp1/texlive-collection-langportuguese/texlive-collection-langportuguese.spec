%global source0_hash 7eb0c67ec373c29b1fdd820c20ab3912e92bf834b9ebfb8c556105cb509d44b818f088c0a9e232e9507f302e9c2d9c1129160483314318a1f9d95634cbcdfce5

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langportuguese
Epoch:          12
Version:        svn73303
Release:        3%{?dist}
Summary:        Portuguese

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 803b7aed66605f3312c01641091b6531aead90bf6c8498a8c0f3f60b119b4fecdbcbfbb80e860add9ca1ddb297267507c3d589f5ac1468c287d87fde8340963b
%global source3_hash ab942f154ec4ad325e439f63a8e292d31296b7f53fc93a61bc17008f115e98107fbf9bc20d3ef17941d8366d8ac393f5dac16c8824ce5c24c1a4ce57883ab367
%global source4_hash 6074f5933b945f02b24c31353bd7d683b35a54f53aacfa2ac19de382f56fbb9f6284316ee70c0eacea3760101d98d4a6b7d78412a0d41b13c9e1c907d181ee16
%global source5_hash ef6e80c3417cfad3e2f3e0ecd3ce249aa0b4cf0a6b5dced09c27138e34a8c86a74d0d03c6888d0944fe2b03bb5b8180872306263c58f54281f4ed2fe3424d4bc
%global source6_hash 6c58f5a0f6fb8f129e202b786c258ba088efa44639f162b9e0109182072c16bfc6ba928953d6e9b31b2b1c2f693fe064476095c232dcb9e0c6bfcf18bfb7994e
%global source7_hash a0f726330a5b2d8da94cbf25fb1b1a2b22e5e9010e0cafdfdee3781bf518f0cb48adb27dce0fe2e46572460f8c1749c0db1c16e06343cabb8cb94227e3da58b6
%global source8_hash b4d4285b33f314720cd07eea903bb2fc6092f96033f75d4b06cf315fd24d1a34722aa73db4cb6410a847e1d23a131ae329f8ebe75fca15dcaffb99097768f55e
%global source9_hash d87c0a7722f62a599bcc63f7ecfea190c64d82a4a4a1ba21d18c69866f80ec77a527a82cb94b0d081002073f5faab95119c6902e8f8f2c10d815ca2d206b1d4c
%global source10_hash 620ff6cc3c9e154fd04cecc02839bed5f30c916589a4d899bbb84a0678580fcbc57830776dd09831e0686be2abbc7656c964f2a0550f2964bdcefe8b8cd551e0
%global source11_hash 98bb6ce5128ad4eaeee9d5fe8372bdf0611e79b462de8efecb3a8cde6266821eb651026c9891280ea3b9d6699ff01ef0f524bbf76b13f5e8bc0d701b0ea074a7
%global source12_hash b3aa1b8cd8342d20b5223ae9b733e776d79dc5f1eabe2a1612ca86ab00dc8c8b9bec136be2ee7228186bcbd516dddf7af132bfe871cd4958408a8f3dcafd9992
%global source13_hash e50cd94941704f1a620a7411624ffd61d47aa4ef2944220ef0bfa9fbc428d8ea46be17bb3b18b30d645dcddf3c8091dafa9532f809dee7af230e2133c86b9bf5
%global source14_hash 00369fce725567a85310afd3063a4a20e670d8a0c57ef7e4515579ee0f91157f44bac2471b076c2ba51253e2c172447cc4b915877d80b0c43874c4e125f5f9d4
%global source15_hash 22b0b611784ad13539f012a326f7763396a4215e05068a23ea7305f50897d66ca48f0ee22681efd12db0ad9d4cca014c2684b680ab79b622b55451f50bcb5477
%global source16_hash 949b4a2396c913191b4f6819418924ad67208349a7bd492431f43362d64f9f17b70ff695833edea9475389999e2d8da62b8a789428b2dc62647a09ac44195894
%global source17_hash c8ce6215b875e717a49a59c7eef809c4677e81c715e7021a6dd43ae102bc4795db35dab7b4f234dea7f1bf1db4a11d463a78bec69b2d54a75fe2df1c17d0ffcc
%global source18_hash 0aa4feeefc9e29420fcc573ae0ba963d0c8378b2f4a589c9b4c09fefbc00ca50a5b08205232483b5ea45340214aa4eafa9443ba6153186907e29109c77294476
%global source19_hash 338daa3afb3e8591c6b0f25af393d38396690bda9092ccb5e73afd5b8254188136a701f197aa3c88daf2a0b43fc9a62995513176afc4cb054d0bb9ed511337db
%global source20_hash ea949bec80fcbdbb587b12048c806ed66183f08ea1d587b80153e2e9926e78db53d00132d160b85a622b9e6ff292c3655450a88c3e59dd60bd51f7db50baf7ed
%global source21_hash 2a2924af70b0ed8d76f6062482a500371d67d5a3bc0b87382d76626b34da9c1acdf9c123ebfdab2e5e79041b10d0e327e9cd732781e5fa1620247bdf02dc21fb
%global source22_hash 5b9fc92a4cb3597c0c95936d5fb6ad475ca4f9896f8165a0e391e591bb3fc9ea75ae79c14ee62197200d69d577df8025e6017960beafe6bef0bda90a6a615118
%global source23_hash d0f99c101be436a2017384e9cd4e2a176150d83b44079da2ecdf680873e2edfe931375daf6dde9023a268dbcf5a9df5a622968af0305034ebf1fc5d40d6ed191
%global source24_hash 9650b539bb25457f0428db74607d8f6e91e336123615937cbc39b46fa274de3bd4e2b4bbd78951e78d94b9ce888f58805aec85629dc308972fd1b6f3f95a51e7
%global source25_hash 291825c3461b397deb825266c7ee4316c5d04b8db1a29759378409de55c20d81552e31260468f4fa6a9a04f04705422714a8ec70a866c87fca2f4f1e189e0e4e
%global source26_hash e27dfa0b36341bcd02ba63a8b543f1a6c55c674745cc790543ea2cfded80e536e5901f184a3af62b92b4534c738a06bf4fd5cbd4dfb4da865d13991279309aac

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langportuguese.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-portuges.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-portuges.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer-tut-pt.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer-tut-pt.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cursolatex.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cursolatex.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feupphdteses.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feupphdteses.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-portuguese.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-via-exemplos.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-via-exemplos.doc.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-ptbr.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-ptbr.doc.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-portuguese.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-portuguese.doc.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numberpt.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numberpt.doc.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ordinalpt.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ordinalpt.doc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptlatexcommands.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptlatexcommands.doc.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabularray-abnt.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabularray-abnt.doc.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xypic-tut-pt.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xypic-tut-pt.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-babel-portuges
Requires:       texlive-beamer-tut-pt
Requires:       texlive-collection-basic
Requires:       texlive-cursolatex
Requires:       texlive-feupphdteses
Requires:       texlive-hyphen-portuguese
Requires:       texlive-latex-via-exemplos
Requires:       texlive-latexcheat-ptbr
Requires:       texlive-lshort-portuguese
Requires:       texlive-numberpt
Requires:       texlive-ordinalpt
Requires:       texlive-ptlatexcommands
Requires:       texlive-tabularray-abnt
Requires:       texlive-xypic-tut-pt

%description
Support for Portuguese and Brazilian Portuguese.

%package -n texlive-babel-portuges
Summary:        Babel support for Portuges
Version:        svn77468
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(brazil.ldf) = %{tl_version}
Provides:       tex(brazilian.ldf) = %{tl_version}
Provides:       tex(portuges.ldf) = %{tl_version}
Provides:       tex(portuguese.ldf) = %{tl_version}

%description -n texlive-babel-portuges
The package provides the language definition file for support of Portuguese and
Brazilian Portuguese in babel. Some shortcuts are defined, as well as
translations to Portuguese of standard "LaTeX names".

%package -n texlive-beamer-tut-pt
Summary:        An introduction to the Beamer class, in Portuguese
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-beamer-tut-pt-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-beamer-tut-pt-doc <= 11:%{version}

%description -n texlive-beamer-tut-pt
An introduction to the Beamer class, in Portuguese

%package -n texlive-cursolatex
Summary:        A LaTeX tutorial
Version:        svn24139
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-cursolatex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cursolatex-doc <= 11:%{version}

%description -n texlive-cursolatex
The tutorial is presented as a set of slides (in Portuguese).

%package -n texlive-feupphdteses
Summary:        Typeset Engineering PhD theses at the University of Porto
Version:        svn30962
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(backref.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(couriers.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(grffile.sty)
Requires:       tex(helvet.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lineno.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(multirow.sty)
Requires:       tex(natbib.sty)
Requires:       tex(pdflscape.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(pgfgantt.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(placeins.sty)
Requires:       tex(setspace.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tabulary.sty)
Requires:       tex(tikz.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(feupphdteses.sty) = %{tl_version}

%description -n texlive-feupphdteses
A complete template for thesis/works of Faculdade de Engenharia da Universidade
do Porto (FEUP) Faculty of Engineering University of Porto.

%package -n texlive-hyphen-portuguese
Summary:        Portuguese hyphenation patterns.
Version:        svn74203
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-pt.ec.tex) = %{tl_version}
Provides:       tex(hyph-pt.tex) = %{tl_version}
Provides:       tex(loadhyph-pt.tex) = %{tl_version}

%description -n texlive-hyphen-portuguese
Hyphenation patterns for Portuguese in T1/EC and UTF-8 encodings.

%package -n texlive-latex-via-exemplos
Summary:        A LaTeX course written in Brazilian Portuguese language
Version:        svn77105
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-via-exemplos-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-via-exemplos-doc <= 11:%{version}

%description -n texlive-latex-via-exemplos
This is a LaTeX2e course written in Brazilian Portuguese language.

%package -n texlive-latexcheat-ptbr
Summary:        A LaTeX cheat sheet, in Brazilian Portuguese
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latexcheat-ptbr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latexcheat-ptbr-doc <= 11:%{version}

%description -n texlive-latexcheat-ptbr
This is a translation to Brazilian Portuguese of Winston Chang's LaTeX cheat
sheet

%package -n texlive-lshort-portuguese
Summary:        Introduction to LaTeX in Portuguese
Version:        svn55643
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-portuguese-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-portuguese-doc <= 11:%{version}

%description -n texlive-lshort-portuguese
This is the Portuguese translation of A Short Introduction to LaTeX2e.

%package -n texlive-numberpt
Summary:        Counters spelled out in Portuguese
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(numberpt.sty) = %{tl_version}

%description -n texlive-numberpt
This packages defines commands to display counters spelled out in Portuguese.
The styles are \numberpt for "all lowercase" \Numberpt for "First word
capitalized" \NumberPt for "All Capitalized" \NUMBERPT for "ALL UPPERCASE" For
example, \renewcommand{\thechapter}{\NumberPt{chapter}} makes chapter titles to
be rendered as "Capitulo Um", "Capitulo Dois" etc. Options are offered to
select variations in the spelling of "14", or Brazilian vs. European Portuguese
forms in the spelling of "16", "17", and "19". The package requires expl3 and
xparse.

%package -n texlive-ordinalpt
Summary:        Counters as ordinal numbers in Portuguese
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ordinalpt.sty) = %{tl_version}

%description -n texlive-ordinalpt
The package provides a counter style (like \arabic, \alph and others) which
produces as output strings like "primeiro" ("first" in Portuguese), "segundo"
(second), and so on up to 1999th. Separate counter commands are provided for
different letter case variants, and for masculine and feminine gender
inflections.

%package -n texlive-ptlatexcommands
Summary:        LaTeX to commands in Portuguese
Version:        svn67125
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algorithm.sty)
Requires:       tex(algorithmic.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(PTLatexCommands.sty) = %{tl_version}

%description -n texlive-ptlatexcommands
This package transforms common commands used in LaTeX to commands in
Portuguese.

%package -n texlive-tabularray-abnt
Summary:        An ABNT (Brazilian standard) theme for tabularray
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(float.sty)
Requires:       tex(tabularray.sty)
Provides:       tex(tabularray-abnt-2025A.sty) = %{tl_version}
Provides:       tex(tabularray-abnt.sty) = %{tl_version}

%description -n texlive-tabularray-abnt
This is the abnt Brazilian standard style for tabularray. It provides the
themes abnt (for tables with numerical data) and quadro (for tables with text
information). Additional environments abnttblr, tallabnttblr, and longabnttblr
are wrappers to tblr, talltblr, and longtblr that apply the abnt theme
automatically and permit to set the table font using \SetAbntTblrFont{}
provided here.

%package -n texlive-xypic-tut-pt
Summary:        A tutorial for XY-pic, in Portuguese
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xypic-tut-pt-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xypic-tut-pt-doc <= 11:%{version}

%description -n texlive-xypic-tut-pt
A tutorial for XY-pic, in Portuguese

%post -n texlive-hyphen-portuguese
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/portuguese.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "portuguese loadhyph-pt.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=portuges.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=portuges" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{portuguese}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{portuguese}{loadhyph-pt.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{portuges}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{portuges}{loadhyph-pt.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-portuguese
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/portuguese.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=portuges.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{portuguese}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{portuges}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-portuges
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-portuges/
%doc %{_texmf_main}/doc/generic/babel-portuges/

%files -n texlive-beamer-tut-pt
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/beamer-tut-pt/

%files -n texlive-cursolatex
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/cursolatex/

%files -n texlive-feupphdteses
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/feupphdteses/
%doc %{_texmf_main}/doc/latex/feupphdteses/

%files -n texlive-hyphen-portuguese
%license bsd.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-latex-via-exemplos
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-via-exemplos/

%files -n texlive-latexcheat-ptbr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latexcheat-ptbr/

%files -n texlive-lshort-portuguese
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-portuguese/

%files -n texlive-numberpt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/numberpt/
%doc %{_texmf_main}/doc/latex/numberpt/

%files -n texlive-ordinalpt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ordinalpt/
%doc %{_texmf_main}/doc/latex/ordinalpt/

%files -n texlive-ptlatexcommands
%license mit.txt
%{_texmf_main}/tex/latex/ptlatexcommands/
%doc %{_texmf_main}/doc/latex/ptlatexcommands/

%files -n texlive-tabularray-abnt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tabularray-abnt/
%doc %{_texmf_main}/doc/latex/tabularray-abnt/

%files -n texlive-xypic-tut-pt
%license gpl2.txt
%doc %{_texmf_main}/doc/generic/xypic-tut-pt/

%changelog
%autochangelog
