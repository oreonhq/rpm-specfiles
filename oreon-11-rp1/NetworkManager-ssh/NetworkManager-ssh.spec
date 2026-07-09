%global source0_hash 764ea968c0b951db5564f4de5dc7d4b5f14e834b3f6a95da84852253ee4dd10e

Summary:   NetworkManager VPN plugin for SSH tunnels
Name:      NetworkManager-ssh
Epoch:     1
Version:   1.4.4
Release:   1%{?dist}
License:   GPL-2.0-or-later
URL:       https://github.com/danfruehauf/NetworkManager-ssh

Source0:        https://github.com/danfruehauf/NetworkManager-ssh/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1.1.0
BuildRequires: glib2-devel
BuildRequires: gettext
BuildRequires: libnma-devel >= 1.1.0
BuildRequires: libsecret-devel
BuildRequires: intltool
BuildRequires: /usr/bin/file

Requires: dbus
Requires: NetworkManager >= 1:1.1.0
Requires: openssh-clients
Requires: sshpass

%global __provides_exclude ^libnm-.*\\.so

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
%autosetup -p1

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

%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-ssh.so
%{_prefix}/lib/NetworkManager/VPN/nm-ssh-service.name
%{_libexecdir}/nm-ssh-service
%{_datadir}/dbus-1/system.d/nm-ssh-service.conf
%doc README README.md NEWS
%license COPYING

%files -n NetworkManager-ssh-gnome
%{_libexecdir}/nm-ssh-auth-dialog
%{_libdir}/NetworkManager/libnm-gtk3-vpn-plugin-ssh-editor.so
%{_datadir}/metainfo/network-manager-ssh.metainfo.xml

%changelog
%autochangelog
