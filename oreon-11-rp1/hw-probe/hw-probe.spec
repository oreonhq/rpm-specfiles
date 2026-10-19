%global source0_hash 42030ba2fb3f6fb0772ab34744fbb91a89b1b6a9b0ed99e861fa05ff86968fb1
Summary:        Check operability of computer hardware and find drivers
Name:       hw-probe
Version:    1.6.5
Release:        1%{?dist}
BuildArch:  noarch
License:    LGPL-2.1-or-later OR BSD-4-Clause
URL:        https://github.com/linuxhw/hw-probe
Source0:        https://github.com/linuxhw/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:   perl-libwww-perl
Requires:   curl
Requires:   hwinfo
Requires:   pciutils
Requires:   usbutils
Requires:   smartmontools
Requires:   hdparm
Requires:   sysstat
Requires:   util-linux
Requires:   lm_sensors
%if 0%{?el6}%{?el7}
Requires:   dmidecode
%endif
%if 0%{?el8}
Recommends: dmidecode
Recommends: mcelog
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-generators
# /oreon:deps
%description
A tool to probe for hardware, check operability and find drivers
with the help of Linux hardware database:

    sudo -E hw-probe -all -upload

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_prefix}
%make_install prefix=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
