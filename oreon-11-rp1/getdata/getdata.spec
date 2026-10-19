%global source0_hash d16feae0907090047f5cc60ae0fb3500490e4d1889ae586e76b2d3a2e1c1b273
%global tests_enabled 0
Name:           getdata
Version:        0.11.0
Release:        14%{?dist}
Summary:        Library for reading and writing dirfile data
License:        GPL-2.0-or-later
URL:            http://getdata.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
%ifarch %{ix86} x86_64
%endif
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zziplib-devel
# /oreon:deps
%description
The GetData Project is the reference implementation of the Dirfile Standards,
a filesystem-based database format for time-ordered binary data. The Dirfile
database format is designed to provide a fast, simple format for storing and
reading data.

%package devel
Summary: Headers required when building programs against getdata
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: gcc-gfortran%{_isa}
%description devel
Headers required when building a program against the GetData library.
Includes C++ and FORTRAN (77 & 95) bindings. 

%package fortran
Summary: getdata bindings for fortran
Requires: %{name} = %{version}-%{release}
%description fortran
The GetData library for fortran programs.  

%package gzip
Summary: Enables getdata read ability of gzip compressed dirfiles
Requires: %{name} = %{version}-%{release}
%description gzip
Enables getdata to read dirfiles that are encoded (compressed) with gzip.
Fields must be fully compressed with gzip, not actively being written to.
Does not yet allow writing of gzip encoded dirfiles.  

%package bzip2
Summary: Enables getdata read ability of bzip2 compressed dirfiles
Requires: %{name} = %{version}-%{release}
%description bzip2
Enables getdata to read dirfiles that are encoded (compressed) with bzip2.
Fields must be fully compressed with bzip2, not actively being written to.
Does not yet allow writing of bzip2 encoded dirfiles.

%ifarch %{ix86} x86_64 #slim is only available on for these.
%package slim
Summary: Enables getdata read ability of slim compressed dirfiles
Requires: %{name} = %{version}-%{release}
%description slim
Enables getdata to read dirfiles that are encoded (compressed) with slimdata.
%endif

%package lzma
Summary: Enables getdata read ability of lzma compressed dirfiles
Requires: %{name} = %{version}-%{release}
%description lzma
Enables getdata to read dirfiles that are encoded (compressed) with lzma.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

export FCFLAGS="$FCFLAGS -fallow-argument-mismatch"
%configure --disable-static --enable-modules --disable-perl --disable-python
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
mkdir -p %{buildroot}
make DESTDIR=%{buildroot} SUID_ROOT="" install
rm -f %{buildroot}/%{_libdir}/lib*.la
rm -f %{buildroot}/%{_libdir}/getdata/lib*.la
rm -f %{buildroot}/%{_datadir}/doc/%{name}/*
mkdir -p %{buildroot}/%{_fmoddir}
mv %{buildroot}/%{_includedir}/getdata.mod  %{buildroot}/%{_fmoddir}/
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n getdata-devel -f %{oreon_filedir}/getdata-devel.list
%files -n getdata-fortran -f %{oreon_filedir}/getdata-fortran.list
%files -n getdata-gzip -f %{oreon_filedir}/getdata-gzip.list
%files -n getdata-bzip2 -f %{oreon_filedir}/getdata-bzip2.list
%files -n getdata-lzma -f %{oreon_filedir}/getdata-lzma.list

%changelog

%autochangelog
