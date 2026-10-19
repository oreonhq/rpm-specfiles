%global source0_hash 2a50fd423fce0e4f79966fd4cd887692f564778289ee6988af10eca7566d7a4a
Name:          lxqt-notificationd
Summary:        Notification daemon for LXQt desktop suite
Version:       2.4.0
Release:        1%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       notifications.conf
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-notificationd-l10n -f %{oreon_filedir}/lxqt-notificationd-l10n.list

%changelog

%autochangelog
