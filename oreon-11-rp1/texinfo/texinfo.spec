%global source0_hash none

%global tex_texinfo %{_datadir}/texlive/texmf-dist/tex/texinfo

Summary: Tools needed to create Texinfo format documentation files
Name: texinfo
Version: 7.3
Release: 1%{?dist}
License: GPL-3.0-or-later
Url: http://www.gnu.org/software/texinfo/
Source0:        ftp://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.xz.sig
Source2: fix-info-dir
# Patch0: we need to fix template fix-info-dir generates
Patch0: info-6.5-sync-fix-info-dir.patch
# Patch1: rhbz#1592433, bug in fix-info-dir --delete
Patch1: texinfo-6.5-fix-info-dir.patch
# Patch3: fixes issues detected by static analysis
Patch3: texinfo-7.1-various-sast-fixes.patch
# Patch4: fixes issues detected by static analysis
Patch4: texinfo-7.1-make-tainted-data-safe.patch
# Patch5: add support for zstd compression
Patch5: texinfo-6.7-zstd-compression.patch
# Patch6: include limits header
Patch6: texinfo-7.3-limits.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-generators
BuildRequires: ncurses-devel, help2man, perl(Data::Dumper)
BuildRequires: perl(Locale::Messages), perl(Unicode::EastAsianWidth), perl(Text::Unidecode)
BuildRequires: perl(Storable), perl(Unicode::Normalize), perl(File::Copy)

# Texinfo perl packages are not installed in default perl library dirs
%global __provides_exclude ^perl\\(.*Texinfo.*\\)$
%global __requires_exclude ^perl\\(.*Texinfo.*\\)$

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. The GNU
Project uses the Texinfo file format for most of its documentation.

Install texinfo if you want a documentation system for producing both
online and print documentation from the same source file and/or if you
are going to write documentation for the GNU Project.

%package -n info
Summary: A stand-alone TTY-based reader for GNU texinfo documentation
Provides: /sbin/install-info

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. The info package provides a standalone TTY-based
browser program for viewing texinfo files.

%package tex
Summary: Tools for formatting Texinfo documentation files using TeX
Requires: texinfo = %{version}-%{release}
Requires: tex(tex) tex(epsf.tex)
Requires: /usr/bin/cmp
Requires: /usr/bin/diff
Requires(post): %{_bindir}/texconfig-sys
Requires(postun): %{_bindir}/texconfig-sys
Provides: tex-texinfo
Provides: texlive-texinfo
Obsoletes: texlive-texinfo <= 9:2019-15

%description tex
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. The GNU
Project uses the Texinfo file format for most of its documentation.

The texinfo-tex package provides tools to format Texinfo documents
for printing using TeX.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
mkdir contrib
install -Dpm0755 -t contrib %{SOURCE2}
%autopatch -p1

%build
%configure --with-external-Text-Unidecode \
           --with-external-libintl-perl \
           --with-external-Unicode-EastAsianWidth \
           --disable-perl-xs
%make_build

%install
%make_install

mkdir -p %{buildroot}%{tex_texinfo}
install -p -m644 doc/texinfo.tex doc/txi-??.tex %{buildroot}%{tex_texinfo}

install -Dpm0755 -t %{buildroot}%{_sbindir} contrib/fix-info-dir

%find_lang %{name}
%find_lang %{name}_document

%check
#export ALL_TESTS=yes
#%make_build check

%post tex
%{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun tex
%{_bindir}/texconfig-sys rehash 2> /dev/null || :

%transfiletriggerin -n info -- %{_infodir}
[ -f %{_infodir}/dir ] && create_arg="" || create_arg="--create"
%{_sbindir}/fix-info-dir $create_arg %{_infodir}/dir &>/dev/null || :

%transfiletriggerpostun -n info -- %{_infodir}
[ -f %{_infodir}/dir ] && %{_sbindir}/fix-info-dir --delete %{_infodir}/dir &>/dev/null || :

%files -f %{name}.lang -f %{name}_document.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/makeinfo
%{_bindir}/texi2any
%{_bindir}/pod2texi
%{_datadir}/texinfo
%{_datadir}/texi2any
%{_infodir}/texinfo*
%{_infodir}/texi2any_api.info*
%{_infodir}/texi2any_internals.info*
%{_mandir}/man1/makeinfo.1*
%{_mandir}/man5/texinfo.5*
%{_mandir}/man1/texi2any.1*
%{_mandir}/man1/pod2texi.1*

%files -n info
%license COPYING
%{_bindir}/info
%{_infodir}/info-stnd.info*
%{_sbindir}/install-info
%{_sbindir}/fix-info-dir
%{_mandir}/man1/info.1*
%{_mandir}/man1/install-info.1*
%{_mandir}/man5/info.5*
%ghost %{_infodir}/dir
%ghost %attr(644, root, root) %{_infodir}/dir.old

%files tex
%{_bindir}/texindex
%{_bindir}/texi2dvi
%{_bindir}/texi2pdf
%{_bindir}/pdftexi2dvi
%{tex_texinfo}/
%{_mandir}/man1/texindex.1*
%{_mandir}/man1/texi2dvi.1*
%{_mandir}/man1/texi2pdf.1*
%{_mandir}/man1/pdftexi2dvi.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.3-1
- Prepare for Oreon 11 (RP1)
