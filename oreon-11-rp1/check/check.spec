# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a8de4e0bacfb4d76dd1c618ded263523b53b85d92a146d8835eb1a52932fa20a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           check
Version:        0.15.2
Release:        1%{?dist}
Summary:        A unit test framework for C
License:        LGPL-2.1-or-later AND GFDL-1.2-no-invariants-or-later
SourceLicense:  %{shrink:%{license}
                  AND BSD-3-Clause
                  AND checkmk
                  AND GPL-2.0-or-later
                  AND GPL-2.0-or-later WITH Autoconf-exception-macro
                  AND GPL-3.0-or-later WITH Autoconf-exception-macro
                }
URL:            https://libcheck.github.io/check/
Source0:        https://github.com/libcheck/check/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.11.0-info-in-builddir.patch
Patch1:         %{name}-0.15.2-texinfo.patch
Patch2:         %{name}-0.11.0-fp.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  texinfo

%description
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer.  Tests are
run in a separate address space, so Check can catch both assertion failures
and code errors that cause segmentation faults or other signals.  The output
from unit tests can be used within source code editors and IDEs.

%package devel
Summary:        Libraries and headers for developing programs with check
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-static%{?_isa} = %{version}-%{release}
Provides:       pkgconfig(check) = %{version}

%description devel
Libraries and headers for developing programs with check

%package static
Summary:        Static libraries of check
License:        LGPL-2.1-or-later

%description static
Static libraries of check.

%package checkmk
Summary:        Translate concise versions of test suites into C programs
License:        checkmk
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description checkmk
The checkmk binary translates concise versions of test suites into C programs
suitable for use with the Check unit test framework.

%prep
%oreon_sha256
%autosetup -p1

%conf
sed -e '/DECLS(\[a/s|)|,,,[AC_INCLUDES_DEFAULT\n[#include <time.h>\n #include <sys/time.h>]]&|' \
    -i configure.ac

sed -i 's/fgrep/grep -F/' Makefile.am

find . -name .cvsignore -delete

autoreconf -ivf

sed -i 's,set(libdir .*),set(libdir "%{_libdir}"),' CMakeLists.txt

%build
mkdir autotools_build
cd autotools_build
%global _configure ../configure
%configure

sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build
cd -

%cmake
%cmake_build

%install
cd autotools_build
%make_install
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_docdir}/%{name}
cd -

%cmake_install

sed -i 's/ -pthread//' %{buildroot}%{_libdir}/pkgconfig/check.pc

%check
cd autotools_build
export LD_LIBRARY_PATH=$PWD/src/.libs
make check
rm -rf checkmk/test/check_checkmk*
rm -rf checkmk/test/empty_input
cd -

%files
%doc AUTHORS NEWS
%license COPYING.LESSER
%{_libdir}/libcheck.so.0{,.*}
%{_infodir}/check*

%files devel
%doc doc/example
%{_includedir}/check.h
%{_includedir}/check_stdint.h
%{_libdir}/cmake/check/
%{_libdir}/libcheck.so
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4

%files static
%license COPYING.LESSER
%{_libdir}/libcheck.a

%files checkmk
%doc checkmk/README checkmk/examples
%doc checkmk/test
%{_bindir}/checkmk
%{_mandir}/man1/checkmk.1*

%changelog
%autochangelog
