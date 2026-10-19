%global source0_hash 6acdc0b3f144f0d7f71a361c3653b5ccc1ee5760b5eb5b2470c363bc5daed210
%global _hardened_build 1
%global username OpenPrinting
Summary:        A printer administration tool
Name: system-config-printer
Version: 1.5.18
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/%{username}/%{name}
Source0:        https://github.com/OpenPrinting/system-config-printer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0001:        0001-Fix-debugprint-in-options.py-fixes-291.patch
Patch0002:        0001-udev-Fix-exit-value-when-device-is-already-handled.patch
Requires: dbus-x11
Requires: desktop-file-utils >= 0.2.92
Requires: desktop-notification-daemon
Requires: gtk3%{?_isa}
Requires: libcanberra-gtk3
Requires: libnotify%{?_isa}
Requires: python3-cairo%{?_isa}
Requires: python3-dbus%{?_isa}
Requires: python3-firewall
Requires: python3-gobject%{?_isa}
%{?systemd_requires}
Requires: system-config-printer-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  intltool
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  xmlto
# /oreon:deps
%description
system-config-printer is a graphical user interface that allows
the user to configure a CUPS print server.

%package libs
Summary: Libraries and shared code for printer administration tool
Recommends: PackageKit
Recommends: PackageKit-glib
Requires: gobject-introspection
Requires: gtk3
Requires: libnotify
Requires: python3-cups >= 1.9.60
Requires: python3-dbus
Requires: python3-gobject
Suggests: python3-smbc
BuildArch: noarch
%description libs
The common code used by both the graphical and non-graphical parts of
the configuration tool.

%if 0%{?rhel} <= 8 || 0%{?fedora} || (0%{?oreon} >= 11)
%package applet
Summary: Print job notification applet
Requires: %{name}-libs
%description applet
Print job notification applet.
%endif

%package udev
Summary: Rules for udev for automatic configuration of USB printers
Requires: system-config-printer-libs = %{version}-%{release}
%description udev
The udev rules and helper programs for automatically configuring USB
printers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git
# workaround https://github.com/pypa/setuptools/issues/3143
sed -i 's/setup.py install --prefix=$(DESTDIR)$(prefix)/setup.py install --root $(DESTDIR) --prefix=$(prefix)/' Makefile*

%build

aclocal -I /usr/share/gettext/m4
autoconf -f
automake --add-missing --copy --foreign
%configure --with-udev-rules
touch po/Makefile.in
%make_build
%install
%make_install
%{__mkdir_p} %buildroot%{_localstatedir}/run/udev-configure-printer
touch %buildroot%{_localstatedir}/run/udev-configure-printer/usb-uris
%py_byte_compile %{__python3} %{buildroot}/%{_datadir}/system-config-printer
%find_lang system-config-printer
%if 0%{?rhel} > 8 || (0%{?oreon} >= 11)
rm -rf %{buildroot}%{_bindir}/%{name}-applet \
       %{buildroot}%{_datadir}/%{name}/__pycache__/applet* \
       %{buildroot}%{_datadir}/%{name}/applet.py* \
       %{buildroot}%{_sysconfdir}/xdg/autostart/print-applet.desktop \
       %{buildroot}%{_mandir}/man1/%{name}-applet.1* \
       %{buildroot}%{_bindir}/%{name} \
       %{buildroot}%{_bindir}/install-printerdriver \
       %{buildroot}%{_datadir}/%{name}/__pycache__/check-device-ids* \
       %{buildroot}%{_datadir}/%{name}/__pycache__/HIG* \
       %{buildroot}%{_datadir}/%{name}/__pycache__/SearchCriterion* \
       %{buildroot}%{_datadir}/%{name}/__pycache__/serversettings* \
       %{buildroot}%{_datadir}/%{name}/__pycache__/system-config-printer* \
       %{buildroot}%{_datadir}/%{name}/__pycache__/ToolbarSearchEntry* \
       %{buildroot}%{_datadir}/%{name}/__pycache__/userdefault* \
       %{buildroot}%{_datadir}/%{name}/__pycache__/install-printerdriver* \
       %{buildroot}%{_datadir}/%{name}/check-device-ids.py* \
       %{buildroot}%{_datadir}/%{name}/HIG.py* \
       %{buildroot}%{_datadir}/%{name}/SearchCriterion.py* \
       %{buildroot}%{_datadir}/%{name}/serversettings.py* \
       %{buildroot}%{_datadir}/%{name}/system-config-printer.py* \
       %{buildroot}%{_datadir}/%{name}/ToolbarSearchEntry.py* \
       %{buildroot}%{_datadir}/%{name}/userdefault.py* \
       %{buildroot}%{_datadir}/%{name}/troubleshoot \
       %{buildroot}%{_datadir}/%{name}/icons \
       %{buildroot}%{_datadir}/%{name}/install-printerdriver.py* \
       %{buildroot}%{_datadir}/%{name}/xml/__pycache__ \
       %{buildroot}%{_datadir}/%{name}/xml/validate.py* \
       %{buildroot}%{_datadir}/%{name}/ui \
       %{buildroot}%{_datadir}/applications/system-config-printer.desktop \
       %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml \
       %{buildroot}%{_mandir}/man1/%{name}.1* \
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post

%{_bindir}/rm -f /var/cache/foomatic/foomatic.pickle
exit 0
%endif
%files -f %{oreon_filedir}/main.list
%files -n system-config-printer-libs -f %{oreon_filedir}/system-config-printer-libs.list
%files -n system-config-printer-applet -f %{oreon_filedir}/system-config-printer-applet.list
%files -n system-config-printer-udev -f %{oreon_filedir}/system-config-printer-udev.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.18-17
- Import
