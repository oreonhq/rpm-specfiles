%global source0_hash 568ebe0bc1988a23843fce6426602e555b7840bf6714edcdf0ed530214977f1b
Name: ck
Version: 0.7.2
Release:        4%{?dist}
Summary:        Library for high performance concurrent programming
License: BSD-2-clause AND Apache-2.0 AND BSD-3-clause
URL: https://github.com/concurrencykit/ck
Source0:        https://github.com/concurrencykit/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch3: ck_disable_ck_hclh_test.patch
Patch4: ck-unit-time.patch
Patch5: ck-unit-sequence.patch
Patch6: ck-ec-missing-cast.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures designed to
aid in the design and implementation of high performance concurrent systems. It
is designed to minimize dependencies on operating system-specific interfaces
and most of the interface relies only on a strict subset of the standard
library and more popular compiler extensions.

%package devel
Summary: Header files and libraries for CK development
Requires: %{name} = %{version}-%{release}
%description devel
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures designed to
aid in the design and implementation of high performance concurrent systems. It
is designed to minimize dependencies on operating system-specific interfaces
and most of the interface relies only on a strict subset of the standard
library and more popular compiler extensions.

This package provides the libraries, include files, and other
resources needed for developing Concurrency Kit applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{optflags}"
./configure 		\
	--libdir=%{_libdir} 			\
	--includedir=%{_includedir}/%{name}	\
	--mandir=%{_mandir}			\
	--prefix=%{_prefix}
%make_build
%install
%make_install
chmod 0755 %{buildroot}%{_libdir}/libck.so.*
rm %{buildroot}%{_libdir}/libck.a
%oreon_autofiles ck-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

MAX_CORES=4
CORES=$(grep '^CORES=' build/regressions.build | cut -d= -f2)
SEQUENCE_CORES="$CORES"
TIMEOUT=$((30*60))
TIMEOUT_KILL=$((TIMEOUT+100))
[ "${CORES}" -gt "${MAX_CORES}" ] && CORES="${MAX_CORES}"
%ifarch %{power64}
    sed -e '/^OBJECTS=/ s, barrier_mcs,,' -i regressions/ck_barrier/validate/Makefile
%endif
%ifarch %{arm32} %{arm64}
    sed -e '/^\s*brlock\s/ d' -e '/^\s*cohort\s/ d' -e '/^\s*rwlock\s/ d' \
        -e '/^\s*epoch\s/ d' -i regressions/Makefile
%endif
%ifarch s390x
    sed -e '/^\s*epoch\s/ d' -i regressions/Makefile
%endif
time timeout -k $TIMEOUT_KILL $TIMEOUT \
    make check CORES=${CORES} SEQUENCE_CORES=${SEQUENCE_CORES}
%files -f %{oreon_filedir}/main.list
%files -n ck-devel -f %{oreon_filedir}/ck-devel.list

%changelog

%autochangelog
