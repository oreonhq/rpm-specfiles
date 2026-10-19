%global source0_hash 489abb253514f819adb7e3aab3273b184c484dfe082fbe2166de2fd3a88dfb2b
%global debug_package %{nil}
Name:           safeint
Version:        3.0.27
Release:        1%{?dist}
Summary:        Class library for C++ that manages integer overflows
License:        MIT
URL:            https://github.com/dcleblanc/SafeInt
Source0:        https://github.com/dcleblanc/SafeInt/archive/%{version}/SafeInt-%{version}.tar.gz
Patch0:         safeint-3.0.27-gcc13_fix.patch
Patch1:         safeint-3.0.27-gcc98_test_rm.patch
Patch2:         safeint-3.0.27-gcc14_test_fix.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
An integer overflow library that was originally created in Microsoft
Office in 2003, and later was made open source on CodePlex using the MS-PL
license. After CodePlex was deprecated, the project was moved to github
and the license was changed to the MIT license.

%package devel
Summary: %{summary}
Provides: %{name}-static = %{version}-%{release}
%description devel
An integer overflow library that was originally created in Microsoft
Office in 2003, and later was made open source on CodePlex using the MS-PL
license. After CodePlex was deprecated, the project was moved to github
and the license was changed to the MIT license.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir SafeInt-%{version}
%oreon_prep
%check

%cmake
%cmake_build
%ctest
%build

%install
install -d %{buildroot}%{_includedir}/SafeInt
install -D -p SafeInt.hpp -t %{buildroot}%{_includedir}/SafeInt/
install -D -p safe_math.h -t %{buildroot}%{_includedir}/SafeInt/
install -D -p safe_math_impl.h -t %{buildroot}%{_includedir}/SafeInt/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n safeint-devel -f %{oreon_filedir}/safeint-devel.list

%changelog

%autochangelog
