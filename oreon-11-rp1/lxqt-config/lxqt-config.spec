%global source0_hash 2b27590967d087a95c8c21ccdb04844e9797eae5c06a552aabe8d4dc7e8ce13a

Name:          lxqt-config
Summary:       Config tools for LXQt desktop suite
Version:       2.3.1
Release:       1%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: lxqt-menu-data
BuildRequires: perl

BuildRequires: cmake(KF6Screen)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(zlib)

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-libinput)
BuildRequires: pkgconfig(x11)

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

%check
for cfgapp in appearance file-associations input monitor monitor-autostart locale brightness touchpad-autostart; do
if [ -f %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop ]; then
desktop-file-validate %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
fi
done
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/lxqt-config
%{_bindir}/lxqt-config-brightness
%{_bindir}/lxqt-config-appearance
%{_bindir}/lxqt-config-file-associations
%{_bindir}/lxqt-config-input
%{_bindir}/lxqt-config-monitor
%{_bindir}/lxqt-config-locale
%{_datadir}/applications/%{name}-appearance.desktop
%{_datadir}/applications/%{name}-file-associations.desktop
%{_datadir}/applications/%{name}-input.desktop
%{_datadir}/applications/%{name}-monitor.desktop
%{_datadir}/applications/%{name}-monitor-autostart.desktop
%{_datadir}/applications/%{name}-locale.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-brightness.desktop
%{_datadir}/applications/%{name}-touchpad-autostart.desktop
%{_libdir}/lxqt-config/liblxqt-config-cursor.so
%{_datadir}/icons/*/*
%{_datadir}/lxqt/icons/*
%{_mandir}/man1/lxqt-config*

%files l10n -f lxqt-config.lang -f lxqt-config-appearance.lang -f lxqt-config-brightness.lang -f lxqt-config-cursor.lang -f lxqt-config-file-associations.lang -f lxqt-config-input.lang -f lxqt-config-locale.lang -f lxqt-config-monitor.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-config
%dir %{_datadir}/lxqt/translations/lxqt-config-appearance
%dir %{_datadir}/lxqt/translations/lxqt-config-brightness
%dir %{_datadir}/lxqt/translations/lxqt-config-cursor
%dir %{_datadir}/lxqt/translations/lxqt-config-file-associations
%dir %{_datadir}/lxqt/translations/lxqt-config-input
%dir %{_datadir}/lxqt/translations/lxqt-config-locale

%changelog
%autochangelog
