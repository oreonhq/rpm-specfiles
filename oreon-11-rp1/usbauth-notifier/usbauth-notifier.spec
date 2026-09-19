%global source0_hash 17965209b1450aa633e8cb15bdd80f29176b759acb06a5efb645aeabfd6dda07

#
# spec file for package usbauth-notifier
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 SUSE LLC
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 Stefan Koch <stefan.koch10@gmail.com>
# Copyright (c) 2015 SUSE LLC. All Rights Reserved.
# Author: Stefan Koch <skoch@suse.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           usbauth-notifier
Version:        1.0.4
Summary:        Notifier for USB Firewall to use with desktop environments
URL:            https://github.com/kochstefan/usbauth-all/tree/master/usbauth-notifier
Source:         https://github.com/kochstefan/usbauth-all/archive/v%{version}.tar.gz

Release:        9%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only

Requires:       usbauth
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  libusbauth-configparser-devel
BuildRequires:  gcc
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig

%description
A notifier for the usbauth firewall against BadUSB attacks. The user could manually allow or deny USB devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n usbauth-all-%{version} -p1

# Create a sysusers.d config file
cat >usbauth-notifier.sysusers.conf <<EOF
g usbauth -
g usbauth-notifier -
EOF

%build
pushd %{name}/
autoreconf -f -i
%configure
%make_build
popd

%pre
%install
pushd %{name}/
%make_install
%find_lang %name
popd

install -m0644 -D usbauth-notifier.sysusers.conf %{buildroot}%{_sysusersdir}/usbauth-notifier.conf

%files -f %{name}/%name.lang
%license %{name}/COPYING
%doc %{name}/README
%doc %_mandir/*/*
%dir %_sysconfdir/xdg/autostart
%_sysconfdir/xdg/autostart/usbauth-notifier.desktop
%attr(04750,root,usbauth) %_libexecdir/usbauth-npriv
%dir %attr(00750,root,usbauth-notifier) %_libexecdir/usbauth-notifier
%attr(02755,root,usbauth) %_libexecdir/usbauth-notifier/usbauth-notifier
%{_sysusersdir}/usbauth-notifier.conf

%changelog
%autochangelog
