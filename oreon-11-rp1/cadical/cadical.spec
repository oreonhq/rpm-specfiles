%global source0_hash 16d24cc143632b9990a3fbe062e2858d5dd9599a0f369dc02a40c2a76036f931
%global giturl  https://github.com/arminbiere/cadical
Name:           cadical
Epoch:          1
Version:        3.0.1
Release:        1%{?dist}
Summary:        Simplified SAT solver
License:        MIT
URL:            http://fmv.jku.at/cadical/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/rel-%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-shared.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  drat-trim-tools
BuildRequires:  gcc-c++
BuildRequires:  glibc-langpack-en
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
CaDiCaL is a simplified Satisfiability solver.  The goal of the development of
CaDiCaL is to obtain a CDCL solver, which is easy to understand and change,
while at the same time not being much slower than other state-of-the-art CDCL
solvers.

%package libs
Summary:        Simplified SAT solver library
%description libs
This package contains the CaDiCaL simplified Satisfiability solver as a
library, for use in applications that need a SAT solver.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
Library links and header files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-rel-%{version}
%oreon_prep
%build

CXXFLAGS="%{build_cxxflags} -fPIC" ./configure -shared
sed -i "s|@LDFLAGS@|%{build_ldflags}|" build/makefile
%make_build
export LD_LIBRARY_PATH=$PWD/build
help2man --version-string=%{version} -N -o cadical.1 \
  -n 'Simplified SAT solver' build/cadical
help2man --version-string=%{version} -N -o mobical.1 -h -h \
  -n 'Model Based Tester for CaDiCaL' build/mobical
%install
mkdir -p %{buildroot}%{_bindir}
cp -p build/{cad,mob}ical %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
cp -p build/libcadical.so.0.0.0 %{buildroot}%{_libdir}
ln -s libcadical.so.0.0.0 %{buildroot}%{_libdir}/libcadical.so.0
ln -s libcadical.so.0 %{buildroot}%{_libdir}/libcadical.so
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -p src/*.{h,hpp} %{buildroot}%{_includedir}/%{name}
ln -s %{name}/cadical.hpp %{buildroot}%{_includedir}
ln -s %{name}/ccadical.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p *.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles cadical-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cadical-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

sed -i '/make -C \$CADICALBUILD/d;/^make$/d' test/*/run.sh
sed -i 's/ mbt$//' test/makefile
export LD_LIBRARY_PATH=$PWD/build
make -C test
%files -f %{oreon_filedir}/main.list
%files -n cadical-libs -f %{oreon_filedir}/cadical-libs.list
%files -n cadical-devel -f %{oreon_filedir}/cadical-devel.list

%changelog

%autochangelog
