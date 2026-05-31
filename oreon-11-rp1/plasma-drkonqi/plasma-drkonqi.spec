%global source0_hash b2b104d5f30224bca88280246ca990ac314d81cb1bf0d3857613ff683db92d82

%global stable_kf6 stable


%global base_name drkonqi


# 
ExcludeArch: %{ix86}

Name:    plasma-drkonqi
Summary: DrKonqi crash handler for KF6/Plasma6
Version: 6.6.5
Release: 1%{?dist}
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

## upstreamable Patches
# dnf debuginfo-install
Patch:          drkonqi-installdbgsymbols.patch

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  systemd-devel
BuildRequires:  git-core

Requires:       kf6-kirigami
Requires:       kf6-kitemmodels
Requires:       kf6-kcmutils
Requires:       python3dist(psutil)
Requires:       python3dist(pygdbmi)
Requires:       python3dist(sentry-sdk)
Requires:       systemd-udev
Requires:       elfutils

# retired from plasma-workspace
Obsoletes: plasma-workspace-drkonqi < 5.10.95
Provides: plasma-workspace-drkonqi = %{version}-%{release}

%if (0%{?fedora} && 0%{?fedora} < 41) || (0%{?rhel} && 0%{?rhel} < 11) || (0%{?oreon} >= 11)
Requires: (dnf-command(debuginfo-install) if dnf)
%endif
Requires: konsole
Requires: polkit


%description
%{summary}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{base_name}-%{version} -p1

%build
%cmake_kf6 -DWITH_PYTHON_VENDORING=OFF -DWITH_GDB12=ON
%cmake_build

%install
%cmake_install
# installdbgsymbols script
install -p -D -m755 src/doc/examples/installdbgsymbols_fedora.sh \
    %{buildroot}%{_libexecdir}/installdbgsymbols.sh

%find_lang all --with-html --with-qt --all-name
grep drkonqi.mo all.lang > plasma-drkonqi.lang

%post
%systemd_user_post drkonqi-sentry-postman.service

%preun
%systemd_user_preun drkonqi-sentry-postman.service

%postun
%systemd_user_postun drkonqi-sentry-postman.service

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.{drkonqi.coredump.gui,drkonqi}.desktop

%files -f plasma-drkonqi.lang
%license LICENSES/*
%{_bindir}/drkonqi-coredump-gui
%{_libexecdir}/drkonqi
%{_libexecdir}/installdbgsymbols.sh
%{_libexecdir}/drkonqi-coredump-cleanup
%{_libexecdir}/drkonqi-coredump-launcher
%{_libexecdir}/drkonqi-coredump-processor
%{_kf6_datadir}/drkonqi/
%{_kf6_datadir}/applications/org.kde.drkonqi.coredump.gui.desktop
%{_kf6_datadir}/applications/org.kde.drkonqi.desktop
%{_kf6_datadir}/qlogging-categories6/drkonqi.categories
%{_userunitdir}/drkonqi-coredump-*
%{_unitdir}/drkonqi-coredump-processor@.service
%{_kf6_datadir}/knotifications6/drkonqi-coredump-launcher.notifyrc
%{_bindir}/drkonqi-sentry-data
%{_unitdir}/systemd-coredump@.service.wants/drkonqi-coredump-processor@.service
%{_userunitdir}/default.target.wants/*
%{_userunitdir}/drkonqi-sentry-postman.*
%{_userunitdir}/plasma-core.target.wants/drkonqi-*
%{_userunitdir}/sockets.target.wants/drkonqi-coredump-launcher.socket
%{_userunitdir}/timers.target.wants/drkonqi-*
%{_libexecdir}/drkonqi-sentry-postman
%{_kf6_libexecdir}/drkonqi-polkit-helper
%{_kf6_datadir}/dbus-1/system-services/org.kde.drkonqi.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.drkonqi.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.drkonqi.policy

%changelog
* Mon May 25 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.6.5-1
- Update to KDE Plasma 6.6.5

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.5-1
- Import
