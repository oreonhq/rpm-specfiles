%global source0_hash 6d71440f299f6ffc76b94821f85be9a6bca202292b821498e122d98fad473479

Name:          lxqt-sudo
Version:       2.3.0
Release:       2%{?dist}
Summary:       GUI frontend for sudo/su
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(lxqt)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(Qt6Linguist)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: perl

Requires: sudo

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-sudo
Requires:       lxqt-sudo
%description l10n
This package provides translations for the lxqt-sudo package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang lxqt-sudo --with-qt

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/lx*
%{_mandir}/man1/lx*.1*

%files l10n -f lxqt-sudo.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/%{name}
%{_datadir}/lxqt/translations/%{name}/%{name}_ast.qm
%{_datadir}/lxqt/translations/%{name}/%{name}_arn.qm

%changelog
%autochangelog
