%global source0_hash 7e3db35c6f856d04da69036fdeb93e6874f7059004f21cdeea013691bc6528c4

Name:           pavucontrol-qt
Version:        2.2.0
Release:        3%{?dist}
License:        GPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Summary:        Qt port of volume control pavucontrol
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  perl

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

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang pavucontrol-qt --with-qt

%files
%license LICENSE
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%files l10n -f pavucontrol-qt.lang
%license LICENSE
%doc AUTHORS
%dir %{_datadir}/%{name}/translations

%changelog
%autochangelog
