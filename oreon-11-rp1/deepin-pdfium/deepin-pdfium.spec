%global source0_hash a49c82949b8718603a92102238860b75f0b33586ee5d3ecb2547929dc32f418f
Name:           deepin-pdfium
Version:        1.5.8
Release:        1%{?dist}
Summary:        development library for pdf on Deepin
License:        LGPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/linuxdeepin/deepin-pdfium
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         deepin-pdfium-fix-header.patch
Provides:       bundled(pdfium)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(chardet)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libopenjp2)
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{optflags} -fpermissive"
%cmake -GNinja
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n deepin-pdfium-devel -f %{oreon_filedir}/deepin-pdfium-devel.list

%changelog

%autochangelog
