# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 16a7ad9b31ba5880dac55d62b5d6f243c3ebc8d46a3514149e56b5e7ea81f85f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Debuginfo packages are disabled to prevent rpmbuild from generating an empty
# debuginfo package for the empty main package.
%global debug_package %{nil}
%bcond mingw %[%{undefined rhel} || %{defined epel}]

Name:           cereal
Version:        1.3.2
Release:        13%{?dist}
Summary:        A header-only C++11 serialization library
# include/cereal/details/polymorphic_impl.hpp is BSL-1.0
# include/cereal/external/base64.hpp is Zlib
# include/cereal/external/rapidjson/ is MIT
# include/cereal/external/rapidxml/license.txt is MIT OR BSL-1.0
License:        BSD-3-Clause AND BSL-1.0 AND Zlib AND MIT AND (MIT OR BSL-1.0)
Url:            http://uscilab.github.io/cereal/
Source0:        https://github.com/USCiLab/cereal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.0

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95  
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-boost

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-boost
%endif

%description
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

%package devel
Summary:        Development headers and libraries for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description devel
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

This package contains development headers and libraries for the cereal library


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library

%description -n mingw64-%{name}
MinGW Windows %{name} library.
%endif

%prep
%oreon_verify_sources
%setup -q

%build
%{cmake} -DSKIP_PORTABILITY_TEST=ON -DWITH_WERROR=OFF
%cmake_build

%if %{with mingw}
# MinGW build
%mingw_cmake -DSKIP_PORTABILITY_TEST=ON -DBUILD_SANDBOX=OFF -DWITH_WERROR=OFF
%mingw_make_build
%endif

%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%endif

%check
# https://github.com/USCiLab/cereal/issues/744
%ifarch ppc64le
%global testargs --exclude-regex '\(test_complex\|test_pod\)'
%endif
%ctest  --output-on-failure %{?testargs}

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}

%if %{with mingw}
%files -n mingw32-%{name}
%doc README.md
%license LICENSE
%{mingw32_includedir}/%{name}
%{mingw32_libdir}/cmake/%{name}
%files -n mingw64-%{name}
%doc README.md
%license LICENSE
%{mingw64_includedir}/%{name}
%{mingw64_libdir}/cmake/%{name}
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-13
- Prepare for Oreon 11 (RP1)
