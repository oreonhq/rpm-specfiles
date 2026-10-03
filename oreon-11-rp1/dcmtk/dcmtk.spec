%global source0_hash b93ff5561244916a6e1e7e3ecccf2e26e6932c4edb5961268401cea7d4ab9c16

# Notes on soname versioning
# There's absolutely no guarantee of ABI stability, so a soname bump is
# included for every new release:
# https://github.com/DCMTK/dcmtk/blob/master/CMake/dcmtkPrepare.cmake#L37

# Odd number releases are dev snapshots, so we will stick to even number
# (official releases) only.

%global abi_version 19

%bcond_with charls2

Name: dcmtk
Summary: Offis DICOM Toolkit (DCMTK)
Version: 3.6.9

# soname version is "abi_version.version"
# https://github.com/DCMTK/dcmtk/blob/master/CMake/dcmtkPrepare.cmake#L78
%global soname_version %{abi_version}.%{version}

Release: 5%{?dist}

# see licenses-3.6.9.txt for license breakdown
License: BSD-3-Clause and Apache-2.0 and BSD-2-Clause and (WTFPL or MIT) and GPL-3.0-or-later and ISC and MIT
Source: https://dicom.offis.de/download/dcmtk/dcmtk369/dcmtk-%{version}.tar.gz
URL: http://dicom.offis.de/dcmtk.php.en

# Downstream fixes
# Use bundled charls version and wait until upstream ports to new charls version
# charls version 2 includes a regression: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=923433
%if %{with charls2}
# not merged upstream yet: https://github.com/DCMTK/dcmtk/pull/18
# were generated against 3.6.7, not yet updated for 3.6.8
Patch:      0001-Use-system-CharLS-include.patch
Patch:      0002-Add-FindCharLS.patch
Patch:      0003-Find-and-include-CharLS.patch
Patch:      0004-Use-cmake-suggested-locations-for-CharLS.patch
Patch:      0005-Correct-CharLS-API-call.patch
Patch:      0006-Remove-reference-to-bundled-CharLS.patch
Patch:      0007-Update-JLS_ERROR-to-jpegls_error-in-CharLS-usage.patch
Patch:      0008-Correct-JpegLsReadHeader-arguments.patch
Patch:      0009-Update-JlsParameters-for-new-CharLS.patch
Patch:      0010-Correct-JpegLsDecode-arguments-for-CharLS-2.patch
Patch:      0011-Update-ilv-for-new-CharLS.patch
Patch:      0012-Correct-extra-include-for-CharLS.patch
Patch:      0013-Update-errors-to-use-enum-class-in-CharLS-2.patch
Patch:      0014-Define-BYTE-for-CharLS.patch
Patch:      0015-Update-colorTransformation-for-CharLS-2.patch
Patch:      0016-Update-JpegLsEncode-for-CharLS-2.patch
%endif

# Upstream fixes, backported to 3.6.9:
# https://github.com/sanjayankur31/dcmtk/tree/fedora-3.6.9

# Increase sleep in tests
# https://forum.dcmtk.org/viewtopic.php?t=5084
Patch:      0001-Increase-sleep-for-tests.patch

# place in correct locations
Patch:      0002-chore-undo-changes-to-standard-dirs.patch
Patch:      dcmtk-3.6.9-serialize-tls-certificate-tests.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: cmake
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libxml2-devel
BuildRequires: openssl-devel >= 1.0.1
BuildRequires: zlib-devel
%if %{with charls2}
BuildRequires: CharLS-devel >= 2.0.0
%endif
BuildRequires: doxygen

%description
DCMTK is a collection of libraries and applications implementing large
parts the DICOM standard. It includes software for examining,
constructing and converting DICOM image files, handling offline media,
sending and receiving images over a network connection, as well as
demonstrative image storage and worklist servers. DCMTK is is written
in a mixture of ANSI C and C++.  It comes in complete source code and
is made available as "open source" software. This package includes
multiple fixes taken from the "patched DCMTK" project.

Install DCMTK if you are working with DICOM format medical image files.

%package devel
Summary: Development Libraries and Headers for dcmtk
Requires: %{name}%{?_isa} = %{version}-%{release}
%if %{with charls2}
Requires: CharLS-devel%{?_isa}
%endif
Requires: libpng-devel%{?_isa}
Requires: libtiff-devel%{?_isa}

%description devel
Development Libraries and Headers for dcmtk.  You only need to install
this if you are developing programs that use the dcmtk libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1 -S git

%if %{with charls2}
# Remove bundled libraries
rm -rf dcmjpls/libcharls/
%endif

# Fix permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.cc" -exec chmod 0644 '{}' \;

%build
export CFLAGS="%{optflags} -fPIC -Wno-error=deprecated-declarations"
export CXXFLAGS="%{optflags} -fPIC -Wno-error=deprecated-declarations"
export LDFLAGS="%{__global_ldflags} -fPIC"
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
 -DDCMTK_INSTALL_LIBDIR=%{_lib} \
 -DDCMTK_INSTALL_CMKDIR=%{_lib}/cmake/%{name} \
 -DCMAKE_INSTALL_DOCDIR:PATH=%{_pkgdocdir} \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=include \
 -DCMAKE_INSTALL_MANDIR:PATH=%{_mandir} \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
 -DCMAKE_INSTALL_DATADIR:PATH=share \
 -DBUILD_APPS:BOOL=ON \
 -DBUILD_SHARED_LIBS:BOOL=ON \
 -DBUILD_SINGLE_SHARED_LIBRARY:BOOL=OFF \
 -DDCMTK_WITH_OPENSSL:BOOL=ON \
 -DDCMTK_WITH_PNG:BOOL=ON \
 -DDCMTK_WITH_PRIVATE_TAGS:BOOL=ON \
 -DDCMTK_WITH_TIFF:BOOL=ON \
 -DDCMTK_WITH_XML:BOOL=ON \
 -DDCMTK_WITH_CHARLS:BOOL=ON \
 -DDCMTK_WITH_ZLIB:BOOL=ON \
 -DDCMTK_ENABLE_CXX11:BOOL=ON \
 -Wno-dev
%cmake_build

%install
%cmake_install

# Remove zero-lenght file
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/wlistdb/OFFIS/lockfile

%ldconfig_scriptlets

%check
# ppc64le, s390x: remove dcmtls_scp_tls and dcmtls_scp_pool_tls that sporadically fails
%ifarch ppc64le s390x
rm -rf %{_vpath_builddir}/dcmtls/tests/
%endif
%ctest

%files
%license COPYRIGHT
%{_pkgdocdir}/
%{_bindir}/*
%{_libdir}/libdcmfg.so.%{soname_version}
%{_libdir}/libcmr.so.%{abi_version}
%{_libdir}/libcmr.so.%{soname_version}
%{_libdir}/libdcmdata.so.%{abi_version}
%{_libdir}/libdcmdata.so.%{soname_version}
%{_libdir}/libdcmdsig.so.%{abi_version}
%{_libdir}/libdcmdsig.so.%{soname_version}
%{_libdir}/libdcmect.so.%{abi_version}
%{_libdir}/libdcmect.so.%{soname_version}
%{_libdir}/libdcmfg.so.%{abi_version}
%{_libdir}/libdcmimage.so.%{abi_version}
%{_libdir}/libdcmimage.so.%{soname_version}
%{_libdir}/libdcmimgle.so.%{abi_version}
%{_libdir}/libdcmimgle.so.%{soname_version}
%{_libdir}/libdcmiod.so.%{abi_version}
%{_libdir}/libdcmiod.so.%{soname_version}
%{_libdir}/libdcmjpeg.so.%{abi_version}
%{_libdir}/libdcmjpeg.so.%{soname_version}
%{_libdir}/libdcmjpls.so.%{abi_version}
%{_libdir}/libdcmjpls.so.%{soname_version}
%{_libdir}/libdcmnet.so.%{abi_version}
%{_libdir}/libdcmnet.so.%{soname_version}
%{_libdir}/libdcmpmap.so.%{abi_version}
%{_libdir}/libdcmpmap.so.%{soname_version}
%{_libdir}/libdcmpstat.so.%{abi_version}
%{_libdir}/libdcmpstat.so.%{soname_version}
%{_libdir}/libdcmqrdb.so.%{abi_version}
%{_libdir}/libdcmqrdb.so.%{soname_version}
%{_libdir}/libdcmrt.so.%{abi_version}
%{_libdir}/libdcmrt.so.%{soname_version}
%{_libdir}/libdcmseg.so.%{abi_version}
%{_libdir}/libdcmseg.so.%{soname_version}
%{_libdir}/libdcmsr.so.%{abi_version}
%{_libdir}/libdcmsr.so.%{soname_version}
%{_libdir}/libdcmtkcharls.so.%{abi_version}
%{_libdir}/libdcmtkcharls.so.%{soname_version}
%{_libdir}/libdcmtls.so.%{abi_version}
%{_libdir}/libdcmtls.so.%{soname_version}
%{_libdir}/libdcmtract.so.%{abi_version}
%{_libdir}/libdcmtract.so.%{soname_version}
%{_libdir}/libdcmwlm.so.%{abi_version}
%{_libdir}/libdcmwlm.so.%{soname_version}
%{_libdir}/libdcmxml.so.%{abi_version}
%{_libdir}/libdcmxml.so.%{soname_version}
%{_libdir}/libi2d.so.%{abi_version}
%{_libdir}/libi2d.so.%{soname_version}
%{_libdir}/libijg16.so.%{abi_version}
%{_libdir}/libijg16.so.%{soname_version}
%{_libdir}/libijg12.so.%{abi_version}
%{_libdir}/libijg12.so.%{soname_version}
%{_libdir}/libijg8.so.%{abi_version}
%{_libdir}/libijg8.so.%{soname_version}
%{_libdir}/liboficonv.so.%{abi_version}
%{_libdir}/liboficonv.so.%{soname_version}
%{_libdir}/liboflog.so.%{abi_version}
%{_libdir}/liboflog.so.%{soname_version}
%{_libdir}/libofstd.so.%{abi_version}
%{_libdir}/libofstd.so.%{soname_version}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/consolog.cfg
%config(noreplace) %{_sysconfdir}/%{name}/dcmpstat.cfg
%config(noreplace) %{_sysconfdir}/%{name}/dcmqrprf.cfg
%config(noreplace) %{_sysconfdir}/%{name}/dcmqrscp.cfg
%config(noreplace) %{_sysconfdir}/%{name}/printers.cfg
%config(noreplace) %{_sysconfdir}/%{name}/storescp.cfg
%config(noreplace) %{_sysconfdir}/%{name}/storescu.cfg
%config(noreplace) %{_sysconfdir}/%{name}/filelog.cfg
%config(noreplace) %{_sysconfdir}/%{name}/logger.cfg
%{_datadir}/%{name}/
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/
%{_libdir}/libcmr.so
%{_libdir}/libdcmdata.so
%{_libdir}/libdcmdsig.so
%{_libdir}/libdcmect.so
%{_libdir}/libdcmfg.so
%{_libdir}/libdcmimgle.so
%{_libdir}/libdcmimage.so
%{_libdir}/libdcmiod.so
%{_libdir}/libdcmjpeg.so
%{_libdir}/libdcmjpls.so
%{_libdir}/libdcmnet.so
%{_libdir}/libdcmpmap.so
%{_libdir}/libdcmpstat.so
%{_libdir}/libdcmqrdb.so
%{_libdir}/libdcmrt.so
%{_libdir}/libdcmseg.so
%{_libdir}/libdcmsr.so
%{_libdir}/libdcmtkcharls.so
%{_libdir}/libdcmtls.so
%{_libdir}/libdcmtract.so
%{_libdir}/libdcmwlm.so
%{_libdir}/libdcmxml.so
%{_libdir}/libi2d.so
%{_libdir}/libijg16.so
%{_libdir}/libijg12.so
%{_libdir}/libijg8.so
%{_libdir}/liboficonv.so
%{_libdir}/liboflog.so
%{_libdir}/libofstd.so

%changelog
%autochangelog
