%global source0_hash 63171467e9deab880842f3e5589c02698c4637cf75106c4aa39affd84ecd8bd4
Name: cpl
Version: 7.4
Release:        1%{?dist}
Summary:        ESO library for automated astronomical data-reduction tasks
License: GPL-2.0-or-later
URL: http://www.eso.org/sci/software/cpl/
Source0:        https://ftp.eso.org/pub/dfs/pipelines/libraries/cpl/%{name}-%{version}.tar.gz
Patch0: cpl-i386.patch
# oreon:deps
BuildRequires:  cfitsio-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  wcslib-devel
# /oreon:deps
%description
The Common Pipeline Library (CPL) comprises a set of ISO-C libraries 
that provide a comprehensive, efficient and robust software toolkit. 
It forms a basis for the creation of automated astronomical data-reduction 
tasks (known as "pipelines") for ESO (European Southern Observatory) 
instruments. The CPL was developed to standardize the way 
VLT (Very Large Telescope) instrument pipelines are built, 
to shorten their development cycle and to ease their maintenance. 

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files and libraries needed to develop a %{name}
application

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%ldconfig_scriptlets
%oreon_autofiles cpl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cpl-devel -f %{oreon_filedir}/cpl-devel.list

%changelog

%autochangelog
