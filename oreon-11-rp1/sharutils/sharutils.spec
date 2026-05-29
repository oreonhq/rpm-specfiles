%global source0_hash none

Summary:    The GNU shar utilities for packaging and unpackaging shell archives
Name:       sharutils
Version:    4.15.2
Release:    31%{?dist}
# The main code:                GPL-3.0-or-later
# intl/dngettext.c:             LGPL-2.0-or-later
# lib (gnulib):                 GPL-3.0-or-later
# lib/md5.c:                    GPL-3.0-or-later and PLicenseRef-Fedora-Public-Domain
# libopts/file.c:               LGPL-3.0-or-later or BSD-3-Clause
# libopts/genshell.h:           LGPL-2.0-or-later
# libopts/m4/libopts.m4:        GPL-3.0-or-later
# doc/sharutils.texi:           GFDL-1.3-or-later
# src/uuencode.c:               GPL-3.0-or-later and BSD-4-Clause
## Not in the binary package
# ar-lib:                       GPL-2.0-or-later
# config.rpath:                 FSFULLR
# INSTALL:                      FSFAP
# install-sh:                   MIT
License:    GPL-3.0-or-later AND (GPL-3.0-or-later AND BSD-4-Clause) AND (LGPL-3.0-or-later OR BSD-3-Clause) AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain AND GFDL-1.3-or-later
SourceLicense:  %{license} AND GPL-2.0-or-later AND FSFULLR AND FSFAP AND MIT
Source:        https://ftp.gnu.org/gnu/sharutils/sharutils-4.15.2.tar.xz
# Pass compilation with -Werror=format-security, bug #1037323
Patch0:     %{name}-4.14.2-Pass-compilation-with-Werror-format-security.patch
# Fix CVE-2018-1000097 (a heap buffer overflow in find_archive()),
# bug #1548019,
# <http://lists.gnu.org/archive/html/bug-gnu-utils/2018-02/msg00004.html>
Patch1:     %{name}-4.15.2-Fix-a-heap-buffer-overflow-in-find_archive.patch
# Adapt bundled gnulib to glibc-2.28
Patch2:     %{name}-4.15.2-fflush-adjust-to-glibc-2.28-libio.h-removal.patch
# Fix building with GCC 10,
# <https://lists.gnu.org/archive/html/bug-gnu-utils/2020-01/msg00001.html>
Patch3:     %{name}-4.15.2-Fix-building-with-GCC-10.patch
# Fix building with GCC 10,
# <https://lists.gnu.org/archive/html/bug-gnu-utils/2020-01/msg00001.html>
Patch4:     %{name}-4.15.2-Do-not-include-lib-md5.c-into-src-shar.c.patch
# 1/3 Fix building with GCC 15, bug #2341343,
# <https://lists.gnu.org/archive/html/bug-gnu-utils/2025-03/msg00000.html>
Patch5:     %{name}-4.15.2-ISO-C23-Backport-stdbool.m4-from-gnulib-devel-0-52.2.patch
# 2/3 Fix building with GCC 15, bug #2341343,
Patch6:     %{name}-4.15.2-ISO-C23-Port-getcwd.m4-to-ISO-C23.patch
# 3/3 Fix building with GCC 15, bug #2341343,
Patch7:     %{name}-4.15.2-ISO-C23-Port-the-code-to-ISO-C23.patch
URL:        http://www.gnu.org/software/%{name}/
BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      binutils
BuildRequires:      coreutils
BuildRequires:      gcc
BuildRequires:      gettext
# glibc-common for iconv
BuildRequires:      glibc-common
BuildRequires:      make
BuildRequires:      sed
# Tests:
BuildRequires:      diffutils
Provides:           bundled(gnulib)
# See libopts/autoopts/options.h for OPTIONS_DOTTED_VERSION
Provides:           bundled(libopts) = 41.1

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

%check
make check

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/{shar,unshar,uudecode,uuencode}
%{_infodir}/sharutils.*
%{_mandir}/man1/{shar,unshar,uudecode,uuencode}.*
%{_mandir}/man5/uuencode.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.15.2-31
- Prepare for Oreon 11 (RP1)
