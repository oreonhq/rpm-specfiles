%global source0_hash bee5d80a7c9467b89c66b904b36aae96c72f136f683867ad986d1e56bee10656
Name:           pavucontrol-qt
Version:        2.4.0
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Summary:        Qt port of volume control pavucontrol
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse)
# /oreon:deps
%description
%{summary}

%package l10n
BuildArch:      noarch
Summary:        Translations for pavucontrol-qt
Requires:       pavucontrol-qt
%description l10n
This package provides translations for the pavucontrol-qt package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang pavucontrol-qt --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pavucontrol-qt-l10n -f %{oreon_filedir}/pavucontrol-qt-l10n.list

%changelog

%autochangelog
