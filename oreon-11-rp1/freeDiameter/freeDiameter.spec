%global source0_hash 0bb4ed33ada0b57ab681d86ae3fe0e3a9ce95892f492c401cbb68a87ec1d47bc

%global _hardened_build 1

Name:           freeDiameter
Version:        1.6.0
Release:        %autorelease
Summary:        A Diameter protocol open implementation

License:        BSD-3-Clause
URL:            http://www.freediameter.net/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn2-devel
BuildRequires:  libpq-devel
BuildRequires:  lksctp-tools-devel

%description
freeDiameter is an open source Diameter protocol implementation. It provides an
extensible platform for deploying a Diameter network for your Authentication,
Authorization and Accounting needs.

%package devel
Summary:        Library for freeDiameter package
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the shared library
for %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=None . -Wno-dev
#       -DCMAKE_C_STANDARD=17
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc doc
%{_bindir}/freeDiameterd
%{_bindir}/%{name}d-%{version}
%{_libdir}/libfdcore.so.*
%{_libdir}/libfdproto.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_libdir}/libfdcore.so
%{_libdir}/libfdproto.so

%changelog
%autochangelog
