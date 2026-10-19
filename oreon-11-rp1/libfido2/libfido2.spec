%global source1_hash 7589ece7d4676ec831216a2be68c5c0e996ace73d718a47d3bdf4c807eb24d45
%global source0_hash c1012c8871d71b65872fd5ff1a9d6b0838a55683a03e85ba97479ce57129c736
Name:           libfido2
Version:        1.17.0
Release:        1%{?dist}
Summary:        FIDO2 library
License:        BSD-2-Clause
URL:            https://github.com/Yubico/%{name}
Source0:        https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:        yubico-release-gpgkeys.asc
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(libcbor)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
%{name} is an open source library to support the FIDO2 protocol.  FIDO2 is
an open authentication standard that consists of the W3C Web Authentication
specification (WebAuthn API), and the Client to Authentication Protocol
(CTAP).  CTAP is an application layer protocol used for communication
between a client (browser) or a platform (operating system) with an external
authentication device (for example the Yubico Security Key).

################################################################################

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{name}-devel contains development libraries and header files for %{name}.

################################################################################

%package -n fido2-tools
Summary:        FIDO2 tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n fido2-tools
FIDO2 command line tools to access and configure a FIDO2 compliant
authentication device.

################################################################################

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
find %{buildroot} -type f -name "*.a" -delete -print
%oreon_autofiles fido2-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest \-E regress_cred
%files -f %{oreon_filedir}/main.list
%files -n libfido2-devel -f %{oreon_filedir}/libfido2-devel.list
%files -n fido2-tools -f %{oreon_filedir}/fido2-tools.list

%changelog

%autochangelog
