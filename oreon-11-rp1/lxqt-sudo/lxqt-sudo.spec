%global source0_hash f7ff3a68fe83efb9a236ea16e23b48408d988ced7f2b8fb727439935ec10c6b4
Name:          lxqt-sudo
Version:       2.4.0
Release:        1%{?dist}
Summary:        GUI frontend for sudo/su
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires: sudo
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
# /oreon:deps
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
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang lxqt-sudo --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-sudo-l10n -f %{oreon_filedir}/lxqt-sudo-l10n.list

%changelog

%autochangelog
