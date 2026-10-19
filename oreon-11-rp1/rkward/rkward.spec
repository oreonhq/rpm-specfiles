%global source0_hash 40d2a6b6ddc77cb226ccd97037350235ca12d3a422f31b1f9ae3c01be427f5e5
Name:           rkward
Version:        0.8.3
Release:        1%{?dist}
Summary:        Graphical frontend for R language
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://%{name}.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.gz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
# oreon:deps
BuildRequires:  R-core-devel
BuildRequires:  cmake
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6BreezeIcons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
RKWard aims to provide an easily extensible, easy to use IDE/GUI for the
R-project. RKWard tries to combine the power of the R-language with the
(relative) ease of use of commercial statistics tools. Long term plans
include integration with office suites

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
rm -rf 3rdparty

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%find_lang %{name} --all-name --with-kde --with-html --with-man
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
