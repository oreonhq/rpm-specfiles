%global source0_hash 648b32e084f76fb1e7f5b71f44fbec65e4f01170cb6c0ddd9b780f782294a415
%bcond_with ipf
Name:           disk-utilities
Version:        2021.03.20
Release:        1%{?dist}
Summary:        Utilities for ripping, dumping, analysing, and modifying disk images
License:        Unlicense
URL:            https://github.com/keirf/Disk-Utilities
Source0:        https://github.com/keirf/Disk-Utilities/archive/%{version}/Disk-Utilities-%{version}.tar.gz
%if %{with ipf}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Disk Utilities is a collection of utilities for ripping, dumping, analysing,
and modifying disk images.

%package -n     libdisk
Summary:        A library for converting and manipulating disk images
%description -n libdisk
libdisk is a library for converting and manipulating disk images. It can
create disk images in a range of formats from Kryoflux STREAM and SPS/IPF
images (among others), and then allow these to be accessed and modified.

%package -n     libdisk-devel
Summary:        Development files for libdisk
Requires:       libdisk%{?_isa} = %{version}-%{release}
%description -n libdisk-devel
The libdisk-devel package contains libraries and header files for
developing applications that use libdisk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Disk-Utilities-%{version}
%oreon_prep
%build

%set_build_flags
%if %{with ipf}
export caps=y
%endif
%make_build
%install
export PREFIX="%{buildroot}%{_prefix}"
%if %{with ipf}
export caps=y
%endif
%make_install LIBDIR="%{buildroot}%{_libdir}"
%oreon_autofiles libdisk usr/*/lib*.so.*
%oreon_autofiles libdisk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdisk -f %{oreon_filedir}/libdisk.list
%files -n libdisk-devel -f %{oreon_filedir}/libdisk-devel.list

%changelog

%autochangelog
