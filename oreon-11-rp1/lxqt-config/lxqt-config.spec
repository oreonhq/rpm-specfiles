%global source0_hash 2f77f98738c9c69f2e4bf7b492d93777119c8ec7833f0d7da9dbe145389def09
Name:          lxqt-config
Summary:        Config tools for LXQt desktop suite
Version:       2.4.0
Release:        1%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt)
BuildRequires:  cmake(zlib)
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  lxqt-menu-data
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-libinput)
# /oreon:deps
%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-config
Requires:       lxqt-config
%description l10n
This package provides translations for the lxqt-config package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%conf
%cmake

%build

%cmake_build
%install
%cmake_install
for cfgapp in monitor input file-associations appearance cursor brightness locale; do
if [ -f %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop ]; then
sed -i "/^GenericName.*/d" %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
sed -i "/^Comment.*/d" %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
fi
done
%fdupes %{buildroot}%{_datadir}/lxqt/translations
%find_lang lxqt-config --with-qt
%find_lang lxqt-config-appearance --with-qt
%find_lang lxqt-config-brightness --with-qt
%find_lang lxqt-config-cursor --with-qt
%find_lang lxqt-config-file-associations --with-qt
%find_lang lxqt-config-input --with-qt
%find_lang lxqt-config-locale --with-qt
%find_lang lxqt-config-monitor --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for cfgapp in appearance file-associations input monitor monitor-autostart locale brightness touchpad-autostart; do
if [ -f %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop ]; then
desktop-file-validate %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
fi
done
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n lxqt-config-l10n -f %{oreon_filedir}/lxqt-config-l10n.list

%changelog

%autochangelog
