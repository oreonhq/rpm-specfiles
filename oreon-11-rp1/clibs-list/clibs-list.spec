%global source0_hash 1ed72cc11d086e3e40cd6112867cc4102cddf5f008213da5de6e2db587b74340
Name:           clibs-list
Version:        0.4.1
%global so_version 0
Release:        1%{?dist}
Summary:        C doubly linked list implementation
License:        MIT
URL:            https://github.com/clibs/list
Source0:        https://github.com/clibs/list/archive/%{version}/list-%{version}.tar.gz
Patch:          %{url}/pull/47.patch
ExcludeArch:    %{ix86}
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description %{common_description}

The clibs-list package contains the clibs/list library.

%package devel
Summary:        Development files for clibs-list
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel %{common_description}

The clibs-list-devel package contains libraries and header files for developing
applications that use clibs-list.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir list-%{version}
%oreon_prep
%build

%make_build \
    AR="${AR-gcc-ar}" CC="${CC-gcc}" STRIP=/bin/true \
    CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}" \
    all bin/test
%install
%make_install PREFIX='%{_prefix}' LIBDIR='%{_libdir}'
rm -vf '%{buildroot}%{_libdir}/libclibs_list.a'
%oreon_autofiles clibs-list-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build test
%files -f %{oreon_filedir}/main.list
%files -n clibs-list-devel -f %{oreon_filedir}/clibs-list-devel.list

%changelog

%autochangelog
