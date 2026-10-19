%global source0_hash b93ff5561244916a6e1e7e3ecccf2e26e6932c4edb5961268401cea7d4ab9c16
%global abi_version 19
%bcond_with charls2
Name: dcmtk
Summary:        Offis DICOM Toolkit (DCMTK)
Version: 3.6.9
%global soname_version %{abi_version}.%{version}
Release:        1%{?dist}
License: BSD-3-Clause and Apache-2.0 and BSD-2-Clause and (WTFPL or MIT) and GPL-3.0-or-later and ISC and MIT
Source0:        https://dicom.offis.de/download/dcmtk/dcmtk369/dcmtk-%{version}.tar.gz
URL: http://dicom.offis.de/dcmtk.php.en
%if %{with charls2}
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
Patch:      0001-Increase-sleep-for-tests.patch
Patch:      0002-chore-undo-changes-to-standard-dirs.patch
Patch:      dcmtk-3.6.9-serialize-tls-certificate-tests.patch
%if %{with charls2}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/wlistdb/OFFIS/lockfile
%ldconfig_scriptlets
%oreon_autofiles dcmtk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch ppc64le s390x
rm -rf %{_vpath_builddir}/dcmtls/tests/
%endif
%ctest
%files -f %{oreon_filedir}/main.list
%files -n dcmtk-devel -f %{oreon_filedir}/dcmtk-devel.list

%changelog

%autochangelog
