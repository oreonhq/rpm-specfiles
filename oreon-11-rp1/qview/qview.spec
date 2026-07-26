%global source0_hash 0d7ab3aaea2e9f89034bdeeb6350d31a5d9fb5ac9158b98348e8ccbf1dc6570a

%global appid com.interversehq.qView
%global upstream_name qView

Name:           qview
Version:        6.1
Release:        8%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Summary:        Practical and minimal image viewer
URL:            https://interversehq.com/qview/
Source:         https://github.com/jurplel/%{upstream_name}/releases/download/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-rpm-macros

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5X11Extras)

Requires: hicolor-icon-theme
Requires: kf5-kimageformats
Requires: qt5-qtimageformats
Requires: qt5-qtsvg

%description
qView is a Qt image viewer designed with minimalism and usability in mind. It
is designed to get out of your way and let you view your image without excess
GUI elements, while also being flexible enough for everyday use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}

%build
PREFIX=%{_prefix} %qmake_qt5
%make_build

%install
INSTALL_ROOT="%{buildroot}" %make_install

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%files
%doc README.md

%license LICENSE

%{_bindir}/%{name}

%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appid}.*
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg

%{_metainfodir}/%{appid}.appdata.xml

%changelog
%autochangelog
