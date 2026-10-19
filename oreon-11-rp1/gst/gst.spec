%global source0_hash 057ee7c6390897625b38ee70d1c7d5af21128c85c1e3282037945b4f0314f436
%global uuid    com.leinardi.%{name}
Name:           gst
Version:        0.7.7
Release:        1%{?dist}
Summary:        System utility designed to stress and monitoring various hardware components
License:        GPL-3.0-or-later
URL:            https://gitlab.com/leinardi/gst
Source0:        https://gitlab.com/leinardi/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       lm_sensors
Requires:       python3-gobject >= 3.50.0
Requires:       python3-humanfriendly >= 10.0
Requires:       python3-injector >= 0.22.0
Requires:       python3-matplotlib-gtk3 >= 3.1.1
Requires:       python3-peewee >= 3.17.8
Requires:       python3-psutil >= 6.1.0
Requires:       python3-pyxdg %dnl >= 0.28 # Try to run with old for now https://bugzilla.redhat.com/show_bug.cgi?id=2242522
Requires:       python3-pyyaml >= 6.0.2
Requires:       python3-requests >= 2.32.3
Requires:       python3-reactivex >= 4.0.4
Recommends:     dmidecode
Recommends:     stress-ng
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
GST is a GTK system utility designed to stress and monitor various hardware
components like CPU and RAM.

Features

- Run different CPU and memory stress tests
- Run multi and single core benchmark
- Show Processor information (name, cores, threads, family, model, stepping,
  flags,bugs, etc)
- Show Processor's cache information
- Show Motherboard information (vendor, model, bios version, bios date, etc)
- Show RAM information (size, speed, rank, manufacturer, part number, etc)
- Show CPU usage (core %, user %, load avg, etc)
- Show Memory usage
- Show CPU's physical's core clock (current, min, max)
- Show Hardware monitor (info provided by sys/class/hwmon)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -e '/meson_post_install/d' -i meson.build

%build

%meson
%meson_build
%install
%meson_install
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2x/
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
