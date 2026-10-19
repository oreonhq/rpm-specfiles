%global source0_hash f9c037a3c1727e98801c2375e6f2efde9881ac1f54b04be3bc928e094f5787a5
Name:           test-drive
Version:        0.4.0
Release:        11%{?dist}
Summary:        The simple testing framework
License:        Apache-2.0 OR LicenseRef-Callaway-MIT
URL:            https://github.com/fortran-lang/test-drive
Source0:        https://github.com/fortran-lang/test-drive/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-gfortran
# /oreon:deps
%description
This project offers a lightweight, procedural unit testing framework
based on nothing but standard Fortran.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/test-drive/*/*.mod %{buildroot}%{_fmoddir}
rm -rf %{buildroot}%{_includedir}/test-drive/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n test-drive-devel -f %{oreon_filedir}/test-drive-devel.list

%changelog

%autochangelog
