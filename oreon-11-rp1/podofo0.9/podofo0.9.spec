%global source0_hash 5de607e15f192b8ad90738300759d88dea0f5ccdce3bf00048a0c932bc645154

Name:           podofo0.9
Version:        0.9.8
Release:        9%{?dist}
Summary:        Podofo 0.9.x compatibility library

# The library is licensed under the LGPL.
# The tests and tools which are included in PoDoFo are licensed under the GPL.
# See the files COPYING and COPYING.LIB for details, see COPYING.exception.
License:        GPL-2.0-or-later and LGPL-2.0-or-later WITH LGPL-3.0-linking-exception
URL:            http://podofo.sourceforge.net
Source0:        http://downloads.sourceforge.net/podofo/podofo-%{version}.tar.gz
# Fix failure to detect FreeType
Patch0:         podofo-0.9.4-freetype.patch
# Raise minimum cmake version
Patch1:         podofo_cmakever.patch

# Downstream patch for CVE-2019-20093
# https://sourceforge.net/p/podofo/tickets/75/
Patch20:        podofo_CVE-2019-20093.patch
# https://sourceforge.net/p/podofo/tickets/101/
Patch22:        podofo_maxbytes.patch
# Comment out some asserts in the testsuite which fail to build with gcc12
Patch23:        podofo-gcc12.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
Podofo 0.9.x compatibility library.

%package libs
Summary:        Runtime library for %{name}

%description libs
Runtime library for %{name}.

%package devel
Summary:        Development files for %{name} library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}
Conflicts:      podofo-devel

%description devel
Development files for the %{name} library.

%package tools
Summary:        Tools for %{name}

%description tools
Tools for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n podofo-%{version}

# switch to system provided files
rm cmake/modules/FindFREETYPE.cmake
rm cmake/modules/FindZLIB.cmake

%build
%cmake \
%if 0%{?__isa_bits} == 64
-DWANT_LIB64=1 \
%endif
-DPODOFO_BUILD_SHARED=1
%cmake_build

%install
%cmake_install

%files libs
%license COPYING.LIB COPYING.exception
%{_libdir}/*.so.0.9.8

%files devel
%{_includedir}/podofo/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpodofo.pc

%files tools
%{_bindir}/podofo*
%{_mandir}/man1/podofo*.1*

%changelog
%autochangelog
