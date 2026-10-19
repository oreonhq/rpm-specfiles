%global source2_hash 76473da61013292011163ef3d8eef5d1207908f276e1aadc5958efdfb3123f4d
%global source1_hash 8de306e28ab46c303abea86d8f06b42aa3c6d4a08bab6752236f29e5642da177
%global source0_hash 1b81ba4e9a006ca8e6eb5cbbe4cf4f75dfc1fc9301b459aa0d40393e85590a0b
Summary:        A GNU program for formatting C code
Name:       indent
Version:    2.2.13
Release:        1%{?dist}
License:    GPL-3.0-or-later AND BSD-3-Clause AND BSD-4.3TAHOE AND Latex2e-translated-notice
URL:        https://www.gnu.org/software/%{name}/
Source0:        https://ftpmirror.gnu.org/%{name}/%{name}-%{version}.tar.xz
Source1:    https://ftpmirror.gnu.org/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://shadura.me/key.pgp
Patch0:     indent-2.2.13-Check-for-setlocale-function.patch
Patch1:     indent-2.2.13-Fix-an-out-of-buffer-read-in-search_brace-lexi-on-an.patch
Patch2:     indent-2.2.13-Fix-a-heap-buffer-overwrite-in-search_brace-CVE-2023.patch
Patch3:     indent-2.2.13-Fix-a-heap-buffer-underread-in-set_buf_break.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  texi2html
BuildRequires:  texinfo
# /oreon:deps
%description
Indent is a GNU program for beautifying C code, so that it is easier to
read.  Indent can also convert from one C writing style to a different
one.  Indent understands correct C syntax and tries to handle incorrect
C syntax.

Install the indent package if you are developing applications in C and
you want a program to format your code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Regenerate sources
rm src/gperf.c src/gperf-cc.c
# Regenerate documentation and translatations
rm man/indent.1 doc/indent.info po/*.gmo po/stamp-po
# Remove bundled and pregenerated build scripts
rm -r aclocal.m4 config configure m4 {,doc/,src/,man/}Makefile.in \
    po/Makefile.in.in po/*.sed po/*.sin po/Rules-quot

%build

autoreconf -i -f
%configure \
    --enable-largefile \
    --enable-nls \
    --disable-rpath
%{make_build}
%install
%{make_install}
rm -f %{buildroot}%{_infodir}/dir %{buildroot}%{_bindir}/texinfo2man \
    %{buildroot}%{_datadir}/doc/indent/indent.html
%find_lang %name
%oreon_autofiles main

%check

make check %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
