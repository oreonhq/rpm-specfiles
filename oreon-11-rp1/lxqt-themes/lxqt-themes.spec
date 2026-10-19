%global source0_hash e30dd9e21267c3b0b4e129933a5d2adf48539e4b7ab23a454c3f02ea37860950
Name:           lxqt-themes
Version:        2.3.0
Release:        1%{?dist}
Summary:        LXQt standard themes
License:        LGPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       hicolor-icon-theme
Requires:       desktop-backgrounds-compat
Requires:       breeze-cursor-themes
Requires:       breeze-icon-theme
# oreon:deps
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  perl
BuildRequires:  pkgconfig(lxqt)
# /oreon:deps
%description
This package contains the standard themes for the LXQt desktop, namely
ambiance, dark, frost, kde-plasma, light and system.

%package fedora
Summary: Default Fedora theme for LXQt
Requires: lxqt-themes = %{version}
Requires: breeze-cursor-theme
Requires: breeze-icon-theme
%description fedora
%{summary}.

%prep
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-themes-fedora -f %{oreon_filedir}/lxqt-themes-fedora.list

%changelog

%autochangelog
