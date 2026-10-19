%global source0_hash 086d61f1be7f54f909a20a47f32511c741d72948c2967c37ac1f402f6381a6bf
Name:            mesaflash
Version:         3.4.9
%global forgeurl https://github.com/LinuxCNC/%{name}
%global tag     release/%{version}
%forgemeta
Release:        1%{?dist}
Summary:        Configuration and diagnostic tool for Mesa Electronics boards
License:         GPL-2.0-or-later
Url:             %{forgeurl}
Source0:        %{forgeurl}/archive/%{tag}/%{name}-release-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libmd)
BuildRequires:  pkgconfig(libpci)
# /oreon:deps
%description
Configuration and diagnostic tool for Mesa Electronics
PCI(E)/ETH/EPP/USB/SPI boards.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -S git
# Remove binary files
rm -rf *.dll *.sys libpci

%build

CFLAGS='%{build_cflags} -DVERSION=\"%{version}-%{release}\"'
%set_build_flags
%ifarch i386 x86_64
  export USE_STUBS=0
%else
  export USE_STUBS=1
%endif
%{make_build} OWNERSHIP=""
%install
%ifarch i386 x86_64
  export USE_STUBS=0
%else
  export USE_STUBS=1
%endif
%{make_install} OWNERSHIP="" DESTDIR="%{buildroot}%{_prefix}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
