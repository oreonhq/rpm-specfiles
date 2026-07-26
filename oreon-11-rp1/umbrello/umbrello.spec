%global source0_hash 45714539df740badcbbd7cba63a8436786ff85ef071af8e5d04f4971e7d62dcb

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    umbrello
Summary: UML modeler and UML diagram tool
Version: 25.12.3
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://www.kde.org/applications/development/umbrello/

Source0: http://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: boost-devel
BuildRequires: pkgconfig(libxslt)
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)

%ifnarch s390x
BuildRequires: cmake(KDevelop-PG-Qt)
BuildRequires: cmake(KDevPlatform)
%endif

BuildRequires: cmake(LLVM)
BuildRequires: cmake(Clang)
BuildRequires: pkgconfig(cups)
BuildRequires: llvm-devel

Conflicts:      kdesdk-common < 4.10.80
Provides:       kdesdk-umbrello = %{version}-%{release}
Obsoletes:      kdesdk-umbrello < 4.10.80

Conflicts: kde-l10n < 17.08.3-2

%description
GUI for diagramming Unified Modeling Language (UML)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.umbrello.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.umbrello.desktop

%files -f %{name}.lang
%doc README
%license COPYING
%{_kf6_bindir}/umbrello6
%{_kf6_bindir}/po2xmi6
%{_kf6_bindir}/xmi2pot6
%{_kf6_metainfodir}/org.kde.umbrello.appdata.xml
%{_kf6_datadir}/applications/org.kde.umbrello.desktop
%{_kf6_datadir}/umbrello6/
%{_kf6_datadir}/icons/hicolor/*/*/*

%changelog
%autochangelog
