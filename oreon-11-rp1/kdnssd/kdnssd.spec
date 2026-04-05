%global base_name kio-zeroconf


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdnssd
Summary: KDE Network Monitor for DNS-SD services (Zeroconf)
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-or-later AND LGPL-2.0-only
URL:     https://invent.kde.org/network/%{base_name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

# new upstream name in 4.12.95
Provides: %{base_name} = %{version}-%{release}

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(Qt6Core)

BuildRequires: pkgconfig(avahi-compat-libdns_sd)

# when split occurred
Conflicts: kdenetwork-common < 7:4.10.80
Obsoletes: kdenetwork-kdnssd < 7:4.10.80
Conflicts: kdenetwork-common <= 22.04.3
Obsoletes: kdenetwork-kdnssd <= 22.04.3
Provides:  kdenetwork-kdnssd = 7:%{version}-%{release}


%description
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_plugindir}/kded/dnssdwatcher.so
%{_kf6_plugindir}/kio/zeroconf.so
%{_kf6_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
%dir %{_kf6_datadir}/remoteview/
%{_kf6_datadir}/remoteview/zeroconf.desktop
%{_kf6_metainfodir}/org.kde.kio_zeroconf.metainfo.xml


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
