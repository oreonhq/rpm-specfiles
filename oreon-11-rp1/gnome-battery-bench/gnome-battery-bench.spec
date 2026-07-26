%global source0_hash 40b211c306e14f36f1ab75aa1b13b551ac49c23c8881074558e4f0fc3fa8dd18

Name:           gnome-battery-bench
Version:        3.15.4
Release:        27%{?dist}
Summary:        Measure power usage in defined scenarios

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://git.gnome.org/browse/%{name}
Source0:        https://download.gnome.org/sources/%{name}/3.15/%{name}-%{version}.tar.xz

Patch0:         wayland-no-shortcut.patch

BuildRequires:  gcc
BuildRequires: asciidoc
BuildRequires: desktop-file-utils
BuildRequires: xmlto
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xtst)
BuildRequires: make

%description
This application is designed for measuring power usage. It does it by
recording the reported battery statistics as it replays recorded event
logs, and then using that to estimate power consumption and total
battery lifetime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0  -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.BatteryBench.desktop

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/gbb
%{_datadir}/%{name}
%{_datadir}/applications/org.gnome.BatteryBench.desktop
%{_datadir}/dbus-1/services/org.gnome.BatteryBench.service
%{_datadir}/dbus-1/system-services/org.gnome.BatteryBench.Helper.service
%{_datadir}/polkit-1/actions/org.gnome.BatteryBench.Helper.policy
%{_libexecdir}/gnome-battery-bench-helper
%{_mandir}/man1/gbb.1*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.gnome.BatteryBench.Helper.conf

%changelog
%autochangelog
