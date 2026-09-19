%global source0_hash 7146932ea4fc8e12b9152e23e18e46699174c531ef1e0fc351b05fcd12295a81

Name: libnetconf2
Version: 3.7.10
Release: 2%{?dist}
Summary: NETCONF protocol library
Url: https://github.com/CESNET/libnetconf2
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
License: BSD-3-Clause

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libssh-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libyang) >= 2
BuildRequires:  curl-devel

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

%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RELWITHDEBINFO
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md FAQ.md
%{_libdir}/libnetconf2.so.*
%dir %{_datadir}/yang/modules/libnetconf2
%{_datadir}/yang/modules/libnetconf2/*.yang

%files devel
%doc CODINGSTYLE.md
%{_libdir}/libnetconf2.so
%{_libdir}/pkgconfig/libnetconf2.pc
%{_includedir}/*.h
%{_includedir}/libnetconf2/*.h
%dir %{_includedir}/libnetconf2/

%changelog
%autochangelog
