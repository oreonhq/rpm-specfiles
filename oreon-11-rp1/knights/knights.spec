%global source0_hash a4ce42235f47bd5a90c87c9fb51c43de40bd325c7ba046634a36499bbd16dff3

%undefine __cmake_in_source_build

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:		knights
Version:	25.12.3
Release:	1%{?dist}
Summary:	A chess board for KDE

# KDE e.V. may determine that future GPL versions are accepted
License: GPL-2.0-only OR GPL-3.0-only
URL:     https://invent.kde.org/games/knights

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  libkdegames-devel >= 22.03.80
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules >= 5.240.0
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcrash-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kplotting-devel
BuildRequires:  kf6-kdoctools-devel
BuildRequires:  kf6-ktextwidgets-devel
BuildRequires:  kf6-kwallet-devel
BuildRequires:  kf6-plasma-devel
BuildRequires:  kf6-ksvg-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qt5compat-devel

Requires:	gnuchess

%description
Knights is a chess board for KDE that supports playing against
computer engines that support the XBoard protocol like GNUChess and also
multiplayer games over the internet on FICS. It features automatic rule
checking, themes, and nice animations

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.knights.desktop

%files -f %{name}.lang
%doc README* ChangeLog DESIGN doc/
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/org.kde.Knights.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/applications/org.kde.knights.desktop
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/metainfo/org.kde.knights.appdata.xml
%exclude %{_datadir}/doc/HTML/
%{_datadir}/qlogging-categories6/knights.categories
%{_datadir}/knsrcfiles/knights.knsrc
%{_datadir}/qlogging-categories6/knights.renamecategories

%changelog
%autochangelog
