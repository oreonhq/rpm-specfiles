%global source0_hash 21c692105db15299b5529af81a11a7ad80397f92c122bd7bf1e4a4b0e85654f7
%global forgeurl https://github.com/cpputest/cpputest
Name:           cpputest
Version:        4.0
Release:        1%{?dist}
Summary:        Unit testing and mocking framework for C/C++
License:        LicenseRef-Callaway-BSD
URL:            https://cpputest.github.io/
Source0:        %{forgeurl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-no-static-ext.patch
Patch1:         %{name}-fix-cmake-dest.patch
Patch2:         %{name}-remove-stdcxx-linking.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
Requires:       cmake-filesystem
Requires:       gcc-c++
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
