%global source0_hash 78fe8bcebf496520ac29b5b65049f5ec1977c6bd956640bdc6d1da6ea04d8504
%global common_description %{expand:
The purpose of libfixposix is to offer replacements for parts of POSIX
whose behavior is inconsistent across *NIX flavors.}
Name:           libfixposix
Summary:        Thin wrapper over POSIX syscalls
Version:        0.4.3
Release:        17%{?dist}
License:        BSL-1.0
URL:            https://github.com/sionescu/%{name}
Source0:        https://github.com/sionescu/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description %{common_description}

%package        devel
Summary:        Thin wrapper over POSIX syscalls (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel %{common_description}

This package contains the development headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vfi
%configure
%make_build
%install
%make_install
find %{buildroot} -name "*.la" -print -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libfixposix-devel -f %{oreon_filedir}/libfixposix-devel.list

%changelog

%autochangelog
