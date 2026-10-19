%global source0_hash f806e77e8cd08a0d3e4c002d8a8d3fefc64840ff663c2ac46bd66398c779c6db
%{!?with_static: %global with_static 0}
%bcond_with bundled_libpfm
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
Summary:        Performance Application Programming Interface
Name: papi
Version: 7.2.0
Release:        1%{?dist}
License: BSD-3-Clause
Requires: papi-libs = %{version}-%{release}
URL: http://icl.cs.utk.edu/papi/
Source0:        https://deb.debian.org/debian/pool/main/p/papi/papi_7.2.0.orig.tar.gz
Patch1: papi-nostatic.patch
Patch2: papi-avail-path-fix.patch
Patch3: papi-revert-event-depr.patch
Patch4: papi-revert-arm-test.patch
%if %{without bundled_libpfm}
%if %{with_static}
%endif
%endif
%if  %{with_rdma}
%endif
%if %{with_pcp}
%endif
ExcludeArch: s390 s390x
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  chrpath
BuildRequires:  doxygen
BuildRequires:  gcc-gfortran
BuildRequires:  infiniband-diags-devel
BuildRequires:  kernel-headers
BuildRequires:  libpfm-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  net-tools
BuildRequires:  pcp-libs-devel
BuildRequires:  perl-generators
BuildRequires:  rdma-core-devel
# /oreon:deps
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
%setup -q -n papi-papi-7-2-0-t
%patch 1 -p1 -b papi-nostatic.patch
%patch 2 -p1 -b papi-avail-path-fix.patch
%patch 3 -p1 -b revert-event-depr.patch
%patch 4 -p1 -b revert-arm-test.patch

%build

%if %{without bundled_libpfm}
%global libpfm_config --with-pfm-incdir=%{_includedir} --with-pfm-libdir=%{_libdir}
%endif
%if %{with_static}
%global static_lib_config --with-static-lib=yes
%else
%global static_lib_config --with-static-lib=no
%endif
%if  %{with_rdma}
  export PAPI_INFINIBAND_UMAD_ROOT=/usr
%endif
export PAPI_LMSENSORS_ROOT=/usr
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
DBG="" make %{?_smp_mflags}
pushd ../doc
DBG="" make
DBG="" make install
popd
%install
rm -rf $RPM_BUILD_ROOT
cd src
make DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true install-all
find %{buildroot} -type f -executable ! -iname "*.py" ! -iname "*.sh" | xargs chrpath --delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n papi-libs -f %{oreon_filedir}/papi-libs.list
%files -n papi-devel -f %{oreon_filedir}/papi-devel.list
%files -n papi-testsuite -f %{oreon_filedir}/papi-testsuite.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.2.0-3
- Import
