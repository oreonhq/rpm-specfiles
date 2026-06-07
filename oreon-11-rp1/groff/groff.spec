%global source0_hash none

%{!?with_x:%global with_x 1}

Summary: A document formatting system
Name: groff
Version: 1.23.0
Release: 12%{?dist}
# Everything is under GPL-3.0-or-later, except for the following files:
# MIT license
#  -- tmac/hyphen.den
#     tmac/hyphen.det
# GFDL license
#  -- contrib/mom/momdoc/*
#     contrib/pdfmark/pdfmark.ms
#     contrib/pdfmark/pdfroff.1.man
#     contrib/hdtbl/groff_hdtbl.7.man
#     tmac/groff_trace.7.man
#     src/roff/groff/groff.1.man
#     src/roff/troff/troff.1.man
#     man/groff_diff.7.man
#     man/ditroff.7.man
#     man/groff_out.5.man
#     man/groff_tmac.5.man
#     man/groff.7.man
#     man/roff.7.man
#     doc/fdl.texi
#     doc/groff.texi
# BSD-4-Clause-UC
#  -- tmac/doc.tmac
#     tmac/doc-old.tmac
#     tmac/doc-common
#     tmac/doc-ditroff
#     tmac/doc-nroff
#     tmac/doc-syms
#     tmac/groff_mdoc.man
#     tmac/e.tmac
#     tmac/groff_me.man
#     doc/meintro.me
#     doc/meintro_fr.me
#     doc/meref.me
# X11 license
#  -- src/devices/xditview/*
# Public domain
#  -- src/preproc/grn
#     contrib/grap2graph/grap2graph.sh
#     contrib/pic2graph/pic2graph.sh
#     contrib/eqn2graph/eqn2graph.sh
License: GPL-3.0-or-later AND GFDL-1.3-or-later AND BSD-4-Clause-UC AND MIT AND X11 AND LicenseRef-Public-Domain
URL: http://www.gnu.org/software/groff/

Provides: nroff-i18n = %{version}-%{release}
Provides: bundled(gnulib)

Source:        https://mirrors.kernel.org/gnu/groff/groff-%{version}.tar.gz

# resolves: #530788
Patch0:        0001-missing-groff-x11-info-message-when-gxditview-not-fo.patch
Patch1:        0002-load-site-font-and-site-tmac-from-etc-groff.patch
# resolves: #709413, #720058, #720057
Patch2:        0003-various-security-fixes.patch
# resolves: #987069
Patch3:        0004-don-t-use-usr-bin-env-in-shebang.patch
# allow to specify custom docdir
Patch4:        0005-do-not-overwrite-docdir.patch
# Revert upstream change of mapping special characters for UTF-8 devices
# Debian commit: https://salsa.debian.org/debian/groff/-/commit/d5394c68d70e6c5199b01d2522e094c8fd52e64e
Patch5:        0006-Revert-upstream-change-of-mapping-special-characters.patch

Requires: coreutils, groff-base = %{version}-%{release}

Recommends: psutils

Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
Requires(preun): /usr/sbin/update-alternatives

BuildRequires: gcc, gcc-c++
BuildRequires: bison, texinfo
# psutils is required for the "psselect" command
BuildRequires: git, netpbm-progs, perl-generators, psutils, ghostscript

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\([^.]*\\.pl\\)

%description
Groff is a document formatting system. Groff takes standard text and
formatting commands as input and produces formatted output. The
created documents can be shown on a display or printed on a printer.
Groff's formatting commands allow you to specify font type and size,
bold type, italic type, the number and size of columns on a page, and
more.

Groff can also be used to format man pages. If you are going to use
groff with the X Window System, you will also need to install the
groff-x11 package.

%package base
Summary: Parts of the groff formatting system required to display manual pages
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
Requires(preun): /usr/sbin/update-alternatives

%description base
The groff-base package contains only necessary parts of groff formatting
system which are required to display manual pages, and the groff's default
display device (PostScript).

%package perl
Summary: Parts of the groff formatting system that require Perl
Requires: groff-base = %{version}-%{release}

%description perl
The groff-perl package contains the parts of the groff text processor
package that require Perl. These include the afmtodit (font processor
for creating PostScript font files), groffer (tool for displaying groff
files), grog (utility that can be used to automatically determine groff
command-line options), chem (groff preprocessor for producing chemical
structure diagrams), mmroff (reference preprocessor) and roff2dvi
roff2html roff2pdf roff2ps roff2text roff2x (roff code converters).

%if %{with_x}
%package x11
Summary: Parts of the groff formatting system that require X Windows System
Requires: groff-base = %{version}-%{release}
BuildRequires: libXaw-devel, libXmu-devel
BuildRequires: make
Provides: groff-gxditview = %{version}-%{release}
Obsoletes: groff-gxditview < 1.20.1

%description x11
The groff-x11 package contains the parts of the groff text processor
package that require X Windows System. These include gxditview (display
groff intermediate output files on X Window System display) and
xtotroff (converts X font metrics into groff font metrics).
%endif

%package doc
Summary: Documentation for groff document formatting system
BuildArch: noarch
Requires: groff = %{version}-%{release}

%description doc
The groff-doc package includes additional documentation for groff
text processor package. It contains examples, documentation for PIC
language and documentation for creating PDF files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
git init
git config user.email groff-owner@fedoraproject.org
git config user.name "groff owner"
git add .
git commit -n -m "release %{version}"
git am %{patches}

for file in NEWS src/devices/grolbp/grolbp.1.man doc/webpage.ms \
                contrib/mm/*.man contrib/mom/examples/{README.txt,*.mom,mom.vim}; do
    iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
    mv "${file}_" "$file"
done

%build
%configure \
    --docdir=%{_pkgdocdir} \
    --with-appdefdir=%{_datadir}/X11/app-defaults \
    --with-grofferdir=%{_datadir}/%{name}/%{version}/groffer
%make_build

%install
%make_install

# rename files for alternative usage
mv %{buildroot}%{_bindir}/soelim %{buildroot}%{_bindir}/soelim.%{name}
touch %{buildroot}%{_bindir}/soelim
mv %{buildroot}%{_mandir}/man1/soelim.1 %{buildroot}%{_mandir}/man1/soelim.%{name}.1
touch %{buildroot}%{_mandir}/man1/soelim.1
mv %{buildroot}%{_mandir}/man7/roff.7 %{buildroot}%{_mandir}/man7/roff.%{name}.7
touch %{buildroot}%{_mandir}/man7/roff.7

# some binaries need alias with 'g' or 'z' prefix
for file in g{nroff,troff,tbl,pic,eqn,neqn,refer,lookbib,indxbib,soelim} zsoelim; do
    ln -s ${file#?} %{buildroot}%{_bindir}/${file}
    ln -s ${file#?}.1.gz %{buildroot}%{_mandir}/man1/${file}.1.gz
done

# fix absolute symlink to relative symlink
rm -f %{buildroot}%{_pkgdocdir}/pdf/mom-pdf.pdf
ln -s ../examples/mom/mom-pdf.pdf %{buildroot}%{_pkgdocdir}/pdf/mom-pdf.pdf

# rename groff downloadable postscript fonts to meet Fedora Font Packaging guidelines,
# as these files are more PS instructions, than general-purpose fonts (bz #477394)
for file in $(find %{buildroot}%{_datadir}/%{name}/%{version}/font/devps -name "*.pfa"); do
    mv ${file} ${file}_
done
sed --in-place 's/\.pfa$/.pfa_/' %{buildroot}%{_datadir}/%{name}/%{version}/font/devps/download

# remove unnecessary files
rm -f %{buildroot}%{_infodir}/dir

# remove CreationDate from documentation
pushd %{buildroot}%{_pkgdocdir}
    find -name "*.html" | xargs sed -i "/^<!-- CreationDate: /d"
    find -name "*.ps"   | xargs sed -i "/^%%%%CreationDate: /d"
popd

# /bin/sed moved to /usr/bin/sed in Fedora
sed --in-place 's|#! /bin/sed -f|#! /usr/bin/sed -f|' %{buildroot}%{_datadir}/groff/%{version}/font/devps/generate/symbol.sed

%pre
# remove alternativized files if they are not symlinks
[ -L %{_mandir}/man7/roff.7.gz ] || %{__rm} -f %{_mandir}/man7/roff.7.gz >/dev/null 2>&1 || :

%post
# set up the alternatives files
/usr/sbin/update-alternatives --install %{_mandir}/man7/roff.7.gz roff.7.gz %{_mandir}/man7/roff.%{name}.7.gz 300 \
    >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ]; then
    /usr/sbin/update-alternatives --remove roff.7.gz %{_mandir}/man7/roff.%{name}.7.gz >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ]; then
    if [ "$(readlink /etc/alternatives/roff.7.gz)" == "%{_mandir}/man7/roff.%{name}.7.gz" ]; then
        /usr/sbin/update-alternatives --set roff.7.gz %{_mandir}/man7/roff.%{name}.7.gz >/dev/null 2>&1 || :
    fi
fi

%pre base
# remove alternativized files if they are not symlinks
[ -L %{_bindir}/soelim ] || %{__rm} -f %{_bindir}/soelim >/dev/null 2>&1 || :
[ -L %{_mandir}/man1/soelim.1.gz ] || %{__rm} -f %{_mandir}/man1/soelim.1.gz >/dev/null 2>&1 || :

%post base
# set up the alternatives files
/usr/sbin/update-alternatives --install %{_bindir}/soelim soelim %{_bindir}/soelim.%{name} 300 \
    --slave %{_mandir}/man1/soelim.1.gz soelim.1.gz %{_mandir}/man1/soelim.%{name}.1.gz \
    >/dev/null 2>&1 || :

%preun base
if [ $1 -eq 0 ]; then
    /usr/sbin/update-alternatives --remove soelim %{_bindir}/soelim.%{name} >/dev/null 2>&1 || :
fi

%postun base
if [ $1 -ge 1 ]; then
    if [ "$(readlink /etc/alternatives/soelim)" == "%{_bindir}/soelim.%{name}" ]; then
        /usr/sbin/update-alternatives --set soelim %{_bindir}/soelim.%{name} >/dev/null 2>&1 || :
    fi
fi

%files
# data
%{_datadir}/%{name}/%{version}/font/devcp1047/
%{_datadir}/%{name}/%{version}/font/devdvi/
%{_datadir}/%{name}/%{version}/font/devlbp/
%{_datadir}/%{name}/%{version}/font/devlj4/
%{_datadir}/%{name}/%{version}/oldfont/
%{_datadir}/%{name}/%{version}/pic/
%{_datadir}/%{name}/%{version}/tmac/62bit.tmac
%{_datadir}/%{name}/%{version}/tmac/dvi.tmac
%{_datadir}/%{name}/%{version}/tmac/e.tmac
%{_datadir}/%{name}/%{version}/tmac/ec.tmac
%{_datadir}/%{name}/%{version}/tmac/hdmisc.tmac
%{_datadir}/%{name}/%{version}/tmac/hdtbl.tmac
%{_datadir}/%{name}/%{version}/tmac/lbp.tmac
%{_datadir}/%{name}/%{version}/tmac/lj4.tmac
%{_datadir}/%{name}/%{version}/tmac/m.tmac
%{_datadir}/%{name}/%{version}/tmac/me.tmac
%{_datadir}/%{name}/%{version}/tmac/mm.tmac
%{_datadir}/%{name}/%{version}/tmac/mm/
%{_datadir}/%{name}/%{version}/tmac/mmse.tmac
%{_datadir}/%{name}/%{version}/tmac/mom.tmac
%{_datadir}/%{name}/%{version}/tmac/ms.tmac
%{_datadir}/%{name}/%{version}/tmac/mse.tmac
%{_datadir}/%{name}/%{version}/tmac/om.tmac
%{_datadir}/%{name}/%{version}/tmac/pdfmark.tmac
%{_datadir}/%{name}/%{version}/tmac/refer-me.tmac
%{_datadir}/%{name}/%{version}/tmac/refer-mm.tmac
%{_datadir}/%{name}/%{version}/tmac/refer-ms.tmac
%{_datadir}/%{name}/%{version}/tmac/refer.tmac
%{_datadir}/%{name}/%{version}/tmac/s.tmac
%{_datadir}/%{name}/%{version}/tmac/spdf.tmac
%{_datadir}/%{name}/%{version}/tmac/trace.tmac
%{_datadir}/%{name}/%{version}/tmac/zh.tmac
# programs
%{_bindir}/addftinfo
%{_bindir}/eqn2graph
%{_bindir}/gdiffmk
%{_bindir}/grap2graph
%{_bindir}/grn
%{_bindir}/grodvi
%{_bindir}/grolbp
%{_bindir}/grolj4
%{_bindir}/hpftodit
%{_bindir}/indxbib
%{_bindir}/lkbib
%{_bindir}/lookbib
%{_bindir}/pdfroff
%{_bindir}/pfbtops
%{_bindir}/pic2graph
%{_bindir}/refer
%{_bindir}/tfmtodit
%{_mandir}/man1/addftinfo.*
%{_mandir}/man1/eqn2graph.*
%{_mandir}/man1/gdiffmk.*
%{_mandir}/man1/grap2graph.*
%{_mandir}/man1/grn.*
%{_mandir}/man1/grodvi.*
%{_mandir}/man1/grohtml.*
%{_mandir}/man1/grolbp.*
%{_mandir}/man1/grolj4.*
%{_mandir}/man1/hpftodit.*
%{_mandir}/man1/indxbib.*
%{_mandir}/man1/lkbib.*
%{_mandir}/man1/lookbib.*
%{_mandir}/man1/pdfroff.*
%{_mandir}/man1/pfbtops.*
%{_mandir}/man1/pic2graph.*
%{_mandir}/man1/refer.*
%{_mandir}/man1/tfmtodit.*
# compatibility symlinks
%{_bindir}/grefer
%{_bindir}/glookbib
%{_bindir}/gindxbib
%{_mandir}/man1/grefer.*
%{_mandir}/man1/glookbib.*
%{_mandir}/man1/gindxbib.*
# groff processor documentation
%{_mandir}/man5/*
%ghost %{_mandir}/man7/roff.7*
%{_mandir}/man7/*
%{_infodir}/groff.info*

%files base
%{!?_licensedir:%global license %%doc}
%license COPYING FDL LICENSES
%doc BUG-REPORT MORE.STUFF NEWS PROBLEMS
# configuration
%dir %{_sysconfdir}/groff/
%config(noreplace) %{_sysconfdir}/groff/*
# data
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/%{version}/
%dir %{_datadir}/%{name}/%{version}/font/
%dir %{_datadir}/%{name}/%{version}/tmac/
%{_datadir}/%{name}/current
%{_datadir}/%{name}/%{version}/eign
%{_datadir}/%{name}/%{version}/font/devascii/
%{_datadir}/%{name}/%{version}/font/devlatin1/
%{_datadir}/%{name}/%{version}/font/devps/
%{_datadir}/%{name}/%{version}/font/devutf8/
%{_datadir}/%{name}/%{version}/font/devhtml/
%{_datadir}/%{name}/%{version}/tmac/an-ext.tmac
%{_datadir}/%{name}/%{version}/tmac/an.tmac
%{_datadir}/%{name}/%{version}/tmac/andoc.tmac
%{_datadir}/%{name}/%{version}/tmac/composite.tmac
%{_datadir}/%{name}/%{version}/tmac/cp1047.tmac
%{_datadir}/%{name}/%{version}/tmac/cs.tmac
%{_datadir}/%{name}/%{version}/tmac/de.tmac
%{_datadir}/%{name}/%{version}/tmac/den.tmac
%{_datadir}/%{name}/%{version}/tmac/en.tmac
%{_datadir}/%{name}/%{version}/tmac/devtag.tmac
%{_datadir}/%{name}/%{version}/tmac/doc-old.tmac
%{_datadir}/%{name}/%{version}/tmac/doc.tmac
%{_datadir}/%{name}/%{version}/tmac/eqnrc
%{_datadir}/%{name}/%{version}/tmac/europs.tmac
%{_datadir}/%{name}/%{version}/tmac/fallbacks.tmac
%{_datadir}/%{name}/%{version}/tmac/fr.tmac
%{_datadir}/%{name}/%{version}/tmac/html-end.tmac
%{_datadir}/%{name}/%{version}/tmac/html.tmac
%{_datadir}/%{name}/%{version}/tmac/hyphen.cs
%{_datadir}/%{name}/%{version}/tmac/hyphen.den
%{_datadir}/%{name}/%{version}/tmac/hyphen.det
%{_datadir}/%{name}/%{version}/tmac/hyphen.fr
%{_datadir}/%{name}/%{version}/tmac/hyphen.sv
%{_datadir}/%{name}/%{version}/tmac/hyphen.en
%{_datadir}/%{name}/%{version}/tmac/hyphen.it
%{_datadir}/%{name}/%{version}/tmac/hyphenex.cs
%{_datadir}/%{name}/%{version}/tmac/hyphenex.en
%{_datadir}/%{name}/%{version}/tmac/ja.tmac
%{_datadir}/%{name}/%{version}/tmac/ptx.tmac
%{_datadir}/%{name}/%{version}/tmac/it.tmac
%{_datadir}/%{name}/%{version}/tmac/rfc1345.tmac
%{_datadir}/%{name}/%{version}/tmac/sanitize.tmac
%{_datadir}/%{name}/%{version}/tmac/sboxes.tmac
%{_datadir}/%{name}/%{version}/tmac/latin1.tmac
%{_datadir}/%{name}/%{version}/tmac/latin2.tmac
%{_datadir}/%{name}/%{version}/tmac/latin5.tmac
%{_datadir}/%{name}/%{version}/tmac/latin9.tmac
%{_datadir}/%{name}/%{version}/tmac/man.tmac
%{_datadir}/%{name}/%{version}/tmac/mandoc.tmac
%{_datadir}/%{name}/%{version}/tmac/mdoc.tmac
%{_datadir}/%{name}/%{version}/tmac/mdoc/
%{_datadir}/%{name}/%{version}/tmac/papersize.tmac
%{_datadir}/%{name}/%{version}/tmac/pdfpic.tmac
%{_datadir}/%{name}/%{version}/tmac/pic.tmac
%{_datadir}/%{name}/%{version}/tmac/ps.tmac
%{_datadir}/%{name}/%{version}/tmac/psatk.tmac
%{_datadir}/%{name}/%{version}/tmac/psold.tmac
%{_datadir}/%{name}/%{version}/tmac/pspic.tmac
%{_datadir}/%{name}/%{version}/tmac/sv.tmac
%{_datadir}/%{name}/%{version}/tmac/trans.tmac
%{_datadir}/%{name}/%{version}/tmac/troffrc
%{_datadir}/%{name}/%{version}/tmac/troffrc-end
%{_datadir}/%{name}/%{version}/tmac/tty-char.tmac
%{_datadir}/%{name}/%{version}/tmac/tty.tmac
%{_datadir}/%{name}/%{version}/tmac/www.tmac
# programs
%{_bindir}/eqn
%{_bindir}/groff
%{_bindir}/grops
%{_bindir}/grotty
%{_bindir}/neqn
%{_bindir}/nroff
%{_bindir}/pic
%{_bindir}/post-grohtml
%{_bindir}/pre-grohtml
%{_bindir}/preconv
%ghost %{_bindir}/soelim
%{_bindir}/soelim.%{name}
%{_bindir}/tbl
%{_bindir}/troff
%{_mandir}/man1/eqn.*
%{_mandir}/man1/groff.*
%{_mandir}/man1/grops.*
%{_mandir}/man1/grotty.*
%{_mandir}/man1/neqn.*
%{_mandir}/man1/nroff.*
%{_mandir}/man1/pic.*
%{_mandir}/man1/preconv.*
%ghost %{_mandir}/man1/soelim.1*
%{_mandir}/man1/soelim.%{name}.*
%{_mandir}/man1/tbl.*
%{_mandir}/man1/troff.*
# compatibility symlinks
%{_bindir}/gnroff
%{_bindir}/gtroff
%{_bindir}/gtbl
%{_bindir}/gpic
%{_bindir}/geqn
%{_bindir}/gneqn
%{_bindir}/gsoelim
%{_bindir}/zsoelim
%{_mandir}/man1/gnroff.*
%{_mandir}/man1/gtroff.*
%{_mandir}/man1/gtbl.*
%{_mandir}/man1/gpic.*
%{_mandir}/man1/geqn.*
%{_mandir}/man1/gneqn.*
%{_mandir}/man1/gsoelim.*
%{_mandir}/man1/zsoelim.*

%files perl
# data
%{_datadir}/%{name}/%{version}/font/devpdf/
%{_datadir}/%{name}/%{version}/tmac/pdf.tmac
# programs
%{_bindir}/afmtodit
%{_bindir}/chem
%{_bindir}/gperl
%{_bindir}/gpinyin
%{_bindir}/glilypond
%{_bindir}/grog
%{_bindir}/gropdf
%{_bindir}/mmroff
%{_bindir}/pdfmom
%{_mandir}/man1/afmtodit.*
%{_mandir}/man1/chem.*
%{_mandir}/man1/gperl.*
%{_mandir}/man1/gpinyin.*
%{_mandir}/man1/glilypond.*
%{_mandir}/man1/grog.*
%{_mandir}/man1/gropdf.*
%{_mandir}/man1/mmroff.*
%{_mandir}/man1/pdfmom.*

%if %{with_x}
%files x11
# data
%{_datadir}/%{name}/%{version}/font/devX*/
%{_datadir}/%{name}/%{version}/tmac/X.tmac
%{_datadir}/%{name}/%{version}/tmac/Xps.tmac
%{_datadir}/X11/app-defaults/GXditview
%{_datadir}/X11/app-defaults/GXditview-color
%{_datadir}/%{name}/%{version}/font/FontMap-X11
# programs
%{_bindir}/gxditview
%{_bindir}/xtotroff
%{_mandir}/man1/gxditview.*
%{_mandir}/man1/xtotroff.*
%endif

%files doc
%doc %{_pkgdocdir}/*.me
%doc %{_pkgdocdir}/*.ps
%doc %{_pkgdocdir}/*.ms
%doc %{_pkgdocdir}/groff*
%doc %{_pkgdocdir}/me-revisions
%doc %{_pkgdocdir}/automake.pdf
%doc %{_pkgdocdir}/examples/
%doc %{_pkgdocdir}/html/
%doc %{_pkgdocdir}/pdf/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.23.0-12
- Import
