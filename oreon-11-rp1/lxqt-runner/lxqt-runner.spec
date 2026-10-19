%global source0_hash 9dec5b79434be351af58de0a7f718a29ad22b4a76f8ecc577fc3bc867ac11a97
Name:          lxqt-runner
Summary:        Application runner agent for LXQt desktop suite
Version:       2.4.0
Release:        1%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(lxqt-globalkeys)
BuildRequires:  pkgconfig(lxqt-globalkeys-ui)
BuildRequires:  pkgconfig(muparser)
# /oreon:deps
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
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang lxqt-runner --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-runner-l10n -f %{oreon_filedir}/lxqt-runner-l10n.list

%changelog

%autochangelog
