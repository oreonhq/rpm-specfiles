%global source0_hash bc28a133ce320df0dbcfbeea8a0205407fcb21aac7e881ca4b741d14f2d9f0b7
Name:           photoqt
Version:        5.4.1
Release:        1%{?dist}
Summary:        A fast Qt image viewer
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            http://photoqt.org/
Source0:        https://photoqt.org/downloads/source/%{name}-%{version}.tar.gz
Requires:       python3-chromecast
Requires:       qt6-qtcharts
Requires:       qt6-qtdeclarative
Requires:       qt6-qtmultimedia
Recommends:     kf6-kimageformats
Recommends:     xcftools
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(exiv2)
BuildRequires:  cmake(phonon4qt6)
BuildRequires:  cmake(pugixml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  freeimage-plus-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(vips)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-chromecast
BuildRequires:  python3-devel
BuildRequires:  zxing-cpp-devel
# /oreon:deps
%description
PhotoQt is a fast and highly configurable image viewer with a simple and
nice interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake -DVIDEO_MPV=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.PhotoQt.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.%{name}.PhotoQt.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
