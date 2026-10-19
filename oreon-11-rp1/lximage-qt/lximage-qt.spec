%global source0_hash 0976c821c823cf1fedf0ec31312b88386306291dc83ea861e934744d12ac4ea4
Name:           lximage-qt
Version:        2.4.0
Release:        1%{?dist}
Summary:        The image viewer and screenshot tool for LXQt
License:        GPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libfm-qt6)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(xfixes)
# /oreon:deps
%description
The Qt port of LXImage, a simple and fast image viewer.

%package l10n
BuildArch:      noarch
Summary:        Translations for lximage-qt
Requires:       lximage-qt
%description l10n
This package provides translations for the lximage-qt package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
for desktop in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
done
%find_lang lximage-qt --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lximage-qt-l10n -f %{oreon_filedir}/lximage-qt-l10n.list

%changelog

%autochangelog
