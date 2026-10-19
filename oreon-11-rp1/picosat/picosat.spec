%global source0_hash 15169b4f28ba8f628f353f6f75a100845cdef4a2244f101a02b6e5a26e46a754
Name:           picosat
Version:        965
Release:        1%{?dist}
Summary:        A SAT solver
License:        MIT
URL:            https://fmv.jku.at/picosat/
VCS:            git:%{url}.git
Source0:        https://fmv.jku.at/%{name}//%{name}-%{version}.tar.gz
Source1:        picosat.1
Source2:        picosat.trace.1
Source3:        picomus.1
Patch:          %{name}-trace.patch
ExcludeArch:    %{ix86}
Requires:       bzip2
Requires:       gzip
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  R-core-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
PicoSAT solves the SAT problem, which is the classical NP-complete problem of
searching for a satisfying assignment of a propositional formula in
conjunctive normal form (CNF).  PicoSAT can generate proofs and cores in
memory by compressing the proof trace.  It supports the proof format of
TraceCheck.

%package R
Summary:        A SAT solver library for R
%description R
The PicoSAT library, which contains routines that solve the SAT problem.  The
library has a simple API which is similar to that of previous solvers by the
same authors.  This version of the library is built for use with R projects.

%package libs
Summary:        A SAT solver library
%description libs
The PicoSAT library, which contains routines that solve the SAT problem.  The
library has a simple API which is similar to that of previous solvers by the
same authors.

%package devel
Summary:        Development files for PicoSAT
Requires:       %{name}-R%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Headers and other development files for PicoSAT.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build

sed -e 's/@CC@/gcc/' \
    -e 's|@CFLAGS@|%{build_cflags} -D_GNU_SOURCE=1 -DNDEBUG -DRCODE -I%{_includedir}/R|' \
    -e 's|-Xlinker libpicosat.so|-Xlinker libpicosat.so.0 %{build_ldflags} -L%{_libdir}/R/lib -lR|' \
    -e 's/libpicosat/libpicosat-R/g' \
    -e 's/-lpicosat/-lpicosat-R/g' \
    -e 's/@TARGETS@/libpicosat-R.so/' \
  makefile.in > makefile
%make_build
sed -e 's/@CC@/gcc/' \
    -e 's|@CFLAGS@|%{build_cflags} -D_GNU_SOURCE=1 -DNDEBUG -DTRACE|' \
    -e 's|-Xlinker libpicosat.so|-Xlinker libpicosat.so.0 %{build_ldflags}|' \
    -e 's/libpicosat/libpicosat-trace/g' \
    -e 's/-lpicosat/-lpicosat-trace/g' \
    -e 's/@TARGETS@/libpicosat-trace.so picosat picomus/' \
  makefile.in > makefile
%make_build
mv picosat picosat.trace
rm -f *.o *.s config.h
sed -e 's/@CC@/gcc/' \
    -e 's|@CFLAGS@|%{build_cflags} -D_GNU_SOURCE=1 -DNDEBUG|' \
    -e 's|-Xlinker libpicosat.so|-Xlinker libpicosat.so.0 %{build_ldflags}|' \
    -e 's/@TARGETS@/libpicosat.so picosat picomcs picogcnf/' \
  makefile.in > makefile
%make_build
%install
mkdir -p %{buildroot}%{_includedir}
cp -p picosat.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
install -m 0755 -p libpicosat-R.so \
  %{buildroot}%{_libdir}/libpicosat-R.so.0.0.%{version}
ln -s libpicosat-R.so.0.0.%{version} %{buildroot}%{_libdir}/libpicosat-R.so.0
ln -s libpicosat-R.so.0 %{buildroot}%{_libdir}/libpicosat-R.so
install -m 0755 -p libpicosat-trace.so \
  %{buildroot}%{_libdir}/libpicosat-trace.so.0.0.%{version}
ln -s libpicosat-trace.so.0.0.%{version} \
  %{buildroot}%{_libdir}/libpicosat-trace.so.0
ln -s libpicosat-trace.so.0 %{buildroot}%{_libdir}/libpicosat-trace.so
install -m 0755 -p libpicosat.so \
  %{buildroot}%{_libdir}/libpicosat.so.0.0.%{version}
ln -s libpicosat.so.0.0.%{version} %{buildroot}%{_libdir}/libpicosat.so.0
ln -s libpicosat.so.0 %{buildroot}%{_libdir}/libpicosat.so
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -p picosat picosat.trace picomus picomcs picogcnf \
  %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n picosat-R -f %{oreon_filedir}/picosat-R.list
%files -n picosat-libs -f %{oreon_filedir}/picosat-libs.list
%files -n picosat-devel -f %{oreon_filedir}/picosat-devel.list

%changelog

%autochangelog
