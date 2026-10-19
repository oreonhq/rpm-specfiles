%global source0_hash 5ae52e1f1a66bd7d0f1a9bcaccc80447e0b8ea181c40c87119b2427546ed0e26
%undefine __cmake_in_source_build
%bcond_without tests
%global optflags %(echo %{optflags} -Wl,--as-needed | sed "/-Wl,--as-needed/!s/$/ -Wl,--as-needed/")
%global _kf5_iconsdir %{_datadir}/icons
Name:       smb4k
Version:    4.0.6
Release:        1%{?dist}
Summary:        The SMB/CIFS Share Browser for KDE
License:    GPL-2.0-or-later
URL:        https://smb4k.sourceforge.net/
Source0:        https://downloads.sourceforge.net/smb4k/%{name}-%{version}.tar.xz
Requires:   kf6-kirigami
Requires:   samba-client
Requires:   cifs-utils
%{?_qt6_version:Requires: qt6-qtbase%{?_isa} >= %{_qt6_version}}
# oreon:deps
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(KDSoapWSDiscoveryClient)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(smbclient)
# /oreon:deps
%description
Smb4K is an SMB/CIFS share browser for KDE. It uses the Samba software suite to
access the SMB/CIFS shares of the local network neighborhood. Its purpose is to
provide a program that's easy to use and has as many features as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{cmake_kf6} -Wno-dev -DSMB4K_WITH_WS_DISCOVERY=ON
%cmake_build
%install
%cmake_install
desktop-file-install \
    --add-category Network \
    --delete-original \
    %{buildroot}%{_kf6_datadir}/applications/org.kde.smb4k.desktop
sed -i  %{buildroot}/%{_kf6_metainfodir}/*.appdata.xml -e 's/type="stock"//'
appstream-util validate-relax --nonet %{buildroot}/%{_kf6_metainfodir}/*.appdata.xml
%find_lang %{name} --with-html --all-name
%oreon_autofiles main

%check

%if %{with tests}
%ctest
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
