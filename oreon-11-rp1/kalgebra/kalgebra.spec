%global source0_hash e8740deba96ba4d47079695a34f41850a080a631ba318fab88e9d744825d92ae

%global stable_kf6 stable


Name:    kalgebra
Summary: 2D and 3D Graph Calculator
Version: 26.08.1
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later
URL:     https://apps.kde.org/kalgebra/
Source:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6OpenGLWidgets)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: qt6-qtwebengine-devel >= 6.11.1-5

BuildRequires: cmake(Analitza6)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(Plasma)

# calgebra deps
BuildRequires: ncurses-devel readline-devel

Recommends: (%{name}-plasma-applet%{?_isa} = %{version}-%{release} if plasma-workspace)

%description
%{summary}.

%package plasma-applet
Summary:        Plasma plotting applet
Requires:       %{name}%{?_isa} = %{version}-%{release}
# QML module dependencies
Requires:       libplasma%{?_isa}

%description plasma-applet
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kalgebra.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kalgebramobile.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kalgebra.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kalgebramobile.desktop


%files -f %{name}.lang
%doc TODO
%license COPYING*
%{_kf6_bindir}/calgebra
%{_kf6_bindir}/kalgebra
%{_kf6_bindir}/kalgebramobile
%{_datadir}/icons/hicolor/*/*/kalgebra.*
%{_kf6_metainfodir}/org.kde.kalgebra.appdata.xml
%{_kf6_metainfodir}/org.kde.kalgebramobile.appdata.xml
%{_kf6_datadir}/applications/org.kde.kalgebra.desktop
%{_kf6_datadir}/applications/org.kde.kalgebramobile.desktop
%{_kf6_datadir}/katepart5/syntax/kalgebra.xml

%files plasma-applet
%{_kf6_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/


%changelog
%autochangelog
