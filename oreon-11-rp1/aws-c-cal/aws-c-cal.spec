%global source0_hash 516ff370a45bfc49fd6d34a9bd2b1b3e753221046a9e2fbd117341d6f9d39edc

%global _description %{expand:
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives}

Name:           aws-c-cal
Version:        0.9.0
Release:        5%{?dist}
Summary:        AWS Crypto Abstraction Layer

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Upstream introduced SHA1 related code and tests in v0.8.1
# Fedora 41 and RHEL 9 distrust SHA1 signatures
# Disabling tests of additional functionality to unblock package build
Patch0001:      0001-patch-Disable-SHA1-related-tests.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-common-devel

# Dependency aws-c-common doesn't build on s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2279275
ExcludeArch: s390x

%description %{_description}

%package libs
Summary:        AWS Crypto Abstraction Layer
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs %{_description}

%package devel
Summary:        AWS Crypto Abstraction Layer
Requires:       openssl-devel
Requires:       aws-c-common-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON -DUSE_OPENSSL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE NOTICE
%doc README.md

%files libs
%{_libdir}/libaws-c-cal.so.1{,.*}

%files devel
%{_libdir}/libaws-c-cal.so
%dir %{_includedir}/aws/cal
%{_includedir}/aws/cal/*.h
%dir %{_libdir}/cmake/aws-c-cal
%dir %{_libdir}/cmake/aws-c-cal/modules
%dir %{_libdir}/cmake/aws-c-cal/shared
%{_libdir}/cmake/aws-c-cal/aws-c-cal-config.cmake
%{_libdir}/cmake/aws-c-cal/modules/Findcrypto.cmake
%{_libdir}/cmake/aws-c-cal/shared/aws-c-cal-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-cal/shared/aws-c-cal-targets.cmake

%changelog
%autochangelog
