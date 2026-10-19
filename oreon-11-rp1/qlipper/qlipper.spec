%global source0_hash 6d1aa86060cdcd97ae409b6d77cb95c86db3da4ccba02bdd06c159bc7482ce8f
Name:		qlipper
Version:	6.1.0
Release:        1%{?dist}
License:	GPL-3.0-or-later
Summary:        Lightweight clipboard history
URL:		https://github.com/pvanek/qlipper
Source0:        https://github.com/pvanek/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Provides:       bundled(libqxt) = 0.7.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools
BuildRequires:  perl
BuildRequires:  pkgconfig(KF6GuiAddons)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
Lightweight clipboard history applet.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=release -DUSE_SYSTEM_QXT=OFF -DUSE_SYSTEM_QTSA=ON -DENABLE_LXQT_AUTOSTART=ON -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt --without-mo
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
