%global source0_hash 8fc8d5d0d0b0975ed4a5d266e82841c4e94eb041cb459357b92dba4e3b64ebb8

Summary:        An enterprise-level RPC system
Name:           srpc
License:        Apache-2.0

Version:        0.10.3
Release:        5%{?dist}

URL:            https://github.com/sogou/srpc
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz
# https://github.com/sogou/srpc/pull/429
Patch:          srpc-gtest.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(liblz4)
# Using pkgconfig for openssl gives a fedora-review warning
# that openssl1.1 is deprecated and should not be used
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  workflow-devel

%global _description %{expand:
SRPC is an enterprise-level RPC system used by almost all online services
in Sogou. It handles tens of billions of requests every day, covering
searches, recommendations, advertising system, and other types of services.}

%description
%_description

%package devel
Summary:        Development files for SRPC
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# Do not package static library
rm %{buildroot}/%{_libdir}/libsrpc.a
# README is packaged later
rm %{buildroot}/%{_docdir}/%{name}-%{version}/README.md

%check
# change build directory
sed -i "s/DEFAULT_BUILD_DIR := build.cmake/DEFAULT_BUILD_DIR := %__cmake_builddir/g"  GNUmakefile
make check

%files 
%license LICENSE
%doc README.md
%{_bindir}/%{name}_generator
%{_libdir}/libsrpc.so.0*

%files devel
%{_libdir}/libsrpc.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_includedir}/%name/*.inl
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake

%changelog
%autochangelog
