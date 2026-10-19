%global source0_hash e72241ac9524bb653ae52ced768b508045d4438726a303f10181a38f764a453c
%global common_description %{expand:
Highway is a C++ library for SIMD (Single Instruction, Multiple Data), i.e.
applying the same operation to 'lanes'.}
%global toolchain clang
Name:           highway
Version:        1.4.0
Release:        1%{?dist}
Summary:        Efficient and performance-portable SIMD
License:        Apache-2.0
URL:            https://github.com/google/highway
Source0:        https://github.com/google/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  gtest-devel
BuildRequires:  libatomic
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake \
    -DHWY_SYSTEM_GTEST:BOOL=ON \
    -DHWY_CMAKE_RVV:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n highway-devel -f %{oreon_filedir}/highway-devel.list
%files -n highway-doc -f %{oreon_filedir}/highway-doc.list

%changelog

* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-%autorelease
- Import from Fedora dist-git f43 for Oreon 11
