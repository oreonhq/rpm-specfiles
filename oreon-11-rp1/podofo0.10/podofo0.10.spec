%global source0_hash 49b159e88ba177ad2561b5cf6cbd68ecbe83272f5488bc527e44f97dbf695273
Name:           podofo0.10
Version:        0.10.5
Release:        1%{?dist}
Summary:        Podofo 0.10.x compatibility library
License:        LGPL-2.0-or-later
URL:            https://github.com/podofo/podofo
Source0:        https://github.com/podofo/podofo/archive/%{version}/podofo-%{version}.tar.gz
Patch0:         podofo-case.patch
Patch1:         podofo_CVE-2019-20093.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Podofo 0.10.x compatibility library.

%package devel
Summary:        Development files for %{name} library
Requires:       openssl-devel%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      podofo-devel
%description devel
Development files and documentation for the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir podofo-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}/cmake/podofo/
mv %{buildroot}%{_datadir}/podofo/*.cmake %{buildroot}%{_libdir}/cmake/podofo/
rmdir %{buildroot}%{_datadir}/podofo/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n podofo0.10-devel -f %{oreon_filedir}/podofo0.10-devel.list

%changelog

%autochangelog
