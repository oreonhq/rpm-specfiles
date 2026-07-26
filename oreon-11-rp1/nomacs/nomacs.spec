%global source0_hash 0842ce44999fe6a315069ca06b1b3d189dcb34308c8b359b83c453eb76366c0f

%global github_owner    nomacs

Name:		nomacs
Summary:	Lightweight image viewer
Version:	3.22.0
Release:	5%{?dist}
# Automatically converted from old format: GPLv3+ and CC-BY - review is highly recommended.
License:	GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY
Url:		http://nomacs.org
Source0:	https://github.com/%{github_owner}/%{name}/releases/tag/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	qt6-linguist
BuildRequires:	qt6-qttools-devel
# qt6-qtsvg-devel
BuildRequires:	cmake(Qt6Svg)
# quazip-qt6-devel
BuildRequires:	cmake(QuaZip-Qt6)
# exiv2-devel
BuildRequires:	pkgconfig(exiv2) >= 0.20
# opencv-devel
BuildRequires:	pkgconfig(opencv) >= 2.1.0
# LibRaw-devel
BuildRequires:	pkgconfig(libraw) >= 0.12.0
# libtiff-devel
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	lcov
Obsoletes:	nomacs-plugins < %{version}
Recommends:	qt6-qtimageformats
Recommends:	kf6-kimageformats

%description
nomacs is image viewer based on Qt5 library.
nomacs is small, fast and able to handle the most common image formats.
Additionally it is possible to synchronize multiple viewers
running on the same computer or via LAN is possible.
It allows to compare images and spot the differences
e.g. schemes of architects to show the progress).

%package  plugins
Summary:  Plugins for nomacs image viewer.
# qt6-qt5compat-devel
BuildRequires:  cmake(Qt6Core5Compat)
Requires: %{name} = %{version}-%{release}

%description  plugins
Some usefull plugins for nomacs:
- Affine transformations
- RGB image from greyscales
- Fake miniature filter
- Page extractions
- Painting

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup
# Be sure
rmdir {3rd-party/*,3rd-party}

%build
%cmake -S ImageLounge -DCMAKE_BUILD_TYPE=Release -DENABLE_QUAZIP=ON
%{cmake_build}

%install
%{cmake_install}
%find_lang %{name} --with-qt --without-mo
# workaround errors wrt to spaces
sed -i -e 's|Image Lounge|Image?Lounge|g' %{name}.lang

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.nomacs.ImageLounge.desktop

%files -f %{name}.lang
%license ImageLounge/license/*
%doc README.md
%{_bindir}/%{name}
%{_libdir}/libnomacsCore.so*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/Image?Lounge/themes/
%dir %{_datadir}/%{name}/Image?Lounge/
%dir %{_datadir}/%{name}/Image?Lounge/translations/
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/%{name}.*

%files  plugins
%license ImageLounge/license/*
%{_libdir}/nomacs-plugins/

%changelog
%autochangelog
