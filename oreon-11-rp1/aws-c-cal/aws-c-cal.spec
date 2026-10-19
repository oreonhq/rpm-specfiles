%global source0_hash 9c6d424d206dd7822aa44fa39ce31575dcbaa83133620abdac8e56e4cea9667c
Name:           aws-c-cal
Version:        1.0.0
Release:        1%{?dist}
Summary:        AWS Crypto Abstraction Layer
License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0001:      0001-patch-Disable-SHA1-related-tests.patch
ExcludeArch: s390x
# oreon:deps
BuildRequires:  aws-c-common-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  openssl-devel
# /oreon:deps
%description

%package libs
Summary:        AWS Crypto Abstraction Layer
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description libs

%package devel
Summary:        AWS Crypto Abstraction Layer
Requires:       openssl-devel
Requires:       aws-c-common-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_SHARED_LIBS=ON -DUSE_OPENSSL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
