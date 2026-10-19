%global source0_hash c33e573c6a1d758fa358a878044227139c425b46bb214d49b2c773072cab5089
Name:           aws-c-common
Version:        1.0.2
Release:        1%{?dist}
Summary:        Core c99 package for AWS SDK for C
License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
ExcludeArch: s390x
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
# /oreon:deps
%description

%package libs
Summary:        Core c99 package for AWS SDK for C
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description libs

%package devel
Summary:        Core c99 package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
