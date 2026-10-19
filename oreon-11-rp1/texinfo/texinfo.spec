%global source1_hash 946772924f2d0626b472eb1d4bf63675e846f38ab457738bd0d3e6fb7634faff
%global source0_hash 51f74eb0f51cfa9873b85264dfdd5d46e8957ec95b88f0fb762f63d9e164c72e
%global tex_texinfo %{_datadir}/texlive/texmf-dist/tex/texinfo
Summary:        Tools needed to create Texinfo format documentation files
Name: texinfo
Version: 7.3
Release:        1%{?dist}
License: GPL-3.0-or-later
Url: http://www.gnu.org/software/texinfo/
Source0:        https://mirrors.kernel.org/gnu/texinfo/texinfo-%{version}.tar.xz
Source1:        https://mirrors.kernel.org/gnu/texinfo/texinfo-%{version}.tar.xz.sig
Source2: fix-info-dir
Patch0: info-6.5-sync-fix-info-dir.patch
Patch1: texinfo-6.5-fix-info-dir.patch
Patch3: texinfo-7.1-various-sast-fixes.patch
Patch4: texinfo-7.1-make-tainted-data-safe.patch
Patch5: texinfo-6.7-zstd-compression.patch
Patch6: texinfo-7.3-limits.patch
%global __provides_exclude ^perl\\(.*Texinfo.*\\)$
%global __requires_exclude ^perl\\(.*Texinfo.*\\)$
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Locale::Messages)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Unicode::EastAsianWidth)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl-generators
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles info usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%post tex

%{_bindir}/texconfig-sys rehash 2> /dev/null || :
%postun tex

%{_bindir}/texconfig-sys rehash 2> /dev/null || :
%transfiletriggerin -n info -- %{_infodir}
[ -f %{_infodir}/dir ] && create_arg="" || create_arg="--create"
%{_sbindir}/fix-info-dir $create_arg %{_infodir}/dir &>/dev/null || :
%transfiletriggerpostun -n info -- %{_infodir}
[ -f %{_infodir}/dir ] && %{_sbindir}/fix-info-dir --delete %{_infodir}/dir &>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n info -f %{oreon_filedir}/info.list
%files -n texinfo-tex -f %{oreon_filedir}/texinfo-tex.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.3-1
- Prepare for Oreon 11 (RP1)
