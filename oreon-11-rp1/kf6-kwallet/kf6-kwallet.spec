%global source0_hash 66a47fc170ea074cce8b916fa313f309d7c9497bd2132e0598d4b63bbad2ac88

%global framework kwallet

%global stable_kf6 stable
%global majmin_ver_kf6 6.29

Name:    kf6-%{framework}
Version: 6.29.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for password management

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6ConfigWidgets) >= %{version}

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6Config) >= %{version}
BuildRequires:  cmake(KF6Config) >= %{version}
BuildRequires:  cmake(KF6CoreAddons) >= %{version}
BuildRequires:  cmake(KF6DBusAddons) >= %{version}
BuildRequires:  cmake(KF6DocTools) >= %{version}
BuildRequires:  cmake(KF6I18n) >= %{version}
BuildRequires:  cmake(KF6Notifications) >= %{version}
BuildRequires:  cmake(KF6Service) >= %{version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{version}
BuildRequires:  cmake(KF6WindowSystem) >= %{version}
BuildRequires:  cmake(KF6Crash) >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6ColorScheme) >= %{version}
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  pkgconfig(libsecret-1)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf6-filesystem
Requires:       pinentry-gui
Requires:       qca-qt6-ossl%{?_isa}

%description
KWallet is a secure and unified container for user passwords.

%package        libs
Summary:        KWallet framework libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gpgmepp%{?_isa}
%description    libs
Provides API to access KWallet data from applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kwallet-query
%{_kf6_bindir}/kwalletd6
%{_kf6_bindir}/ksecretd
%{_kf6_datadir}/applications/org.kde.ksecretd.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.secretservicecompat.service
%{_kf6_datadir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf6_datadir}/dbus-1/services/org.kde.kwalletd6.service
%{_kf6_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kwallet.service
%{_kf6_datadir}/knotifications6/ksecretd.notifyrc
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_datadir}/xdg-desktop-portal/portals/kwallet.portal
%{_mandir}/man1/kwallet-query.1*

%files libs
%{_kf6_libdir}/libKF6Wallet.so.*
%{_libdir}/libKF6WalletBackend.so.*

%files devel
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.KWallet.xml
%{_kf6_includedir}/KWallet/
%{_kf6_libdir}/cmake/KF6Wallet/
%{_kf6_libdir}/libKF6Wallet.so


%changelog
* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.29.0-1
- Latest upstream release

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-10
- Rebuild

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-9
- Rebuild for gpgmepp 7 (ISO)

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-8
- Rebuild for gpgmepp SONAME

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

