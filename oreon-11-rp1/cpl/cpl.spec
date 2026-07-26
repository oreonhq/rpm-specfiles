%global source0_hash a50c265a8630e61606567d153d3c70025aa958a28473a2411585b96894be7720

Name: cpl
Version: 7.3.2
Release: 12%{?dist}
Summary: ESO library for automated astronomical data-reduction tasks

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.eso.org/sci/software/cpl/
Source: https://ftp.eso.org/pub/dfs/pipelines/libraries/cpl/%{name}-%{version}.tar.gz
Patch0: cpl-i386.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: cfitsio-devel >= 3.450
BuildRequires: wcslib-devel >= 4.24
BuildRequires: fftw-devel > 3.3.4

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
# http://fedoraproject.org/wiki/PackagingGuidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%ldconfig_scriptlets

%files
%doc AUTHORS BUGS COPYING NEWS
%license COPYING 
%{_libdir}/*so.*

%files devel
%doc README
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/cext.pc

%changelog
%autochangelog
