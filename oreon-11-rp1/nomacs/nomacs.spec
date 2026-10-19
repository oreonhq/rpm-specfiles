%global source0_hash 0842ce44999fe6a315069ca06b1b3d189dcb34308c8b359b83c453eb76366c0f
%global github_owner    nomacs
Name:		nomacs
Summary:        Lightweight image viewer
Version:	3.23.3
Release:        1%{?dist}
License:	GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY
Url:		http://nomacs.org
Source0:        https://github.com/%{name}/%{name}/releases/tag/%{name}-%{version}.tar.gz
Obsoletes:	nomacs-plugins < %{version}
Recommends:	qt6-qtimageformats
Recommends:	kf6-kimageformats
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(QuaZip-Qt6)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lcov
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
nomacs is image viewer based on Qt5 library.
nomacs is small, fast and able to handle the most common image formats.
Additionally it is possible to synchronize multiple viewers
running on the same computer or via LAN is possible.
It allows to compare images and spot the differences
e.g. schemes of architects to show the progress).

%package  plugins
Summary:  Plugins for nomacs image viewer.
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
sed -i -e 's|Image Lounge|Image?Lounge|g' %{name}.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.nomacs.ImageLounge.desktop
%files -f %{oreon_filedir}/main.list
%files -n nomacs-plugins -f %{oreon_filedir}/nomacs-plugins.list

%changelog

%autochangelog
