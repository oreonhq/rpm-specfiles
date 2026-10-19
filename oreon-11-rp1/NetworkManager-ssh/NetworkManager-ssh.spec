%global source0_hash 765523ad935cae2f85ff37bd73760854cea9ae799eb319964a8fa3ab8f83b3c2
Summary:        NetworkManager VPN plugin for SSH tunnels
Name:      NetworkManager-ssh
Epoch:     1
Version:   1.4.5
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://github.com/danfruehauf/NetworkManager-ssh
Source0:        https://github.com/danfruehauf/NetworkManager-ssh/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires: dbus
Requires: NetworkManager >= 1:1.1.0
Requires: openssh-clients
Requires: sshpass
%global __provides_exclude ^libnm-.*\\.so
# oreon:deps
BuildRequires:  /usr/bin/file
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libnma-devel
BuildRequires:  libsecret-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package contains software for integrating VPN capabilities with SSH
tunnels (SOCKS/PPP over SSH) with NetworkManager.

%package -n NetworkManager-ssh-gnome
Summary: NetworkManager VPN plugin for SSH - GNOME files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: shared-mime-info
%description -n NetworkManager-ssh-gnome
This package contains software for integrating VPN capabilities with SSH
tunnels with NetworkManager (GNOME/KDE authentication dialog files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fvi
%configure \
        --disable-static \
        --with-dist-version=%{version}-%{release}
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
%find_lang %{name}
%oreon_autofiles NetworkManager-ssh-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-ssh-gnome -f %{oreon_filedir}/NetworkManager-ssh-gnome.list

%changelog

%autochangelog
