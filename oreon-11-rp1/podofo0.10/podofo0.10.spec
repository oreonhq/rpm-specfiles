%global source0_hash 49b159e88ba177ad2561b5cf6cbd68ecbe83272f5488bc527e44f97dbf695273

Name:           podofo0.10
Version:        0.10.5
Release:        2%{?dist}
Summary:        Podofo 0.10.x compatibility library

License:        LGPL-2.0-or-later
URL:            https://github.com/podofo/podofo
Source0:        https://github.com/podofo/podofo/archive/%{version}/podofo-%{version}.tar.gz

# Fix header case
Patch0:         podofo-case.patch
# Downstream patch for CVE-2019-20093
# https://sourceforge.net/p/podofo/tickets/75/
Patch1:         podofo_CVE-2019-20093.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

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

%autosetup -p1 -n podofo-%{version}

%build
# Natve build
%cmake
%cmake_build

%install
%cmake_install

# Move incorrectly installed files
mkdir -p %{buildroot}%{_libdir}/cmake/podofo/
mv %{buildroot}%{_datadir}/podofo/*.cmake %{buildroot}%{_libdir}/cmake/podofo/
rmdir %{buildroot}%{_datadir}/podofo/

%check
%ctest

%files
%doc AUTHORS.md CHANGELOG.md README.md TODO.md
%license COPYING
%{_libdir}/*.so.0.10.5
%{_libdir}/*.so.2

%files devel
%{_includedir}/podofo
%{_libdir}/*.so
%{_libdir}/cmake/podofo/
%{_libdir}/pkgconfig/libpodofo.pc

%changelog
%autochangelog
