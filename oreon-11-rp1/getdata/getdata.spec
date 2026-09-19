%global source0_hash d16feae0907090047f5cc60ae0fb3500490e4d1889ae586e76b2d3a2e1c1b273

%global tests_enabled 0

Name:           getdata
Version:        0.11.0
Release:        14%{?dist}
Summary:        Library for reading and writing dirfile data

License:        GPL-2.0-or-later
URL:            http://getdata.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:     gcc-gfortran libtool-ltdl-devel
BuildRequires:     bzip2-devel zlib-devel xz-devel zziplib-devel flac-devel
%ifarch %{ix86} x86_64
#slim is only available on ix86 and x86_64
BuildRequires:     slimdata-devel
%endif
BuildRequires: make

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
# FIXME: FFLAGS/FCFLAGS are not being honored; looking into it with upstream.
export FCFLAGS="$FCFLAGS -fallow-argument-mismatch"
%configure --disable-static --enable-modules --disable-perl --disable-python

# removing rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%if %{tests_enabled}
%check
LD_LIBRARY_PATH="%{buildroot}/%{_libdir}:%{buildroot}/%{_libdir}/getdata" make check
%endif

%install
mkdir -p %{buildroot}
make DESTDIR=%{buildroot} SUID_ROOT="" install
# Remove .la files.  
rm -f %{buildroot}/%{_libdir}/lib*.la
rm -f %{buildroot}/%{_libdir}/getdata/lib*.la
# Remove simple docs, as we install them ourselves (along with others)
rm -f %{buildroot}/%{_datadir}/doc/%{name}/*
# Place fortran module in the correct location
mkdir -p %{buildroot}/%{_fmoddir}
mv %{buildroot}/%{_includedir}/getdata.mod  %{buildroot}/%{_fmoddir}/

%ldconfig_scriptlets

%files
%doc README NEWS COPYING AUTHORS TODO ChangeLog
%{_bindir}/dirfile2ascii
%{_bindir}/checkdirfile
%{_libdir}/libgetdata++.so.7*
%{_libdir}/libgetdata.so.8*

%dir %{_libdir}/getdata
%{_libdir}/getdata/libgetdataflac-0.11.0.so
%{_libdir}/getdata/libgetdatazzip-0.11.0.so
%{_mandir}/man5/*
%{_mandir}/man1/*

%files fortran
%{_libdir}/libf95getdata.so.7*
%{_libdir}/libfgetdata.so.6*

%files devel
%doc doc/README.cxx doc/README.f77 doc/unclean_database_recovery.txt
%{_libdir}/libgetdata.so
%{_libdir}/libf*getdata.so
%{_libdir}/libgetdata++.so
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/pkgconfig/getdata.pc
%{_fmoddir}/getdata.mod
%{_libdir}/getdata/libgetdataflac.so
%{_libdir}/getdata/libgetdatazzip.so

%files gzip
%{_libdir}/getdata/libgetdatagzip.so
%{_libdir}/getdata/libgetdatagzip-0.11.0.so

%files bzip2
%{_libdir}/getdata/libgetdatabzip2.so
%{_libdir}/getdata/libgetdatabzip2-0.11.0.so

%ifarch %{ix86} x86_64
%files slim
%{_libdir}/getdata/libgetdataslim.so
%{_libdir}/getdata/libgetdataslim-0.11.0.so
%endif

%files lzma
%{_libdir}/getdata/libgetdatalzma.so
%{_libdir}/getdata/libgetdatalzma-0.11.0.so

%changelog
%autochangelog
