%global source0_hash bdaa5d361c66a99f9af03be351d437e896bfb405e8623729d2f7450548d60145

Name:          lxqt-notificationd
Summary:       Notification daemon for LXQt desktop suite
Version:       2.3.1
Release:       2%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       notifications.conf
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(LayerShellQt)
BuildRequires: pkgconfig(lxqt)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: perl

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-notificationd
Requires:       lxqt-notificationd
%description l10n
This package provides translations for the lxqt-notificationd package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
	--remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-config-notificationd.desktop
mkdir -p %{buildroot}%{_sysconfdir}/lxqt/
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/lxqt/

%find_lang lxqt-notificationd --with-qt
%find_lang lxqt-config-notificationd --with-qt

%files
%{_bindir}/lxqt-notificationd
%{_bindir}/lxqt-config-notificationd
%{_datadir}/applications/lxqt-config-notificationd.desktop
%{_sysconfdir}/xdg/autostart/lxqt-notifications.desktop
%{_sysconfdir}/lxqt/notifications.conf

%files l10n -f lxqt-notificationd.lang -f lxqt-config-notificationd.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-notificationd
%{_datadir}/lxqt/translations/lxqt-notificationd/lxqt-notificationd_arn.qm
%{_datadir}/lxqt/translations/lxqt-notificationd/lxqt-notificationd_ast.qm
%dir %{_datadir}/lxqt/translations/lxqt-config-notificationd
%{_datadir}/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_ast.qm

%changelog
%autochangelog
