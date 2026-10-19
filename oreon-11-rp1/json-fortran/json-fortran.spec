%global source0_hash 5fe9ad709a726416cec986886503e0526419742e288c4e43f63c1c22026d1e8a
Name:           json-fortran
Version:        8.3.0
Release:        1%{?dist}
Summary:        A Modern Fortran JSON API
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://github.com/jacobwilliams/json-fortran
Source0:        https://github.com/jacobwilliams/json-fortran/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-gfortran
# /oreon:deps
%description
JSON-Fortran is a user-friendly, thread-safe, and object-oriented API
for reading and writing JSON files, written in modern Fortran.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake -DUSE_GNU_INSTALL_CONVENTION=TRUE
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/*.mod %{buildroot}%{_fmoddir}/
rm -f %{buildroot}%{_libdir}/*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n json-fortran-devel -f %{oreon_filedir}/json-fortran-devel.list

%changelog

%autochangelog
