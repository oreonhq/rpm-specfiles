%global source1_hash 082879328a3b3d34f1f321fe23aa8c169d012a0a994f040a0407a0f98e699f66
%global source0_hash b2d6cfb36dbe6a408f22c9ddabdae623eb7aa0de15485827f30a725a645e6e0f
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    plasma-sdk
Version:        6.7.5
Release:        1%{?dist}
Summary:        Development tools for Plasma 6
License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
Requires:       hicolor-icon-theme
Obsoletes:      plasmate < 5.2
Provides:       plasmate = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
Plasma SDK contains tools for plasma development

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang plasmasdk6 --with-man --with-qt --all-name
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasma.themeexplorer.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.iconexplorer.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasmaengineexplorer.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasmoidviewer.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasma.lookandfeelexplorer.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
