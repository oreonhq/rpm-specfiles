
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    krfb
Summary: Desktop sharing
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-only AND LGPL-2.1-only AND GFDL-1.2-no-invariants-only
URL:     https://apps.kde.org/krfb/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: hicolor-icon-theme

BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: qt6-qtbase-private-devel
BuildRequires: lzo-devel
BuildRequires: libpng-devel
BuildRequires: libgcrypt-devel
BuildRequires: openssl-devel

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KPipeWire)
BuildRequires: cmake(KWayland)

BuildRequires: pipewire-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libvncserver)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-shape)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(libsystemd)

BuildRequires: pkgconfig(xtst)
BuildRequires: libjpeg-devel
BuildRequires: libepoxy-devel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# when split occurred
Conflicts: kdenetwork-common < 7:4.10.80
Obsoletes: kdenetwork-krfb < 7:4.10.80
Provides:  kdenetwork-krfb = 7:%{version}-%{release}

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: kdenetwork-krfb-libs < 7:4.10.80
Provides:  kdenetwork-krfb-libs = 7:%{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.krfb.desktop


%files -f %{name}.lang
%license COPYING*
%doc README AUTHORS
%{_kf6_bindir}/krfb
# package seperately? -- rdieter
%{_kf6_bindir}/krfb-virtualmonitor
%{_kf6_datadir}/krfb/
%{_kf6_datadir}/applications/org.kde.krfb.desktop
%{_kf6_datadir}/applications/org.kde.krfb.virtualmonitor.desktop
%{_kf6_metainfodir}/org.kde.krfb.appdata.xml
%{_kf6_datadir}/qlogging-categories6/*categories
%{_datadir}/icons/hicolor/*/apps/krfb.*

%files libs
%{_kf6_libdir}/libkrfbprivate.so.5*
%{_kf6_qtplugindir}/krfb/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
