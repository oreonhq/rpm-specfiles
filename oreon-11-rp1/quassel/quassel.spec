%global source0_hash bbd46ca429c1518480904c9e2b0ab3a0412fe197f3ce4879974e06ed3a0093a3
%global quassel_data_dir    %{_var}/lib/quassel
Name:    quassel
Summary:        A modern distributed IRC system
Version: 0.14.0
Release:        1%{?dist}
License: GPL-2.0-only OR GPL-3.0-only
URL:     https://quassel-irc.org/
Source0:        https://quassel-irc.org/pub/quassel-%{version}.tar.bz2
Requires: oxygen-icon-theme
Provides: %{name}-gui = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Source1: quasselcore.service
Source2: quassel.conf
Source3: quassel.sysusers
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dbusmenu-qt5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  phonon-qt5-devel
BuildRequires:  qca-qt5-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Quassel IRC is a modern, distributed IRC client,
meaning that one (or multiple) client(s) can attach
to and detach from a central core --
much like the popular combination of screen and a
text-based IRC client such as WeeChat, but graphical

%package common
Summary: Quassel common/shared files
Requires: %{name}-gui = %{version}-%{release}
BuildArch: noarch
%description common
%{summary}.

%package core
Summary: Quassel core component
Recommends: qt5-qtbase-postgresql
%description core
The Quassel IRC Core maintains a connection with the
server, and allows for multiple clients to connect

%package client
Summary: Quassel client
Provides: %{name}-gui = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
%description client
Quassel client

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{version}

%build

%cmake_kf5 \
  -DWANT_MONO=1 -DUSE_QT5=1 -DWITH_KDE=1 -DHAVE_SSL=1 -DENABLE_SHARED=OFF
%cmake_build
%install
%cmake_install
rm -f %{buildroot}/%{_datadir}/pixmaps/quassel.png
install -Dp -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}.conf
install -Dp -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/quasselcore.service
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf
install -d -m 0750 %{buildroot}/%{quassel_data_dir}
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
install -p -m 0644 data/*.appdata.xml %{buildroot}%{_datadir}/metainfo/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%post core

%systemd_post quasselcore.service
%preun core

%systemd_preun quasselcore.service
%postun core

%systemd_postun_with_restart quasselcore.service
%files -f %{oreon_filedir}/main.list
%files -n quassel-common -f %{oreon_filedir}/quassel-common.list
%files -n quassel-core -f %{oreon_filedir}/quassel-core.list
%files -n quassel-client -f %{oreon_filedir}/quassel-client.list

%changelog

%autochangelog
