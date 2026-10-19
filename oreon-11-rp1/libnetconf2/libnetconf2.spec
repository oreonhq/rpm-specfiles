%global source0_hash 7146932ea4fc8e12b9152e23e18e46699174c531ef1e0fc351b05fcd12295a81
Name: libnetconf2
Version: 3.7.10
Release:        1%{?dist}
Summary:        NETCONF protocol library
Url: https://github.com/CESNET/libnetconf2
Source0:        https://github.com/CESNET/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License: BSD-3-Clause
# oreon:deps
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  libssh-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libyang)
# /oreon:deps
%package devel
Summary:    Headers of libnetconf2 library
Conflicts:  libnetconf-devel
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
%description devel
Headers of libnetconf library.

%description
libnetconf2 is a NETCONF library in C intended for building NETCONF clients and
servers. NETCONF is the NETwork CONFiguration protocol introduced by IETF.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=RELWITHDEBINFO
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnetconf2-devel -f %{oreon_filedir}/libnetconf2-devel.list

%changelog

%autochangelog
