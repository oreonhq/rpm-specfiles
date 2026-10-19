%global source0_hash 8eb6df3b47fcaad8ea6d35453ffc884b1ef2148f7a0984a3556795bab650fa9b
Name: dapl
Version: 2.1.10
Release:        1%{?dist}
Summary:        Library providing access to the DAT 2.0 API
License: GPL-2.0-only OR LicenseRef-Callaway-BSD OR CPL-1.0
Url: https://www.openfabrics.org/
Source0:        https://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
Patch0: dapl-c99.patch
Patch1: dapl-c23.patch
Requires: rdma
ExcludeArch: s390, armv7hl
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ibacm-devel
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  make
# /oreon:deps
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
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles dapl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dapl-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dapl-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n dapl-devel -f %{oreon_filedir}/dapl-devel.list
%files -n dapl-static -f %{oreon_filedir}/dapl-static.list
%files -n dapl-utils -f %{oreon_filedir}/dapl-utils.list

%changelog

%autochangelog
