%global source0_hash dd1a2c9c6a614911a2b9f2a80b7a8c4d67072a37cf1d46dfb37399f2fc865182

Name:          lxqt-runner
Summary:       Application runner agent for LXQt desktop suite
Version:       2.3.0
Release:       2%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(lxqt-globalkeys)
BuildRequires: pkgconfig(lxqt-globalkeys-ui)
BuildRequires: cmake(LayerShellQt)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(muparser)
BuildRequires: perl

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-runner
Requires:       lxqt-runner
%description l10n
This package provides translations for the lxqt-runner package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang lxqt-runner --with-qt

%files
%{_bindir}/lxqt-runner
%{_sysconfdir}/xdg/autostart/lxqt-runner.desktop
%{_mandir}/man1/%{name}*

%files l10n -f lxqt-runner.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/%{name}

%changelog
%autochangelog
