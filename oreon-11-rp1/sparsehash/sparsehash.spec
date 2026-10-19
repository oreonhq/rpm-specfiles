%global source0_hash 8cd1a95827dfd8270927894eb77f62b4087735cbede953884647f16c521c7e58
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global debug_package %{nil}
Name:           sparsehash
Version:        2.0.4
Release:        1%{?dist}
Summary:        Extremely memory-efficient C++ hash_map implementation
License:        LicenseRef-Callaway-BSD
URL:            http://code.google.com/p/sparsehash
Source0:        https://github.com/sparsehash/sparsehash/archive/refs/tags/sparsehash-%{version}.tar.gz#/sparsehash-%{version}.tar.gz
Patch0:         https://github.com/sparsehash/sparsehash/pull/165.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

# all files are in -devel package
%package        devel
Summary:        Extremely memory-efficient C++ hash_map implementation
%description    devel
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT docdir=%{_pkgdocdir}
rm $RPM_BUILD_ROOT%{_pkgdocdir}/INSTALL
rm $RPM_BUILD_ROOT%{_pkgdocdir}/README_windows.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n sparsehash-devel -f %{oreon_filedir}/sparsehash-devel.list

%changelog

%autochangelog
