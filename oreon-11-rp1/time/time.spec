%global source0_hash none

%global source2_key_fpr F576AAAC1B0FF849792D8CB129A794FD2272BC86

Summary:    A GNU utility for monitoring a program's use of system resources
Name:       time
Version:    1.9
Release:    28%{?dist}
# src/time.c:               GPL-3.0-or-later
# COPYING:                  GPL-3.0 text
# doc/time.texi:            GFDL-1.3-no-invariants-or-later
# doc/fdl.texi:             GFDL-1.3 text
# doc/time.info:            GFDL-1.3-no-invariants-or-later
# lib/stdnoreturn.in.h:     GPL-3.0-or-later
# lib/strerror-override.c:  GPL-3.0-or-later
# lib/error.h:              GPL-3.0-or-later
## Not in a binary package
# tests/init.sh:            GPL-3.0-or-later
# INSTALL:                  FSFAP
# configure:                FSFUL
# build-aux/config.guess:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/install-sh:     X11 AND LicenseRef-Fedora-Public-Domain
# build-aux/config.rpath:   FSFULLR
# build-aux/test-driver:    GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/update-copyright:   GPL-3.0-or-later
# build-aux/useless-if-before-free: GPL-3.0-or-later
# build-aux/vc-list-files:  GPL-3.0-or-later
# build-aux/missing:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/compile:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/config.sub:     GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/gitlog-to-changelog:    GPL-3.0-or-later
# build-aux/git-version-gen:        GPL-3.0-or-later
# build-aux/texinfo.tex:    GPL-3.0-or-later WITH Texinfo-exception AND GPL-1.0-or-later
# build-aux/depcomp:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/mdate-sh:       GPL-2.0-or-later WITH Autoconf-exception-generic
# GNUmakefile:              GPL-3.0-or-later
# m4/asm-underscore.m4:     FSFULLR
# m4/gnulib-cache.m4:       GPL-3.0-or-later WITH Autoconf-exception-generic
#                           (Waiting on an approval
#                           <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/473?)
# m4/host-cpu-c-abi.m4:     FSFULLR
# m4/longlong.m4:           FSFULLR
# m4/ssize_t.m4:            FSFULLR
# m4/stdnoreturn.m4:        FSFULLR
# maint.mk:                 GPL-3.0-or-later
# tests/time-posix-quiet.sh:    GPL-3.0-or-later
License:    GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later
SourceLicense: %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Texinfo-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-1.0-or-later AND X11 AND FSFAP AND FSFUL AND FSFULLR AND LicenseRef-Fedora-Public-Domain
Url:        https://www.gnu.org/software/%{name}/
Source0:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
# Obtained from a key server
Source2:        gpgkey-F576AAAC1B0FF849792D8CB129A794FD2272BC86.gpg
# Fix measuring time when a clock experiences a jump, bug #1004416,
# <http://lists.gnu.org/archive/html/bug-gnu-utils/2013-09/msg00003.html>
Patch0:        time-1.8-Prefer-clock_gettime-CLOCK_MONOTONIC.patch
# Fix info directory entry
Patch1:        time-1.9-Improve-info-directory-index-entry-description.patch
# Clarify RSS size as kibibytes in a documentation, proposed to an upstream,
# <https://lists.gnu.org/archive/html/bug-time/2020-07/msg00000.html>
Patch2:        time-1.9-Use-kibibytes-instead-of-kilobytes-in-a-documentatio.patch
# Do not leak a file descriptor of the --output argument to a command,
# proposed to an upstream,
# <https://lists.gnu.org/archive/html/bug-time/2020-11/msg00001.html>
Patch3:        time-1.9-Close-outfp-before-exec.patch
# The time-max-rss.sh test randomly fails( mallocating 5 MB more does not have
# to increase RSS in 5 MB). In addition there is regression in ppc64le kernel
# (bug #2212765) which always fails.
Patch4:        time-1.9-drop-flawed-rss-test.patch
# Fix formatting a trailing backslash, proposed to the upstream,
# <https://lists.gnu.org/archive/html/bug-time/2024-01/msg00000.html>
Patch5:        time-1.9-Fix-formatting-a-trailing-backslash-and-a-percent-si.patch
# Fixes compiler error that occured after the switch to GCC15
# <https://lists.gnu.org/archive/html/bug-time/2025-01/msg00000.html>
Patch6:        time-1.9-Fix-compiling-with-GCC15.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  texinfo

%description
The GNU time utility runs another program, collects information about
the resources used by that program while it is running, and displays
the results.

%prep
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Set time stamp stored in an info page to the latest patch
touch -d "$(sed -n -e '/^Date: /{s/^[^:]*: //;p}' %{PATCH2})" doc/time.texi
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
# Correct version VERSION flag for doc/time.texi
# <https://lists.gnu.org/archive/html/bug-time/2021-01/msg00000.html>
printf '%{version}\n' > .tarball-version
autoreconf -fi

%build
%configure
%{make_build}

%install
%{make_install}
# Remove info index, it's updated by file triggers
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%check
%{make_build} check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/time
%{_infodir}/time.info*
# time(1) manual page lives in man-pages package, bug #1612294.

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9-28
- Prepare for Oreon 11 (RP1)
