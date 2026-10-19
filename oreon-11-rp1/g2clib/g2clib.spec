%global source0_hash 8520a24c066500cfd0d07a05c6b7b0cb92383d1a4737cf6e79d9f4919c8e79ab
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
Name:           g2clib
Version:        2.3.0
Release:        1%{?dist}
Summary:        GRIB2 encoder/decoder and search/indexing routines in C
License:        LGPL-3.0-only
URL:            https://github.com/NOAA-EMC/NCEPLIBS-g2c
Source0:        https://github.com/NOAA-EMC/NCEPLIBS-g2c/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
%global g2clib g2c
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  jasper-devel
BuildRequires:  libaec-devel
BuildRequires:  libpng-devel
# /oreon:deps
%description
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in ASCII file "grib2c.doc".

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-static = %{version}-%{release}
Requires:       jasper-devel%{?_isa}
Requires:       libpng-devel%{?_isa}
%description    devel
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in file "grib2c.doc".

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel = %{version}-%{release}
%description    static
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in file "grib2c.doc".

The %{name}-static package contains the g2c static library.

%package        utils
Summary:        %{name} utilities
Requires:       %{name} = %{version}-%{release}
%description    utils
The %{name}-utils package contains utilities for g2clib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir NCEPLIBS-g2c-%{version}
%oreon_prep
%build

%cmake -DENABLE_DOCS=ON \
  -DUSE_AEC=ON \
  -DPTHREADS=ON
%cmake_build
%install
mkdir -p $RPM_BUILD_ROOT%{macrosdir}
echo %%g2clib %g2clib > $RPM_BUILD_ROOT%{macrosdir}/macros.g2clib
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch s390x
%ctest --verbose || :
%else
%ctest --verbose
%endif
%files -f %{oreon_filedir}/main.list
%files -n g2clib-devel -f %{oreon_filedir}/g2clib-devel.list
%files -n g2clib-static -f %{oreon_filedir}/g2clib-static.list
%files -n g2clib-utils -f %{oreon_filedir}/g2clib-utils.list

%changelog

%autochangelog
