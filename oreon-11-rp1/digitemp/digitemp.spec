%global source0_hash 683df4ab5cc53a45fe4f860c698f148d34bcca91b3e0568a342f32d64d12ba24

Summary:        Dallas Semiconductor 1-wire device reading console application
Name:           digitemp
Version:        3.7.2
Release:        17%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.digitemp.com/
Source0:        https://github.com/bcl/digitemp/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        dthowto.txt
Source2:        DS9097_Schematic.gif
Patch0:         https://github.com/bcl/digitemp/pull/38.patch#/digitemp-3.7.2-prototype.patch
BuildRequires:  gcc
%if 0%{!?_without_libusb:1}
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires:  libusb-compat-0.1-devel
%else
BuildRequires:  libusb-devel
%endif
%endif
BuildRequires:  make

%description
DigiTemp is a simple to use console application for reading values from
Dallas Semiconductor 1-wire devices. Its main use is for reading temperature
sensors, but it also reads counters and understands the 1-wire hubs with
devices on different branches of the network. DigiTemp now supports the
following 1-wire temperature sensors: DS18S20 (and DS1820), DS18B20, DS1822,
the DS2438 Smart Battery Monitor, DS2422 and DS2423 Counters, DS2409
MicroLAN Coupler (used in 1-wire hubs) and the AAG TAI-8540 humidity sensor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp -pf %{SOURCE1} %{SOURCE2} .

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIE -DPIC"
%make_build ds9097
%make_build clean
%make_build ds9097u
%if 0%{!?_without_libusb:1}
%make_build clean
%make_build ds2490
%endif

%install
install -D -p -m 0755 %{name}_DS9097 $RPM_BUILD_ROOT%{_bindir}/%{name}_DS9097
install -D -p -m 0755 %{name}_DS9097U $RPM_BUILD_ROOT%{_bindir}/%{name}_DS9097U
%if 0%{!?_without_libusb:1}
install -D -p -m 0755 %{name}_DS2490 $RPM_BUILD_ROOT%{_bindir}/%{name}_DS2490
%endif
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o ChangeLog.utf8 ChangeLog
touch -c -r ChangeLog ChangeLog.utf8; mv -f ChangeLog.utf8 ChangeLog

%files
%license COPYING COPYRIGHT
%doc ChangeLog CREDITS FAQ README TODO
%doc dthowto.txt DS9097_Schematic.gif
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
