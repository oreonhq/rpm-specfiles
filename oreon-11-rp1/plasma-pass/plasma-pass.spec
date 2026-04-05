Name:           plasma-pass
Version:        1.3.0
Release:	3%{?dist}
Summary:        Plasma applet to access passwords from the Pass password manager
License:        CC0-1.0 AND LGPL-2.1-or-later
URL:            https://invent.kde.org/plasma/%{name}.git
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz


BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Concurrent)

BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Package)

BuildRequires:  cmake(QGpgmeQt6)

BuildRequires:  gettext-devel
BuildRequires:  gpgmepp-devel
BuildRequires:  pkgconfig(liboath)


Requires:       plasmashell(desktop)
# Invokes the gpg2 executable to decrypt passwords
Requires:       gnupg2

# Does not use pass directly, but is a GUI for its store, also using
# the command line is currently the only way how to add new passwords.
Recommends:     pass

%description
Plasma Pass is a Plasma systray applet to easily access passwords from the Pass
password manager.

%prep
%autosetup


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang plasma_applet_org.kde.plasma.pass

%files -f plasma_applet_org.kde.plasma.pass.lang
%license LICENSES/*
%doc README.md
%{_kf6_qmldir}/org/kde/plasma/private/plasmapass/
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.pass/
%{_kf6_datadir}/qlogging-categories6/plasma-pass.categories


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-2
- Prepare for Oreon 11 (RP1)
