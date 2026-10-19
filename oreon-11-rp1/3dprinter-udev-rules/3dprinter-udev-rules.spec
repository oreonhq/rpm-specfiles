%global source0_hash 222fe23dffeb1143a85de30c9076452f5f27bc180cadc848a574a54dc711226a
Name:           3dprinter-udev-rules
Version:        0.4
Release:        1%{?dist}
Summary:        Rules for udev to give regular users access to operate 3D printers
License:        MIT-0
URL:            https://github.com/hroncok/%{name}
Source0:        https://github.com/hroncok/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
Requires:       systemd-udev
%global file_name 66-3dprinter.rules
# oreon:deps
BuildRequires:  systemd
# /oreon:deps
%description
Normally, when you connect a RepRap like 3D printer to a Linux machine by an
USB cable, you need to be in dialout or similar group to be able to control
it via OctoPrint, Printrun, Cura or any other control software. Not any more.

Install this rule to grant all users read and write access to collected
devices based on the VID and PID.

Disclaimer: Such device might not be a 3D printer, it my be an Arduino, it
might be a modem and it might even be a blender. But normally you would
add your user to dialout and get access to all of those and more anyway.
So I guess be careful when some of the users should not get access to
your blenders.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
install -D -p -m 644 %{file_name} %{buildroot}%_udevrulesdir/%{file_name}
%oreon_autofiles main

%post

%udev_rules_update
%postun

%udev_rules_update
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
