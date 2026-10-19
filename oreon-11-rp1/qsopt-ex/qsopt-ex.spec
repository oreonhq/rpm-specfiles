%global source0_hash 2057309accfe27fee553090e19f0c051a101e393a758cc31549e194a88bf0fbe
%global commit  e5d498fde468e4669a3fbc4736e5d3b878e8c148
%global date    20170729
%global forgeurl https://github.com/jonls/qsopt-ex
Name:           qsopt-ex
Version:        2.5.10.3
Summary:        Exact linear programming solver
%forgemeta
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Release:        1%{?dist}
URL:            https://www.math.uwaterloo.ca/~bico/qsopt/ex/
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          %{name}-free-warning.patch
Patch:          %{name}-silence-mempool-log.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
QSopt_ex is an exact linear programming solver.  This is a fork of the version
originally released by Daniel Espinoza et al.  The goal of the fork is to
update the software, and in particular the build system, to be more friendly.
 In addition, the external dependencies have been reduced.

%package        libs
Summary:        Exact linear programming solver library
%description    libs
This package contains a library interface to the QSopt_ex exact linear
programming solver.

%package        devel
Summary:        Development files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
This package contains header files and library links for developing
applications that use QSopt_ex.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%conf
# Update obsolete macros
sed -i '/AC_HEADER_STDC/d;/AC_HEADER_TIME/d;/AC_TYPE_SIGNAL/d' configure.ac
sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' configure.ac
autoupdate -f

# Generate the configure script
autoreconf -fiv .

%build

%configure --disable-debug --disable-static --enable-shared
%make_build
help2man -N --version-string=%{version} --no-discard-stderr esolver/esolver \
  -n 'Exact linear programming solver' > esolver.1
%install
%make_install
mv %{buildroot}%{_bindir}/esolver %{buildroot}%{_bindir}/qsopt-ex-esolver
mkdir -p %{buildroot}%{_mandir}/man1
sed -e 's/esolver/qsopt-ex-&/g;s/ESOLVER/QSOPT-EX-&/g' \
    -e 's/Using QSopt_ex.*/Exact Mixed Integer Linear Solver/' \
    esolver.1 > %{buildroot}%{_mandir}/man1/qsopt-ex-esolver.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n qsopt-ex-libs -f %{oreon_filedir}/qsopt-ex-libs.list
%files -n qsopt-ex-devel -f %{oreon_filedir}/qsopt-ex-devel.list

%changelog

%autochangelog
