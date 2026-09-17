%global source0_hash e03e6b01dac55e50ac1a1381f21fb2c9b16a39ef5fc42542f7b9ea22e39cb416

Name:           lximage-qt
Version:        2.3.0
Release:        2%{?dist}
Summary:        The image viewer and screenshot tool for LXQt
License:        GPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(libfm-qt6)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  desktop-file-utils
BuildRequires:  perl

# we place additional files in icons/hicolor
Requires:       hicolor-icon-theme

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

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
for desktop in %{buildroot}/%{_datadir}/applications/*.desktop; do
    # Exclude category as been Service
    desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
done
%find_lang lximage-qt --with-qt

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/%{name}
%{_datadir}/metainfo/lximage-qt.metainfo.xml

%files l10n -f lximage-qt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lximage-qt/translations

%changelog
%autochangelog
