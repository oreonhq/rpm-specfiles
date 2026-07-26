%global source0_hash fa0650c3edcd5dfd68d3a69a94c8f436224c71fabdcecfe521a2fd63e56992b9

Name:           deepin-pdfium
Version:        1.5.1
Release:        %autorelease
Summary:        development library for pdf on Deepin
# the library is under LGPL-3.0-or-later license
# pdfium: Apache-2.0
License:        LGPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/linuxdeepin/deepin-pdfium
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# add cstdint header to fix build
Patch0:         deepin-pdfium-fix-header.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  pkgconfig(chardet)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  libjpeg-turbo-devel

Provides:       bundled(pdfium)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CFLAGS="%{optflags} -fpermissive"
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdeepin-pdfium.so.1*

%files devel
%{_includedir}/deepin-pdfium/
%{_libdir}/libdeepin-pdfium.so
%{_libdir}/cmake/deepin-pdfium/
%{_libdir}/pkgconfig/deepin-pdfium.pc

%changelog
%autochangelog
