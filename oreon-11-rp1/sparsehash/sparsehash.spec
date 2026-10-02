%global source0_hash 8cd1a95827dfd8270927894eb77f62b4087735cbede953884647f16c521c7e58

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
# disable -debuginfo subpackage
%global debug_package %{nil}

Name:           sparsehash
Version:        2.0.4
Release:        1%{?dist}
Summary:        Extremely memory-efficient C++ hash_map implementation

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://code.google.com/p/sparsehash
Source0:        https://github.com/sparsehash/sparsehash/archive/refs/tags/sparsehash-%{version}.tar.gz#/sparsehash-%{version}.tar.gz

# fix build with -std=c++20
# https://github.com/sparsehash/sparsehash/pull/165
Patch0:         https://github.com/sparsehash/sparsehash/pull/165.patch

BuildRequires: make
BuildRequires:  gcc-c++
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
%autosetup -n %{name}-%{name}-%{version} -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT docdir=%{_pkgdocdir}

# Remove unneeded files
rm $RPM_BUILD_ROOT%{_pkgdocdir}/INSTALL
rm $RPM_BUILD_ROOT%{_pkgdocdir}/README_windows.txt

%check
make check

%files devel
%doc %{_pkgdocdir}/
%{_includedir}/google/
%{_includedir}/sparsehash/
%{_libdir}/pkgconfig/libsparsehash.pc

%changelog
%autochangelog
