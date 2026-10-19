%global source0_hash 2b05cff7de5d7b646dc1669bc36c35fdac02ac6ae4b6c19cb3340d87ec553a9a
Summary:        The GNU shar utilities for packaging and unpackaging shell archives
Name:       sharutils
Version:    4.15.2
Release:        31%{?dist}
License:    GPL-3.0-or-later AND (GPL-3.0-or-later AND BSD-4-Clause) AND (LGPL-3.0-or-later OR BSD-3-Clause) AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain AND GFDL-1.3-or-later
SourceLicense:  %{license} AND GPL-2.0-or-later AND FSFULLR AND FSFAP AND MIT
Source0:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.xz
Patch0:     %{name}-4.14.2-Pass-compilation-with-Werror-format-security.patch
Patch1:     %{name}-4.15.2-Fix-a-heap-buffer-overflow-in-find_archive.patch
Patch2:     %{name}-4.15.2-fflush-adjust-to-glibc-2.28-libio.h-removal.patch
Patch3:     %{name}-4.15.2-Fix-building-with-GCC-10.patch
Patch4:     %{name}-4.15.2-Do-not-include-lib-md5.c-into-src-shar.c.patch
Patch5:     %{name}-4.15.2-ISO-C23-Backport-stdbool.m4-from-gnulib-devel-0-52.2.patch
Patch6:     %{name}-4.15.2-ISO-C23-Port-getcwd.m4-to-ISO-C23.patch
Patch7:     %{name}-4.15.2-ISO-C23-Port-the-code-to-ISO-C23.patch
URL:        http://www.gnu.org/software/%{name}/
Provides:           bundled(gnulib)
Provides:           bundled(libopts) = 41.1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
The sharutils package contains the GNU shar utilities, a set of tools for
encoding and decoding packages of files (in binary or text format) in
a special plain text format called shell archives (shar).  This format can be
sent through e-mail (which can be problematic for regular binary files).  The
shar utility supports a wide range of capabilities (compressing, uuencoding,
splitting long files for multi-part mailings, providing check-sums), which
make it very flexible at creating shar files.  After the files have been sent,
the unshar tool scans mail messages looking for shar files.  Unshar
automatically strips off mail headers and introductory text and then unpacks
the shar files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# convert TODO, THANKS to UTF-8
for i in TODO THANKS; do
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,}
  mv $i{.utf8,}
done

%build

autoreconf
%configure
%{make_build}
%install
%{make_install}
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
chmod 644 AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%find_lang %{name}
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.15.2-31
- Prepare for Oreon 11 (RP1)
