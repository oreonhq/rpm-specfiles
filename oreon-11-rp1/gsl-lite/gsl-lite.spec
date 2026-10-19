%global source0_hash 6746753379b00a8148c3b0714a3a9c2bc84735f0cfa82077f2f3b36f8d330a24
%bcond tests 1
%global debug_package %{nil}
Name:           gsl-lite
Version:        1.1.1
Release:        1%{?dist}
Summary:        Header-only version of ISO C++ Guidelines Support Library (GSL)
License:        MIT
SourceLicense:  %{license} AND BSL-1.0
URL:            https://github.com/gsl-lite/gsl-lite
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DGSL_LITE_OPT_BUILD_EXAMPLES=ON \
    -DGSL_LITE_OPT_BUILD_TESTS=%{?with_tests:ON}%{?!with_tests:OFF}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with tests}
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n gsl-lite-devel -f %{oreon_filedir}/gsl-lite-devel.list

%changelog

%autochangelog
