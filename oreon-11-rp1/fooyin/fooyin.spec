%global source0_hash ebd630c6d7b2811498fcae33e030caf6b2fccb6c98e93497c00628876684ba83
Name:           fooyin
Version:        0.13.1
Release:        1%{?dist}
Summary:        A customizable music player
License:        GPL-3.0-or-later
URL:            https://www.fooyin.org/
Source0:        https://github.com/fooyin/fooyin/archive/v%{version}/fooyin-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(taglib)
# /oreon:deps
%description
fooyin is a music player built around customization. It provides a variety
of widgets to help you manage and play your local collection.

%package devel
Summary:        Support for developing fooyin plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides development files used to create plugins for fooyin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_LIBVGM=OFF -DBUILD_TESTING=ON -DINSTALL_HEADERS=ON
%cmake_build
%install
%cmake_install
%find_lang fooyin --with-qt
rm %{buildroot}%{_docdir}/fooyin/LICENSE
rm %{buildroot}%{_docdir}/fooyin/README
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest --test-dir %{_vpath_builddir}/tests/
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n fooyin-devel -f %{oreon_filedir}/fooyin-devel.list

%changelog

%autochangelog
