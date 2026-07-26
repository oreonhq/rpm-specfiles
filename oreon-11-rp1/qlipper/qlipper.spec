%global source0_hash e4e70f54d007e1e1cd715944b6742c4c70bab5b28838aa33d673de0c7a6c1570

Name:		qlipper
Version:	6.0.0
Release:	2%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Summary:	Lightweight clipboard history
URL:		https://github.com/pvanek/qlipper
Source0:	https://github.com/pvanek/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	lxqt-build-tools
BuildRequires:	perl
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(KF6GuiAddons)
BuildRequires:	qt6-qttools-devel
BuildRequires:	qt6-qtbase-private-devel
# Contains a modified copy of qxt, we cannot use the Fedora one (segfaults)
Provides:       bundled(libqxt) = 0.7.0

%description
Lightweight clipboard history applet.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=release -DUSE_SYSTEM_QXT=OFF -DUSE_SYSTEM_QTSA=ON -DENABLE_LXQT_AUTOSTART=ON -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%license COPYING
%doc README
%{_sysconfdir}/xdg/autostart/lxqt-qlipper-autostart.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/qlipper.png

%changelog
%autochangelog
