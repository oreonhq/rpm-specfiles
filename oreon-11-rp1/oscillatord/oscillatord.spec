%global source0_hash cfc28c29262db2e938f588154e304e6b9626d2bff67ba5c16588a1e0a6011cec
Name:           oscillatord
Version:        3.10.0
Release:        1%{?dist}
Summary:        Daemon for disciplining an oscillator
License:        GPL-2.0-or-later
URL:            https://github.com/Orolia2s/oscillatord
Source0:        https://github.com/Orolia2s/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires: liboscillator-disciplining = %{version}
Requires: ubloxcfg >= 1.13-1.20220420gita46d97c
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gpsd-devel
BuildRequires:  json-c-devel
BuildRequires:  liboscillator-disciplining-devel
BuildRequires:  pps-tools-devel
BuildRequires:  sed
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  ubloxcfg-devel
# /oreon:deps
%description
The oscillatord daemon takes input from a PHC clock, reporting once per second,
the phase error between an oscillator and a reference GNSS receiver. For an
example of such a device, please see the ptp_ocp kernel driver.

The phase error read is then used as an input to the disciplining-minipod
library which will compute a setpoint, used by oscillatord to control an
oscillator and discipline it to the 1PPS from a GNSS receiver. Oscillatord also
sets PHC'stime at start up, using Output from a GNSS receiver.

To communicate with GNSS receiver's serial it uses ubloxcfg

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Fix paths in systemd unit
sed -e 's/^Environment=LD_LIBRARY_PATH.*$//' \
    -e "s@/usr/local/bin@%{_bindir}@" \
    -i systemd/oscillatord.service
# Drop hardcoded CFLAGS
sed -e 's/-O0//g' -i CMakeLists.txt

%build

%cmake -DBUILD_UTILS=1
%cmake_build
%install
%cmake_install
install -Dpm0644 example_configurations/%{name}_default.conf \
    %{buildroot}%{_sysconfdir}/%{name}.conf
%oreon_autofiles main

%post

%systemd_post oscillatord.service
%preun

%systemd_preun oscillatord.service
%postun

%systemd_postun_with_restart oscillatord.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
