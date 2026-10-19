%global source0_hash bfe93eaa6323b48011e4b1fcf74b3f2e20f9de544767e728009e5b2018296193
%global sover   0.0.0
%global majver  %(cut -d. -f1 <<< %{sover})
%global giturl  https://github.com/arminbiere/kissat
Name:           kissat
Version:        4.0.4
Release:        1%{?dist}
Summary:        Keep It Simple SAT solver
License:        MIT
URL:            http://fmv.jku.at/kissat/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/rel-%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-shared.patch
Patch:          %{name}-logical-not.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%global _desc %{expand:KISSAT is a "keep it simple and clean bare metal SAT solver" written in C.  It
is a port of CaDiCaL back to C with improved data structures, better
scheduling of inprocessing and optimized algorithms and implementation.
Coincidentally 'kissat' also means 'cats' in Finnish.}
# oreon:deps
BuildRequires:  7zip
BuildRequires:  drat-trim-tools
BuildRequires:  gcc
BuildRequires:  glibc-langpack-en
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  xz-lzma-compat
# /oreon:deps
%description
%_desc

This package contains a command-line interface to KISSAT.

%package libs
Summary:        Keep It Simple SAT solver library
%description libs
%_desc

This package contains KISSAT as a library, for use in applications that
need a SAT solver.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Library links and header files for developing applications that use
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-rel-%{version}

%conf
# Set the library soname
sed -i 's/@SOVER@/%{sover}/;s/@MAJVER@/%{majver}/' makefile.in

# Use Fedora flags by default
sed -e 's|-W -Wall|%{build_cflags} -fPIC|' \
    -e 's|^\(passtolinker=\)""|\1" %{build_ldflags}"|' \
    -i configure

%build

./configure -O2 --test
%make_build
export LD_LIBRARY_PATH=$PWD/build
help2man --version-string=%{version} -N -n 'Keep It Simple SAT solver' \
  -o kissat.1 build/kissat
%install
mkdir -p %{buildroot}%{_bindir}
cp -p build/kissat %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
cp -p build/libkissat.so.%{sover} %{buildroot}%{_libdir}
ln -s libkissat.so.%{sover} %{buildroot}%{_libdir}/libkissat.so.%{majver}
ln -s libkissat.so.%{majver} %{buildroot}%{_libdir}/libkissat.so
mkdir -p %{buildroot}%{_includedir}
cp -p src/kissat.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p kissat.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=$PWD/build build/tissat
%files -f %{oreon_filedir}/main.list
%files -n kissat-libs -f %{oreon_filedir}/kissat-libs.list
%files -n kissat-devel -f %{oreon_filedir}/kissat-devel.list

%changelog

%autochangelog
