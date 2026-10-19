%global source0_hash 5de607e15f192b8ad90738300759d88dea0f5ccdce3bf00048a0c932bc645154
Name:           podofo0.9
Version:        0.9.8
Release:        1%{?dist}
Summary:        Podofo 0.9.x compatibility library
License:        GPL-2.0-or-later and LGPL-2.0-or-later WITH LGPL-3.0-linking-exception
URL:            http://podofo.sourceforge.net
Source0:        http://downloads.sourceforge.net/podofo/podofo-%{version}.tar.gz
Patch0:         podofo-0.9.4-freetype.patch
Patch1:         podofo_cmakever.patch
Patch20:        podofo_CVE-2019-20093.patch
Patch22:        podofo_maxbytes.patch
Patch23:        podofo-gcc12.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n podofo0.9-libs -f %{oreon_filedir}/podofo0.9-libs.list
%files -n podofo0.9-devel -f %{oreon_filedir}/podofo0.9-devel.list
%files -n podofo0.9-tools -f %{oreon_filedir}/podofo0.9-tools.list

%changelog

%autochangelog
