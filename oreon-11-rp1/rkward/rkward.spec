%global source0_hash be8abdfcd7a17aa5196f63e0136fdbc693e93d9f2f0ec66f2bdacacfc22b9ca8

Name:           rkward
Version:        0.8.2
Release:        2%{?dist}
Summary:        Graphical frontend for R language

License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://%{name}.kde.org/
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.gz
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.gz.sig
Source:         https://invent.kde.org/sysadmin/release-keyring/-/raw/master/keys/tfry@key1.asc?ref_type=heads#/signing-key.pgp

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-rpm-macros
BuildRequires:  R-core-devel

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

BuildRequires:  cmake(KDSingleApplication-qt6)

Requires:       hicolor-icon-theme
Requires:       shared-mime-info

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

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt LICENSES/MIT.txt LICENSES/LGPL-2.1-or-later.txt
%doc README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/kio/servicemenus/%{name}.protocol
%{_kf6_datadir}/ktexteditor_snippets/data/RKWard*.xml
%{_kf6_datadir}/metainfo/org.kde.%{name}.metainfo.xml
%{_kf6_datadir}/mime/packages/vnd.kde.rkward-output.xml
%{_kf6_datadir}/mime/packages/vnd.kde.rmarkdown.xml
%{_kf6_datadir}/mime/packages/vnd.rkward.r.xml
%{_kf6_libdir}/librkward.rbackend.lib.so
%{_kf6_mandir}/man1/%{name}.1*
%{_libexecdir}/%{name}.rbackend

%changelog
%autochangelog
