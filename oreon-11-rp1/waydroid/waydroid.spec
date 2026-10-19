%global source0_hash 4b963aceb9de2884020e98b26e40147b3f26a0444606633adc45b63752f57dca
%global forgeurl https://github.com/waydroid/waydroid
%global selinuxtype targeted
Version:        1.6.3
%global tag %{version}
%forgemeta
Name:           waydroid
Release:        1%{?dist}
Summary:        Container-based approach to boot a full Android system on GNU/Linux
License:        GPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        waydroid.te
Source4:        dev-binderfs.mount
Source6:        waydroid.fc
Patch0:         setup-firewalld.patch
Patch1:         mount-secontext.patch
Patch2:         no-apparmor.patch
BuildArch:      noarch
Requires:       python3dist(gbinder-python) >= 1.3
Requires:       python3dist(dbus-python)
Requires:       python3-gobject
Requires:       lxc
Requires:       gtk3
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
Requires:       nftables
Requires:       iproute
Requires:       dnsmasq
# oreon:deps
BuildRequires:  container-selinux
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-devel
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Waydroid uses Linux namespaces to run a full Android system in a container
and provide Android applications on any GNU/Linux-based platform.
The Android system inside the container has direct access to needed hardware
through LXC and the binder interface.

%package selinux
Summary:            SELinux policy module for waydroid
Requires:           %{name} = %{version}-%{release}
Requires:           container-selinux
%{?selinux_requires}
%description selinux
This package contains the SELinux policy module necessary to run waydroid.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
mkdir SELinux
cp %{S:1} SELinux/
cp %{S:6} SELinux/

%build

sed -i -e '/"system_channel":/ s/: ".*"/: ""/' tools/config/__init__.py
sed -i -e '/"vendor_channel":/ s/: ".*"/: ""/' tools/config/__init__.py
sed -i -e '/options: OTA channel URL/ s/default is Official OTA server/mandatory/' tools/helpers/arguments.py
cd SELinux
%{__make} NAME=%{selinuxtype} -f /usr/share/selinux/devel/Makefile
%install
%make_install LIBDIR=%{_libdir} DESTDIR=%{buildroot} USE_SYSTEMD=1 USE_DBUS_ACTIVATION=1 USE_NFTABLES=1
%py_byte_compile %{python3} %{buildroot}%{_prefix}/lib/waydroid
%{__install} -d %{buildroot}%{_unitdir}
%{__install} -d %{buildroot}%{_datadir}/selinux/%{selinuxtype}
%{__install} -p -m 644 %{S:4} %{buildroot}%{_unitdir}/
%{__install} -p -m 644 SELinux/%{name}.pp %{buildroot}%{_datadir}/selinux/%{selinuxtype}/%{name}.pp
sed -i '/^\[Unit\]/a Wants=dev-binderfs.mount' %{buildroot}%{_unitdir}/waydroid-container.service
sed -i '/^\[Service\]/a ExecStartPre=/usr/bin/ln -sf /dev/binderfs/binder /dev/binderfs/vndbinder /dev/binderfs/hwbinder /dev/' %{buildroot}%{_unitdir}/waydroid-container.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/Waydroid.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/waydroid.market.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/waydroid.app.install.desktop
appstream-util validate --nonet %{buildroot}%{_metainfodir}/id.waydro.waydroid.metainfo.xml
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/%{selinuxtype}/%{name}.pp
%selinux_relabel_post -s %{selinuxtype}
if [ "$1" -le "1" ]; then # First install
  %systemd_postun_with_restart waydroid-container.service
fi
%postun selinux

if [ $1 -eq 0 ]; then
  %selinux_modules_uninstall -s %{selinuxtype} %{name}
  %selinux_relabel_post -s %{selinuxtype}
fi
%post

waydroid upgrade -o > /dev/null || :
%systemd_post waydroid-container.service
if [ $1 -eq 1 ]; then
  if systemctl -q is-enabled waydroid-container.service > /dev/null 2>&1 ; then
    systemctl start waydroid-container.service > /dev/null 2>&1 || :
  fi
fi
%preun

%systemd_preun waydroid-container.service
%postun

%systemd_postun_with_restart waydroid-container.service
%files -f %{oreon_filedir}/main.list
%files -n waydroid-selinux -f %{oreon_filedir}/waydroid-selinux.list

%changelog

%autochangelog
