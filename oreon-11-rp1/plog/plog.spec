%global source0_hash d60b8b35f56c7c852b7f00f58cbe9c1c2e9e59566c5b200512d0cdbb6309a7c2
%global debug_package %{nil}
Name:           plog
Version:        1.1.11
Release:        1%{?dist}
Summary:        Portable, simple and extensible C++ logging library
License:        MIT
URL:            https://github.com/SergiusTheBest/plog
Source0:        https://github.com/SergiusTheBest/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          plog-test-c-lang.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DPLOG_BUILD_SAMPLES=OFF -DPLOG_BUILD_TESTS=ON
%cmake_build
%install
%cmake_install
rm -rv %{buildroot}%{_datadir}/doc/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n plog-devel -f %{oreon_filedir}/plog-devel.list

%changelog

%autochangelog
