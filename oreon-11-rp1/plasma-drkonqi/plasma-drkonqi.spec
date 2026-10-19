%global source1_hash 1132fbb41773c74a498e1df9c045cd9165f41bdc59299565f011672c0de088c4
%global source0_hash 9d02b9bd8534ac98dbb77a73248112654e2dee3ab1cf3cc59e69ba78027ab423
%global stable_kf6 stable
%global base_name drkonqi
ExcludeArch: %{ix86}
Name:    plasma-drkonqi
Summary:        DrKonqi crash handler for KF6/Plasma6
Version:        6.7.5
Release:        1%{?dist}
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig
Patch:        drkonqi-installdbgsymbols.patch
Requires:       kf6-kirigami
Requires:       kf6-kitemmodels
Requires:       kf6-kcmutils
Requires:       python3dist(psutil)
Requires:       python3dist(pygdbmi)
Requires:       python3dist(sentry-sdk)
Requires:       systemd-udev
Requires:       elfutils
Obsoletes: plasma-workspace-drkonqi < 5.10.95
Provides: plasma-workspace-drkonqi = %{version}-%{release}
%if (0%{?fedora} && 0%{?fedora} < 41) || (0%{?rhel} && 0%{?rhel} < 11) || (0%{?oreon} >= 11)
Requires: (dnf-command(debuginfo-install) if dnf)
%endif
Requires: konsole
Requires: polkit
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  git-core
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
install -p -D -m755 src/doc/examples/installdbgsymbols_fedora.sh \
    %{buildroot}%{_libexecdir}/installdbgsymbols.sh
%find_lang all --with-html --with-qt --all-name
grep drkonqi.mo all.lang > plasma-drkonqi.lang
%oreon_autofiles main

%post

%systemd_user_post drkonqi-sentry-postman.service
%preun

%systemd_user_preun drkonqi-sentry-postman.service
%postun

%systemd_user_postun drkonqi-sentry-postman.service
%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.{drkonqi.coredump.gui,drkonqi}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
