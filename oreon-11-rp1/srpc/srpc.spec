%global source0_hash 8fc8d5d0d0b0975ed4a5d266e82841c4e94eb041cb459357b92dba4e3b64ebb8
Summary:        An enterprise-level RPC system
Name:           srpc
License:        Apache-2.0
Version:        0.10.3
Release:        5%{?dist}
URL:            https://github.com/sogou/srpc
Source0:        https://github.com/sogou/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch:          srpc-gtest.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  workflow-devel
# /oreon:deps
%description
SRPC is an enterprise-level RPC system used by almost all online services
in Sogou. It handles tens of billions of requests every day, covering
searches, recommendations, advertising system, and other types of services.

%package devel
Summary:        Development files for SRPC
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
SRPC is an enterprise-level RPC system used by almost all online services
in Sogou. It handles tens of billions of requests every day, covering
searches, recommendations, advertising system, and other types of services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
rm %{buildroot}/%{_libdir}/libsrpc.a
rm %{buildroot}/%{_docdir}/%{name}-%{version}/README.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

sed -i "s/DEFAULT_BUILD_DIR := build.cmake/DEFAULT_BUILD_DIR := %__cmake_builddir/g"  GNUmakefile
make check
%files -f %{oreon_filedir}/main.list
%files -n srpc-devel -f %{oreon_filedir}/srpc-devel.list

%changelog

%autochangelog
