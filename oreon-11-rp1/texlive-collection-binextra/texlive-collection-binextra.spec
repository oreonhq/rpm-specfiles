%global source0_hash 21e3f7cec40bed8bfa215c2f455b565cc69ae32e4a8cdb8e699b854170bdee00d21fb80c2f6f3a8723d9925de53af6728ebcace4b4c2905e6f432e669f54851a

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-binextra
Epoch:          12
Version:        svn77772
Release:        7%{?dist}
Summary:        TeX auxiliary programs

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 6eabd7281d79ff0ad19080350dfcca8ee3a33ddfa6d17827a7851cc53f09f627729c8d715a1dfe50e0c079add44331a07d543cb8b6a57000efa6d73c30f2ffe0
%global source3_hash c61bc0d70cadcc4382dae55cdc1af076882801321a2de16f164223267732e476e41f949f566808c928f446d69aa22bd9965adb155c97905e32b93808810c76c0
%global source4_hash f8cb6152ef1429684ebc92c37fc2fd414527ebf6d847d248f10dd50cb4e7d91f7bd0f7a5ba487dc5c5d87c288e7b5a862721985f4be983536666d58a9c3fcdb1
%global source5_hash 05ab867635e1a4a4970ce81ec01a4287822b5de6bf6fa9b4b54d939be49af559509d0889ef732c1e6e4938c4ca2e027574d51b8ea6448e2736f307b860e0002f
%global source6_hash 7e5310672cea8c86394cb61f2cf8c4930fb56070bfe12083a7cb1ee8b7ea6786c5582ec0f5ed95b1d4ec88eebb0e3035a446a9a846ad0a96533ac4256d5b1d27
%global source7_hash 2e66b1364c2fceecd750758c0c0348f9da7b7d490825d54a1dccf61e07a7d07ad1a62c9078e797b209570a946d643c926e92ff8bde5f8b0dfb36d1d66910dc39

Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/collection-binextra.tar.xz#/collection-binextra.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ctan_chk.tar.xz#/ctan_chk.or11.tar.xz
Source3:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/ctan_chk.doc.tar.xz#/ctan_chk.doc.or11.tar.xz
Source4:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/hook-pre-commit-pkg.tar.xz#/hook-pre-commit-pkg.or11.tar.xz
Source5:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/hook-pre-commit-pkg.doc.tar.xz#/hook-pre-commit-pkg.doc.or11.tar.xz
Source6:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xdvipsk-support.tar.xz#/xdvipsk-support.or11.tar.xz
Source7:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xdvipsk-support.doc.tar.xz#/xdvipsk-support.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-a2ping
Requires:       texlive-adhocfilelist
Requires:       texlive-arara
Requires:       asymptote
Requires:       texlive-bibtex8
Requires:       texlive-bibtexu
Requires:       texlive-bundledoc
Requires:       texlive-checklistings
Requires:       texlive-chklref
Requires:       texlive-chktex
Requires:       texlive-clojure-pamphlet
Requires:       texlive-cluttex
Requires:       texlive-collection-basic
Requires:       texlive-ctan-o-mat
Requires:       texlive-ctan_chk
Requires:       texlive-ctanbib
Requires:       texlive-ctanify
Requires:       texlive-ctanupload
Requires:       texlive-ctie
Requires:       texlive-cweb
Requires:       texlive-de-macro
Requires:       texlive-detex
Requires:       texlive-digestif
Requires:       texlive-dtl
Requires:       texlive-dtxgen
Requires:       texlive-dvi2tty
Requires:       texlive-dviasm
Requires:       texlive-dvicopy
Requires:       texlive-dvidvi
Requires:       texlive-dviinfox
Requires:       texlive-dviljk
Requires:       texlive-dviout-util
Requires:       texlive-dvipng
Requires:       texlive-dvipos
Requires:       texlive-dvisvgm
Requires:       texlive-easydtx
Requires:       texlive-expltools
Requires:       texlive-findhyph
Requires:       texlive-fragmaster
Requires:       texlive-git-latexdiff
Requires:       texlive-gsftopk
Requires:       texlive-hook-pre-commit-pkg
Requires:       texlive-installfont
Requires:       texlive-ketcindy
Requires:       texlive-l3sys-query
Requires:       texlive-lacheck
Requires:       texlive-latex-git-log
Requires:       texlive-latex-papersize
Requires:       texlive-latex2man
Requires:       texlive-latex2nemeth
Requires:       texlive-latexdiff
Requires:       texlive-latexfileversion
Requires:       texlive-latexindent
Requires:       latexmk
Requires:       texlive-latexpand
Requires:       texlive-light-latex-make
Requires:       texlive-listings-ext
Requires:       texlive-ltxfileinfo
Requires:       texlive-ltximg
Requires:       texlive-make4ht
Requires:       texlive-match_parens
Requires:       texlive-mflua
Requires:       texlive-mkjobtexmf
Requires:       texlive-optexcount
Requires:       texlive-patgen
Requires:       texlive-pdfbook2
Requires:       texlive-pdfcrop
Requires:       texlive-pdfjam
Requires:       texlive-pdflatexpicscale
Requires:       texlive-pdftex-quiet
Requires:       texlive-pdftosrc
Requires:       texlive-pdfxup
Requires:       texlive-pfarrei
Requires:       texlive-pkfix
Requires:       texlive-pkfix-helper
Requires:       texlive-ppmcheckpdf
Requires:       texlive-purifyeps
Requires:       texlive-pythontex
Requires:       texlive-runtexfile
Requires:       texlive-runtexshebang
Requires:       texlive-seetexk
Requires:       texlive-show-pdf-tags
Requires:       texlive-spix
Requires:       texlive-sqltex
Requires:       texlive-srcredact
Requires:       texlive-sty2dtx
Requires:       texlive-synctex
Requires:       texlive-tex4ebook
Requires:       texlive-texaccents
Requires:       texlive-texblend
Requires:       texlive-texcount
Requires:       texlive-texdef
Requires:       texlive-texdiff
Requires:       texlive-texdirflatten
Requires:       texlive-texdoc
Requires:       texlive-texdoctk
Requires:       texlive-texfot
Requires:       texlive-texlive-scripts-extra
Requires:       texlive-texliveonfly
Requires:       texlive-texloganalyser
Requires:       texlive-texlogfilter
Requires:       texlive-texlogsieve
Requires:       texlive-texosquery
Requires:       texlive-texplate
Requires:       texlive-texware
Requires:       texlive-tie
Requires:       texlive-tpic2pdftex
Requires:       texlive-typeoutfileinfo
Requires:       texlive-upmendex
Requires:       texlive-web
Requires:       texlive-xdvipsk
Requires:       texlive-xdvipsk-support
Requires:       texlive-xindex
Requires:       texlive-xindy
Requires:       texlive-xpdfopen

%description
Myriad additional TeX-related support programs. Includes programs and macros
for DVI file manipulation, literate programming, patgen, and plenty more.

%package -n texlive-ctan_chk
Summary:        CTAN guidelines verifier and corrector for uploading projects
Version:        svn36304
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ctan_chk-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ctan_chk-doc <= 11:%{version}

%description -n texlive-ctan_chk
Basic gawk program that uses CTAN's published guidelines for authors to help
eliminate sloppiness in uploaded files/projects. It is completely open for
users to program additional guidelines as well as CTAN's future adjustments.

%package -n texlive-hook-pre-commit-pkg
Summary:        Pre-commit git hook for LaTeX package developers
Version:        svn76790
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-hook-pre-commit-pkg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hook-pre-commit-pkg-doc <= 11:%{version}

%description -n texlive-hook-pre-commit-pkg
This package provides a pre-commit git hook to check basic LaTeX syntax for the
use of package developers. It is installed by copying it into the .git/.hooks
file. It then checks the following file types: .sty, .dtx, .bbx, .cbx, and
.lbx. List of performed checks: Each line must be terminated by a %, without a
space before it. Empty lines are allowed, but not lines with nothing but spaces
in them. \begin{macro} and \end{macro} must be paired. \begin{macrocode} and
\end{macrocode} must be paired. \begin{macro} must have a second argument. One
space must be printed between % and \begin{macro} or \end{macro}. % must be the
first character in the line. Four spaces must be printed between % and
\begin{macrocode} or \end{macrocode}. \cs argument must not start with a
backslash.

%package -n texlive-xdvipsk-support
Summary:        LuaLaTeX packages for the xdvipsk binary (dvips extension)
Version:        svn77772
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-xdvipsk
Requires:       tex(luatexbase.sty)
Provides:       tex(xdvipsk-support.sty) = %{tl_version}
Provides:       tex(xdvipsk.def) = %{tl_version}
Provides:       tex(xdvipskmaps.sty) = %{tl_version}

%description -n texlive-xdvipsk-support
This LaTeX package bundle offers support for xdvipsk, an extension of the dvips
binary. xdvipsk supports BMP, PCX, TIFF, JPEG, and PNG formats and performs
scaling, rotating, trim, and viewport operations like EPS images. The
xdvispk.def driver for the graphics package offers a LaTeX interface. However,
it lacks clipping, trimming, and viewport operations. The LuaLaTeX package
xdvipskmaps provides OpenType font support for xdvipsk. It generates map files
containing information about OpenType fonts used in DVI files.

%prep
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h_expected="%{source2_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h_expected="%{source3_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h_expected="%{source4_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h_expected="%{source5_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h_expected="%{source6_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
test "%{source7_hash}" = "none" || { f="%{SOURCE7}"; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h_expected="%{source7_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source7_hash}" || { echo "oreon: Source7 hash mismatch" >&2; exit 1; }; }
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-ctan_chk
%license gpl3.txt
%doc %{_texmf_main}/doc/support/ctan_chk/

%files -n texlive-hook-pre-commit-pkg
%license gpl3.txt
%doc %{_texmf_main}/doc/support/hook-pre-commit-pkg/

%files -n texlive-xdvipsk-support
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/xdvipsk-support/
%doc %{_texmf_main}/doc/lualatex/xdvipsk-support/

%changelog
%autochangelog
