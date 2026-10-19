%global source0_hash d9a6c10537d64a285bc465675fe59aaa94ce3223823dfbecf0ae2c9599082d57
%global link_tcmalloc 1
%global development 0
%if 0%{?development}
%global commit 4059ae5bcad8e18443bf8f37bcff84de1dcc0d03
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%endif
ExcludeArch:    %{ix86}
Name:           rawtherapee
%if 0%{?development}
Version:        5.9~20221002git%{shortcommit}
%else
Version:        5.12
%endif
Release:        1%{?dist}
Summary:        Raw image processing software
License:        GPL-3.0-or-later and AGPL-3.0-or-later and MIT-open-group and IJG and BSL-1.0 and Apache-2.0
URL:            http://www.rawtherapee.com/
%if 0%{?development}
Source0:        https://github.com/Beep658%{link_tcmalloc}/RawTherapee/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        create_ReleaseInfo.sh
Source2:        ReleaseInfo.cmake
%else
%endif
Patch:          0001-Fix-static-init-order-fiasco-crashes.patch
Patch:          0001-Fix-typos.patch
%if 0%{?link_tcmalloc}
%endif
Requires:       hicolor-icon-theme
Provides:       bundled(dcraw) = 9.27
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  klt-devel
BuildRequires:  libappstream-glib
BuildRequires:  libatomic
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Rawtherapee is a RAW image processing software. It gives full control over
many parameters to enhance the raw picture before finally exporting it
to some common image format.

%prep

%if 0%{?development}
%autosetup -p1 -n RawTherapee-%{commit}
cp -p %SOURCE2 .
%else
%autosetup -p1 -n %{name}-%{version}
%endif

# remove bundled KLT, so we're sure to use system provided KLT
rm -rf rtengine/klt/

# remove bundled libraw, so we're sure to use system provided libraw
rm -rf rtengine/libraw/

%build

%{cmake} \
        -DCMAKE_BUILD_TYPE=release \
        -DLIBDIR=%{_libdir} \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
%if 0%{?link_tcmalloc}
        -DENABLE_TCMALLOC=ON \
%endif
        -DWITH_SYSTEM_KLT=ON \
        -DWITH_SYSTEM_LIBRAW="ON" \
        -DWITH_JXL="ON"
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/doc
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/com.%{name}.RawTherapee.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
