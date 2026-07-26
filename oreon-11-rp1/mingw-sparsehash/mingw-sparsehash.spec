%global source0_hash 05e986a5c7327796dad742182b2d10805a8d4f511ad090da0490f146c1ff7a8c

%{?mingw_package_header}

%global mingw_pkg_name sparsehash

Name:           mingw-%{mingw_pkg_name}
Version:        2.0.3
Release:        16%{?dist}
Summary:        MinGW Extremely memory-efficient C++ hash_map implementation

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sparsehash/sparsehash
Source0:        %{url}/archive/sparsehash-%{version}.tar.gz
BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildArch:      noarch

%description
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}

%description -n mingw32-%{mingw_pkg_name}
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}

%description -n mingw64-%{mingw_pkg_name}
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{mingw_pkg_name}-%{mingw_pkg_name}-%{version}

%build
%mingw_configure
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Remove unneeded files
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}

%files -n mingw32-%{mingw_pkg_name}
%license COPYING
%doc AUTHORS NEWS README TODO
%{mingw32_includedir}/google/
%{mingw32_includedir}/sparsehash/
%{mingw32_libdir}/pkgconfig/libsparsehash.pc

%files -n mingw64-%{mingw_pkg_name}
%license COPYING
%doc AUTHORS NEWS README TODO
%{mingw64_includedir}/google/
%{mingw64_includedir}/sparsehash/
%{mingw64_libdir}/pkgconfig/libsparsehash.pc

%changelog
%autochangelog
