%global source0_hash e08d92550a0f10890e722cc7db1e6d6cbde7e9fb47e61a8c6cec51f54a0b63d8
Name:           inxi
Version:        3.3.41
Release:        1%{?dist}
Summary:        A full featured system information script
License:        GPL-3.0-or-later
URL:            https://smxi.org/docs/inxi.htm
Source0:        https://codeberg.org/smxi/inxi/archive/%{version}-1.tar.gz
BuildArch:      noarch
Requires:       iproute
Requires:       pciutils
Requires:       procps
Requires:       lm_sensors
Requires:       usbutils
Requires:       hddtemp
Requires:       xdpyinfo xprop xrandr
Requires:       bind-utils
Requires:       ipmitool
Requires:       freeipmi
Requires:       wmctrl
Requires:       perl(Cpanel::JSON::XS)
Requires:       perl(Time::HiRes)
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(Net::FTP)
Requires:       perl(File::Spec)
Requires:       perl(File::Spec::Functions)
Requires:       tar
Recommends:     perl(XML::Dumper)
Recommends:     perl(HTTP::Tiny) perl(IO::Socket::SSL)
Recommends:     perl(Sys::Hostname)
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
Inxi offers a wide range of built-in options, as well as a good number of extra
features which require having the script recommends installed on the system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}
#Disable update option
sed -i 's/my ($b_sysctl_disk,$b_update,$b_weather) = (1,1,1);/my ($b_sysctl_disk,$b_update,$b_weather) = (1,0,1);/' inxi
#Correct shebang
sed -i 's|/usr/bin/env perl|/usr/bin/perl|' inxi

%build

%install
install -p -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
gzip %{name}.1
install -p -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
