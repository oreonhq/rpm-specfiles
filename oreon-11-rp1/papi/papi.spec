%global source0_hash f806e77e8cd08a0d3e4c002d8a8d3fefc64840ff663c2ac46bd66398c779c6db

# Default to no static libraries
%{!?with_static: %global with_static 0}
%bcond_with bundled_libpfm
# rdma is not available
%ifarch %{arm}
%{!?with_rdma: %global with_rdma 0}
%else
%{!?with_rdma: %global with_rdma 1}
%endif
%ifarch %{ix86}
%{!?with_pcp: %global with_pcp (0%{?fedora} < 40 && 0%{?rhel} < 10)}
%else
%{!?with_pcp: %global with_pcp 1}
%endif
Summary: Performance Application Programming Interface
Name: papi
Version: 7.2.0
Release: 3%{?dist}
License: BSD-3-Clause
Requires: papi-libs = %{version}-%{release}
URL: http://icl.cs.utk.edu/papi/
Source0:        https://deb.debian.org/debian/pool/main/p/papi/papi_7.2.0.orig.tar.gz
Patch1: papi-nostatic.patch
Patch2: papi-avail-path-fix.patch
Patch3: papi-revert-event-depr.patch
Patch4: papi-revert-arm-test.patch
BuildRequires: make
BuildRequires: autoconf
BuildRequires: doxygen
BuildRequires: ncurses-devel
BuildRequires: gcc-gfortran
BuildRequires: kernel-headers >= 2.6.32
BuildRequires: chrpath
BuildRequires: lm_sensors-devel
%if %{without bundled_libpfm}
BuildRequires: libpfm-devel >= 4.13.0-1
%if %{with_static}
BuildRequires: libpfm-static >= 4.6.0-1
%endif
%endif
# Following required for net component
BuildRequires: net-tools
%if  %{with_rdma}
# Following required for inifiband component
BuildRequires: rdma-core-devel
BuildRequires: infiniband-diags-devel
%endif
%if %{with_pcp}
BuildRequires: pcp-libs-devel
%endif
BuildRequires: perl-generators
#Right now libpfm does not know anything about s390 and will fail
ExcludeArch: s390 s390x

%description
PAPI provides a programmer interface to monitor the performance of
running programs.

%package libs
License: BSD-3-Clause
Summary: Libraries for PAPI clients
%description libs
This package contains the run-time libraries for any application that wishes
to use PAPI.

%package devel
License: BSD-3-Clause
Summary: Header files for the compiling programs with PAPI
Requires: papi = %{version}-%{release}
Requires: papi-libs = %{version}-%{release}
Requires: pkgconfig
%description devel
PAPI-devel includes the C header files that specify the PAPI user-space
libraries and interfaces. This is required for rebuilding any program
that uses PAPI.

%package testsuite
License: BSD-3-Clause
Summary: Set of tests for checking PAPI functionality
Requires: papi = %{version}-%{release}
Requires: papi-libs = %{version}-%{release}
%description testsuite
PAPI-testsuite includes compiled versions of papi tests to ensure
that PAPI functions on particular hardware.

%if %{with_static}
%package static
License: BSD-3-Clause
Summary: Static libraries for the compiling programs with PAPI
Requires: papi = %{version}-%{release}
%description static
PAPI-static includes the static versions of the library files for
the PAPI user-space libraries and interfaces.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch 1 -p1 -b papi-nostatic.patch
%patch 2 -p1 -b papi-avail-path-fix.patch
%patch 3 -p1 -b revert-event-depr.patch
%patch 4 -p1 -b revert-arm-test.patch

%build

%if %{without bundled_libpfm}
# Build our own copy of libpfm.
%global libpfm_config --with-pfm-incdir=%{_includedir} --with-pfm-libdir=%{_libdir}
%endif

%if %{with_static}
%global static_lib_config --with-static-lib=yes
%else
%global static_lib_config --with-static-lib=no
%endif

# set up environment variable for the various components
# cuda
# host_micpower
%if  %{with_rdma}
  export PAPI_INFINIBAND_UMAD_ROOT=/usr
%endif
# lmsensors
export PAPI_LMSENSORS_ROOT=/usr
#pushd vmware; ./configure; popd
%if %{with_pcp}
%global pcp_enable pcp
export PAPI_PCP_ROOT=/usr
%endif

cd src
autoconf
%configure --with-perf-events \
%{?libpfm_config} \
%{?static_lib_config} \
--with-shared-lib=yes --with-shlib-tools \
--with-components="appio coretemp example infiniband lmsensors lustre micpower mx net %{?pcp_enable} rapl stealtime"
# implicit enabled components: perf_event perf_event_uncore
#components currently left out because of build configure/build issues
# --with-components="bgpm coretemp_freebsd cuda host_micpower nvml vmware"

#DBG workaround to make sure libpfm just uses the normal CFLAGS
DBG="" make %{?_smp_mflags}

#generate updated versions of the documentation
#DBG workaround to make sure libpfm just uses the normal CFLAGS
pushd ../doc
DBG="" make
DBG="" make install
popd

%install
rm -rf $RPM_BUILD_ROOT
cd src
make DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true install-all

# Scrub the rpath/runpath from all the binaries.
find %{buildroot} -type f -executable ! -iname "*.py" ! -iname "*.sh" | xargs chrpath --delete

%files
%{_bindir}/*
%dir /usr/share/papi
/usr/share/papi/papi_events.csv
%doc INSTALL.txt README.md LICENSE.txt RELEASENOTES.txt
%doc %{_mandir}/man1/*

%ldconfig_scriptlets libs

%files libs
%{_libdir}/*.so.*
%doc INSTALL.txt README.md LICENSE.txt RELEASENOTES.txt

%files devel
%{_includedir}/*.h
%{_includedir}/*.hpp
%if %{with bundled_libpfm}
%{_includedir}/perfmon/*.h
%endif
%{_libdir}/*.so
%{_libdir}/pkgconfig/papi*.pc
%doc %{_mandir}/man3/*

%files testsuite
/usr/share/papi/run_tests*
/usr/share/papi/ctests
/usr/share/papi/ftests
/usr/share/papi/validation_tests
/usr/share/papi/components
/usr/share/papi/testlib

%if %{with_static}
%files static
%{_libdir}/*.a
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.2.0-3
- Import
