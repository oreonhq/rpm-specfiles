%global source0_hash a0aec1ddcedef9db994cb4e90dd78c9b12962febf7dd3b5f7344ae3abb9f591c
Name:           obconf-qt
Version:        0.16.6
Release:        1%{?dist}
Summary:        A configuration editor for the OpenBox window manager
License:        GPL-2.0-only
URL:            https://github.com/lxde/obconf-qt
Source0:        https://github.com/lxde/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Requires:       openbox
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  perl
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
# /oreon:deps
%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for obconf-qt
Requires:       obconf-qt
%description l10n
This package provides translations for the obconf-qt package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DPULL_TRANSLATIONS=NO
%cmake_build
%install
%cmake_install
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n obconf-qt-l10n -f %{oreon_filedir}/obconf-qt-l10n.list

%changelog

%autochangelog
