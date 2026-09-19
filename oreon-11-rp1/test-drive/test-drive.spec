%global source0_hash f9c037a3c1727e98801c2375e6f2efde9881ac1f54b04be3bc928e094f5787a5

Name:           test-drive
Version:        0.4.0
Release:        11%{?dist}
Summary:        The simple testing framework
# Automatically converted from old format: ASL 2.0 or MIT - review is highly recommended.
License:        Apache-2.0 OR LicenseRef-Callaway-MIT
URL:            https://github.com/fortran-lang/test-drive
Source0:        https://github.com/fortran-lang/test-drive/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-gfortran
BuildRequires:  cmake

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
# Move module files
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/test-drive/*/*.mod %{buildroot}%{_fmoddir}
rm -rf %{buildroot}%{_includedir}/test-drive/

%files
%license LICENSE-Apache LICENSE-MIT
%doc README.md
%{_libdir}/libtest-drive.so.0*

%files devel
%{_fmoddir}/testdrive*.mod
%{_libdir}/pkgconfig/test-drive.pc
%{_libdir}/cmake/test-drive/
%{_libdir}/libtest-drive.so

%changelog
%autochangelog
