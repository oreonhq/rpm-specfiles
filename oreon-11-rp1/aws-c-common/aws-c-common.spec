%global source0_hash ecea168ea974f2da73b5a0adc19d9c5ebca73ca4b9f733de7c37fc453ee7d1c2

%global _description %{expand:
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.}

Name:           aws-c-common
Version:        0.12.2
Release:        5%{?dist}
Summary:        Core c99 package for AWS SDK for C

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
BuildRequires:  cmake

# Bug: Three tests fail when building on s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2279089
ExcludeArch: s390x

%description %{_description}

%package libs
Summary:        Core c99 package for AWS SDK for C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs %{_description}

%package devel
Summary:        Core c99 package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE NOTICE
%doc README.md

%files libs
%{_libdir}/libaws-c-common.so.1{,.*}

%files devel
%{_libdir}/libaws-c-common.so
%dir %{_includedir}/aws/common
%dir %{_includedir}/aws/common/posix
%dir %{_includedir}/aws/common/external
%dir %{_includedir}/aws/testing
%{_includedir}/aws/common/*.h
%{_includedir}/aws/common/*.inl
%{_includedir}/aws/common/posix/common.inl
%{_includedir}/aws/common/external/*.h
%{_includedir}/aws/testing/aws_test_harness.h
%dir %{_libdir}/cmake/aws-c-common
%dir %{_libdir}/cmake/aws-c-common/shared
%dir %{_libdir}/cmake/aws-c-common/modules
%{_libdir}/cmake/aws-c-common/aws-c-common-config.cmake
%{_libdir}/cmake/aws-c-common/shared/*.cmake
%{_libdir}/cmake/aws-c-common/modules/*.cmake

%changelog
%autochangelog
