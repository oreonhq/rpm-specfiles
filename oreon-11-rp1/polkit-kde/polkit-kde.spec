%global         base_name polkit-kde-agent-1

Name:    polkit-kde
Summary: PolicyKit integration for KDE Desktop
Version: 6.6.2
Release:	2%{?dist}

License: GPL-2.0-or-later AND CC0-1.0
URL:     https://invent.kde.org/plasma/%{base_name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig


## upstreamable patches


BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Declarative)

BuildRequires:  polkit-qt6-1-devel

Provides: PolicyKit-authentication-agent = %{version}-%{release}
Provides: polkit-kde-1 = %{version}-%{release}
Provides: polkit-kde-agent-1 = %{version}-%{release}

Obsoletes: PolicyKit-kde < 4.5

# Add explicit dependency on polkit, since polkit-libs were split out
Requires: polkit

%description
Provides Policy Kit Authentication Agent that nicely fits to KDE.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6 \
  -DKDE_INSTALL_LIBEXECDIR:PATH=%{_kf6_libexecdir}

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang polkit-kde-authentication-agent-1


%files -f polkit-kde-authentication-agent-1.lang
%license LICENSES/*
%{_kf6_libexecdir}/polkit-kde-authentication-agent-1
%{_sysconfdir}/xdg/autostart/polkit-kde-authentication-agent-1.desktop
%{_kf6_datadir}/knotifications6/polkit-kde-authentication-agent-1.notifyrc
%{_kf6_datadir}/applications/org.kde.polkit-kde-authentication-agent-1.desktop
%{_userunitdir}/plasma-polkit-agent.service


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
