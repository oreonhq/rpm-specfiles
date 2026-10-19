%global source0_hash 7a96da4e6657e3810574bfe39a383c130f0565206b087d0326ea09833eb9fab1
Name:          lxqt-powermanagement
Summary:        Powermanagement daemon for LXQt desktop suite
Version:       2.4.0
Release:        1%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lxqt-globalkeys-devel
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
# /oreon:deps
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
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
   --remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-config-powermanagement.desktop
%find_lang lxqt-powermanagement --with-qt
%find_lang lxqt-config-powermanagement --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-powermanagement-l10n -f %{oreon_filedir}/lxqt-powermanagement-l10n.list

%changelog

%autochangelog
