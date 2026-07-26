%global source0_hash 568ebe0bc1988a23843fce6426602e555b7840bf6714edcdf0ed530214977f1b

Name: ck
Version: 0.7.2
Release: 4%{?dist}
Summary: Library for high performance concurrent programming

License: BSD-2-clause AND Apache-2.0 AND BSD-3-clause
# concurrencykit.org has been done for many months now, so use github instead
URL: https://github.com/concurrencykit/ck
Source: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# disable ck_hclh_test from ck_spinlock temporary solution
# github issue: https://github.com/concurrencykit/ck/issues/153
Patch3: ck_disable_ck_hclh_test.patch
# measure unit test times
Patch4: ck-unit-time.patch
# specify SEQUENCE_CORES different for one test
Patch5: ck-unit-sequence.patch
# add missing cast when assigning uint to pointer
Patch6: ck-ec-missing-cast.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: sed

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

%autosetup -p1

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

# fix weird mode of the shared library
chmod 0755 %{buildroot}%{_libdir}/libck.so.*

# remove static library
rm %{buildroot}%{_libdir}/libck.a

%check
MAX_CORES=4
# 8+ CORES take quite long, limit them to 4
CORES=$(grep '^CORES=' build/regressions.build | cut -d= -f2)
# ck_sequence tests wants all cores on the system to be quick
SEQUENCE_CORES="$CORES"
TIMEOUT=$((30*60))
TIMEOUT_KILL=$((TIMEOUT+100))
[ "${CORES}" -gt "${MAX_CORES}" ] && CORES="${MAX_CORES}"
%ifarch %{power64}
    # It hangs often on this test for some reason
    sed -e '/^OBJECTS=/ s, barrier_mcs,,' -i regressions/ck_barrier/validate/Makefile
%endif
%ifarch %{arm32} %{arm64}
    # Some tests take quite long on ARMs. Skip them
    # epoch test ends up in a very long/infinite loop
    sed -e '/^\s*brlock\s/ d' -e '/^\s*cohort\s/ d' -e '/^\s*rwlock\s/ d' \
        -e '/^\s*epoch\s/ d' -i regressions/Makefile
%endif
%ifarch s390x
    # epoch test ends up in a very long/infinite loop
    sed -e '/^\s*epoch\s/ d' -i regressions/Makefile
%endif

# Protect builders against hard lock
time timeout -k $TIMEOUT_KILL $TIMEOUT \
    make check CORES=${CORES} SEQUENCE_CORES=${SEQUENCE_CORES}

%files
%license LICENSE
%{_libdir}/libck.so.*

%files devel
%{_libdir}/libck.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.gz

%changelog
%autochangelog
