%global source0_hash 40982b43c5e2f1d5b007add9917bc461fdffb95bd52f589de95b15aa59a9d0b6

Name: dapl
Version: 2.1.9
Release: 28%{?dist}
Summary: Library providing access to the DAT 2.0 API
# Automatically converted from old format: GPLv2 or BSD or CPL - review is highly recommended.
License: GPL-2.0-only OR LicenseRef-Callaway-BSD OR CPL-1.0
Url: https://www.openfabrics.org/
Source0: https://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
Patch0: dapl-c99.patch
Patch1: dapl-c23.patch
BuildRequires: libibverbs-devel >= 1.2.1
BuildRequires: librdmacm-devel >= 1.1.0
BuildRequires: ibacm-devel
BuildRequires: gcc
BuildRequires: make
Requires: rdma
# Platforms missing in dapl/udapl/linux/dapl_osd.h
ExcludeArch: s390, armv7hl
%description
Along with the RDMA kernel drivers, libdat and libdapl provide
a user-space RDMA API that supports DAT 2.0 specification and IB
transport extensions for atomic operations and RDMA write with
immediate data.

%package devel
Summary: Development files for the libdat and libdapl libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files for libdat and libdapl libraries.

%package static
Summary: Static libdat and libdapl libraries
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static versions of the libdat and libdapl libraries.

%package utils
Summary: Test suites for dapl libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Useful test suites to validate the dapl library APIs and operation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
find . -type f -iname '*.[ch]' -exec chmod a-x '{}' ';'

%build
%configure --sysconfdir=/etc/rdma
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%{_mandir}/man5/*
%config(noreplace) %{_sysconfdir}/rdma/dat.conf
%doc AUTHORS README ChangeLog README.mcm
%license COPYING LICENSE.txt LICENSE2.txt LICENSE3.txt

%files devel
%{_libdir}/*.so
%dir %{_includedir}/dat2
%{_includedir}/dat2/*

%files static
%{_libdir}/*.a

%files utils
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
