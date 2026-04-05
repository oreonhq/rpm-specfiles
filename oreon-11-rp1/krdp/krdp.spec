%global qt6minver 6.6.0
%global kf6minver 6.2


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           krdp
Summary:        Desktop sharing using RDP
Version:        6.6.2
Release:	2%{?dist}

License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/plasma/krdp
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig


BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  extra-cmake-modules >= %{kf6minver}
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Crash) >= %{kf6minver}
BuildRequires:  cmake(KF6Config) >= %{kf6minver}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6minver}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6minver}
BuildRequires:  cmake(KF6I18n) >= %{kf6minver}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6minver}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6minver}
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  qt6-qtbase-private-devel >= %{qt6minver}
BuildRequires:  cmake(Qt6Core) >= %{qt6minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6minver}
BuildRequires:  cmake(Qt6Network) >= %{qt6minver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6minver}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6minver}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(FreeRDP) >= 3.1
BuildRequires:  cmake(WinPR) >= 3.1
BuildRequires:  cmake(FreeRDP-Server) >= 3.1
BuildRequires:  cmake(KPipeWire) >= 5.27.80
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  /usr/bin/winpr-makecert
Requires:       /usr/bin/openssl

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-server < 6.0.90
Provides:       %{name}-server = %{version}-%{release}
Provides:       %{name}-server%{?_isa} = %{version}-%{release}

%description
%{summary}.


%package libs
Summary:        Library for creating an RDP server
Requires:       /usr/bin/winpr-makecert
Conflicts:      %{name} < 6.0.90
Conflicts:      %{name}-server < 6.0.90

%description libs
%{summary}.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-html --all-name

%post
%systemd_user_post app-org.kde.krdpserver.service

%preun
%systemd_user_preun app-org.kde.krdpserver.service

%postun
%systemd_user_postun_with_restart app-org.kde.krdpserver.service
%systemd_user_postun_with_reload app-org.kde.krdpserver.service
%systemd_user_postun app-org.kde.krdpserver.service

%files -f %{name}.lang
%doc README.md
%{_kf6_bindir}/krdpserver
%{_kf6_datadir}/applications/kcm_krdpserver.desktop
%{_kf6_datadir}/applications/org.kde.krdpserver.desktop
%{_kf6_datadir}/qlogging-categories6/kcm_krdpserver.categories
%{_kf6_datadir}/qlogging-categories6/krdp.categories
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_krdpserver.so
%{_userunitdir}/app-org.kde.krdpserver.service
%{_userpresetdir}/00-krdp.preset

%files libs
%license LICENSES/LGPL-*.txt LICENSES/LicenseRef-KDE-*
%{_kf6_libdir}/libKRdp.so.6{,.*}

%files devel
%{_kf6_libdir}/libKRdp.so
%{_kf6_libdir}/cmake/KRdp/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
