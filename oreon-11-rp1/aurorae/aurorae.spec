%global source0_hash f7dbc82de06a53dd2c3ff54ae542351485cd5b27e071fada5bb7fc87911054f3

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           aurorae
Summary:        Aurorae is a themeable window decoration for KWin
Version:        6.6.4
Release:        1%{?dist}
License:        GPL-2.0-or-later AND MIT AND CC0-1.0
URL:            https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: cmake(KDecoration3)

# Account for being split out of kwin
Conflicts:     kwin < 6.3.90
Supplements:   kwin%{?_isa} >= %{version}

%description
Aurorae is a themeable window decoration for KWin.
It supports theme files consisting of several SVG files for
decoration and buttons. Themes can be installed and selected
directly in the configuration module of KWin decorations.
Please have a look at theme-description on how to write a theme file.

%package devel
Summary: Development libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS TODO
%license LICENSES/*
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_auroraedecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.so
%{_kf6_qmldir}/org/kde/kwin/decoration/AppMenuButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/ButtonGroup.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/Decoration.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/DecorationButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/MenuButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/libdecorationplugin.so
%{_kf6_qmldir}/org/kde/kwin/decoration/qmldir
%{_kf6_qmldir}/org/kde/kwin/decorations/plastik/libplastikplugin.so
%{_kf6_qmldir}/org/kde/kwin/decorations/plastik/qmldir
%{_libexecdir}/plasma-apply-aurorae
%{_kf6_datadir}/knsrcfiles/aurorae.knsrc
%{_kf6_datadir}/kwin/aurorae/
%{_kf6_datadir}/kwin/decorations/kwin4_decoration_qml_plastik/
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.v2.so

%files devel
%{_kf6_libdir}/cmake/Aurorae/

%changelog
%autochangelog
