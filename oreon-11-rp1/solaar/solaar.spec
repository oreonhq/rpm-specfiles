%global source0_hash faf3e1bf86a97766c1c0ad443cd4272bf23a77f5a2555c796e6d80e535cc7aeb
%bcond check 1
%global app_id io.github.pwr_solaar.solaar
Name:           solaar
Version:        1.1.20
Release:        1%{?dist}
Summary:        Device manager for a wide range of Logitech devices
URL:            https://github.com/pwr-Solaar/Solaar
Source0:        https://github.com/pwr-Solaar/Solaar/archive/%{version}/Solaar-%{version}.tar.gz
Patch:          https://github.com/pwr-Solaar/Solaar/pull/3099.patch
BuildArch:      noarch
License:        GPL-2.0-or-later
%if %{with check}
%endif
Requires:       hicolor-icon-theme
Requires:       solaar-udev
Requires:       python3dist(typing-extensions)
Recommends:     (gnome-shell-extension-appindicator if gnome-shell)
Recommends:     gtk3
Recommends:     libappindicator-gtk3
Recommends:     python3dist(pygobject)
Recommends:     python3dist(hid-parser)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-solaar = %{version}-%{release}
# /oreon:deps
%description
Solaar is a Linux device manager for many Logitech peripherals that connect
through Unifying and other receivers or via USB or Bluetooth. Solaar is able to
pair/unpair devices with receivers and show and modify some of the modifiable
features of devices.

gtk3 is recommended.  Without it, you can run solaar commands to view the
configuration of the devices and pair/unpair peripherals but you cannot use the
graphical interface.

%package doc
Summary:        Developer documentation for Solaar
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
This package provides documentation for Solaar, a device manager for
Logitech's Unifying Receiver peripherals.

%package udev
Summary:        Udev rules for Logitech receivers
BuildArch:      noarch
%description udev
This package contains udev rules which grant users permission to access various
connected Logitech wireless receivers.  This includes Unifying receivers,
various types of Nano receivers and some other types which can be used by
Solaar.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Solaar-%{version}
rm docs/.gitignore
rm -rv lib/hid_parser

%build

%pyproject_wheel
tools/po-compile.sh
%install
%pyproject_install
install -pm755 tools/hidconsole %{buildroot}%{_bindir}
sed -i -e '1d' %{buildroot}/%{python3_sitelib}/solaar/{gtk,tasks}.py
sed -i -e '1s,^#!.*$,#!/usr/bin/python3,' %{buildroot}/%{_bindir}/hidconsole
desktop-file-install --dir %{buildroot}/%{_datadir}/applications share/applications/solaar.desktop
desktop-file-install --dir %{buildroot}%{_sysconfdir}/xdg/autostart share/autostart/solaar.desktop
install -Dpm644 share/solaar/%{app_id}.metainfo.xml %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
appstreamcli validate --no-net --explain %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
install -Dpm644 rules.d-uinput/42-logitech-unify-permissions.rules %{buildroot}%{_udevrulesdir}/42-logitech-unify-permissions.rules
for dir in share/locale/* ; do
    lang=$(basename $dir)
    install -dm755 %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
    install -pm644 $dir/LC_MESSAGES/solaar.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%posttrans udev

if [ -S /run/udev/control ]; then
    /usr/bin/udevadm trigger --subsystem-match=hidraw --action=add
fi
%files
%files -n solaar-doc -f %{oreon_filedir}/solaar-doc.list
%files -n solaar-udev -f %{oreon_filedir}/solaar-udev.list

%changelog

%autochangelog
