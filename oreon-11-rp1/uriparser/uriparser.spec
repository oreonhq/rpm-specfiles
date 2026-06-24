%global source0_hash none

%if 0%{?fedora} || 0%{?epel} >= 9
%bcond_without mingw
%else
%bcond_with mingw
%endif

Name:           uriparser
Version:        1.0.2
Release:        1%{?dist}
Summary:        URI parsing library - RFC 3986

# main license is BSD-3-Clause
# test suite is licensed under the LGPL-2.1-or-later, but it is not included in the binary RPM
# fuzzing code is licensed under the Apache-2.0 license, but it is not included in the binary RPM
# /doc/rfc* are under LicenseRef-scancode-iso-8879, LicenseRef-scancode-ietf, LicenseRef-scancode-ietf-trust but not included in RPM
License:        BSD-3-Clause
URL:            https://uriparser.github.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  gtest-devel
BuildRequires:  make

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
%endif


%description
Uriparser is a strictly RFC 3986 compliant URI parsing library written
in C. uriparser is cross-platform, fast, supports Unicode and is
licensed under the New BSD license.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package doc
Summary:        HTML documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains HTML documentation files for %{name}.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%{?mingw_debug_package}
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove qhelpgenerator dependency by commenting Doxygen.in:
sed -i 's/GENERATE_QHP\ =\ yes/GENERATE_QHP\ =\ no/g' doc/Doxyfile.in


%build
# Native build
%cmake
%cmake_build

%if %{with mingw}
# MinGW build
%mingw_cmake -DURIPARSER_BUILD_TESTS=OFF -DURIPARSER_BUILD_DOCS=OFF
%mingw_make_build
%endif


%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%endif


%check
%ctest


%files
%doc THANKS AUTHORS ChangeLog
%license COPYING.BSD-3-Clause
%{_bindir}/uriparse
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}-%{version}/
%{_libdir}/pkgconfig/lib%{name}.pc

%files doc
%license COPYING.BSD-3-Clause
%doc %{_docdir}/%{name}/html

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING.BSD-3-Clause
%{mingw32_bindir}/uriparse.exe
%{mingw32_bindir}/lib%{name}-1.dll
%{mingw32_includedir}/%{name}/
%{mingw32_libdir}/lib%{name}.dll.a
%{mingw32_libdir}/pkgconfig/lib%{name}.pc
%{mingw32_libdir}/cmake/%{name}-%{version}/

%files -n mingw64-%{name}
%license COPYING.BSD-3-Clause
%{mingw64_bindir}/uriparse.exe
%{mingw64_includedir}/%{name}/
%{mingw64_bindir}/lib%{name}-1.dll
%{mingw64_libdir}/lib%{name}.dll.a
%{mingw64_libdir}/pkgconfig/lib%{name}.pc
%{mingw64_libdir}/cmake/%{name}-%{version}/
%endif


%changelog
%autochangelog

