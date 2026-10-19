%global source0_hash 8cd1a95827dfd8270927894eb77f62b4087735cbede953884647f16c521c7e58
%{?mingw_package_header}
%global mingw_pkg_name sparsehash
Name:           mingw-%{mingw_pkg_name}
Version:        2.0.4
Release:        1%{?dist}
Summary:        MinGW Extremely memory-efficient C++ hash_map implementation
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sparsehash/sparsehash
Source0:        https://github.com/%{mingw_pkg_name}/%{mingw_pkg_name}/archive/%{mingw_pkg_name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        MinGW Extremely memory-efficient C++ hash_map implementation
%description -n mingw32-%{mingw_pkg_name}
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        MinGW Extremely memory-efficient C++ hash_map implementation
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
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-sparsehash -f %{oreon_filedir}/mingw32-sparsehash.list
%files -n mingw64-sparsehash -f %{oreon_filedir}/mingw64-sparsehash.list

%changelog

%autochangelog
