%global source0_hash 5fa0fa718fda8ab6ab8411874516b8f2c757bb9d57c44bb286f2337f43b23247

Name:          lxqt-globalkeys
Summary:       Global keys utility for LXQt desktop suite
Version:       2.3.0
Release:       2%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: pkgconfig(lxqt)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: perl

Requires: dbus-x11

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-globalkeys
Requires:       lxqt-globalkeys
%description l10n
This package provides translations for the lxqt-globalkeys package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-config-globalkeyshortcuts.desktop
%find_lang lxqt-config-globalkeyshortcuts --with-qt

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/lxqt-globalkeysd
%{_bindir}/lxqt-config-globalkeyshortcuts
%{_datadir}/applications/lxqt-config-globalkeyshortcuts.desktop
%{_libdir}/liblxqt-globalkeys.so.2
%{_libdir}/liblxqt-globalkeys.so.%{version}
%{_libdir}/liblxqt-globalkeys-ui.so.2
%{_libdir}/liblxqt-globalkeys-ui.so.%{version}
%{_sysconfdir}/xdg/autostart/lxqt-globalkeyshortcuts.desktop
%{_datadir}/lxqt/globalkeyshortcuts.conf

%files devel
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_includedir}/lxqt-globalkeys
%{_includedir}/lxqt-globalkeys-ui
%{_libdir}/liblxqt-globalkeys.so
%{_libdir}/liblxqt-globalkeys-ui.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/cmake/lxqt-globalkeys
%dir %{_datadir}/cmake/lxqt-globalkeys-ui
%{_datadir}/cmake/lxqt-globalkeys/*
%{_datadir}/cmake/lxqt-globalkeys-ui/*

%files l10n -f lxqt-config-globalkeyshortcuts.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts
%{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_arn.qm

%changelog
%autochangelog
