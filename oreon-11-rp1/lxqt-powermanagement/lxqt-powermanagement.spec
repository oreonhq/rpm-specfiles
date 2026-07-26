%global source0_hash a816d8bca81677487d9b9cc5d8ff85cc2c646accba26a83d0a48ad559dad4a2e

Name:          lxqt-powermanagement
Summary:       Powermanagement daemon for LXQt desktop suite
Version:       2.3.0
Release:       2%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: lxqt-globalkeys-devel
BuildRequires: perl

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-powermanagement
Requires:       lxqt-powermanagement
%description l10n
This package provides translations for the lxqt-powermanagement package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
   --remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-config-powermanagement.desktop

%find_lang lxqt-powermanagement --with-qt
%find_lang lxqt-config-powermanagement --with-qt

%files
%{_bindir}/lxqt-powermanagement
%{_bindir}/lxqt-config-powermanagement
%{_datadir}/applications/lxqt-config-powermanagement.desktop
%{_datadir}/icons/hicolor/*
%{_sysconfdir}/xdg/autostart/lxqt-powermanagement.desktop

%files l10n -f lxqt-powermanagement.lang -f lxqt-config-powermanagement.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-powermanagement
%dir %{_datadir}/lxqt/translations/lxqt-config-powermanagement

%changelog
%autochangelog
