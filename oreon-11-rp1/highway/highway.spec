%global source0_hash none

%global common_description %{expand:
Highway is a C++ library for SIMD (Single Instruction, Multiple Data), i.e.
applying the same operation to 'lanes'.}

%global toolchain clang

Name:           highway
Version:        1.3.0
Release:        %autorelease
Summary:        Efficient and performance-portable SIMD

License:        Apache-2.0
URL:            https://github.com/google/highway
Source:        https://github.com/google/highway/archive/refs/tags/v1.3.0.tar.gz

# https://github.com/google/highway/commit/4201022df1c66193863b7d58fea8ac899bd56c45
Patch: 0001-Detect-clang-19-20-21-also-allow-user-override.patch
# https://github.com/google/highway/commit/54fc0d7eb59874d0fb03fc24e06c9c5e021d0071
Patch: 0002-Detect-not-yet-released-clang-22-for-users-building-.patch
# https://github.com/google/highway/commit/0913de4cffcb4707a7b32aecd7376096148f0cd4
Patch: 0003-SVE-still-broken-on-Clang-22-msan-fail-on-svcnt.patch

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  gtest-devel
BuildRequires:  libatomic

%description
%common_description

%package        devel
Summary:        Development files for Highway
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{common_description}

Development files for Highway.

%package        doc
Summary:        Documentation for Highway
BuildArch:      noarch

%description doc
%{common_description}

Documentation for Highway.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
    -DHWY_SYSTEM_GTEST:BOOL=ON \
    -DHWY_CMAKE_RVV:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_libdir}/libhwy.so.1
%{_libdir}/libhwy.so.%{version}
%{_libdir}/libhwy_contrib.so.1
%{_libdir}/libhwy_contrib.so.%{version}
%{_libdir}/libhwy_test.so.1
%{_libdir}/libhwy_test.so.%{version}

%files devel
%license LICENSE
%{_includedir}/hwy/
%{_libdir}/cmake/hwy/
%{_libdir}/libhwy.so
%{_libdir}/libhwy_contrib.so
%{_libdir}/libhwy_test.so
%{_libdir}/pkgconfig/libhwy.pc
%{_libdir}/pkgconfig/libhwy-contrib.pc
%{_libdir}/pkgconfig/libhwy-test.pc

%files doc
%license LICENSE
%doc g3doc hwy/examples

%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-%autorelease
- Import from Fedora dist-git f43 for Oreon 11
