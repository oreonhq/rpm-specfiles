%global source0_hash b3f307f06c3b969bd65151d39729b97a767af42fddd3d9bab971135c0e7cd873

Name:           inxi
Version:        3.3.40
Release:        2%{?dist}
Summary:        A full featured system information script

License:        GPL-3.0-or-later
URL:            https://smxi.org/docs/inxi.htm
Source0:        https://codeberg.org/smxi/inxi/archive/%{version}-1.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators

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
# inxi can use any one of Cpanel::JSON::XS, JSON::XS or JSON::PP, but
# Cpanel::JSON::XS seems to be its preference, so let's go with that
Requires:       perl(Cpanel::JSON::XS)
# The debugger requires all of these, but the requirements are hedged
# around upstream to try and gracefully handle them being missing,
# so the dependency generator misses them. I tried
# https://codeberg.org/smxi/pinxi/pulls/2 , but upstream was not
# interested, so these need to be explicitly specified
Requires:       perl(Time::HiRes)
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(Net::FTP)
# inxi does not actually use Spec::Functions at all - only Spec -
# but the debugger refuses to run if it cannot load it. specify
# both the actual functional requirement, and the bogus checked
# requirement
Requires:       perl(File::Spec)
Requires:       perl(File::Spec::Functions)
# the debugger also requires tar to create the debug archive
Requires:       tar
# inxi documents that this isn't strictly required and works without
# it, you just can't output to XML, so let's call it Recommends:
Recommends:     perl(XML::Dumper)
# inxi likes to use these for downloading, but will use curl or wget
# if they are not present
Recommends:     perl(HTTP::Tiny) perl(IO::Socket::SSL)
# inxi defends against this not being present by falling back to
# a subshell of 'hostname', so it will work without it
Recommends:     perl(Sys::Hostname)

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
#Nothing to build

%install
install -p -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
gzip %{name}.1
install -p -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%files
%doc %{name}.changelog README.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
